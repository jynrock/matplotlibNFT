"""
==========================
3D voxel / volumetric plot
==========================

Demonstrates plotting 3D volumetric objects with `.Axes3D.voxels`.
"""

import matplotlib.pyplot as plt
import numpy as np
import random as rd


# prepare some coordinates
x, y, z = np.indices((24, 24, 24))

# draw cuboids in the top left and bottom right corners, and a link between
# them
cube1 = (x < rd.randint(0,24)) & (y < rd.randint(0,24)) & (z < rd.randint(0,24))
cube2 = (x >= rd.randint(0,24)) & (y >= rd.randint(0,24)) & (z >= rd.randint(0,24))
link = abs(x - y) + abs(y - z) + abs(z - x) <= 2

# combine the objects into a single boolean array
voxelarray = cube1 | cube2 | link

# set the colors of each object
colors = np.empty(voxelarray.shape, dtype=object)
colors[link] = 'red'
colors[cube1] = 'blue'
colors[cube2] = 'green'

# and plot everything
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, alpha=0.5)
plt.axis('off')
plt.savefig('books_read.png', transparent=True)