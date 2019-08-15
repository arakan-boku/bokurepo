import numpy.random as nr
import numpy as np
from matplotlib import pyplot as plt

d = nr.poisson(0.05, 100)
print(d)

r = nr.poisson(10/3600, [300, 3600])
print(r)
r2 = []
for x in r:
    r2.append(np.sum(x))

labels = [n for n in range(300)]
av = np.average(r2)
print(av)
plt.scatter(x=labels, y=r2)
plt.show()
