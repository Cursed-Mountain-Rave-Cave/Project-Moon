from datetime import datetime
from stl import mesh
from mesh import Mesh
from scalar_field import ScalarField
from matplotlib import pyplot
from mpl_toolkits import mplot3d


def plot(
    mesh: Mesh, 
    field: ScalarField,
    borders
):
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(
        figure,  
        auto_add_to_figure=False
    )
    figure.add_axes(axes)

    mesh.plot(figure, axes)
    field.plot(figure, axes)

    l = 1.5
    axes.auto_scale_xyz(*borders)
    pyplot.show()


if __name__ == '__main__':
    borders = [
        [-5, 5],
        [-5, 5],
        [-5, 5],
    ]
    mesh = Mesh('meshes/cube.stl')
    field = ScalarField(20, *borders[0], *borders[1], *borders[2])
    
    t = datetime.now()

    mask = mesh.contains_mask(
        field.xv, 
        field.yv, 
        field.zv
    )
    print('Calculate mask', (datetime.now() - t).total_seconds())

    field.mask = mask
    field.init_borders(15, 0)
    field.iterate(n=1e5, precision=1e-6)

    plot(mesh, field, borders)
