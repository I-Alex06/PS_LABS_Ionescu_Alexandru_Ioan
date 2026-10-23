import numpy as np
import matplotlib.pyplot as plt
pi=np.pi
def b(t):
    return np.cos(1600*np.pi*t+0)


t=np.arange(0,3,0.00001)

fig, ax = plt.subplots()
ax.plot(t,b(t))
ax.set_title("b) Semnal 800Hz, 3 secunde")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")

fig.show()
plt.savefig("b.pdf")
plt.show()