import matplotlib.pyplot as plt
import numpy as np

R = 8.31
Cp = 40
m_ = 44 * 10 ** (-3)
T = [20, 30, 50]
dP1 = [4, 3.5, 3, 2.5, 2]
dP2 = [4, 3.6, 3.1, 2.4, 2]
dP3 = [4, 3.5, 3, 2.5, 2]
U1 = [.111, .091, .078, .057, .039]
U2 = [.109, .094, .071, .049, .035]
U3 = [.095, .081, .061, .048, .031]
dT1 = [40.2 * U1[i] for i in range(5)]
dT2 = [41.2 * U2[i] for i in range(5)]
dT3 = [42.9 * U3[i] for i in range(5)]

plt.scatter(dP1, dT1, color="black", s=np.array([2.5]) * 5)
plt.plot(dP1, np.polyval(np.polyfit(dP1, dT1, 1), dP1), color="red", label="T=20`C")
k1 = np.polyfit(dP1, dT1, 1)[0]
plt.scatter(dP2, dT2, color="black", s=np.array([2.5]) * 5)
plt.plot(dP2, np.polyval(np.polyfit(dP2, dT2, 1), dP2), color="green", label="T=30`C")
k2 = np.polyfit(dP2, dT2, 1)[0]
plt.scatter(dP3, dT3, color="black", s=np.array([2.5]) * 5)
plt.plot(dP3, np.polyval(np.polyfit(dP3, dT3, 1), dP3), color="blue", label="T=50`C")
k3 = np.polyfit(dP3, dT3, 1)[0]
plt.legend()
plt.xlabel("dP, атм")
plt.ylabel("dT, K")
plt.grid()
plt.savefig("1.png")
# plt.show()

m_1 = k1
m_2 = k2
m_3 = k3

t1 = T[0] + 273
t2 = T[1] + 273
t3 = T[2] + 273

a1 = (m_1 - m_2) / (10 ** 5) * Cp * R * t1 * t2 / (2 * (t2 - t1))
b1 = Cp * (m_2 * t2 - m_1 * t1) / 10 / (t2 - t1)

a2 = (m_2 - m_3) / (10 ** 5) * Cp * R * t2 * t3 / (2 * (t3 - t2))
b2 = Cp * (m_3 * t3 - m_2 * t2) / 10 / (t3 - t2)

# print(m_1, m_2, m_3)


print('a1, b1, a2, b2:')
print(a1, b1, a2, b2, sep=', ')

T_x = [1 / (T[i] + 273) for i in range(3)]
m_y = [m_1, m_2, m_3]
plt.scatter(T_x, m_y, color="black", s=np.array([7] * 3))
plt.plot(T_x, np.polyval(np.polyfit(T_x, m_y, 1), T_x), color="red")
plt.grid()
plt.xlabel("1/T, 1/K")
plt.ylabel("m, K/атм")
plt.savefig("2.png")
# plt.show()

k, kk = np.polyfit(T_x, m_y, 1)[0], np.polyfit(T_x, m_y, 1)[1]
a = k * R * Cp / 2 / 10 ** 5
print('a =', a)
b = kk * Cp
print('b =', b)

T_inv = 2 * a / R / b
print('T_inv =', abs(T_inv) + 273)
T_inv1 = 2 * a1 / R / b1 * 10 ** 4
print('T_inv1 =', abs(T_inv1) + 273)
T_inv2 = 2 * a2 / R / b2 * 10 ** 4
print('T_inv2 =', abs(T_inv2) + 273)
