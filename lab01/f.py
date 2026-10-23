import numpy as np
import matplotlib.pyplot as plt

semnal = np.zeros((128,128))
for i in range(128):
    for j in range(128):
        semnal[i][j] = i+j
plt.imshow(semnal)
plt.title("f) Semnal ales 128x128")
plt.savefig("f.pdf")
plt.show()