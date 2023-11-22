import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

import math

n1 = [3, 2, 3, 2, 2]
n2 = [2, 2, 2, 2, 2]
n3 = [1.5, 1.5, 1.5, 1.5, 1.5]
n4 = [1, 1, 1, 1, 1]
n5 = [1, 1, 0.5, 0.5, 0.5]
tn1 = [124.87, 81.91, 125.13, 81.56, 75.44]
tn2 = [94.97, 93.00, 93.84, 94.16, 93.12]
tn3 = [106.91, 106.75, 106.78, 105.91, 106.31]
tn4 = [89.00, 89.34, 88.94, 91.28, 90.81]
tn5 = [129.56, 135.60, 66.44, 66.41, 65.28]
T = list()
T.append(sum(tn1[i] / n1[i] for i in range(5)) / 5)
T.append(sum(tn2[i] / n2[i] for i in range(5)) / 5)
T.append(sum(tn3[i] / n3[i] for i in range(5)) / 5)
T.append(sum(tn4[i] / n4[i] for i in range(5)) / 5)
T.append(sum(tn5[i] / n5[i] for i in range(5)) / 5)
# print(T)

fi1 = [10, 9, 12, 8, 8]
fi2 = [10, 9, 10, 10, 9]
fi3 = [9, 9, 9, 9, 9]
fi4 = [6, 6, 6, 7, 7]
fi5 = [12, 11, 6, 6, 6]
fi = list()
fi.append(sum(fi1) / 5)
fi.append(sum(fi2) / 5)
fi.append(sum(fi3) / 5)
fi.append(sum(fi4) / 5)
fi.append(sum(fi5) / 5)
# print(fi)
W = [154.8, 133.8, 88.8, 70.0, 47.2]
M = [320, 260, 170, 130, 90]
sigma_t = 0.3
sigma_w = [W[i] * sigma_t / T[i] for i in range(5)]
# print(sigma_w)
m = [266.6, 214.2, 141.2, 111.2, 75.6]
sigma_m = 0.5 / 1000
sigma_g = 4 / 1000
sigma_l = 0.001
g = 9.815034
l = 120 / 1000
sigma_M = [M[i] * ((sigma_m / m[i]) ** 2 + (sigma_g / g) ** 2 + (sigma_l / l) ** 2) ** 0.5 for i in range(5)]
# print(sigma_M)

k, b = np.polyfit(M, W, 1)
print(k)
W_ = np.polyval(np.polyfit(M, W, 1), M)
plt.xlabel('момент силы M, мН*м')
plt.ylabel('угловая скорость W, рад/c * 10^(-3)')

plt.grid()
plt.plot(M, W_)
xerr = np.array(sigma_M)
yerr = np.array(sigma_w)
x = np.array(M)
y = np.array(W)


def foo(a, x, b):
    return a * x + b


popt, pcov = curve_fit(foo, x, y)
plt.axline((x[0], foo(x, *popt)[0]), (x[4], foo(x, *popt)[4]), slope=None)
M_0 = (((foo(x, *popt)[4] - foo(x, *popt)[0]) / (x[4] - x[0])) * x[0] - foo(x, *popt)[0]) / (
        (foo(x, *popt)[4] - foo(x, *popt)[0]) / (x[4] - x[0]))
print('M tr = ', M_0)
# plt.errorbar(x, y, yerr=yerr, fmt='| ', ecolor='#9F0202', elinewidth=0.5, capsize=1.5)
# plt.errorbar(x, y, xerr=xerr, fmt='_ ', ecolor='#9F0202', elinewidth=0.5, capsize=1.5)
plt.scatter(M, W, s=np.array([1.2]) * len(M), color='black')
plt.savefig('1.png')
plt.show()

I_c = 1.25 / 1000
m_c = 1.6165
sigma_l1 = 0.0001
r = 3.93 / 100
sigma_I_c = I_c * ((sigma_m / m_c) ** 2 + 2 * (sigma_l1 / r) ** 2) ** 0.5
# print(sigma_I_c)

I_0 = I_c * (3.1889 / 4.01) ** 2
sigma_I_0 = I_0 * ((sigma_I_c / I_c) ** 2 + 2 * (0.5 / 3.1889) ** 2 + (0.5 / 4.01) ** 2) ** 0.5
# print(sigma_I_0)

nu = [391, 382, 373, 364, 356, 347, 339, 331, 323, 315]
t = np.arange(0, len(nu) * 30, 30)
nu_ = np.polyval(np.polyfit(t, nu, 1), t)
knu, bnu = np.polyfit(t, nu, 1)
plt.plot(t, nu_)
plt.scatter(t, nu, s=np.array([1.2]) * len(t), color='black')
plt.grid()
plt.ylabel('частота ротора, Гц')
plt.xlabel('время, с')
plt.savefig('2.png')
plt.show()

e = knu * 2 * math.pi
print(e)
sigma_M = sum(
    [M[i] * ((sigma_m / m[i]) ** 2 + (sigma_g / g) ** 2 + (sigma_l / l) ** 2) ** 0.5 for i in range(len(M))]) / 5
print(2695.5 * ((2695.5 * 790 / sigma_M) ** 2 + (790 / 0.0002) ** 2) ** 0.5)
