import matplotlib.pyplot as plt
import scipy.fft as sp
import numpy as np
import math
from prettytable import PrettyTable


# 1 ////////////////////////////////////////////////////////////////////////////
N = 2048
filter = 10000
Ax = [1,5,3,7,3,2,1]
fx = [0.5,1,2,5,7,9,12]

show = False

samples = range(0,N)

k = 7
pi = math.pi

fx = [i*10**3 for i in fx]

fd = 2.2 * max(fx)

Td = 1/fd

t = []
x = []

for n in samples:
    t.append(n * Td)
    x.append(0)
    for i in range(0,k):
        x[n] += Ax[i] * math.sin(2*pi*fx[i]*t[n])

if show:
    plt.figure(figsize=(10,8))
    plt.plot(samples,x)

    plt.show()

# 2 ////////////////////////////////////////////////////////////////////////////
h = [0 for i in range(0,16)]

h[0] =  8.58398885E-3
h[15] = h[0]

h[1] = 1.01415502E-2
h[14] = h[1]

h[2] = -1.18238033E-2
h[13] = h[2]

h[3] = -4.97749198E-2
h[12] = h[3]

h[4] = -5.10048196E-2
h[11] = h[4]

h[5] = 3.87851131E-2
h[10] = h[5]

h[6] = 2.01367094E-1
h[9] = h[6]

h[7] = 3.33522835E-1
h[8] = h[7]

def A(x):
    b = h
    first = 0
    for j in range(0,len(b)):
        first += b[j] * math.cos(2*pi*x*j)
    first = first**2

    second = 0
    for j in range(0,len(b)):
        second += b[j] * math.sin(2*pi*x*j)
    second = second**2

    return(math.sqrt(first+second))

def fi(x):
    b = h
    first = 0
    for j in range(0,len(b)):
        first += b[j] * math.cos(2*pi*x*j)

    second = 0
    for j in range(0,len(b)):
        second += b[j] * math.sin(2*pi*x*j)

    return(math.atan(second/first))

fns = np.linspace(0,1,N)

As = [A(i) for i in fns]
fi = [fi(i) for i in fns]



srez = [1/math.sqrt(2) for i in fns[:N//2]]
fn_abs = np.fft.fftfreq(N, 1/fd)

if show:
    plt.figure(figsize=(10,8))
    plt.title("АЧХ")
    plt.plot(fn_abs[:N//2],As[:N//2])
    plt.plot(fn_abs[:N//2],srez)

    plt.show()

# <4.15

#3 /////////////////////////////////////////////////////////////////

Ae = [1,5,3,0,0,0,0]
fe = [0.5,1,2,0,0,0,0]

fe = [i*10**3 for i in fe]

fde = 2.2 * max(fe)
    
Tde = 1 / fde

te = []
xe = []

for n in samples:
    te.append(n * Tde)
    xe.append(0)
    for i in range(0,k):
        xe[n] += Ae[i] * math.sin(2*pi*fe[i]*te[n])

if show:
    plt.figure(figsize=(10,8))
    plt.plot(samples,x)
    plt.plot(samples,xe)

    plt.show()

# 4 ////////////////////////////////////////////////////////
intX = [int(i) for i in x]
intXe = [int(i) for i in xe]

for i in intX:
    if i > 127 or i < -127:
        print("AAAAAAAAAAAAA")

if show:
    plt.figure(figsize=(10,8))
    plt.plot(samples,intX)
    plt.plot(samples,intXe)

    plt.show()

# 5 /////////////////////////////////////////////////
discret_signal_file = "./lab5/signal.mif"
with open(discret_signal_file, 'w') as f:
    f.write(f"ADDRESS_RADIX=DEC;\n")
    f.write(f"DATA_RADIX=DEC;\n")
    f.write(f"CONTENT BEGIN\n")
    for idx in range(len(intX)):
        f.write(f"\t{idx} : {str(intX[idx])};\n")
    f.write(f"END;")

# 6
q = 8

D = 2**q

intH = [int(i*D/2) for i in h]

table = PrettyTable()
table.add_column("ids",[i for i in range(0,len(intH))])
table.add_column("hs",intH)

print(table)

#12

out_Data = []
with open("lab5/filtered.txt", 'r') as f:
    for line in f:
        temp = line.split()
        for i in temp:
            out_Data.append(i)

print(len(out_Data))

show = True
if show:
    plt.figure(figsize=(15,10))
    plt.plot(samples,x,"blue") # Изначальный
    plt.plot(samples,xe,"green") # Эталон
    plt.plot(samples,out_Data,"pink") #quartus


    plt.show()


def yn(n):
    res = 0
    for i in range(0,len(h)):
        if n-i < 0:
            res += 0
        else:
            res += h[i]*x[n-i]

    return(res)

ys = [yn(i) for i in samples]

temp =  ys[len(ys)//2:] + ys[0:len(ys)//2]

ys = temp

plt.figure(figsize=(18,10))
plt.plot(samples,ys)
plt.plot(samples,out_Data)

plt.show()