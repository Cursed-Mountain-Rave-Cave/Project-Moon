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
    from datetime import datetime
    t = datetime.now()

    mesh = Mesh('meshes/cube.stl')
    
    print('Load mesh', (datetime.now() - t).total_seconds())
    t = datetime.now()
    
    field = ScalarField(n=10)
    
    print('Load field', (datetime.now() - t).total_seconds())
    t = datetime.now()

    mask = mesh.contains_mask(
        field.xv, 
        field.yv, 
        field.zv
    )
    
    print('Calculate mask', (datetime.now() - t).total_seconds())

    plot(mesh, field, mask)
