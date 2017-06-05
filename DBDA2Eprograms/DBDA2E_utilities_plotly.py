# Author :Sushmit Roy (sushmit86@gmail.com)
# This module tries to replicate DBDA2E-utilities.R second edition
# Implemented in Python 3.6

import warnings
import numpy as np
import scipy as sc
warnings.filterwarnings("ignore")
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from scipy import stats
import pymc3

init_notebook_mode(connected=True)


def HDIofMCMC(sampleVec, credMass=0.95 ):
	  # Computes highest density interval from a sample of representative values,
	  #   estimated as shortest credible interval.
	  # Arguments:
	  #   sampleVec
	  #     is a vector of representative values from a probability distribution.
	  #   credMass
	  #     is a scalar between 0 and 1, indicating the mass within the credible
	  #     interval that is to be estimated.
	  # Value:
	  #   HDIlim is a vector containing the limits of the HDI
	  # We will avoid using this function instead of that we will be using pymc3 
	  # pymc3.stats.hpd(a)
	sorted_points = sorted(sampleVec)
	ciIdxInc = np.ceil(credMass * len(sorted_points)).astype('int')
	nCIs = len(sorted_points) - ciIdxInc
	ciWidth = [0]*nCIs
	for i in range(0, nCIs):
		ciWidth[i] = sorted_points[i + ciIdxInc] - sorted_points[i]
	HDImin = sorted_points[ciWidth.index(min(ciWidth))]
	HDImax = sorted_points[ciWidth.index(min(ciWidth))+ciIdxInc]
	return(HDImin, HDImax)

def plotPost(paramSampleVec, cenTend = 'mode', col = None, showCurve=False ,title = None):
	cenTendHt = 0.09*max(np.histogram(paramSampleVec,range=(0,1),bins=20,density=True)[0])
	#cenTendHt =0.35
	col = 'skyblue' if col is None else col 
	data = [go.Histogram(x=paramSampleVec ,histnorm='probability', autobinx=False,
    xbins=dict(
        start=0,
        end=1,
        size=0.05,
    ),marker=dict(
        color=col,
    ))]
	layout = go.Layout(
    title=title,
       yaxis=dict(
        showgrid=False,
        autotick=False
    ),
    xaxis=dict(
        title='$\\theta$',
        dtick=0.2,
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor='black'

    ),
     bargap=0.2,
     annotations=[
        dict(
            x=sc.stats.mode(paramSampleVec)[0][0],
            y=cenTendHt,
            xref='x',
            yref='y',
            text='mode = {0:.2f}'.format(sc.stats.mode(paramSampleVec)[0][0]),
            showarrow=False,
            ax=0,
            ay=-40
        )
    ]

    )

	fig = go.Figure(data=data,layout = layout)
	return py.iplot(fig)





