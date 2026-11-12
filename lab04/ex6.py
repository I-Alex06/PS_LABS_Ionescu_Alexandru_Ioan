from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt


rate, data = wavfile.read('semnal.wav')
n=len(data)
grupuri=[data[i:i+n//100] for i in range(0,n-n//100,n//200)]
fft_grupuri=[np.abs(np.fft.fft(grup)) for grup in grupuri]
m=np.array(fft_grupuri).T
m=m[:n//200]
m2=20*np.log10(m+1e-10)

plt.figure(figsize=(10,6))
plt.imshow(m2, cmap='viridis',aspect='auto',origin='lower',extent=[0,n/rate,0,rate/2])
plt.colorbar()
plt.tight_layout()
plt.savefig('ex6.pdf')
plt.show()
