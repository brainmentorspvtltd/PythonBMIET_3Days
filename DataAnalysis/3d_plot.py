import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.array([i for i in range(1,301)])
y = np.random.randint(1,1000,300)
z = np.random.randint(100,500,300)

fig = plt.figure(figsize=(12,8))
ax = Axes3D(fig)
ax.scatter(x,y,z,color='red')

plt.show()
