import numpy as np
import matplotlib.pyplot as plt
pi=np.pi
def s(t):
    return np.sin(10*np.pi*t+pi/2)
def c(t):
    return np.cos(10*np.pi*t+0)


t=np.arange(0,1,0.00001)

fig, axs = plt.subplots(2)
axs[0].plot(t,s(t))
axs[0].set_title("Sin")
axs[0].set_xlabel("Time")
axs[0].set_ylabel("Amplitude")

axs[1].plot(t,c(t))
axs[1].set_title("Cos")
axs[1].set_xlabel("Time")
axs[1].set_ylabel("Amplitude")

plt.tight_layout()
fig.show()
plt.savefig("ex1.pdf")
plt.show()