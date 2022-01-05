"""
==========================
3D voxel / volumetric plot
==========================

Demonstrates plotting 3D volumetric objects with `.Axes3D.voxels`.
"""

import matplotlib.pyplot as plt
import numpy as np
import random as rd

i = 0
while i < 5:
	name = i +1
	# prepare some coordinates
	x, y, z = np.indices((24, 24, 24))
	
	# draw cuboids in the top left and bottom right corners, and a link between
	# them
	cube1 = (x < rd.randint(0,24)) & (y < rd.randint(0,24)) & (z < rd.randint(0,24))
	cube2 = (x >= rd.randint(0,24)) & (y >= rd.randint(0,24)) & (z >= rd.randint(0,24))
	link = abs(x - y) + abs(y - z) + abs(z - x) <= 1
	
	# combine the objects into a single boolean array
	voxelarray = cube1 | cube2 | link
	
	list=['green','blue','yellow','red','purple']
	# set the colors of each object
	colors = np.empty(voxelarray.shape, dtype=object)
	colors[link] = rd.choice(list)
	colors[cube1] = rd.choice(list)
	colors[cube2] = rd.choice(list)
	
	# and plot everything
	ax = plt.figure().add_subplot(projection='3d')
	ax.voxels(voxelarray, facecolors=colors, alpha=0.5)
	plt.axis('off')
	plt.savefig('NFT_%s.png' % name, transparent=True)
	i = i +1
