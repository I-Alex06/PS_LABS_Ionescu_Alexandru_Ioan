import matplotlib.pyplot as plt
import numpy as np
import math

# e**(-2pi*j* a*b /N)

N=8
a=np.arange(N)
b=np.arange(N)

ab=np.ogrid[0:N,0:N]

c=ab[0]*ab[1]
F=math.e**(-2*math.pi*1j*c/N)
# print(F)
temp=F @ F.conj().T
print(np.allclose(temp,N * np.eye(N)))

fig,axs=plt.subplots(N)
fig.suptitle("F")
# for ax in axs:
#     ax.set_xlabel("Real")
#     ax.set_ylabel("Imaginar")
for i in range(N):
    axs[i].plot(np.arange(N),np.real(F[i]))
    axs[i].plot(np.arange(N),np.imag(F[i]))

plt.tight_layout()
fig.show()
plt.savefig('ex1.pdf')

plt.show()
