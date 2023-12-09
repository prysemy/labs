import numpy as np

import math
import matplotlib.pyplot as plt

f1 = [3.246, 6.503, 9.742, 12.992, 16.212]
f2 = [4.253, 8.522, 12.766, 17.021, 21.260]
f3 = [4.131, 8.251, 12.381, 16.525, 20.630]
L = 600 / 1000
m1 = 39.379 / 1000
l1 = 43.3 / 1000
d1 = 11.42 / 1000
m2 = 12.484 / 1000
l2 = 45.2 / 1000
d2 = 11.23 / 1000
m3 = 36.918 / 1000
l3 = 40.5 / 1000
d3 = 12.21 / 1000
ro1 = m1 * 4 / (l1 * math.pi * d1 ** 2)
ro2 = m2 * 4 / (l2 * math.pi * d2 ** 2)
ro3 = m3 * 4 / (l3 * math.pi * d3 ** 2)
print('плотности: медь -', ro1, ', дюраль -', ro2, ', сталь -', ro3)

f_1 = 4.25178
f_2 = 4.25437
df = f_2 - f_1
Q = f_1 / 2 / df
print('добротность: ', Q)

n = [1, 2, 3, 4, 5]
f1_ = np.polyval(np.polyfit(n, f1, 1), n)
k1 = np.polyfit(n, f1, 1)[0]
plt.scatter(n, f1, color='red', s=np.array([1.3]) * len(n))
plt.plot(n, f1_, color='red', label='медь')

f2_ = np.polyval(np.polyfit(n, f2, 1), n)
k2 = np.polyfit(n, f2, 1)[0]
plt.scatter(n, f2, color='black', s=np.array([1.3]) * len(n))
plt.plot(n, f2_, color='black', label='дюраль')

f3_ = np.polyval(np.polyfit(n, f3, 1), n)
k3 = np.polyfit(n, f3, 1)[0]
plt.scatter(n, f3, color='blue', s=np.array([1.3]) * len(n))
plt.plot(n, f3_, color='blue', label='сталь')
plt.grid()
plt.legend()
plt.xlabel('номер гармоники n')
plt.ylabel('частота f(n), кГц')
# plt.savefig('1.png')
# plt.show()

print('k1=', k1, 'k2=', k2, 'k3=', k3)
u1 = 2 * L * k1 * 1000
u2 = 2 * L * k2 * 1000
u3 = 2 * L * k3 * 1000
print('скорости:: медь:', u1, 'дюраль:', u2, 'сталь:', u3)

E1 = u1 ** 2 * ro1
E2 = u2 ** 2 * ro2
E3 = u3 ** 2 * ro3
print('модули Юнга:: медь:', E1, 'дюраль:', E2, 'сталь:', E3)

s_u1 = 33
s_u2 = 36
s_u3 = 35
s_ro1 = 3
s_ro2 = 1.1
s_ro3 = 3
s_E1 = (4 * (s_u1 / u1) ** 2 + (s_ro1 / ro1) ** 2) ** 0.5
s_E2 = (4 * (s_u2 / u2) ** 2 + (s_ro2 / ro2) ** 2) ** 0.5
s_E3 = (4 * (s_u3 / u3) ** 2 + (s_ro3 / ro3) ** 2) ** 0.5
print('погрешности:: медь:', s_E1, 'дюраль:', s_E2, 'сталь:', s_E3)

