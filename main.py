import matplotlib.pyplot as plt
import scipy.fft as sp
import math

# пункт 1
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

# пункт 2

# plt.figure(figsize=(10, 8))
# plt.plot(n, x, 'b')
# plt.title("Дискретный сигнал по сэмплам")

# plt.figure(figsize=(10, 8))
# plt.plot(tns, x, 'r')
# plt.title("Дискретный сигнал по абсолютному времени")

# пункты 3 и 4
Y1 = sp.fft(x)
Y2 = sp.ifft(Y1)

# plt.figure(figsize=(10, 8))
# plt.plot(n, Y1, 'pink')
# plt.title("ДНФ")

# plt.figure(figsize=(10, 8))
# plt.plot(n, Y2, 'green')
# plt.title("ОДНФ")

# plt.show()

# пункт 5
Y3 = Y1[:len(Y1)//2]/(4096//4)

# пункт 6

N2 = int(samples/2)

Fstep = fd/N2

fi = [n[i]*Fstep for i in range(0,N2)]

# plt.figure(figsize=(10, 8))
# plt.plot(fi, Y3, 'violet')
# plt.title("Нормализованный сигнал по частотам")

# plt.figure(figsize=(10, 8))
# plt.plot([i for i in range(0,N2)], Y3, 'black')
# plt.title("Нормализованный сигнал по сэмплам")

# plt.show()

# пункт 7