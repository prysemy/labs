import math

import matplotlib.pyplot as plt
import numpy as np

c = 299792458
nu = 36e9
lam = c / nu
print(round(lam * 10 ** 3, 2), 'мм')

l1 = np.array([2, 2.5, 3, 3.5, 4, 4.5, 5])
I1 = np.array([77, 60, 51, 38, 29, 22, 16])

# plt.scatter(l1, I1)
# plt.plot(l1, np.polyval(np.polyfit(l1, I1, 1), l1))
# plt.grid()
# plt.xlabel('l, мм')
# plt.ylabel('I, мкА')
# plt.show()


I2 = np.array([48, 64, 71, 82, 87, 95, 98])
l2 = np.array([2, 2.5, 3, 3.5, 4, 4.5, 5])

# plt.scatter(l2, I2, color='orange')
# plt.plot(l2, np.polyval(np.polyfit(l2, I2, 1), l2), color='orange')
# plt.grid()
# plt.xlabel('l, мкм')
# plt.ylabel('I, мкА')
# plt.show()

t = (I1 / 100)
r = (I2 / 100)
print(t)
print(r)
print(t + r)
# xerr = np.array([0.1] * len(l1))
# yerr = np.array([0.01] * len(t))
# plt.scatter(l1, t)
# plt.plot(l1, np.polyval(np.polyfit(l1, t, 1), l1), label='t')
# # plt.errorbar(l1, t, xerr=xerr, yerr=yerr, fmt='o-', ecolor='red')
# plt.scatter(l2, r)
# plt.plot(l2, np.polyval(np.polyfit(l2, r, 1), l2), label='r')
# # plt.errorbar(l2, r, xerr=xerr, yerr=yerr, fmt='o-', ecolor='red')
# plt.scatter(l1, t+r)
# plt.plot(l2, np.polyval(np.polyfit(l2, t+r, 1), l2), label='t+r')
# # plt.errorbar(l1, t+r, xerr=xerr, yerr=yerr, fmt='o-', ecolor='red')
# plt.grid()
# plt.legend()
# plt.xlabel('l, мм')
# plt.savefig('graph1.png')
# plt.show()

# logt = np.log(t)
# print('log:', logt)
# plt.scatter(l1, logt)
# k, b = np.polyfit(l1, logt, 1)[0], np.polyfit(l1, logt, 1)[1]
# plt.plot(l1, np.polyval(np.polyfit(l1, logt, 1), l1), label='y='+str(round(float(k), 4))+'x+'+str(round(float(b), 4)))
# plt.grid()
# plt.ylabel('logT')
# plt.xlabel('l, мм')
# plt.legend()
# plt.savefig('graph2.png')
# plt.show()

# L = -k / 1000
# print('Lambda = -k =', -L)
# n = (16 * 3.1415 * L ** 2 + (8.33 / 1000) ** 2) ** 0.5 / (4 * 3.1415 * L) / math.sin(45)
# print(n)

dx = 55.25 - 55

x = np.array([0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35])
I = np.array([50, 52, 55, 59, 62, 67, 70])

plt.scatter(x, I)
plt.plot(x, np.polyval(np.polyfit(x, I, 1), x))
plt.grid()
plt.xlabel('x, мм')
plt.ylabel('I, мкА')
plt.savefig('graph3.png')
plt.show()
