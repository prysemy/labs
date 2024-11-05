import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def func(x, minn, maxx):
    return (x - minn) * 255 / (maxx - minn)


path = 'lunar_images'
os.chdir(path)
for im in os.listdir():
    img = Image.open(im)
    data = np.array(img)
    maxx = data.max()
    minn = data.min()
    new_data = []
    for i in range(data.shape[0]):
        ar = []
        for j in range(data.shape[1]):
            ar.append(func(data[i][j], minn, maxx))
        new_data.append(ar)
    res_img = Image.fromarray(np.array(new_data))
    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].imshow(img)
    ax[0].set_title('До обработки')
    ax[1].imshow(res_img)
    ax[1].set_title('После обработки')
    plt.savefig('new_' + str(im)[:-8] + '.jpg')
    plt.show()


def filt(arr, win, dw=10):
    shape = arr.shape[:-1] + (int((arr.shape[-1] - win.shape[-1]) / dw) + 1,) + win.shape()
    strides = arr.strides[:-1] + (arr.strides[-1] * dw,) + arr.strides[-1:]
    return np.lib.stride_tricks.as_strided(arr, shape=shape, strides=strides)


path_sig = 'signals'
os.chdir(path_sig)
for signal in os.listdir():
    new_sig = []
    sig = [float(i.strip()) for i in open(signal).readlines()]
    print(sig)
    for t in range(10):
        new_sig.append(sum(sig[:t + 1]) / (t + 1))
    for t in range(10, len(sig)):
        new_sig.append(sum(sig[t - 9: t + 1]) / 10)
    fig, ax = plt.subplots(ncols=2, nrows=1)
    ax[0].plot(sig)
    ax[0].grid()
    ax[0].set_title('Было')
    ax[1].plot(new_sig)
    ax[1].grid()
    ax[1].set_title('Стало')
    plt.savefig('new_' + signal[:-4] + '.jpg')
    plt.show()

data = list(map(float, open('start.dat.txt').readlines()))
plt.plot(data)
plt.grid()
plt.savefig('u0.png')
plt.show()

u0 = np.array(data)
u = []
A = np.diag(np.full(u0.shape, 1))
rows, cols = np.indices(A.shape)
A[rows == cols + 1] = -1
A[0, 49] = -1
u.append(u0)
for i in range(1, 500):
    u.append(u[i - 1] - np.dot(A, u[i - 1]) / 2)

t = np.arange(0, 50)

fig = plt.figure()
axis = plt.axes(xlim=(0, 50), ylim=(0, 10))
line, = axis.plot(t, u[0], lw=3, color='purple')
plt.grid()


def animate(i):
    line.set_data(t, u[i])
    return line,


anim = animation.FuncAnimation(fig, animate, frames=255, interval=200, blit=True)
anim.save('u.gif', writer='pillow')
plt.show()
