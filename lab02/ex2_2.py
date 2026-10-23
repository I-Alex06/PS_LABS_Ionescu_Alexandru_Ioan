import numpy as np
import matplotlib.pyplot as plt
pi=np.pi
def b(t):
    return np.cos(10*np.pi*t+0)
def add_noise(snr):
    pass

t=np.arange(0,1,0.00001)
x=b(t)
noise = np.random.normal(size=len(t))



fig, axs = plt.subplots(4)
axs[0].plot(t,b(t))

axs[0].set_title("SNR: 0.1")
axs[0].set_xlabel("Time")
axs[0].set_ylabel("Amplitude")
plt.tight_layout()



fig.show()
plt.savefig("ex2_1.pdf")
plt.show()