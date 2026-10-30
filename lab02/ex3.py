import numpy as np
import sounddevice as sd
import scipy.io.wavfile
import scipy.signal
import time
t=t=np.arange(0,1,0.00001)
def a(t):
    return np.cos(800*np.pi*t+0)
def b(t):
    return np.cos(1600*np.pi*t+0)
def c(t):
    return 240*t-np.floor(240*t)
def d(t):
    return np.sign(np.cos(600*np.pi*t+0))

fs=44100

sd.play(a(t),fs)
sd.wait()
print("Played a")
time.sleep(1)

sd.play(b(t),fs)
sd.wait()
print("Played b")
time.sleep(1)

sd.play(c(t),fs)
scipy.io.wavfile.write("c.wav", fs, c(t))
sd.wait()
print("Played c")
time.sleep(1)

sd.play(d(t),fs)
sd.wait()
print("Played d")
time.sleep(1)

rate,cwav=scipy.io.wavfile.read("c.wav")
sd.play(cwav,rate)
sd.wait()
print("Played c from wav file")

