import numpy as np
import matplotlib.pyplot as plt

fig,axs=plt.subplots(3)
fig.suptitle("Semnale")
for ax in axs:
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")

t=np.arange(0,1,1/1000)

def a(t):
    return np.sin(200* np.pi * t)
a_sig=a(t)
b_sig=[a_sig[i] for i in range(0,len(a_sig),4)]
t2=[t[i] for i in range(0,len(t),4)]

c_sig=[a_sig[i] for i in range(1,len(a_sig),4)]
t3=[t[i] for i in range(1,len(t),4)]

axs[0].plot(t,a_sig)
axs[1].plot(t2,b_sig)
axs[2].plot(t3,c_sig)

#in functi de frecventa semnalulul pierdem forma de sin
#se muta in timp cu 1 esantion

plt.tight_layout()
fig.show()
plt.savefig('lab02/ex7.pdf')

plt.show()
