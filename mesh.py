import stl
import numpy as np
import numpy.linalg as linalg
from mpl_toolkits import mplot3d


class Mesh:

    def __init__(self, filepath: str) -> None:
        self.mesh = stl.mesh.Mesh.from_file(filepath)
        self.vectors = self.mesh.vectors
        self.x = self.vectors[:, :, 0].flatten()
        self.y = self.vectors[:, :, 1].flatten()
        self.z = self.vectors[:, :, 2].flatten()

    def contains(self, x0, y0, z0) -> bool:
        x1 = x0 + 11
        y1 = y0 + 7
        z1 = z0 + 5

        intersections_count = 0
        for a, b, c in self.vectors:
            se = linalg.det(np.array([
                [x0   - a[0], y0   - a[1], z0   - a[2]],
                [b[0] - a[0], b[1] - a[1], b[2] - a[2]],
                [c[0] - a[0], c[1] - a[1], c[2] - a[2]],
            ])) * linalg.det(np.array([
                [x1   - a[0], y1   - a[1], z1   - a[2]],
                [b[0] - a[0], b[1] - a[1], b[2] - a[2]],
                [c[0] - a[0], c[1] - a[1], c[2] - a[2]],
            ]))
            ae = linalg.det(np.array([
                [a[0] - x0, a[1] - y0, a[2] - z0],
                [b[0] - x0, b[1] - y0, b[2] - z0],
                [c[0] - x0, c[1] - y0, c[2] - z0],
            ])) * linalg.det(np.array([
                [x1   - x0, y1   - y0, z1   - z0],
                [b[0] - x0, b[1] - y0, b[2] - z0],
                [c[0] - x0, c[1] - y0, c[2] - z0],
            ]))
            be = linalg.det(np.array([
                [b[0] - x0, b[1] - y0, b[2] - z0],
                [a[0] - x0, a[1] - y0, a[2] - z0],
                [c[0] - x0, c[1] - y0, c[2] - z0],
            ])) * linalg.det(np.array([
                [x1   - x0, y1   - y0, z1   - z0],
                [a[0] - x0, a[1] - y0, a[2] - z0],
                [c[0] - x0, c[1] - y0, c[2] - z0],
            ]))
            ce = linalg.det(np.array([
                [c[0] - x0, c[1] - y0, c[2] - z0],
                [a[0] - x0, a[1] - y0, a[2] - z0],
                [b[0] - x0, b[1] - y0, b[2] - z0],
            ])) * linalg.det(np.array([
                [x1   - x0, y1   - y0, z1   - z0],
                [a[0] - x0, a[1] - y0, a[2] - z0],
                [b[0] - x0, b[1] - y0, b[2] - z0],
            ]))
            if se < 0 and ae > 0 and be > 0 and ce > 0:
                intersections_count += 1
        return intersections_count % 2 == 1

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
