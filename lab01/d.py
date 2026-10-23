import numpy as np
import matplotlib.pyplot as plt
pi=np.pi
def d(t):
    return np.sign(np.cos(600*np.pi*t+0))


t=np.arange(0,1,0.00001)

fig, ax = plt.subplots()
ax.plot(t,d(t))
ax.set_title("d) Semnal 300Hz, square")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")

fig.show()
plt.savefig("d.pdf")
plt.show()