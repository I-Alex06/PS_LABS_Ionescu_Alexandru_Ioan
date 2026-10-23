import numpy as np
import matplotlib.pyplot as plt
pi=np.pi
def b(t):
    return np.cos(10*np.pi*t+0)
def c(t):
    return np.cos(10*np.pi*t+pi/4)
def d(t):
    return np.cos(10*np.pi*t+pi/2)
def e(t):
    return np.cos(10*np.pi*t+pi)


t=np.arange(0,1,0.00001)

fig, ax = plt.subplots()
ax.plot(t,b(t))
ax.plot(t,c(t))
ax.plot(t,d(t))
ax.plot(t,e(t))
ax.set_title("4 faze")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
plt.tight_layout()

fig.show()
plt.savefig("ex2_1.pdf")
plt.show()