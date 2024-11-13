import math

import matplotlib.pyplot as plt
import numpy as np

R = np.arange(20, 91, 10)
x = np.array([135, 97, 74, 59, 51, 44, 40, 35])
x = x / 10
U0 = 1.39
R1_2 = 1 / 1000
R0 = 560
a = 1.14  # м
I = U0 * R1_2 / (R * 1000 + R0)
print('I =', I)
fig, ax = plt.subplots()
plt.scatter(x, I * 10 ** 8, s=np.array([1.2] * len(x)))
plt.plot(x, np.polyval(np.polyfit(x, I * 10 ** 8, 1), x))
ax.errorbar(x, I * 10 ** 8, xerr=[.2] * len(x), fmt='.', linewidth=2, capsize=2)
plt.grid()
plt.xlabel('x, cм')
plt.ylabel(r'$I, 10^{-8} A$')
plt.savefig('1.png')
plt.show()
k = np.polyfit(x, I, 1)[0]
print('k =', round(k * 10 ** 8, 2), '10^-8 A/cм')
k *= 100
CI = 2 * a * k
print(r'$C_I$=', round(CI * 10 ** 8, 2), '10^-8 A')

x10 = 13.4
x20 = 10.7
T0 = 5
O0 = math.log(x10 / x20, math.e)
print('teta =', O0)

R = np.arange(24, 80, 4)
x1 = [213, 182, 154, 138, 124, 187, 164, 156, 146, 211, 194, 175, 194, 177]
x2 = [20, 22, 22, 25, 25, 44, 43, 46, 45, 73, 68, 66, 74, 69]
O = np.array([round(math.log(x1[i] / x2[i], math.e), 2) for i in range(len(x1))])
print(O)

R_cr = np.array((R * 1000 + R0) / (1 + 4 * math.pi ** 2 / O ** 2) - R0)
print('R_cr =', R_cr)
print(R_cr.mean() + 6000)

Rl = np.arange(4, 23, 2)
l = np.array([63, 78, 90, 101, 104, 116, 122, 126, 131, 137])
fig1, ax1 = plt.subplots()
plt.scatter(Rl + R0 / 1000, l / 10, s=np.array([1.4] * len(l)))
ax1.errorbar(Rl + R0 / 1000, l / 10, yerr=[.2] * len(l), fmt='.', linewidth=2, capsize=3)
plt.grid()
plt.xlabel(r'$R + R_0$, кОм')
plt.ylabel(r'$l$, cм')
plt.savefig('2.png')
plt.show()
