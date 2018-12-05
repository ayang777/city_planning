import pandas as pd
import numpy as np
import math

new_df = []
df = pd.read_csv('edges_small.csv')

def distance(p1, p2):
	x1 = float(p1[0])
	y1 = float(p1[1])
	x2 = float(p2[0])
	y2 = float(p2[1])
	dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 
	return dist  

def split_coord(coord):

	new_coords = coord.split()

	lat = float(new_coords[1][:-1])
	lon = float(new_coords[0][1:-1])

	return (lat, lon)

for name, row in df.iterrows():
	s = split_coord(row['s'])
	sp = split_coord(row['sp'])

	cur_line = [s, sp] #s, a
	dist = distance(s, sp)
	if dist == 0: continue
	cur_line.append(-dist * 10000) #r
	cur_line.append(sp)
	new_df.append(cur_line)

ndf = pd.DataFrame(new_df, columns = ['S', 'A', 'R', 'SP'])

#print ndf

ndf.to_csv("SARSP_small.csv")

# df2 = pd.read_csv('SARSP.csv')
# grouped = df2.groupby(by="S")
# print grouped.groups.keys()