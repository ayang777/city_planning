import sys
import random
import collections 
import copy
import osmnx as ox
import matplotlib.pyplot as plt
ox.config(use_cache=True, log_console=True)
import numpy as np
import networkx as nx
import geopandas as gpd
import pandas as pd

#%matplotlib inline
'''
def cleaned_intersections_map():	
    G = ox.graph_from_place('San Francisco, California', network_type='drive')
    G_proj = ox.project_graph(G)
    #fig, ax = ox.plot_graph(G_proj, fig_height=20, node_color='orange', node_size=30, node_zorder=2, node_edgecolor='k')
    intersections = ox.clean_intersections(G_proj, tolerance=15, dead_ends=False)
    points = np.array([point.xy for point in intersections])
    fig, ax = ox.plot_graph(G_proj, fig_height=10, show=False, close=False, node_alpha=0)
    ax.scatter(x=points[:,0], y=points[:,1], zorder=2, color='#66ccff', edgecolors='k')
    plt.show()

def plot_shape():
	city = ox.gdf_from_place('San Francisco, California')
	ox.plot_shape(ox.project_gdf(city))

def plot_graph_driving():
	G = ox.graph_from_place('San Francisco, California', network_type='drive')
	ox.plot_graph(G)'''




def main():
	city = ox.gdf_from_place('San Francisco, California, USA')
	G = ox.graph_from_place('San Francisco, California, USA')
	fullTransition = collections.defaultdict(dict)
	for node in G.nodes():
		#print G.node[node].keys()
		#print node['lat']
		nodeLat = G.nodes[node]['x']
		nodeLong = G.nodes[node]['y']
		key = (nodeLat, nodeLong)

		if key not in fullTransition: 
			allEdgeList = []
			allEdges = G.edges(node)
			for edge in allEdges: 
				transition = edge[1]
				if transition in G.nodes():
					transitionLat = G.nodes[transition]['x']
					transitionLong = G.nodes[transition]['y']
					allEdgeList.append((transitionLat, transitionLong))
			fullTransition[key] = allEdgeList
			#fullTransition[key] = 0

	new_df = []
	for k, v in fullTransition.iteritems():
		for value in v:
			new_df.append([k,value])
	ndf = pd.DataFrame(new_df, columns = ['s', 's*'])
	ndf.to_csv("edges.csv")







	#ox.plot_graph(G)
	#print G.edges()
	#edges = ox.graph_to_gdfs(city, nodes=False, edges=True)
	#nodes = ox.graph_to_gdfs(city, nodes=True, edge=False)
	#print(edges.head())
    
    #plot_shape()

        
main()

