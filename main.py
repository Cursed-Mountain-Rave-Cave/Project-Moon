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

    axes.auto_scale_xyz(*borders)
    pyplot.show()


if __name__ == '__main__':
    l = 20
    borders = [
        [-l, l],
        [-l, l],
        [-l, l],
    ]
    mesh = Mesh('meshes/satellite_cubic.stl')
    field = ScalarField(50, *borders[0], *borders[1], *borders[2])
    
    t = datetime.now()
    mask = mesh.contains_mask(
        field.xv, 
        field.yv, 
        field.zv,
        True
    )
    print('Calculate mask', (datetime.now() - t).total_seconds())

    field.mask = mask
    field.init_borders(15, 0)
    field.iterate(n=1e2, precision=1e-4)

    plot(mesh, field, borders)
