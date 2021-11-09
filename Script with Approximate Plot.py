#%%
"""
This script plots the curve we made during our stay at PSI.
"""

#%%
import numpy as np
import matplotlib.pyplot as plt

energy =  np.array([2, 2.5, 3, 3.5, 3.35, 3.64, 3.91, 4.31, 4.47, 4.36, 4.09])
position = np.array([0.1736, 0.246, 0.34, 0.41, 0.4, 0.45, 0.5, 0.6, 0.7, 0.85, 1])


plt.scatter(position, energy)
plt.plot(position, energy)
plt.xlabel('Position')
plt.ylabel('Energy')
plt.xlim(xmin=0)
plt.ylim(ymin=0)

plt.show()

