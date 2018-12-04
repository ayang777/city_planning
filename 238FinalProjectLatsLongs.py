import sys
import pandas as pd
import numpy as np
import timeit
import random
import collections
import copy
import geopy 
from geopy.exc import GeocoderTimedOut
import csv 
from geopy.geocoders import GoogleV3
import json


def main():
    geolocator = GoogleV3(api_key= "AIzaSyAvb-2SXwL71vC4J3_9h0HGrFDYmtqmDsY")
    start = timeit.default_timer()
    #address = geolocator.reverse(point)
    
    inputfilename = "SF Data updated with Lats Longs.csv"
    fullList = []
    with open(inputfilename, 'r') as f:
    	reader = csv.reader(f)
    	for i, line in enumerate(reader):
    		fullList.append(line)
    		#address = geolocator.gecode(line)
    		#print address
    #print fullList
    latLoc = []
    for currAddress in fullList: 
    	fullString = currAddress[0] + ', ' + currAddress[1] + ', ' + currAddress[2] + ", " + "USA"
    	loc = geolocator.geocode(fullString, timeout = 100)
    	if loc != None: 
    		#print json.dumps(loc.raw, indent=4)
            latLoc.append((loc.latitude, loc.longitude))
        else: 
            print fullString

    #with open("Lats + Longs", 'w') as f:
    	#for data in latLoc:
    		#lat = data[0]
    		#lon = data[1]
    		#f.write(str(lat) + ',' + str(lon) +'\n')
    	#f.close()

    		#print loc.latitude, loc.longitude
    	#print latLong


    #data = pd.read_csv(inputfilename, encoding='utf-8')
    #print data
    stop = timeit.default_timer()
    print('Time: ', stop-start)
        
main()