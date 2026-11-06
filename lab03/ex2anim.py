import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.animation import FuncAnimation
import numpy as np
import math

t=np.arange(0,1,0.001)
t2=np.arange(len(t))
f=3
def a(t):
    return np.sin(2*np.pi*f*t+np.pi/2)


x=a(t)

fig, axs=plt.subplots(1,2)
fig.suptitle("FIG 1")
axs[0].set_xlabel("Timp(esantioane)")
axs[0].set_ylabel("Amplitudine")
axs[0].set_xlim(0,len(t2))
axs[0].set_ylim(-1,1)
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

lcs =[LineCollection([],cmap='viridis') for _ in range(2)]
axs[0].add_collection(lcs[0])
axs[1].add_collection(lcs[1])
lcs[0].set_array(np.sqrt(t**2+x**2))
lcs[1].set_array(np.sqrt(np.real(y)**2+np.imag(y)**2))

curr_point=[axs[i].plot([],[],'ko')[0] for i in range(2)]

inds = np.arange(0,len(t), 5)

def init():
    for lc in lcs:
        lc.set_segments([])
    for p in curr_point:
        p.set_data([],[])
    return lcs+curr_point
def animate(frame):
    ind=inds[frame]
    
    if ind>0:
        t_slice = t2[:ind]
        x_slice = x[:ind]
        points = np.reshape(np.transpose(np.array([t_slice,x_slice])),(-1,1,2))
        lines=np.concatenate([points[:-1],points[1:]],axis=1)
        lcs[0].set_segments(lines)
    curr_point[0].set_data([t2[ind]],[x[ind]])
    
    if ind>0:
        y_slice = y[:ind]
        points = np.reshape(np.transpose(np.array([np.real(y_slice),np.imag(y_slice)])),(-1,1,2))
        lines=np.concatenate([points[:-1],points[1:]],axis=1)
        lcs[1].set_segments(lines)
    curr_point[1].set_data([np.real(y[ind])],[np.imag(y[ind])])
    return lcs+curr_point
anim = FuncAnimation(fig, animate, init_func=init, frames=len(inds), interval = 1, blit=True)


plt.tight_layout()
plt.show()
print("SAVING 1")
anim.save('ex2FIG1anim.gif', writer='pillow', fps=30)
print("SAVED 1")



#######  FIG 2

fig, axs=plt.subplots(2,2)
fig.suptitle("FIG 2")

lcs = [LineCollection([],cmap='viridis') for _ in range(4)]
for i, ax in enumerate(axs.flat):
    ax.set_title(f"w = {w[i]}")
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginar")
    ax.set_aspect('equal')
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.axhline(color="black", linewidth=0.5)
    ax.axvline(color="black", linewidth=0.5)
    
    ax.add_collection(lcs[i])
    
    distance = np.sqrt(np.real(z[i])**2+np.imag(z[i])**2)
    lcs[i].set_array(distance)
    
curr_point=[axs[i][j].plot([],[],'ko')[0] for i in range(2) for j in range(2)]

def animate2(frame):
    ind=inds[frame]
    for i in range(4):
        if ind>0:
            z_slice = z[i][:ind]
            points = np.reshape(np.transpose(np.array([np.real(z_slice),np.imag(z_slice)])),(-1,1,2))
            lines=np.concatenate([points[:-1],points[1:]],axis=1)
            lcs[i].set_segments(lines)
        curr_point[i].set_data([np.real(z[i][ind])],[np.imag(z[i][ind])])
    return lcs+curr_point
anim = FuncAnimation(fig, animate2, init_func=init, frames=len(inds), interval = 1, blit=True)

plt.tight_layout()
plt.show()
print("SAVING 2")
anim.save('ex2FIG2anim.gif', writer='pillow', fps=30)
print("SAVED 2")
