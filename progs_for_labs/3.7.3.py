import math

import matplotlib.pyplot as plt
import numpy as np

f11 = [3.85, 7.74, 11.67, 15.57, 19.49]
n = [1, 2, 3, 4, 5]
f12 = [4.12, 8.15, 12.28, 16.37, 20.56]
l = 5030  # см

plt.scatter(n, f11)
k1 = np.polyfit(n, f11, 1)[0]
plt.plot(n, np.polyval(np.polyfit(n, f11, 1), n), label='k=' + str(round(k1, 2)) + 'МГц')
plt.grid()
plt.xlabel('n')
plt.ylabel('f, МГц')
plt.legend()
plt.savefig('1_1.png')
# plt.show()
plt.cla()
plt.clf()
v_f1 = k1 * l * 10 ** 6
print('Фазовая скорость1:', round(v_f1 / 10 ** 10, 3), '10^10 см/c')

plt.scatter(n, f12)
k2 = np.polyfit(n, f12, 1)[0]
plt.plot(n, np.polyval(np.polyfit(n, f12, 1), n), label='k=' + str(round(k2, 2)) + 'МГц')
plt.grid()
plt.xlabel('n')
plt.ylabel('f, МГц')
plt.legend()
plt.savefig('1_2.png')
# plt.show()
plt.cla()
plt.clf()
v_f2 = k2 * l * 10 ** 6
print('Фазовая скорость2:', round(v_f2 / 10 ** 10, 3), '10^10 см/c')

f21 = [3.92, 7.84, 11.75, 15.67, 19.59]
plt.scatter(n, f21)
k3 = np.polyfit(n, f21, 1)[0]
plt.plot(n, np.polyval(np.polyfit(n, f21, 1), n), label='k=' + str(round(k3, 2)) + 'МГц')
plt.grid()
plt.xlabel('n')
plt.ylabel('f, МГц')
plt.legend()
plt.savefig('2_1.png')
# plt.show()
plt.cla()
plt.clf()
v_g1 = k3 * l * 10 ** 6
print('Групповая скорость1:', round(v_g1 / 10 ** 10, 3), '10^10 см/c')

f22 = [3.9, 7.81, 11.72, 15.63, 19.53]
plt.scatter(n, f22)
k4 = np.polyfit(n, f22, 1)[0]
plt.plot(n, np.polyval(np.polyfit(n, f22, 1), n), label='k=' + str(round(k4, 2)) + 'МГц')
plt.grid()
plt.xlabel('n')
plt.ylabel('f, МГц')
plt.legend()
plt.savefig('2_2.png')
# plt.show()
plt.cla()
plt.clf()
v_g2 = k4 * l * 10 ** 6
print('Групповая скорость1:', round(v_g2 / 10 ** 10, 3), '10^10 см/c')

f = [1, 3, 5, 9, 12, 17, 22, 28, 33, 36, 40]
u = [24.6, 24.1, 23.3, 22.3, 21.2, 20.7, 19.7, 17.9, 17, 17.2, 16.2]
u0 = [26.6, 26.6, 25.9, 26.5, 26.6, 26.6, 26.4, 26.4, 26., 26., 25.2]
phi_t = [260, 256, 59, 34.8, 8, 21.2, 28.8, 5.8, 13, 4.8, 5.4]  # нс
phi = [round(phi_t[i] * f[i] / 10 ** 3 + math.pi * f[i] / 2, 3) for i in range(len(f))]
print('фаза в радианах:', phi)
k = [round(phi[i] / l * 10 ** 3, 2) for i in range(len(phi))]
print('волновое число в 10^-3 см^-1:', k)
a = [round(math.log((u0[i] / u[i]), math.e) / l * 10 ** 5, 2) for i in range(len(u))]
print('декремент затухания в 10^-5 см^-1:', a)

plt.scatter(f, u)
plt.plot(f, np.polyval(np.polyfit(f, u, 1), f))
plt.grid()
plt.xlabel('f, Мгц')
plt.ylabel('Амплитуда U, В')
plt.title('АЧХ')
plt.savefig('3_1.png')
# plt.show()
plt.cla()
plt.clf()

plt.scatter(f, phi)
plt.plot(f, np.polyval(np.polyfit(f, phi, 1), f))
plt.grid()
plt.xlabel('f, МГц')
plt.ylabel('Фаза, рад')
plt.title('ФЧХ')
plt.savefig('3_2.png')
# plt.show()
plt.cla()
plt.clf()

