import cmath
import math
from prettytable import PrettyTable
import matplotlib.pyplot as plt

pi = math.pi
N = 16
q = 8
D = 2**q

A = [1,5,3,7,3,2,1]
f = [0.5,1,2,5,7,9,12]

k = 7
f = [i*1000 for i in f]
samples = range(0,N)

fd = 75000
if max(f) > 30000:
    fd = 110000
Td = 1/fd



t = []
x = []

for n in samples:
    t.append(n * Td)
    x.append(0)
    for i in range(0,k):
        x[n] += A[i] * math.sin(2*pi*f[i]*t[n])

x = [int(i) for i in x]

def compMul(C1,C2):
    a = C1.real
    b = C1.imag
    c = C2.real
    d = C2.imag
    
    return complex(a*c-b*d,a*d+b*c)/2

def compSum(C1,C2):
    a = C1.real
    b = C1.imag
    c = C2.real
    d = C2.imag

    return complex(a + c,b + d)

def compSub(C1,C2):
    a = C1.real
    b = C1.imag
    c = C2.real
    d = C2.imag

    return complex(a - c,b - d)

def Bab_2(A,B,W):
    # print(W)
    return [compSum(A,compMul(B,W)),compSub(A,compMul(B,W))]

def Wf_2(x):
    d = ((math.e**(-(cmath.sqrt(-1)*2*(pi/N)*x))))*D/2
    if d.real == 128:
        d = complex(127,d.imag)
    if d.imag == 128:
        d = complex(d.real,127)
    return d

# 0  0  0  0 | 0  0  0 0 | 0 0 0 0 | 0 0 0 0
# 15 14 13 12  11 10 9 8   7 6 5 4   3 2 1 0

ws = [Wf_2(i) for i in range(0,8)]

a = x[:8]
b = x[8:]

resA = []
resB = []
for i in range(0,8):
    tempA,tempB = Bab_2(a[i],b[i],ws[i])
    resA.append((round(tempA.real,1),round(tempA.imag,1)))
    resB.append((round(tempB.real,1),round(tempB.imag,1)))

resA = [complex(i[0],i[1]) for i in resA]
resB = [complex(i[0],i[1]) for i in resB]

tempA2 = []
tempB2 = []

for i in resA:
    # while i.real < -128:
    #     i = complex(i.real + 128,i.imag)
    # while i.real > 128:
    #     i = complex(i.real - 128,i.imag)
    # while i.imag < -128:
    #     i = complex(i.real,i.imag + 128)
    # while i.imag > 128:
    #     i = complex(i.real,i.imag - 128)
    tempA2.append(i)

for i in resB:
    # while i.real < -128:
    #     i = complex(i.real + 127,i.imag)
    # while i.real > 127:
    #     i = complex(i.real - 127,i.imag)
    # while i.imag < -127:
    #     i = complex(i.real,i.imag + 127)
    # while i.imag > 127:
    #     i = complex(i.real,i.imag - 127)
    tempB2.append(i)

resA2 = tempA2
resB2 = tempB2




table = PrettyTable()

table.add_column("id",[i for i in range(0,8)])
table.add_column("a",a)
table.add_column("b",b)
table.add_column("w",[(int(i.real),int(i.imag)) for i in ws])
table.add_column("Ao",resA)
table.add_column("Bo",resB)

print(table)

gen = []
gen.append(x)
# print(x)

a = list()
b = list()

resA = list()
resB = list()

def Babl_2(AB,k):
    AB_out = [0 for i in range(0,len(AB))]
    lenH = len(AB)//2
    for i in range(0,lenH):
        a.append(AB[i])
        b.append(AB[i+lenH])
        AB_out[i],AB_out[i+lenH] = Bab_2(AB[i],AB[i+lenH],ws[k])
        resA.append(AB_out[i])
        resB.append(AB_out[i+lenH])
    return AB_out

gen.append(Babl_2(gen[0],0))
# print(gen[1])

table = PrettyTable()

table.add_column("id",[i for i in range(0,8)])
table.add_column("a",a)
table.add_column("b",b)
table.add_column("w",[(int(i.real),int(i.imag)) for i in ws])
table.add_column("Ao",resA)
table.add_column("Bo",resB)

print(table)

quartus = [
    complex(127,0),
    complex(66,-25),
    complex(57,-45),
    complex(38,-59),
    complex(12,64),
    complex(-89,20),
    complex(-9,-14),
    complex(102,84),

    complex(-127,0),
    complex(-52,25),
    complex(-33,45),
    complex(-10,59),
    complex(12,-64),
    complex(107,-20),
    complex(19,14),
    complex(-96,-84),
]

res2 = resA2 + resB2

fig, axs = plt.subplots(ncols=2,nrows=1,figsize=(6, 3))

axs[0].set_title("Quartus")
axs[0].plot(samples, quartus, 'teal')

axs[1].set_title("Python 1 итерация")
axs[1].plot(samples,res2, 'violet')

plt.show()
t = [complex(round(i.real,3),round(i.imag,3)) for i in res2]
table = PrettyTable()

table.add_column("id",range(0,16))
table.add_column("Quartus",quartus)
table.add_column("Python",t)

print(table)