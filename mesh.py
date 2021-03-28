import stl
import numpy as np
from mpl_toolkits import mplot3d


class Mesh:

    def __init__(self, filepath: str) -> None:
        self.mesh = stl.mesh.Mesh.from_file(filepath)
        self.vectors = self.mesh.vectors
        self.x = self.vectors[:, :, 0].flatten()
        self.y = self.vectors[:, :, 1].flatten()
        self.z = self.vectors[:, :, 2].flatten()

    def plot(self, figure, axes):
        axes.add_collection3d(
            mplot3d.art3d.Poly3DCollection(
                self.vectors, 
                facecolors='w', 
                edgecolors='k',
                linewidths=1,
                alpha=0.5
            )
        )

