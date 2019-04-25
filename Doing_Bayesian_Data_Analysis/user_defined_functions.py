### Author: Sushmit Roy
import pandas as pd
import numpy as np
from scipy import stats
import xarray
import math
from scipy.optimize import minimize_scalar
from scipy.stats import beta
np.random.seed(1)

### Bokeh Libraries
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh.models import Span,Range1d,Label,LabelSet
from bokeh.layouts import column,row
output_notebook()

## matplotlib libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

def BernGrid(Theta,pTheta,Data):
    '''
    Theta is vector of values between 0 and 1.
    pTheta is prior probability mass at each value of Theta
    Data is vector of 0's and 1's.
    '''
    if np.any((Theta < 0)|(Theta > 1 )):
        raise ValueError("Theta values must be between 0 and 1")
    if np.any(pTheta < 0):
        raise ValueError("pTheta values must be non-negative")
    if not(math.isclose(math.fsum(pTheta),1)):
        raise ValueError("pTheta values must sum to 1.0")
    if not(np.all((Data == 0) | (Data == 1))):
        raise ValueError("Data values must be 0 or 1")
    z = np.sum(Data) # No of heads
    N = len(Data)
    # Compute the Bernoulli likelihood at each value of Theta:
    Likelihood = np.multiply(Theta**z,(1-Theta)**(N-z))

    ## calculate the Posterior
    p_Data= np.dot(np.multiply(Theta**z,(1-Theta)**(N-z)),pTheta)
    Posterior = (Likelihood * pTheta)/p_Data
    ## plot the Prior
    plot_prior = figure(plot_width=800, plot_height=250, title='Prior')
    plot_prior.x_range = Range1d(0,1)
    plot_prior.y_range = Range1d(0, max(np.append(pTheta,Posterior)))
    plot_prior.xaxis.axis_label = 'Θ'
    plot_prior.yaxis.axis_label = 'p(Θ)'
    plot_prior.vbar(x=Theta, width=0.001, bottom=0,top=pTheta)

    ## Plot the likelihood
    plot_likelihood = figure(plot_width=800, plot_height=250, title='Likelihood')
    plot_likelihood.x_range = Range1d(0, 1)
    plot_likelihood.y_range = Range1d(0, 1.1*max(Likelihood))
    plot_likelihood.xaxis.axis_label = 'Θ'
    plot_likelihood.yaxis.axis_label = 'p(D|Θ)'
    plot_likelihood.vbar(x=Theta, width=0.001, bottom=0,top=Likelihood)

    ## Plot the Posterior
    plot_posterior = figure(plot_width=800, plot_height=250, title='Posterior')
    plot_posterior.x_range = Range1d(0,1)
    plot_posterior.y_range = Range1d(0, max(np.append(pTheta,Posterior)))
    plot_posterior.xaxis.axis_label = 'Θ'
    plot_posterior.yaxis.axis_label = 'p(Θ|D)'
    plot_posterior.vbar(x=Theta, width=0.001, bottom=0,top=Posterior)

    show(column(plot_prior,plot_likelihood,plot_posterior))


def HDIofICDF (ICDFname,credMass=0.95,**kwargs):
    '''
    ICDFname is the inverse cdf for example : beta.ppf
    Use scipy minimize_scalar method. Default to
    return value: tuple of Highest density iterval (HDI)
    example: udf.HDIofICDF(beta.ppf,a=18.25,b=6.75)
    '''
    incredMass =  1.0 - credMass
    def intervalWidth(lowTailPr):
        return ICDFname(credMass+ lowTailPr,**kwargs) - ICDFname(lowTailPr,**kwargs)
    optInfo = minimize_scalar(intervalWidth, bounds= (0,incredMass),method='Golden')
    HDIlowTailPr = optInfo.x
    return (ICDFname(HDIlowTailPr,**kwargs),ICDFname(HDIlowTailPr+credMass,**kwargs))

