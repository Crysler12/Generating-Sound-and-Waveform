import numpy
import matplotlib.pyplot as plt

sample_rate = 44100
A = 32767
f = 293.66
time=numpy.arange(0,0.3,1/sample_rate)

y=A*numpy.sin(2*numpy.pi*f*time)

plt.figure(figsize=(10,4))
plt.plot(time,y)
plt.title("Sine wave")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()