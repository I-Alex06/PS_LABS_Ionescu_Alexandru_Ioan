import numpy as np
import matplotlib.pyplot as plt

fig,axs=plt.subplots(3)
fig.suptitle("Semnale")
for ax in axs:
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
fs=2000
t=np.arange(0,1,1/2000)

def a(t):
    return np.sin(fs* np.pi * t)
axs[0].plot(t,a(t))
def b(t):
    return np.sin(fs/2* np.pi * t)

axs[1].plot(t,b(t))
def c(t):
    return np.sin(0* np.pi * t)

axs[2].plot(t,c(t))

#a constant zero in teorie, graficul este aproape de zero din cauza floating point error
#b apar triunghiuri in loc de sin
#c este constant zero linie dreapta

plt.tight_layout()
fig.show()
plt.savefig('ex6.pdf')

plt.show()
