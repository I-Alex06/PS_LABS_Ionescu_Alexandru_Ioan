import numpy as np
import sounddevice as sd

t=t=np.arange(0,1,0.00001)
def a(t):
    return np.cos(800*np.pi*t+0)
def b(t):
    return np.cos(6400*np.pi*t+0)
a_sig=a(t)
b_sig=b(t)

sig=np.concatenate((a_sig,b_sig))
fs=44100

# print(a_sig)
# print(b_sig)
# print(sig)

sd.play(sig,fs)
sd.wait()

"""
Se aud diferit avand frecvente diferite.
Al doilea este mai acut/ascutit.

"""
