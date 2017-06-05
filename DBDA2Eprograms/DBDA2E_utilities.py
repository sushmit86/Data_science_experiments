# Author :Sushmit Roy (sushmit86@gmail.com)
# This module tries to replicate DBDA2E-utilities.R second edition
# Implemented in Python 3.6



#### Bokeh libraries

from bokeh.plotting import figure
from bokeh.models import Label,FixedTicker,ColumnDataSource,LabelSet

import numpy as np
import scipy as sc
import pymc3


JS_CODE = """
import {Label, LabelView} from "models/annotations/label"

export class LatexLabelView extends LabelView
  render: () ->

    #--- Start of copied section from ``Label.render`` implementation

    ctx = @plot_view.canvas_view.ctx

    # Here because AngleSpec does units tranform and label doesn't support specs
    switch @model.angle_units
      when "rad" then angle = -1 * @model.angle
      when "deg" then angle = -1 * @model.angle * Math.PI/180.0

    if @model.x_units == "data"
      vx = @xmapper.map_to_target(@model.x)
    else
      vx = @model.x
    sx = @canvas.vx_to_sx(vx)

    if @model.y_units == "data"
      vy = @ymapper.map_to_target(@model.y)
    else
      vy = @model.y
    sy = @canvas.vy_to_sy(vy)

    if @model.panel?
      panel_offset = @_get_panel_offset()
      sx += panel_offset.x
      sy += panel_offset.y

    #--- End of copied section from ``Label.render`` implementation

    # Must render as superpositioned div (not on canvas) so that KaTex
    # css can properly style the text
    @_css_text(ctx, "", sx + @model.x_offset, sy - @model.y_offset, angle)

    # ``katex`` is loaded into the global window at runtime
    # katex.renderToString returns a html ``span`` element
    katex.render(@model.text, @el, {displayMode: true})

export class LatexLabel extends Label
  type: 'LatexLabel'
  default_view: LatexLabelView
"""

class LatexLabel(Label):
    """A subclass of the Bokeh built-in `Label` that supports rendering
    LaTex using the KaTex typesetting library.

    Only the render method of LabelView is overloaded to perform the
    text -> latex (via katex) conversion. Note: ``render_mode="canvas``
    isn't supported and certain DOM manipulation happens in the Label
    superclass implementation that requires explicitly setting
    `render_mode='css'`).
    """
    __javascript__ = ["https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.js"]
    __css__ = ["https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.css"]
    __implementation__ = JS_CODE




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

def plotPost(paramSampleVec, cenTend = 'mode', col = None, showCurve=False ,title = None,xlab = None,credMass=0.95):
    col = 'skyblue' if col is None else col 
    xlab = 'θ' if xlab is None else xlab
    hist, edges = np.histogram(paramSampleVec, density=True, bins=20)
    cenTendHt = 0.9*max(hist)
    mode=sc.stats.mode(paramSampleVec)[0][0]
    HDI= pymc3.stats.hpd(paramSampleVec,alpha = 1 - credMass)
    ## Bokeh plotting
    p1 = figure(title=title,tools="save")
    bottom=0.00001
    HDI_x = [ round(HDI[0],2), round(HDI[1],2)]
    HDI_y = [bottom,bottom]
    source = ColumnDataSource(data=dict(HDI_x = HDI_x,HDI_y =HDI_y))
    p1.quad(top=hist, bottom=bottom, left=edges[:-1], right=edges[1:],
        fill_color=col, line_color="white")
    p1.line([HDI[0],HDI[1]], [bottom,bottom], line_width=2,line_color= "black")

    mode_label = Label(x=mode, y=cenTendHt, x_units='data', y_units='data',
                 text='mode = {0:.2f}'.format(mode), render_mode='css',
                 border_line_color='white', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0)
    labels = LabelSet(x='HDI_x', y='HDI_y', text='HDI_x', level='glyph', source=source, render_mode='canvas')
    p1.add_layout(mode_label)
    p1.add_layout(labels)
    p1.xaxis.axis_label = xlab
    p1.xaxis.minor_tick_line_color = None
    p1.xaxis.bounds = (0, 1)
    p1.ygrid.visible = False
    p1.yaxis.visible = False
    p1.xgrid.visible = False

    return p1



def func_latex():
    x = np.arange(0.0, 1.0 + 0.01, 0.01)
    y = np.cos(2*2*np.pi*x) + 2

    p = figure(title="LaTex Demonstration",plot_width=500, plot_height=500)
    p.line(x, y)

    # Note: must set ``render_mode="css"``
    latex = LatexLabel(text="",
                   x=0.5, y=2,
                    text_font_size='10pt',render_mode='css',
                   background_fill_color='#ffffff')

    #p.add_layout(latex)
    return(p)






