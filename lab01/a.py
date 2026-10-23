import numpy as np
import matplotlib.pyplot as plt
pi=np.pi
def a(t):
    return np.cos(800*np.pi*t+0)


t=np.arange(0,1,0.00001)
esant=np.linspace(0,1,1600)
fig, ax = plt.subplots()

ax.plot(t,a(t))
ax.stem(esant,a(esant))
ax.set_title("a) Semnal 400Hz, 1600 esantioane")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")

fig.show()
plt.savefig("a.pdf")
plt.show()