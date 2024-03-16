import matplotlib.pyplot as plt

import math
samples = 127

n = range(0,samples)

A = [1,5,3,7,3,2,1]

f = [i*1000 for i in [0.5,1,2,5,7,9,12]]
fd = 4*max(f)
Td = 1/fd
tns = []

x = [0 for i in range(0,127)]

print(A)

for i in n:
    tn = i * Td
    tns.append(tn)
    for k in range(0,7):
        x[i] += A[k] * math.sin(2*math.pi*f[k]*tn)

# print(x)
        
plt.figure(figsize=(10, 8))
plt.plot(n, x, 'b')
plt.title("Дискретный сигнал по семплам")
plt.show()
plt.plot(tns, x, 'r')
plt.title("Дискретный сигнал по абсолютному времени")
plt.show()

