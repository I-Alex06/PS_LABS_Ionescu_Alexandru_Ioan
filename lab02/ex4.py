import numpy as np
import matplotlib.pyplot as plt
t=t=np.arange(0,1,0.00001)

def b(t):
    return 0.2*np.cos(5*12*np.pi*t+3*np.pi/2)
def c(t):
    return 6*t-np.floor(6*t+1/2)



import numpy as np
import matplotlib.pyplot as pl

fig,axs=pl.subplots(3)
fig.suptitle("Semnale")
for ax in axs:
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")

b_sig=b(t)
c_sig=c(t)

axs[0].plot(t,b_sig)
axs[1].plot(t,c_sig)

#combinatie
axs[2].plot(t,b_sig+c_sig)

plt.tight_layout
fig.show()
pl.savefig('ex4.pdf')

pl.show()