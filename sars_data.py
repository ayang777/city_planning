import pandas as pd
import numpy as np
import math  
from collections import defaultdict


#s, a, r, s'
df = pd.read_csv('street_intersections.csv')

#neg and pos of lat and long
grouped = df.groupby(by="ST_NAME")


sp = {}

def make_coords_dict(group):
	coords = [split_coord(coord) for coord in group['the_geom']]
	cnns = group['CNN'].tolist()

	coords_dict = defaultdict(int)

	for i, coord in enumerate(coords):
		coords_dict[cnns[i]] = coords[i]

	return coords_dict


def split_coord(coord):
	new_coords = coord.split()[1:]
	lat = float(new_coords[1][:-1])
	lon = float(new_coords[0][1:])
	return (lat, lon)

def distance(p1, p2):
	x1 = p1[0]
	y1 = p1[1]
	x2 = p2[0]
	y2 = p2[1]
	dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
	if dist == 0: return 1
	return dist  


def main():
	for name, group in grouped:


		coords_dict = make_coords_dict(group)


		for cnn, coord in coords_dict.iteritems():
			#print "cur coord: " + str(coord)

			dists = defaultdict(int)
			for cur_cnn, cur_coord in coords_dict.iteritems():
				dists[cur_cnn] = distance(coord, cur_coord)

			sort_dists = sorted(dists.items(), key=lambda tup: tup[1])

			# print coords_dict[sort_dists[0][0]]
			# print coords_dict[sort_dists[1][0]]
			cur_sps = []
			if len(sort_dists) == 1:
				cur_sps.append(sort_dists[0])

			elif len(sort_dists) > 1:
				cur_sps = [sort_dists[0], sort_dists[1]]

			if cnn in sp:
				cur_list = sp[cnn]
				sp[cnn] = list(set(cur_list + cur_sps))
				#print sp[cnn]
			else:
				sp[cnn] = cur_sps
			#print sp[cnn]


	print len(sp)

main()