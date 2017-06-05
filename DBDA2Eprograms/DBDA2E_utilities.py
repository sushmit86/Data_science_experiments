# Author :Sushmit Roy (sushmit86@gmail.com)
# This module tries to replicate DBDA2E-utilities.R second edition
# Implemented in Python 3.6



#### Bokeh libraries

from bokeh.plotting import figure, show
from bokeh.models import Label

import numpy as np
import scipy as sc
import pymc3




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

def plotPost(paramSampleVec, cenTend = 'mode', col = None, showCurve=False ,title = None,xlab = None):
    col = 'skyblue' if col is None else col 
    xlab = 'θ' if xlab is None else xlab
    hist, edges = np.histogram(paramSampleVec, density=True, bins=20)
    cenTendHt = 0.9*max(hist)
    mode=sc.stats.mode(paramSampleVec)[0][0]

    ## Bokeh plotting
    p1 = figure(title=title,tools="save")
    p1.quad(top=hist, bottom=0.00001, left=edges[:-1], right=edges[1:],
        fill_color=col, line_color="white")
    p1.ygrid.visible = False
    p1.yaxis.visible = False
    p1.xgrid.visible = False
    mode_label = Label(x=mode, y=cenTendHt, x_units='data', y_units='data',
                 text='mode = {0:.2f}'.format(mode), render_mode='css',
                 border_line_color='white', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0)
    p1.add_layout(mode_label)
    p1.xaxis.axis_label = xlab
    return p1





