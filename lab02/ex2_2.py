import numpy as np
import matplotlib.pyplot as plt
pi=np.pi
def b(t):
    return np.cos(10*np.pi*t+0)

#pt grafic mai clar foloseste 0.0001
t=np.arange(0,1,0.00001)
x=b(t)
z = np.random.normal(size=len(t))
# print(z)
snr=[0.1,1,10,100]
x_norm=np.linalg.norm(x)
z_norm=np.linalg.norm(z)
x_n_sq= x_norm**2
z_n_sq= z_norm**2
y=[(x_n_sq/(snr[i]*z_n_sq))**0.5 for i in range(len(snr))]
noise=[x+z*y[i] for i in range(len(snr))]
# print(y)
# exit()
fig, axs = plt.subplots(2,2)
for i in range(len(axs)):
    for j in range(len(axs[i])):
        axs[i,j].set_title(f"SNR: {snr[i*len(axs[0])+j]}")
        axs[i,j].set_xlabel("Time")
        axs[i,j].set_ylabel("Amplitude")
        axs[i,j].plot(t,noise[i*len(axs[0])+j])
plt.tight_layout()



fig.show()
plt.savefig("ex2_2.pdf")
plt.show()