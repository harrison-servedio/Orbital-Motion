import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time as t

x = np.linspace(0, 2, 100)

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x**2, label = "testLabel")

plt.show()

