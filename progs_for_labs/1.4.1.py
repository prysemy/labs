import matplotlib.pyplot as plt
import numpy as np
import math


def mnk(x, y):
    n_ = len(x)
    mx = x.sum() / n_
    my = y.sum() / n_
    a2 = np.dot(x.T, x) / n_
    a11 = np.dot(x.T, y) / n_

    kk = (a11 - mx * my) / (a2 - mx ** 2)
    bb = my - kk * mx
    return kk, bb


m_s = 891.4 / 1000
M = 314.1 / 1000
m_p = 78.4 / 1000
l = 996.4 / 1000
a = 226.7 / 1000
x0 = 499 / 1000
dy = 744.8 / 1000
y = [dy - i / 1000 for i in
     [124, 124, 134.5, 134.5, 154.2, 154.2, 165, 165, 205.3, 205.3, 215.8, 215.8, 233.3, 233.3, 277.7, 277.7]]
x_c = [(m_s * x0 + M * y[i]) / (m_s + M) for i in range(len(y))]
print('y = ', [round(i * 1000, 1) for i in y])
print('x_c = ', [round(i * 1000, 1) for i in x_c])
n = 33
t_n = [51.68, 51.67, 51.44, 51.44, 51.03, 51.04, 50.83, 50.82, 50.05, 50.05, 49.86, 49.86, 49.54, 49.54, 48.78, 48.78]
T = [t_n[i] / n for i in range(len(t_n))]
t_s = sum(T) / len(T)
# g_cl = math.sqrt(1/19 * sum((T[i] - t_s) ** 2 for i in range(len(t_n))))
g_sys = 0.005
g_cl = 4.2 * 10 ** (-6)
g_t = math.sqrt(g_cl ** 2 + g_sys ** 2)
print(g_cl, g_t)
N = g_t / t_s / 0.0001
print('N = ', N)
T0 = 1.5349
g0 = ((l * 1.75) ** 2 / 12 + a ** 2) * 4 * math.pi ** 2 / 0.4783 / (1 + m_p / m_s) / T0 ** 2
print(g0)
g = [(l ** 2 * 3.286 / 12 + a ** 2) * 4 * math.pi ** 2 / x_c[i] / (1 + m_p / m_s) / T[i] ** 2 for i in range(len(T))]
print('g = ', [round(i, 3) for i in g])
g_ = sum(g) / len(g)
print('g_ = ', g_)
# fig, ax = plt.subplots()
plt.scatter(y, T, color='blue')
plt.xlabel('y, m')
plt.ylabel('T, s')
plt.plot(y, T, color='black')
plt.grid()
# ax.errorbar(y, T, [0.001] * len(T), [0.001] * len(y), fmt='.', linewidth=2, capsize=4)
plt.savefig('1.png')
# plt.show()

u = np.array([T[i] ** 2 * x_c[i] for i in range(len(T))])
v = np.array([y[i] ** 2 for i in range(len(y))])
print('u = ', u)
print('v = ', v)
plt.scatter(u, v, color='blue')
z2 = np.polyval(np.polyfit(u, v, 1), u)
plt.xlabel('T^2 * x_c, s^2 * m')
plt.ylabel('y^2, m^2')
plt.grid()
plt.plot(u, z2, color='black')
print('y = ', y)
print('T = ', [round(i, 4) for i in T])
print(len(T))
k, b = mnk(u, v)
print('k = ', k, ', b = ', b)
gk = 1 / (n ** 0.5) * ((sum(i ** 2 for i in u) - sum(u) ** 2) / (sum(i ** 2 for i in v) - sum(v) ** 2) - b ** 2) ** 0.5
gk /= 10
gb = gk * (-sum(i ** 2 for i in u) + sum(i for i in u) ** 2) ** 0.5 / 100
print('gk = ', gk, ', gb = ', gb)
g_real = 4 * math.pi ** 2 * (M - 1.95 * m_p) / k / m_s
print('g_real = ', g_real)
gg_real = g_real * gk / k
print('gg_real = ', gg_real)
plt.savefig('2.png')
# plt.show()
