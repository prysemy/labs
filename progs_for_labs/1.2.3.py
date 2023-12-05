import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t0 = [i / 10 for i in [44.82, 44.51, 44.33, 44.22, 44.14]]
T0 = sum(t0) / 5
R = 114.6 / 1000
r = 30.5 / 1000
m = 983.2 / 1000
z = 213.9 / 100
g = 9.81
k = g * R * r / (4 * np.pi ** 2 * z)
I0 = k * m * T0 ** 2
print(T0, I0 * 1000)
t1 = [i / 10 for i in [39.457, 39.377, 39.347, 39.312, 39.278]]
T1 = sum(t1) / 5
m1 = 589.5 / 1000
I1 = (m + m1) * k * T1 ** 2
print('диск: ', I1 * 1000)
Rd = 8.4 / 100
I_1 = m1 * Rd ** 2 / 2
print('теор диск:', I_1 * 1000)
m2 = 776.6 / 1000
t2 = [i / 10 for i in [41.967 / 2, 41.891 / 2, 41.839 / 2, 41.803 / 2, 41.774 / 2]]
T2 = sum(t2) / 5
I2 = (m + m2) * k * T2 ** 2
print('кольцо: ', I2 * 1000)
Rk = 7.6 / 100
I_2 = m2 * Rk ** 2
print('теор кольцо: ', I_2 * 1000)
t3 = [i / 10 for i in [19.67 * 2, 19.65 * 2, 19.65 * 2, 19.62 * 2, 19.6 * 2]]
T3 = sum(t3) / 5
I3 = k * (m + m1 + m2) * T3 ** 2
print('диск+кольцо: ', I3 * 1000)

m11 = 721.2 / 1000
m12 = 720.8 / 1000
h = [0, 0.5, 1, 1.5, 2]
th = [i / 10 for i in
      [15.48, 15.46, 15.46, 15.53, 15.53, 15.5, 15.63, 15.62, 15.59, 15.79, 15.75, 15.75, 15.99, 15.98, 15.92]]
Th = [(th[i - 2] + th[i - 1] + th[i]) / 3 for i in range(2, len(th), 3)]
print(Th)
Ih = [k * (m + m11 + m12) * Th[i] ** 2 for i in range(len(Th))]
print('половинки', [i * 1000 for i in Ih])

sigma_h = 0.1
sigma_I = 0

Ih_ = np.polyval(np.polyfit(h, [i * 1000 for i in Ih], 1), h)
plt.plot(h, Ih_)
plt.scatter(h, [i * 1000 for i in Ih], s=np.array([1.2]) * len(h), color='black')
plt.grid()


plt.xlabel('h, см')
plt.ylabel('I * 10^3, кг*м^2')
plt.show()
