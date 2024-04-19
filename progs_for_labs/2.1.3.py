import matplotlib.pyplot as plt
import numpy as np

k = [1, 2, 3, 4, 5]
T = [294.7, 303.2, 318.1, 333]
f1 = [261, 498, 760, 987, 1232]
df1 = [f1[i] - f1[0] for i in range(len(f1))]
f2 = [503, 749, 1000, 1248, 1496]
df2 = [f2[i] - f2[0] for i in range(len(f2))]
f3 = [516, 767, 1024, 1277, 1530]
df3 = [f3[i] - f3[0] for i in range(len(f3))]
f4 = [527, 784, 1046, 1307, 1562]
df4 = [f4[i] - f4[0] for i in range(len(f4))]

plt.scatter(k, df1)
plt.plot(k, np.polyval(np.polyfit(k, df1, 1), k), label='T=21.7°C')
plt.scatter(k, df2)
plt.plot(k, np.polyval(np.polyfit(k, df2, 1), k), label='T=30.2°C')
plt.scatter(k, df3)
plt.plot(k, np.polyval(np.polyfit(k, df3, 1), k), label='T=45.1°C')
plt.scatter(k, df4)
plt.plot(k, np.polyval(np.polyfit(k, df4, 1), k), label='T=60.0°C')

plt.grid()
plt.legend()
plt.xlabel('номер резонанса k')
plt.ylabel('разность fk+1 - f1')
plt.savefig('1.png')
# plt.show()

k1 = np.polyfit(k, df1, 1)[0]
k2 = np.polyfit(k, df2, 1)[0]
k3 = np.polyfit(k, df3, 1)[0]
k4 = np.polyfit(k, df4, 1)[0]
print(k1, k2, k3, k4)

L = 0.7

c1 = k1 * 2 * L
c2 = k2 * 2 * L
c3 = k3 * 2 * L
c4 = k4 * 2 * L
c = [c1, c2, c3, c4]

s_c = [ci * ((2.82 / 1000) ** 2 + (0.1 / 300) ** 2) ** 0.5 for ci in c]
print('погрешность скоростей: ', s_c)

# plt.scatter(T, [c1, c2, c3, c4])
# plt.show()
print('скорости звука: ', round(c1, 2), round(c2, 2), round(c3, 2), round(c4, 2), 'м/с')

mu = 29 / 1000
R = 8.314
g = [mu / R * c[i] ** 2 / T[i] for i in range(len(T))]
print(g)
gs = sum(g)/4
print('среднее значение: ', gs)

s_g = gs * ((0.99/350) ** 2 + (0.1/300) ** 2) ** 0.5
print('погрешность гамма:', s_g)

A1 = [800, 1700, 1100, 800, 550]
A2 = [1600, 1050, 750, 500, 350]
A3 = [1500, 1000, 700, 500, 300]
A4 = [1400, 900, 700, 400, 250]