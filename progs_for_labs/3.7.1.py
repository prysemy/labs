import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

f = [30, 40, 60, 70, 80, 90, 100, 110, 120, 130, 112, 135, 157, 180, 202, 225, 281, 337, 394, 450, 563, 675, 788, 900,
     1125]
# 140, 160, 180, 200, 220, 240, 260, 300, 450, 600, 750, 900, 1050, 1200,
# 1350]
I = [244.62, 242.12, 235.62, 231.93, 228.22, 224.53, 220.93, 217.49, 214.23, 211.16, 207.9, 202.82, 198.45, 194.75,
     191.58, 188.85, 186.47, 182.56, 172.98, 166.21, 159.97, 15.77, 147.55, 141.33, 135.21]
U = [.101, .1316, .1858, .2091, .2299, .2484, .2647, .2791, .2916, .3026, .312, .3279, .3402, .3496, .357, .3627, .3671,
     .3733, .3796, .3747, .3653, .3535, .3405, .3268, .313]
e = [U[i] / I[i] * 1000 / f[i] for i in range(len(I))]
x = [i ** 2 for i in f]
y = [1 / e1 ** 2 for e1 in e]
k, b = np.polyfit(x[:-4] + x[-3:], y[:-4] + y[-3:], 1)
e0 = 1 / b ** 0.5
print(k, b)
sf = ScalarFormatter()
sf.set_powerlimits((-4, 4))
fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(sf)
plt.scatter(x[:-4] + x[-3:], y[:-4] + y[-3:])
plt.plot(x[:-4] + x[-3:], np.polyval(np.polyfit(x[:-4] + x[-3:], y[:-4] + y[-3:], 1), x[:-4] + x[-3:]),
         label='k=' + str(round(k, 4)))
plt.grid()
plt.ylabel(r'$\frac{1}{\epsilon^2}, \frac{Гц^2}{Ом^2}$')
plt.xlabel(r'$\nu^2, Гц^2$')
plt.legend()
plt.savefig('1.png')
plt.show()

a = 22.5 / 1000
h = 1.5 / 1000
mu0 = 1.256 / 10 ** 6
sigma = e0 * k ** 0.5 / a / h / mu0 / 3.1415
print(round(sigma / 10 ** 7, 2), '*10^7')

# f4 = [140, 160, 180, 200, 220, 240, 260, 300, 450, 600, 750, 900, 1050, 1200, 1350]
# fi4 = [5, 4, 3.1, 2.7, 2.4, 2, 3.3/2, 2.8/2, 2.8/5, 1.4/5, 2.5/10, 1.5/10, 1/10, 0.6/10, 0.3/10]
f4 = [112, 135, 157, 180, 202, 225, 281, 337, 394, 450, 563, 675, 788, 900, 1125]
fi4 = [1.38, 1.29, 1.33, 1.4, 1.12, 1.11, 1.2, 1.15, 1.13, 1.15, 1.1, 1.06, 1.06, 1.01, 1]
psi4 = [fi4[i] * math.pi - math.pi / 2 for i in range(len(f4))]
tanpsi = [abs(math.tan(ps)) for ps in psi4]
k2 = np.polyfit(f4[:-2], tanpsi[:-2], 1)[0]
fig, ax = plt.subplots()
plt.scatter(f4[:-2], tanpsi[:-2])
plt.plot(f4[:-2], np.polyval(np.polyfit(f4[:-2], tanpsi[:-2], 1), f4[:-2]), label='k=' + str(round(k2, 4)))
ax.errorbar(f4[:-2], tanpsi[:-2], yerr=[0.5] * len(tanpsi[:-2]), fmt='.', linewidth=2, capsize=6)
plt.grid()
plt.xlabel(r'$\nu, Гц$')
plt.ylabel(r'$tg\psi$')
plt.legend()
plt.savefig('2.png')
plt.show()

sigma2 = k2 / a / h / mu0 / 3.1415
print(round(sigma2 / 10 ** 7, 2), '*10^7')

# f5 = [1400, 1757, 2205, 2767, 3473, 4359, 5471, 6866, 8617, 10814, 13571, 17032, 21375, 26826, 33666, 42251]
f5 = [1352, 1916, 2592, 3156, 3720, 4283, 4847, 5411, 5974, 6538, 7102, 7662, 8229, 8793, 9357, 9920, 10484, 11048]
fi5 = [0.97, 0.93, 0.93, 0.85, 0.87, 0.86, 0.8, 0.82, 0.81, 0.81, 0.77, 0.76, 0.75, 0.74, 0.72, 0.71, 0.69, 0.7]
psi5 = [fi5[i] * math.pi - math.pi / 2 for i in range(len(fi5))]
nu5 = [f1 ** 0.5 for f1 in f4] + [f1 ** 0.5 for f1 in f5]
psi5g = [ps - math.pi / 4 for ps in psi4] + [ps - math.pi / 4 for ps in psi5]
fig, ax = plt.subplots()
plt.scatter(nu5[::-1], psi5g)
plt.plot([0, 90], [0, 1.3], label='k=' + str(round(1.3 / 90, 4)))
ax.errorbar(nu5[::-1], psi5g, yerr=[0.25] * len(psi5g), fmt='.', linewidth=1, capsize=4)
plt.grid()
plt.xlabel(r'$\sqrt{\nu}$')
plt.ylabel(r'$\psi-\pi/4$')
plt.legend()
plt.savefig('3.png')
plt.show()

sigma3 = (1.3 / 90) ** 2 / 3.1415 / mu0 / h ** 2
print(round(sigma3 / 10 ** 7, 2), '*10^7')

# nu = [50, 200, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 5000, 10000, 15000, 16200, 20000, 25000]
# L = [9.8838, 6.1361, 4.073, 3.6867, 3.4566, 3.2108, 3.0898, 2.965, 2.9212, 2.904, 2.8892, 2.9761, 3.0494, 3.3068,
#      3.7056, 4.7325]
nu = [50, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 5000, 6000, 7500, 10000, 12000, 15000, 20000]
L = [9.99, 5.38, 3.69, 3.25, 3.09, 2.96, 2.91, 2.9, 2.89, 2.88, 2.89, 2.9, 2.95, 3.02, 3.18, 3.62]
plt.scatter(nu, L)
plt.grid()
plt.xlabel(r'$\nu, Гц$')
plt.ylabel(r'$L, мГн$')
plt.savefig('4.png')
plt.show()

Lmin = round(min(L), 2) + 0.01
Lmax = round(max(L), 2)
L_ = [(Lmax - Li) / (Li - Lmin) for Li in L]
nu_ = [ni ** 2 for ni in nu]
plt.scatter(nu_[:8], L_[:8])
plt.grid()
plt.xlabel(r'$\nu^2, Гц^2$')
plt.ylabel(r'$\frac{L_{max} - L}{L - L_{min}}$')
plt.show()
