import numpy as np


class ScalarField:

    def __init__(
        self,
        n: int = 25,
        x_min: float = -2.,
        x_max: float = 2.,
        y_min: float = -2.,
        y_max: float = 2.,
        z_min: float = -2.,
        z_max: float = 2.,
    ) -> None:
        self.n = n

        self.x = np.linspace(x_min, x_max, self.n)
        self.y = np.linspace(y_min, y_max, self.n)
        self.z = np.linspace(z_min, z_max, self.n)

        self.xv, self.yv, self.zv = np.meshgrid(self.x, self.y, self.z)
        self.c = 1 / (1 + self.xv**2 + self.yv**2 + self.zv**2)

    def plot(self, figure, axes, mask):
        p = axes.scatter3D(
            self.xv[mask].flatten(),
            self.yv[mask].flatten(),
            self.zv[mask].flatten(),
            s=2,
            c=self.c[mask].flatten()
        )
        figure.colorbar(p)