def BernBeta(priorBetaAB,Data, HDImass=0.95,showHDI=True):
    '''
    priorBetaAB: Tuple of beta(a,b) parameters
    '''
    # For notational convenience, rename components of priorBetaAB:
    a = priorBetaAB[0]
    b = priorBetaAB[1]

    z = np.sum(Data) # No of heads
    N = len(Data)

    if len(priorBetaAB) != 2:
        raise ValueError("priorBetaAB must be a tuple of two values")
    if not(np.all((Data == 0) | (Data == 1))):
        raise ValueError("Data values must be 0 or 1")
    if any( _ < 0 for _ in priorBetaAB):
        raise ValueError("priorBetaAB values must be nonnegative")

    fig, ax = plt.subplots(3, 1,figsize=(16, 16))
    Theta = np.arange(0.001,1, 0.001) # points for plotting
    pTheta = beta.pdf(Theta, a, b) # prior for plotting
    pThetaGivenData = beta.pdf(Theta,a+z,b+N-z)
    pDataGivenTheta = Theta**z *(1 - Theta)**(N-z)
    ## Plotting the prior
    ax[0].fill_between(Theta, pTheta)
    ylabel = "Beta(θ|" + str(a) + ','+ str(b) + ")"
    ax[0].set(ylabel = ylabel,title = 'Prior(beta)',xlabel= 'θ')
    HDIinfo = HDIofICDF(beta.ppf,a=a,b=b)
    HDIheight = stats.beta.pdf(HDIinfo,a=a,b=b).mean()
    if showHDI and (a+b-2) >0 :
            ax[0].hlines(y=HDIheight,xmin = HDIinfo[0], xmax = HDIinfo[1])
            ax[0].vlines(x=HDIinfo[0],ymin = 0, ymax = HDIheight,linestyles = 'dashed')
            ax[0].vlines(x=HDIinfo[1],ymin = 0, ymax = HDIheight,linestyles = 'dashed')
            s = str(int(HDImass*100)) + '% HDI'
            ax[0].text(np.mean(HDIinfo), HDIheight + 0.00001,s,fontsize= 20)
            ax[0].text(HDIinfo[0], HDIheight + 0.01,'{:04.3f}'.format(HDIinfo[0]),fontsize= 20)
            ax[0].text(HDIinfo[1], HDIheight + 0.01,'{:04.3f}'.format(HDIinfo[1]),fontsize= 20)

    ### plotting the likelihood
    ax[1].fill_between(Theta, pDataGivenTheta)
    ax[1].set(xlabel = 'θ',title = 'Likelihood(Bernoulli)',ylabel='p(D|θ)')
    text = 'Data: z= {0}, N= {1}, max at  {2:.3f}'.format(z,N,Theta[np.argmax(pDataGivenTheta)])
    ax[1].text(0,0.7,text,transform=ax[1].transAxes,fontsize=20,wrap=True)


    ## Plotting the Posterior
    ax[2].fill_between(Theta, pThetaGivenData)
    ylabel = "Beta(θ|" + str(a+z) + ','+ str(b+N-z) + ")"
    ax[2].set(ylabel = ylabel,title = 'Posterior(beta)',xlabel= 'θ')
    HDIinfo = HDIofICDF(beta.ppf,a=a+z,b=b+N-z)
    HDIheight = stats.beta.pdf(HDIinfo,a=a+z,b=b+N-z).mean()
    if showHDI and (a+b-2) >0 :
            ax[2].hlines(y=HDIheight,xmin = HDIinfo[0], xmax = HDIinfo[1])
            ax[2].vlines(x=HDIinfo[0],ymin = 0, ymax = HDIheight,linestyles = 'dashed')
            ax[2].vlines(x=HDIinfo[1],ymin = 0, ymax = HDIheight,linestyles = 'dashed')
            s = str(int(HDImass*100)) + '% HDI'
            ax[2].text(np.mean(HDIinfo), HDIheight + 0.00001,s,fontsize= 20)
            ax[2].text(HDIinfo[0], HDIheight + 0.01,'{:04.3f}'.format(HDIinfo[0]),fontsize= 20)
            ax[2].text(HDIinfo[1], HDIheight + 0.01,'{:04.3f}'.format(HDIinfo[1]),fontsize= 20)
    plt.show()
    return (a+z, b + N-z)
