import matplotlib.pyplot as plt
import scipy.fft as sp
import math
import cmath

sw = True

N = 16
filter = 10000
A = [1,5,3,7,3,2,1]
f = [0.5,1,2,5,7,9,12]

samples = range(0,N)

k = 7
pi = math.pi

f = [i*1000 for i in f]

fd = 75000
if max(f) > 30000:
    fd = 110000
Td = 1/fd

# Пункт 1 /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
t = []
x = []

# Построение изначального сигнала сигнала по сэмплам
for n in samples:
    t.append(n * Td)
    x.append(0)
    for i in range(0,k):
        x[n] += A[i] * math.sin(2*pi*f[i]*t[n])


# Пункт 2 /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

xdpf = list(sp.fft(x))

# Пункт 3 /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def Bab(A,B,W):
    print(W)
    return [A+B*W,A-B*W]

# Пункт 4 /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def Wf(x):
    return ((math.e**(-(cmath.sqrt(-1)*2*(pi/N)*x))))

# Пункт 5 /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

gen = []
gen.append(x)

def BabL(AB,k):
    AB_out = [0 for i in range(0,len(AB))]
    lenH = len(AB)//2
    for i in range(0,lenH):
        AB_out[i],AB_out[i+lenH] = Bab(AB[i],AB[i+lenH],Wf(k))
    return AB_out

gen.append(BabL(gen[0],0))

# for i in range(0,len(gen[0])):
#     print(str(gen[0][i]) + " -> " + str(gen[1][i]))

print("//////////////////////////////////////////////////////////////////////////")


# gen 2
    
gen.append([0 for i in gen[1]])

gen[2][:8] = BabL(gen[1][0:8],0)
gen[2][8:] = BabL(gen[1][8:],4)

# for i in range(0,len(gen[0])):
#     print(str(gen[1][i]) + " -> " + str(gen[2][i]))

print("//////////////////////////////////////////////////////////////////////////")
#  gen 3

gen.append([0 for i in gen[2]])

gen[3][:4] = BabL(gen[2][:4],0)
gen[3][4:8] = BabL(gen[2][4:8],4)
gen[3][8:12] = BabL(gen[2][8:12],2)
gen[3][12:] = BabL(gen[2][12:],6)

# for i in range(0,len(gen[0])):
#     print(str(gen[2][i]) + " -> " + str(gen[3][i]))

print("//////////////////////////////////////////////////////////////////////////")
# gen 4

gen.append([0 for i in gen[3]])

gen[4][:2] = BabL(gen[3][:2],0)
gen[4][2:4] = BabL(gen[3][2:4],4)
gen[4][4:6] = BabL(gen[3][4:6],2)
gen[4][6:8] = BabL(gen[3][6:8],6)
gen[4][8:10] = BabL(gen[3][8:10],1)
gen[4][10:12] = BabL(gen[3][10:12],5)
gen[4][12:14] = BabL(gen[3][12:14],3)
gen[4][14:] = BabL(gen[3][14:],7)

# for i in range(0,len(gen[0])):
#     print(str(gen[3][i]) + " -> " + str(gen[4][i]))

print("//////////////////////////////////////////////////////////////////////////")



ts = [gen[4][0],gen[4][8],gen[4][4],gen[4][12],gen[4][2],gen[4][10],gen[4][6],gen[4][14],gen[4][1],gen[4][9],gen[4][5],gen[4][13],gen[4][3],gen[4][11],gen[4][7],gen[4][15]]

plt.figure(figsize=(8,6))
plt.plot(samples,xdpf,"red")
plt.plot(samples,ts,"blue")

plt.show()