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

    def contains(
        self, 
        x0, 
        y0 = None, 
        z0 = None, 
        n_tries=3,
        l = 10
    ) -> bool:
        if y0 is None and z0 is None:
            x0, y0, z0 = x0
        
        results = list()

        for _ in range(n_tries):
            x1 = x0 + np.random.uniform(-l, l)
            y1 = y0 + np.random.uniform(-l, l)
            z1 = z0 + np.random.uniform(-l, l)
            # TODO replace with sum with random vector with constant length

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
            results.append(intersections_count % 2 == 1)
        
        return np.mean(results) > 0.5

    def contains_mask(self, xv, yv, zv):
        return np.apply_along_axis(
            self.contains,
            0,
            np.array([
                xv, 
                yv, 
                zv
            ]),
        )

    def plot(self, figure, axes):
        axes.add_collection3d(
            mplot3d.art3d.Poly3DCollection(
                self.vectors, 
                facecolors='w', 
                edgecolors='k',
                linewidths=1,
                alpha=0.1
            )
        )
