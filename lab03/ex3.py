import numpy as np
import matplotlib.pyplot as plt
import math

fig,axs=plt.subplots(1,2)
fig.suptitle("FIG 3")
axs[0].set_xlabel("Time")
axs[0].set_ylabel("x(t)")
axs[1].set_xlabel("Frecventa")
axs[1].set_ylabel("|X(w)|")


def semnal(t):
    return 3*np.cos(2*27* np.pi * t +0)+0.5*np.cos(2*7* np.pi * t +0)+1*np.cos(2*20* np.pi * t +0)


t=np.arange(0,1,0.01)
x=semnal(t)
axs[0].plot(t,x)
N=len(t)

ws=np.arange(0,N,1)
m=[]
for w in ws:
    s=0
    for n in range(N):
        s+=x[n] * math.e**(-2j*np.pi*n*w/N)
    m.append(np.abs(s))



# # N=100
# a=np.arange(N)
# b=np.arange(N)

# ab=np.ogrid[0:N,0:N]

# c=ab[0]*ab[1]
# F=math.e**(-2*math.pi*1j*c/N)

# X=F @ x
# m=np.abs(X)


axs[1].stem(ws[:N//2],m[:N//2])

fig.tight_layout()
fig.show()
plt.savefig('ex3.pdf')
plt.show()
