import numpy.random as nr
import numpy as np
import scipy.stats as sr
from matplotlib import pyplot as plt

r = nr.binomial(50, 0.5, 1)
print(r)

labels = [n for n in range(300)]
r2 = nr.binomial(50, 0.5, 300)
av = np.average(r2)
print(av)
plt.scatter(x=labels, y=r2)
plt.show()
