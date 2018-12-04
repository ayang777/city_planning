import pandas as pd
import numpy as np

df = pd.read_csv('street_intersections.csv')

#split lat and long into different columns
#combine intersections...there may be more than 2
#s, a, r, s' 

new_df = []

grouped = df.groupby(by="CNN")
#print grouped.groups
def split_coord(row, coord):
	new_coords = coord.split()[1:]
	row.append(float(new_coords[1][:-1]))
	row.append(float(new_coords[0][1:]))



def concat_streets(row, streets, street_types):
	street_list = []
	for idx, st in enumerate(streets):
		street_list.append(str(st) + " " + str(street_types[idx]))
	row.append(street_list)

for name,group in grouped:
	row = [name]
	#print group
	concat_streets(row, group['ST_NAME'].tolist(), group['ST_TYPE'].tolist())
	split_coord(row, group.iloc[0]['the_geom'])
	#print row
	new_df.append(row)

print len(new_df)

ndf = pd.DataFrame(
	new_df,
	columns = ['CNN', 'ST_NAMES', 'LAT', 'LONG']
	)

print ndf

ndf.to_csv("cleaned_intersections.csv")


# cur_cnn = 0
# for row in dataset:
# 	if cur_cnn 


