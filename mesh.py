#Some info about numpy-stl: https://pypi.org/project/numpy-stl/
import os
import stl
from matplotlib import pyplot
from mpl_toolkits import mplot3d


class Mesh:

    def __init__(self, filepath: str) -> None:
        self.mesh = stl.mesh.Mesh.from_file(filepath)

    def show(self):
        figure = pyplot.figure()
        axes = mplot3d.Axes3D(figure)
        axes.add_collection3d(
            mplot3d.art3d.Poly3DCollection(self.mesh.vectors)
        )
        scale = self.mesh.points.flatten()
        axes.auto_scale_xyz(scale, scale, scale)
        pyplot.show()
