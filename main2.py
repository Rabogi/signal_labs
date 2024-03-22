import matplotlib.pyplot as plt
import scipy.fft as sp
import math

samples = range(0,127)

filter = 10000

A = [1,5,3,7,3,2,1]
f = [0.5,1,2,5,7,9,12]
k = 7
pi = math.pi

f = [i*1000 for i in f]

fd = 4*max(f)
Td = 1/fd

# Пункт 1
t = []
x = []

for n in samples:
    t.append(n * Td)
    x.append(0)
    for i in range(0,k):
        x[n] += A[i] * math.sin(2*pi*f[i]*t[n])

# Пункт 2
        
fig, axs = plt.subplots(ncols=2,nrows=1,figsize=(16, 6))

axs[0].set_title("Дискретный сигнал по сэмплам")
axs[0].plot(list(samples), x, 'b')

axs[1].set_title("Дискретный сигнал по абсолютному времени")    
axs[1].plot(t, x, 'r')

plt.show()


