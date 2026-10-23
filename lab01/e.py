import numpy as np
import matplotlib.pyplot as plt

semnal = np.random.rand(128, 128)
plt.imshow(semnal)
plt.title("e) Semnal aleator 128x128")
plt.savefig("e.pdf")
plt.show()