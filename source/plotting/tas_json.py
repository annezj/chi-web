'''
Plot GFS global forecast on world map
'''
import plotly
from plotly.graph_objs import *
import json
import pandas
from pandas.io.json import json_normalize
'''
load data from json file and flatten
'''
datafile="/Users/annejones/chiweb/data/gfs/json/tas-2m-gfs-1.0.json"
print("loading data from" + datafile)
with open(datafile) as f:
    d = json.load(f)
d = json_normalize(d)
df = pandas.DataFrame({'T2m':d['data'].loc[0]})
'''
Get header info
'''
nx=d['header.nx'][0]
ny=d['header.ny'][0]
lo1=d['header.lo1'][0]
lo2=d['header.lo2'][0]
la1=d['header.la1'][0]
la2=d['header.la2'][0]
dx=d['header.dx'][0]
dy=d['header.dy'][0]
ref_time=d['header.refTime'][0]
fcst_time=d['header.forecastTime'][0]
len(df['T2m'])
'''
Generate the grid and combine with data ready to plot
'''
import numpy as np
xgrid=np.linspace(start=lo1,stop=lo2,num=nx)
ygrid=np.linspace(start=la1,stop=la2,num=ny)
y=np.repeat(ygrid,nx)
x=np.tile(xgrid,ny)
trace1 = {"x" : x, "y" : y, "z" : df['T2m']-273.15,
  "autocolorscale": False, 
  "colorbar": {"title": "Temperature C"}, 
  "colorscale": [
    [0, "rgb(5, 10, 172)"], [0.35, "rgb(106, 137, 247)"], [0.5, "rgb(190,190,190)"], 
      [0.6, "rgb(220, 170, 132)"], [0.7, "rgb(230, 145, 90)"], [1, "rgb(178, 10, 28)"]], 
  "connectgaps": False, 
  "contours": {
    "coloring": "fill", 
    "end": 45.0, 
    "showlines": True, 
    "size": 2.5, 
    "start": 5.0
  }, 
  "name": "00 UTC", 
  "reversescale": False, 
  "type": "contour", 
  "zauto": False, 
  "zmax": 45.0, 
  "zmin": 5.0
}

'''
Set layout and plot
'''
data = Data([trace1])
layout = {
  "autosize": False, 
  "height": 800, 
  "legend": {
    "x": 0.861031518625, 
    "y": 0.1
  }, 
  "title": "Temperature at +00h, GFS 1deg Forecast, UTC Start time : 31/01/2018", 
  "width": 1200, 
  "xaxis": {
    "autorange": False, 
    "gridwidth": 1.2, 
    "mirror": True, 
    "range": [lo1, lo2], 
    "showline": True, 
    "ticks": "", 
    "title": "Longitude", 
    "type": "linear", 
    "zeroline": False
  }, 
  "yaxis": {
    "autorange": False, 
    "gridwidth": 1.2, 
    "mirror": True, 
    "range": [la2, la1], 
    "showline": True, 
    "ticks": "", 
    "title": "Latitude", 
    "type": "linear", 
    "zeroline": False
  }
}
fig = Figure(data=data, layout=layout)
plot_url = plotly.offline.plot(fig)
