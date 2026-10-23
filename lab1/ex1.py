import numpy as np
import matplotlib.pyplot as plt
pi=np.pi
def x(t):
    return np.cos(520*np.pi*t+np.pi/3)
def y(t):
    return np.cos(280*pi*t-pi/3)
def z(t):
    return np.cos(120*pi*t +pi/3)

#a)
t=np.arange(0,0.3,0.0005)

#b)
fig, axs = plt.subplots(3)
for ax in axs:
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
fig.suptitle("Semnale")
axs[0].plot(t,x(t))
axs[1].plot(t,y(t))
axs[2].plot(t,z(t))

esant=np.arange(0,0.3,1/200)
axs[0].stem(esant,x(esant))
axs[1].stem(esant,y(esant))
axs[2].stem(esant,z(esant))

fig.show()
plt.show()