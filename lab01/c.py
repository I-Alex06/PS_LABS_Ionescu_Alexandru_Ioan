import numpy as np
import matplotlib.pyplot as plt
pi=np.pi
def c(t):
    return 240*t-np.floor(240*t)


t=np.arange(0,1,0.00001)


fig, ax = plt.subplots()
ax.plot(t,c(t))
ax.set_title("c) Semnal 240Hz, Sawtooth")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")

fig.show()
plt.savefig("c.pdf")
plt.show()