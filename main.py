from stl import mesh
from mesh import Mesh
from scalar_field import ScalarField
from matplotlib import pyplot
from mpl_toolkits import mplot3d


def plot(
    mesh: Mesh, 
    field: ScalarField,
    mask
):
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(
        figure,  
        auto_add_to_figure=False
    )
    figure.add_axes(axes)

    mesh.plot(figure, axes)
    field.plot(figure, axes, mask)

    l = 1.5
    axes.auto_scale_xyz(
        [-l, l],
        [-l, l],
        [-l, l],
    )
    pyplot.show()


if __name__ == '__main__':
    mesh = Mesh('meshes/cube.stl')
    field = ScalarField(n=20)

    mask = mesh.contains_mask(
        field.xv, 
        field.yv, 
        field.zv
    )

    plot(mesh, field, mask)
