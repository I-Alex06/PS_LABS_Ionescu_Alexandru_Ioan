import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
import math

t=np.arange(0,1,0.001)
f=3
def a(t):
    return np.sin(2*np.pi*f*t+np.pi/2)


x=a(t)

fig, axs=plt.subplots(1,2)
fig.suptitle("FIG 1")
axs[0].set_xlabel("Timp(esantioane)")
axs[0].set_ylabel("Amplitudine")
axs[0].axhline(color="black")
axs[1].set_xlabel("Real")
axs[1].set_ylabel("Imaginar")
axs[1].set_aspect('equal')
axs[1].set_xlim(-1,1)
axs[1].set_ylim(-1,1)
axs[1].axhline(color="black")
axs[1].axvline(color="black")


y=x*math.e**(-2*np.pi*1j*t)

w=[1,2,3,5]


z=[np.array(x*math.e**(-2*np.pi*1j*t*w[i])) for i in range(len(w))]

distance = np.sqrt(t**2+x**2)
points = np.array([np.arange(len(t)), x]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
lc = LineCollection(segments, cmap='viridis')
lc.set_array(distance)
axs[0].add_collection(lc)
# axs[0].plot(np.arange(len(t)),x)
axs[0].stem(620,x[620],markerfmt='ro',linefmt='r')


distance = np.sqrt(np.real(y)**2+np.imag(y)**2)
points = np.array([np.real(y), np.imag(y)]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
lc = LineCollection(segments, cmap='viridis')
lc.set_array(distance)
axs[1].add_collection(lc)
# axs[1].plot(np.real(y),np.imag(y))
axs[1].plot([0,np.real(y[620])],[0,np.imag(y[620])],color='red')
axs[1].plot(np.real(y[620]),np.imag(y[620]),marker='o',color='red')




plt.tight_layout()
fig.show()
plt.savefig('ex2FIG1.pdf')

plt.show()





#######  FIG 2

fig, axs=plt.subplots(2,2)
fig.suptitle("FIG 2")
for i, ax in enumerate(axs.flat):
    ax.set_title(f"w = {w[i]}")
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginar")
    ax.set_aspect('equal')
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.axhline(color="black", linewidth=0.5)
    ax.axvline(color="black", linewidth=0.5)
    # ax.plot(np.real(z[i]),np.imag(z[i]))
    
    distance = np.sqrt(np.real(z[i])**2+np.imag(z[i])**2)
    points = np.array([np.real(z[i]), np.imag(z[i])]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap='viridis')
    lc.set_array(distance)
    ax.add_collection(lc)
    
    
    ax.plot([0,np.real(np.mean(z[i]))],[0,np.imag(np.mean(z[i]))],color='k')
    ax.plot(np.real(np.mean(z[i])),np.imag(np.mean(z[i])),marker='o',color='k')

plt.tight_layout()
fig.show()
plt.savefig('ex2FIG2.pdf')

plt.show()
