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
	sorted_points = sorted(sampleVec)
	ciIdxInc = np.ceil(credMass * len(sorted_points)).astype('int')
	nCIs = len(sorted_points) - ciIdxInc
	ciWidth = [0]*nCIs
	for i in range(0, nCIs):
		ciWidth[i] = sorted_points[i + ciIdxInc] - sorted_points[i]
	HDImin = sorted_points[ciWidth.index(min(ciWidth))]
	HDImax = sorted_points[ciWidth.index(min(ciWidth))+ciIdxInc]
	return(HDImin, HDImax)

def plotPost(paramSampleVec, cenTend = "mode", col = None,showCurve=FALSE):
	if col is None: col = "skyblue" : color = col
	print('test')



