# -*- coding: utf-8 -*-
"""frp_hexagon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KQQhxxlSGLq81Bl-sVUIBR6bZ_MKmrbh
"""

#install packages into our current session
!pip install numpy
!pip install bokeh

#Load our data that is in .csv format. The one supplied was titled: final_genome.csv
#Due to our files being so large, this may take a couple mins
from google.colab import files
uploaded = files.upload()

#load our packages
from bokeh.io import output_notebook
from bokeh.io import output_file, show
from bokeh.models import HoverTool
from bokeh.plotting import figure
from bokeh.util.hex import hexbin
import pandas as pd
import io

# sanity check. Just to make sure the file was uploaded correctly
df.head()

#read our .csv into a dataframe, deliminated by ','
df = pd.read_csv(io.StringIO(uploaded['final_genome.csv'].decode('utf-8')), sep = ',')

#Set DataFrames to X/Y Axis.
#Note: we devided I_Begin/100000 for scaling purposes
x = df.I_Begin/100000
y = df.Identity

#Set axis labels, title, aspect ratio, and background colors
p = figure(title= "Fragment Recruitment Plots", match_aspect=True, background_fill_color = '#440154',
          x_axis_label='Size (np)', y_axis_label = 'Percent Identity (%)')

#Include the tools that we need for end user
TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

#Limit range to max 100 --> 100%
p.y_range.start = 88
p.y_range.end = 102

#make grids not visable. Takes away from everything
p.grid.visible = False

#Intiate the size of the hexagons, hovercolor, and text
p.hexbin(x, y, size=1, hover_color="pink", hover_alpha=0.8)
hover = HoverTool(tooltips=[("count", "@c"), ("(x,y)", "($x, $y)")])
p.add_tools(hover)

#needed to output inline
output_notebook()
show(p)