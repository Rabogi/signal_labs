import matplotlib.pyplot as plt
import scipy.fft as sp
import math

samples = range(1,128)

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
        x[n] += A[k] * math.sin(2*pi*f[k]*t[n])

# Пункт 2
        

    

