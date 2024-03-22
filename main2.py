import matplotlib.pyplot as plt
import scipy.fft as sp
import math

sw = True

N = 128
filter = 10000
A = [1,5,3,7,3,2,1]
f = [0.5,1,2,5,7,9,12]

samples = range(0,N)


k = 7
pi = math.pi

f = [i*1000 for i in f]

fd = 4*max(f)
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
        
fig, axs = plt.subplots(ncols=2,nrows=1,figsize=(16, 6))

axs[0].set_title("Дискретный сигнал по сэмплам")
axs[0].plot(list(samples), x, 'b')

axs[1].set_title("Дискретный сигнал по абсолютному времени")    
axs[1].plot(t, x, 'r')

if sw:
    plt.show()

# Пункт 3 /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Построение ДПФ ОДПФ
dpfx = sp.fft(x)
odpfx = sp.ifft(dpfx)

# Пункт 4 /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
fig, axs = plt.subplots(ncols=2,nrows=1,figsize=(16, 6))

axs[0].set_title("ДПФ")
axs[0].plot(list(samples), dpfx, 'pink')

axs[1].set_title("ОДНФ")    
axs[1].plot(list(samples), odpfx, 'green')

if sw:
    plt.show()

# Пункт 5 /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Уменьшенное количество сэмплов
N2 = N//2 

# Отбрасывание ненужной части спектра сигнала
dpfx_normal = dpfx[:N2]/(4096//4)

# Пункт 6 /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

fstep = fd/N
fn = [i*fstep for i in range(0,N2)]

fig, axs = plt.subplots(ncols=2,nrows=1,figsize=(16, 6))

axs[0].set_title("Нормализованный спектр исходного сигнала в абсолютных частотах ГЦ")
axs[0].plot(fn, dpfx_normal, 'teal')

axs[1].set_title("Нормализованный спектр исходного сигнала в сэмплах")
axs[1].plot(list(range(0,N2)), dpfx_normal, 'violet')

if sw:
    plt.show()

# Пункт 7 /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

dpfx_filtered = dpfx
fn_real = [i*fstep for i in range(0,N)]
# Фильтрация
for i in range(0,len(dpfx_filtered)//2+1):
    if fn_real[i] > 10000:
        dpfx_filtered[i] = 0
        dpfx_filtered[len(dpfx_filtered)-i] = 0


dpfx_filtered = list(dpfx_filtered)

# Пункт 8 /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# fn_real = fn + list(reversed([-i for i in fn]))

plt.figure(figsize=(8,6))
plt.plot(fn_real,dpfx_filtered,"blue",)
plt.title("Отфильтрованный спектр (от 10КГЦ) по абсолютным частотам")

if sw:
    plt.show()

# Пункт 9 /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
odpfx_filtered = list(sp.ifft(dpfx_filtered))

# Пункт 10 /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

plt.figure(figsize=(8,6))
plt.plot(t,odpfx_filtered,"red",)
plt.title("Отфильтрованный сигнал (от 10КГЦ) по абсолютным частотам")

if sw:
    plt.show()