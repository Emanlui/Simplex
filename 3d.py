import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point  = np.array([1, 2, 3])
normal = np.array([1, 1, 2])

point2 = np.array([10, 50, 50])


d = -point.dot(normal)

xx, yy = np.meshgrid(range(100), range(100))

z = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(xx, yy, z, alpha=0.2)

ax.scatter(point2[0] , point2[1] , point2[2],  color='green')

plt.show()
