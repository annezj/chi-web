#!/usr/bin/env python2.7
import pygrib as py
import numpy as np
print "starting grib read..."
file="/Users/annejones/data-science/python2.7/ecmwf/data/tigge.grb"
gr = py.open(file)
#print inventory
#for g in gr:
#    print g
print "grib file: " + gr.name
print 'found ' + str(gr.messages) + ' records'
g=gr[1]
print " getting lat and lons for message 1:"
print g.latlons()