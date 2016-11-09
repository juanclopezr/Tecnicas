import numpy as np
import matplotlib.pyplot as plt
import os

inner = np.linspace(0.01,0.99,100)
SINR = np.array([])

for i in range(inner.shape[0]):
    os.system('python cover.py 1. %f SINR%05d' % (inner[i],i))
    data = np.loadtxt('SINR%05d' % (i))
    SINR = np.append(SINR,np.dot(data,data)**0.5/data.shape[0])

plt.plot(inner,10*np.log10(SINR))
plt.savefig('SINR.png')