y = [k[i] ** 2 - (a[i] / 100) ** 2 for i in range(len(k))]
x = [4 * math.pi ** 2 * fi ** 2 / 10 for fi in f]
koef = np.polyfit(x, y, 1)[0]
sig_y = [10] * len(y)
# fig, ax = plt.subplots()
plt.scatter(x, y)
plt.plot(x, np.polyval(np.polyfit(x, y, 1), x), label='k=' + str(round(koef, 3)))
plt.grid()
plt.xlabel('$w^2, 10^{13} c^{-2}$')
plt.ylabel('$k^2 - a^2, 10^{-6} см^{-2}$')
# ax.errorbar(x, y, yerr=sig_y, fmt='.', linewidth=2, capsize=6)
plt.legend()
plt.savefig('4.png')
# plt.show()
plt.cla()
plt.clf()

c = 2.99792458 * 10 ** 10  # в СГС
LC = c ** 2 * koef / 10 ** 19
print('LC=', LC)

R0 = 50 / 10 ** 12
L = c * R0 * LC ** 0.5
print('L=', round(L, 3), 'ед.СГС')
C = LC ** 0.5 / c / R0
print('C=', round(C, 3), 'ед.СГС')

x2 = [fi ** 0.5 for fi in f]
y2 = a
koef2 = np.polyfit(x2, y2, 1)[0]
sig_y2 = [1] * len(y2)
# fig, ax = plt.subplots()
plt.scatter(x2, y2)
plt.plot(x2, np.polyval(np.polyfit(x2, y2, 1), x2), label='k=' + str(round(koef2, 3)))
# ax.errorbar(x2, y2, yerr=sig_y2, fmt='.', linewidth=2, capsize=6)
plt.grid()
plt.xlabel('$f^{-1/2}, с^{1/2}$')
plt.ylabel('$a, 10^{-5} см^{-1}$')
plt.legend()
plt.savefig('5.png')
# plt.show()
plt.cla()
plt.clf()
d = 1.37 * 10  # см
sig1 = (4 * C * (v_f1 + v_f2)/2 / koef2 * 10 ** 5 / c / d) ** 2
print('sig1=', round(sig1 / 10 ** 8, 2), '10^8 ед. СГС')

x3 = [fi ** (3 / 2) / 100 for fi in f]
y3 = [a[i] * k[i] / 100 for i in range(len(a))]
koef3 = np.polyfit(x3, y3, 1)[0]
sig2 = (4 * math.pi * C * (v_f1 + v_f2)/2 / koef3 * 10 ** 4 / c / d) ** 2
print('sig2=', round(sig2 / 10 ** 8, 2), '10^8 ед. СГС')
sig_y3 = [0.07] * len(y3)
# fig, ax = plt.subplots()
plt.scatter(x3, y3)
plt.plot(x3, np.polyval(np.polyfit(x3, y3, 1), x3), label='k='+str(round(koef3, 3)))
# ax.errorbar(x3, y3, yerr=sig_y3, fmt='.', linewidth=2, capsize=6)
plt.grid()
plt.xlabel('$f^{3/2}, 10^{9} c^{-3/2}$')
plt.ylabel('$a*k, 10^{-6} см^{-2}$')
plt.legend()
plt.savefig('6.png')
# plt.show()
plt.cla()
plt.clf()


phi_dl = [12, 10, 9, 11, 10, 10, 11, 9]
f_dl = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
phi_dl_rad = [round(phi_dl[i] * f_dl[i] / 10 ** 3 + 2 * math.pi * f_dl[i], 3) for i in range(len(f_dl))]
koef4 = np.polyfit(f_dl, phi_dl_rad, 1)[0]
print('фаза в радианах:', phi_dl_rad)
sig_y4 = [1.2] * len(f_dl)
# fig, ax = plt.subplots()
plt.scatter(f_dl, phi_dl_rad)
plt.plot(f_dl, np.polyval(np.polyfit(f_dl, phi_dl_rad, 1), f_dl), label='k='+str(round(koef4, 3)))
# ax.errorbar(f_dl, phi_dl_rad, yerr=sig_y4, fmt='.', linewidth=2, capsize=6)
plt.grid()
plt.xlabel('$f, кГц$')
plt.ylabel('фаза, рад')
plt.legend()
plt.savefig('7.png')
# plt.show()
plt.cla()
plt.clf()


N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
U1 = [18, 9.5, 4.5, 14.1, 19.5, 19.6, 13.2, 2.8, 9.3, 17, 18.2]
U2 = [19.8, 13.4, 4.3, 10.7, 18, 19.1, 14.4, 4.6, 8.5, 16.5, 17.7]
U3 = [28.7, 23.1, 16.6, 21.4, 12.8, 14.1, 16, 6, 18.5, 4.7, 10.4]
plt.scatter(N, U1)
plt.scatter(N, U2)
plt.scatter(N, U3)
plt.plot(N, U1, label='f=4.35кГц')
plt.plot(N, U2, label='f=5.1кГц')
plt.plot(N, U3, label='f=13.8кГц')
plt.grid()
plt.xlabel('N')
plt.ylabel('U, В')
plt.legend()
plt.savefig('8.png')
plt.show()