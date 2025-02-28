import matplotlib.pyplot as plt
import numpy as np

nu = np.array([1.09169, 1.03036, 1.06489, 1.15895, 1.12559])
m = np.arange(-2, 3)
# y в мкм
y1 = np.array([-252, -196, 0, 132, 240])
y2 = np.array([-240, -196, 0, 116, 232])
y3 = np.array([-256, -100, 0, 120, 240])
y4 = np.array([-280, -108, 0, 136, 256])
y5 = np.array([-244, -96, 0, 136, 264])

plt.scatter(m, y1, s=np.array([15] * len(m)))
plt.plot(m, np.polyval(np.polyfit(m, y1, 1), m), label=r'$\nu=1.09$МГц')
plt.scatter(m, y2, s=np.array([15] * len(m)))
plt.plot(m, np.polyval(np.polyfit(m, y2, 1), m), label=r'$\nu=1.03$МГц')
plt.scatter(m, y3, s=np.array([15] * len(m)))
plt.plot(m, np.polyval(np.polyfit(m, y3, 1), m), label=r'$\nu=1.06$МГц')
plt.scatter(m, y4, s=np.array([15] * len(m)))
plt.plot(m, np.polyval(np.polyfit(m, y4, 1), m), label=r'$\nu=1.16$МГц')
plt.scatter(m, y5, s=np.array([15] * len(m)))
plt.plot(m, np.polyval(np.polyfit(m, y5, 1), m), label=r'$\nu=1.13$МГц')
plt.grid()
plt.xlabel('порядок модуляции m')
plt.ylabel('координата y, мкм')
plt.xticks(m)
plt.legend()
plt.savefig('graph1.png')
# plt.show()
plt.clf()
plt.cla()

# расстояние между соседними полосами:
k1 = np.polyfit(m, y1, 1)[0] / 10 ** 6  # м
k2 = np.polyfit(m, y2, 1)[0] / 10 ** 6  # м
k3 = np.polyfit(m, y3, 1)[0] / 10 ** 6  # м
k4 = np.polyfit(m, y4, 1)[0] / 10 ** 6  # м
k5 = np.polyfit(m, y5, 1)[0] / 10 ** 6  # м

f = 28 / 100  # м
lamb = 6400 / 10 ** 10  # м
# длина УЗ-волны
Lamb1 = lamb * f / k1 * 1000  # мм
Lamb2 = lamb * f / k2 * 1000  # мм
Lamb3 = lamb * f / k3 * 1000  # мм
Lamb4 = lamb * f / k4 * 1000  # мм
Lamb5 = lamb * f / k5 * 1000  # мм
Lamb = (Lamb1 + Lamb2 + Lamb3 + Lamb4 + Lamb5) / 5
print('длина УЗ-волны', round(Lamb, 3), 'мм')

# скорость звука
v1 = Lamb1 * nu[0] * 10 ** 3  # м/c
v2 = Lamb2 * nu[1] * 10 ** 3  # м/c
v3 = Lamb3 * nu[2] * 10 ** 3  # м/c
v4 = Lamb4 * nu[3] * 10 ** 3  # м/c
v5 = Lamb5 * nu[4] * 10 ** 3  # м/c
print(v1, v2, v3, v4, v5)
v = (v1 + v2 + v3 + v4 + v5) / 5
print('I. скорость звука в воде:', round(v, 2), 'м/c')
print()

nu_a = np.array([2.04457, 1.71041, 1.50219, 2.08881, 1.37896, 1.82202])
nu_a_sort = np.array([nu_a[4], nu_a[2], nu_a[1], nu_a[-1], nu_a[0], nu_a[3]])
y1 = np.array([0.084, 0.132, 0.084, 0.036, 0.192, 0.048])
y1_sort = np.array([y1[4], y1[2], y1[1], y1[-1], y1[0], y1[3]])
y2 = np.array([1.98, 1.956, 1.908, 1.98, 1.908, 1.968])
y2_sort = np.array([y2[4], y2[2], y2[1], y2[-1], y2[0], y2[3]])
N = np.array([20, 17, 15, 20, 13, 17])
N_sort = np.array([N[4], N[2], N[1], N[-1], N[0], N[3]])
k_a = (y2 - y1) * 2 / N / 10 ** 6  # м
k_a_sort = (y2_sort - y1_sort) * 2 / N_sort / 10 ** 6
Lamb_a = lamb * f / k_a  # мм
Lamb_a_sort = lamb * f / k_a_sort
print(Lamb_a_sort)
print('длина УЗ-волны', round(np.sum(Lamb_a) / 6, 3), 'мм')
v = Lamb_a * nu_a * 10 ** 3
print(v)
print('II. скорость звука в воде:', round(np.sum(v) / 6, 2), 'м/c')

nu1 = 1 / nu_a
plt.scatter(nu1, Lamb_a)
plt.plot(nu1, np.polyval(np.polyfit(nu1, Lamb_a, 1), nu1))
plt.grid()
plt.xlabel(r'$\frac{1}{\nu}, 10^{-6}c$')
plt.ylabel(r'$\Lambda, мм$')
plt.savefig('graph2.png')
plt.show()

v = np.polyfit(nu1[:-1], Lamb_a[:-1], 1)[0] * 1000
print('II. скорость звука в воде:', round(v, 2), 'м/c')
