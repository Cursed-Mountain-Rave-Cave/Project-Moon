"""
========================
3D surface (solid color)
========================

Demonstrates a very basic plot of a 3D surface using a solid color.
"""

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make data
# u = np.linspace(0, 2 * np.pi, 100)
# v = np.linspace(0, np.pi, 100)
# k = 3
# x = 10 * np.outer(np.cos(u), np.sin(v))[0:k, 0:k]
# y = 10 * np.outer(np.sin(u), np.sin(v))[0:k, 0:k]
# z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))[0:k, 0:k]

x = np.array([
    [0., 1., 2.],
    [0., 1., 2.]
])
y = np.array([
    [0., 0., 0.],
    [0., 1., 2.]
])
z = np.array([
    [0., 0., 0.],
    [0., 0., 0.1]
])

# Plot the surface
ax.plot_surface(x, y, z)

# plt.show()
fig.savefig("surface3d_2.png", dpi=250)
