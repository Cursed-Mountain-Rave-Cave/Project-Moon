import numpy as np
from tqdm import tqdm


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
        self.f = np.zeros(self.xv.shape)
        self.mask = np.zeros(self.xv.shape, dtype=np.int32)

    def init_borders(self, f_inner, f_border):
        self.f[0, :, :] = f_border
        self.f[-1, :, :] = f_border
        self.f[:, 0, :] = f_border
        self.f[:, -1, :] = f_border
        self.f[:, :, 0] = f_border
        self.f[:, :, -1] = f_border
        self.f[self.mask] = f_inner

    def iterate(self, precision=0.0, n=10):
        sub_mask = self.mask[1:-1, 1:-1, 1:-1]
        dif = -1

        for _ in tqdm(range(int(n)), desc='Calculation'):
            new_f = (
                self.f[:-2, 1:-1, 1:-1]
                + self.f[2:, 1:-1, 1:-1]
                + self.f[1:-1, :-2, 1:-1]
                + self.f[1:-1, 2:, 1:-1]
                + self.f[1:-1, 1:-1, :-2]
                + self.f[1:-1, 1:-1, 2:]
            ) * (sub_mask == 0) / 6 + self.f[1:-1, 1:-1, 1:-1] * (sub_mask != 0)
            dif = np.abs(new_f - self.f[1:-1, 1:-1, 1:-1]).max()
            self.f[1:-1, 1:-1, 1:-1] = new_f

            if dif < precision:
                print("MAE is:", dif)
                return 

        print("MAE is:", dif)

    def plot(self, figure, axes):
        k = 20
        # m = ~self.mask[k:,:,:]
        m = self.f[k:,:,:] > 1
        p = axes.scatter3D(
            self.xv[k:,:,:][m].flatten()[::],
            self.yv[k:,:,:][m].flatten()[::],
            self.zv[k:,:,:][m].flatten()[::],
            s=2,
            c=self.f[k:,:,:][m].flatten()[::]
        )
        figure.colorbar(p)
