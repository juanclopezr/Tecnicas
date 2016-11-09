import numpy as np
import matplotlib.pyplot as plt
import os

inner = np.linspace(0.01,0.99,100)
avg = np.zeros(100)
SINR = np.zeros(100)

for j in range(100):
    for i in range(inner.shape[0]):
        os.system('python cover.py 1. %f SINR%05d' % (inner[i],i))
        data = np.loadtxt('SINR%05d' % (i))
        SINR[i] = np.dot(data,data)**0.5/data.shape[0]
    avg = avg + SINR/100.
    print(j)

plt.plot(inner,10*np.log10(avg))
plt.savefig('SINR.png')
