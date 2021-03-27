import stl
import numpy as np
from matplotlib import pyplot
from mpl_toolkits import mplot3d


class Mesh:

    def __init__(self, filepath: str) -> None:
        self.mesh = stl.mesh.Mesh.from_file(filepath)
        self.vectors = self.mesh.vectors
        self.x = self.vectors[:, :, 0].flatten()
        self.y = self.vectors[:, :, 1].flatten()
        self.z = self.vectors[:, :, 2].flatten()

    def show(self):
        figure = pyplot.figure()
        axes = mplot3d.Axes3D(figure)
        axes.add_collection3d(
            mplot3d.art3d.Poly3DCollection(
                self.vectors, 
                facecolors='w', 
                edgecolors='k',
                linewidths=1,
                alpha=0.5
            )
        )
        axes.auto_scale_xyz(
            [np.min(self.x), np.max(self.x)], 
            [np.min(self.y), np.max(self.y)], 
            [np.min(self.z), np.max(self.z)]
        )
        pyplot.show()
