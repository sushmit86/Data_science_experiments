### Author: Sushmit Roy
import pandas as pd
import numpy as np
from scipy import stats
import xarray

np.random.seed(1)
### Bokeh Libraries
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh.models import Span,Range1d,Label,LabelSet
from bokeh.layouts import column,row
output_notebook()


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
    if pTheta.sum() != 1:
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
    ## plot the Posterior
    plot_prior = figure(plot_width=800, plot_height=250, title='Prior')
    plot_prior.vbar(x=Theta, width=0.001, bottom=0,top=pTheta)

    ## Plot the likelihood
    plot_likelihood = figure(plot_width=800, plot_height=250, title='Likelihood')
    plot_likelihood.vbar(x=Theta, width=0.001, bottom=0,top=Likelihood)

    ## Plot the Posterior
    plot_posterior = figure(plot_width=800, plot_height=250, title='Posterior')
    plot_posterior.vbar(x=Theta, width=0.001, bottom=0,top=Posterior)

    show(column(plot_prior,plot_likelihood,plot_posterior))
