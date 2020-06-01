import pandas as pd
import numpy as np
import pymc3 as pm
import scipy.stats as stats
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly import tools
from plotly.graph_objs import *

def plot_density(samples,PI = []):
	data = []
	hist_data = [samples]
	group_labels = ['group1']
	KDE = ff.create_distplot(hist_data, group_labels,show_hist=False,show_rug=False)
	layout = go.Layout(
	autosize=False,
	width=500,
	height=500,
	margin=go.Margin(
	    l=50,
	    r=50,
	    b=100,
	    t=100,
	    pad=4
	),
	xaxis=dict(title='x'),
	yaxis=dict(title='PDF(x)')
	)
	trace1 = go.Scatter(
         y= KDE['data'][0]['y'],
         x = KDE['data'][0]['x'],
        mode = 'lines',line=dict(width=2),name='PDF',
        fill= None)
	data.append(trace1)
	if not PI:
			return go.Figure(data=data, layout=layout)
	### plot the PI interval
	y = KDE['data'][0]['y']
	x = KDE['data'][0]['x']
	df=pd.DataFrame(y,x,columns=['Y'])
	df.index.name = 'X'
	df=df.loc[(df.index> PI[0]) & (df.index < PI[1]),:]

	trace2 = go.Scatter(y= df.Y.values,x = df.index,mode = 'line',fill= 'tozeroy',  
		line=dict(width=0.0),name='PI' + ' [' + str(PI[0]) + ',' + str(PI[1]) + ']')
	data.append(trace2)
	return go.Figure(data=data, layout=layout)




### scatter plots
def plot_scatter(x = [], y = []):
	data =[]
	layout = go.Layout(
	autosize=False,
	width=500,
	height=500,
	margin=go.Margin(
	    l=50,
	    r=50,
	    b=100,
	    t=100,
	    pad=4
	)
	)
	if not x:
		trace1 = go.Scatter(
         y = y,
         mode = 'circles')
	data.append(trace1)
	fig = go.Figure(data=data, layout=layout)
	return fig
