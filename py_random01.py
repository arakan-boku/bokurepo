import numpy.random as rnd
from matplotlib import pyplot as plt

labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
          16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

rnd01 = rnd.normal(0, 2, 30)
rnd02 = rnd.chisquare(1, 30)
rnd03 = rnd.exponential(1, 30)

plt.subplot(1, 3, 1)
plt.scatter(x=labels, y=rnd01)
plt.xlabel('normal')
plt.subplot(1, 3, 2)
plt.scatter(x=labels, y=rnd02)
plt.xlabel('chisquare')
plt.subplot(1, 3, 3)
plt.scatter(x=labels, y=rnd03)
plt.xlabel('exponential')
plt.show()
