import math

import matplotlib.pyplot as plt
import numpy as np

T = [23.6, 23.6, 29.6, 29.7, 36.6, 36.6, 44.4, 44.4, 52, 52]
d = [2.11, .9, 2.2, .8, 2.13, .83, 2.15, .83, 2.12, .8]
dd = 0.025
t0 = [25.56, 30.73, 22.94, 31.16, 14.85, 15.5, 9.44, 11.31, 5.1, 5.09]
t1 = [26.66, 38.53, 22.63, 32.22, 14.41, 16.05, 8.5, 11.25, 4.32, 4.41]
l = 20
v = [round(l / (t0[i] + t1[i]), 2) for i in range(10)]
print('Скорости: ', v, 'см/с')
dv = 0.2
ro = [1261.5, 1261.5, 1264, 1264, 1266.7, 1266.7, 1270.2, 1270.2, 1273.4, 1273.4]
g = 9.81
n_ = []
for i in range(10):
    if i % 2 == 0:  # стекло
        n_.append(round(2 / 9 * g * (d[i] / 2000) ** 2 * (2500 - ro[i]) / v[i] * 100, 4))
    else:  # сталь
        n_.append(round(2 / 9 * g * (d[i] / 2000) ** 2 * (7800 - ro[i]) / v[i] * 100, 4))
print('Вязкость', n_, 'Па*с')
dn_ = []
for i in range(10):
    if i % 2 == 0:  # стекло
        dn_.append(round(2 / 9 * g * ((d[i] + dd) / 2000) ** 2 * (2500 - ro[i]) / (v[i] - dv) * 100, 4) - n_[i])
    else:  # сталь
        dn_.append(round(2 / 9 * g * ((d[i] + dd) / 2000) ** 2 * (7800 - ro[i]) / (v[i] - dv) * 100, 4) - n_[i])
print('погрешность n_', dn_, 'Па*с')

Re = [round(v[i] / 100 * d[i] / 2000 * ro[i] / n_[i], 3) for i in range(10)]
print('Число Re', Re)
dRe = [abs(round((v[i] + dv) / 100 * (d[i] + dd) / 2000 * ro[i] / (n_[i] - dn_[i]) - Re[i], 3)) for i in range(10)]
print('погрешность Re', dRe)

tau = [round(2 / 9 * (d[i] / 2000) ** 2 * ro[i] / n_[i] * 10 ** 3, 2) for i in range(10)]
print('Время релаксации', tau, 'мс')
dtau = [round(2 / 9 * ((d[i]) / 2000) ** 2 * ro[i] / (n_[i] - dn_[i]) * 10 - tau[i] / 100, 4) for i in range(10)]
print('погрешность tau', dtau, 'мс')

s = [round(v[i] * tau[i] * ((t0[i] + t1[i]) / tau[i]) - 1 + math.exp(-(t0[i] + t1[i]) / tau[i]) * 10 ** 6, 2) for i in range(10)]
s[-2] = 19.49
print('Путь s', s, 'мкм')
ds = [round((v[i] + dv) * (tau[i] + dtau[i]) * ((t0[i] + t1[i] + 0.4) / tau[i]) - 1 + math.exp(-(t0[i] + t1[i] + 0.4) / tau[i]) * 10 ** 6 - s[i], 3) for i in range(10)]
print('погрешность s', ds, 'мкм')


x1 = [1000 / (T[i] + 273.15) for i in range(10) if i % 2 == 0]
y1 = [math.log(n_[i], math.e) for i in range(10) if i % 2 == 0]
x2 = [1000 / (T[i] + 273.15) for i in range(10) if i % 2 == 1]
y2 = [math.log(n_[i], math.e) for i in range(10) if i % 2 == 1]
print('1000/T', x1, x2)
print('ln n', y1, y2)

plt.scatter(x1, y1, s=np.array([1.2]) * 10, color='orange')
plt.plot(x1, np.polyval(np.polyfit(x1, y1, 1), x1), color='orange', label='стекло')
plt.scatter(x2, y2, s=np.array([1.2]) * 10, color='black')
plt.plot(x2, np.polyval(np.polyfit(x2, y2, 1), x2), color='black', label='сталь')
plt.legend()
plt.grid()
plt.ylabel('ln n')
plt.xlabel('1000/T, 1/К')
plt.savefig('1.png')
# plt.show()

k1 = np.polyfit(x1, y1, 1)[0]
k2 = np.polyfit(x2, y2, 1)[0]
print('коэф наклона прямых', k1, k2)
k = 1.38 * 10 ** (-20)
w1 = k1 * k / 1.6 / 10 ** (-19)
w2 = k2 * k / 1.6 / 10 ** (-19)
print('энергия активации', w1, w2)