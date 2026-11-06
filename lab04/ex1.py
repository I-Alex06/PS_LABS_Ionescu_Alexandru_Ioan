import numpy as np
import matplotlib.pyplot as plt
import math
import time

def fft(x):
    n=len(x)
    if n==1:
        return x
    if n%2!=0:
        print("N nu este putere a lui 2")
        return
    even=fft(x[::2])
    odd=fft(x[1::2])
    exp=math.e**(-2j*np.pi*np.arange(n//2)/n)
    
    half1=even+exp*odd
    half2=even-exp*odd
    return np.concatenate([half1,half2])
def dft(x):

    n=len(x)

    ws=np.arange(0,n,1)
    m=[]
    for w in ws:
        s=0
        for n2 in range(n):
            s+=x[n2] * math.e**(-2j*np.pi*n2*w/n)
        m.append(s)
        

def semnal(t):
    return 3*np.cos(2*27* np.pi * t +0)+0.5*np.cos(2*7* np.pi * t +0)+1*np.cos(2*20* np.pi * t +0)


ts=[2**i for i in range(7,14)]
# print(ts)
xs=[semnal(np.linspace(0,1,t)) for t in ts]
# print (xs)

times={"dft":[],"fft":[],"npfft":[]}
# print("starting in 3")
# time.sleep(3)
for x in xs:
    # x=xs[0]
    print(f"DFT: {len(x)}")
    start=time.time_ns()
    temp=dft(x)
    stop=time.time_ns()
    times["dft"].append(stop-start)
    
    print(f"FFT: {len(x)}")
    start=time.time_ns()
    temp=fft(x)
    stop=time.time_ns()
    times["fft"].append(stop-start)
        
    print(f"NPFFT: {len(x)}")
    start=time.time_ns()
    temp=np.fft.fft(x)
    stop=time.time_ns()
    times["npfft"].append(stop-start)

print("Done")

fig,axs=plt.subplots(1)
# fig.suptitle("TIMPI")
axs.set_xlabel("Dimensiune")
axs.set_ylabel("Timp")
axs.plot(np.log2(ts),np.log10(times["dft"]),color="red")
axs.plot(np.log2(ts),np.log10(times["fft"]),color="blue")
axs.plot(np.log2(ts),[0 if times["npfft"][i]==0 else np.log10(times["npfft"][i]) for i in range(len(times["npfft"]))],color="green")

print(times)

fig.tight_layout()
fig.show()
plt.savefig('ex1.pdf')
plt.show()