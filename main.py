from stl import mesh
from mesh import Mesh
from scalar_field import ScalarField
from matplotlib import pyplot
from mpl_toolkits import mplot3d


def plot(
    mesh: Mesh, 
    field: ScalarField
):
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)

    mesh.plot(figure, axes)
    field.plot(figure, axes)

    axes.auto_scale_xyz(
        [-2, 2],
        [-2, 2],
        [-2, 2],
    )
    pyplot.show()


if __name__ == '__main__':
    mesh = Mesh('meshes/cube.stl')
    field = ScalarField()

    plot(mesh, field)
