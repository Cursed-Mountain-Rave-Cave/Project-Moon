#Some info about numpy-stl: https://pypi.org/project/numpy-stl/
import os
import numpy
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

filepath = os.path.join('..', 'meshes', 'cube.stl')

my_mesh = mesh.Mesh.from_file(filepath)
print(my_mesh.points) #Seems like a list of 12 triangles of model 

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(my_mesh.vectors))
scale = my_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)
pyplot.show()
