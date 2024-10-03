import matplotlib.pyplot as plt
import numpy as np

U_p = [35.21, 34.48, 32.34, 26.78, 24.21, 22.33, 20.78, 19.89, 19.42, 18.99, 19.6, 20., 21.15, 22.77, 24.31, 26.45,
       33.68, 34.94]
I_p = [0.51, .74, 1.09, 1.56, 2.09, 2.66, 3.14, 3.87, 4.27, 4.85, 4.14, 3.63, 3., 2.51, 2.05, 1.6, .93, .58]

U_5 = [24.99, 22.06, 19.06, 16., 13.03, 10.11, 8.04, 5.92, 4.07, 2.03, .48, -.55, -2.09, -4.08, -6.16, -8.18, -10.15,
       -13.03, -16.21, -19.07, -22.16, -25.09]
I_5 = [108.42, 106.32, 103.5, 98.73, 91.14, 79.88, 69.15, 55.56, 41.58, 23.44, 8.17, -21.43, -36.2, -53.31, -68.99,
       -81.72, -92.12, -103.86, -112.76, -118.07, -121.66, -124.64]

U_3 = [24.82, 22.1, 19.08, 16.01, 13.06, 9.98, 8.06, 6.05, 3.99, 2.09, 0.46, -0.47, -2.07, -4.08, -6.12, -8.09, -10.04,
       -13.03, -16.08, -19.18, -22.1, -25.01]
I_3 = [64.69, 63.01, 61.08, 58.71, 55.04, 48.4, 42.23, 33.99, 23.38, 12.03, 1.38, -9.8, -20.21, -32.16, -42.4, -50.47,
       -56.66, -63.23, -67.24, -69.82, -71.78, -73.69]

U_1_5 = [25.07, 22.04, 19.11, 16.13, 13.08, 10.08, 8.02, 6.08, 4.09, 2.12, 0.58, -0.58, -2.08, -3.99, -6.1, -8.02,
         -10.01, -13.05, -16.07, -19.04, -22.09, -25.03]
I_1_5 = [32.33, 31.24, 30.2, 29.08, 27.45, 24.59, 21.55, 17.64, 12.44, 6.06, .44, -4.84, -10.3, -16.58, -22.26, -26.27,
         -29.37, -32.55, -34.42, -35.76, -37.07, -38.85]

# plt.plot(U_p[10:], I_p[10:])
plt.plot(I_p[:10], U_p[:10])
plt.scatter(I_p, U_p, s=np.array([1]) * len(U_p))
k = (U_p[2] - U_p[3]) / (I_p[2] - I_p[3])
b = U_p[2] - k * I_p[2]
plt.plot([1, 2], [k + b, 2 * k + b])
plt.grid()
plt.ylabel('$U_p$, В')
plt.xlabel('$I_p$, мА')
plt.savefig('1.png')
plt.show()

print('R_{диф} =', k * 1000)

plt.plot(U_5, I_5, label='$I_p$ = 5мА', color='blue')
plt.scatter(U_5, I_5, color='blue', s=np.array([1]) * len(U_5))
plt.hlines(110, 0, 26, color='blue')
print('ионный ток для I_p = 5мА: ', 110)
k1 = (I_5[10] - I_5[11]) / (U_5[10] - U_5[11]) / 10 ** 6
print('наклон dI/dU в начале координат для I_p = 5мА: ', k1)

plt.plot(U_3, I_3, label='$I_p$ = 3мА', color='red')
plt.scatter(U_3, I_3, color='red', s=np.array([1]) * len(U_3))
plt.hlines(66, 0, 26, color='red')
print('ионный ток для I_p = 3мА: ', 66)
k2 = (I_3[10] - I_3[11]) / (U_3[10] - U_3[11]) / 10 ** 6
print('наклон dI/dU в начале координат для I_p = 3мА: ', k2)

plt.plot(U_1_5, I_1_5, label='$I_p$ = 1.5мА', color='green')
plt.scatter(U_1_5, I_1_5, color='green', s=np.array([1]) * len(U_1_5))
plt.hlines(34, 0, 26, color='green')
print('ионный ток для I_p = 1.5мА: ', 34)
k3 = (I_1_5[10] - I_1_5[11]) / (U_1_5[10] - U_1_5[11]) / 10 ** 6
print('наклон dI/dU в начале координат для I_p = 1.5мА: ', k3)

plt.grid()
plt.xlabel('U, В')
plt.ylabel('I, мкА')
plt.legend()
plt.savefig('2.png')
plt.show()

k = 1.38 * 10 ** (-23)
e = 1.6 * 10 ** (-19)
Ii = [110 / 10 ** 6, 66 / 10 ** 6, 34 / 10 ** 6]
T1 = 0.5 * e * Ii[0] / k1 / k
T2 = 0.5 * e * Ii[1] / k2 / k
T3 = 0.5 * e * Ii[2] / k3 / k
print('Температуры электронов: ', round(T1), round(T2), round(T3), 'K')

S = 3.27 / 10 ** 6
m = 22 * 1.66 * 10 ** (-27)
n1 = Ii[0] / 0.4 / e / S * (m / 2 / k / T1) ** 0.5
n2 = Ii[1] / 0.4 / e / S * (m / 2 / k / T2) ** 0.5
n3 = Ii[2] / 0.4 / e / S * (m / 2 / k / T3) ** 0.5
print('Концентрации: ', n1, n2, n3)

Te = [T1, T2, T3]
ne = [n1, n2, n3]
me = 9.1 * 10 ** (-31)

w = [(4 * 3.1415 * ne[i] * e ** 2 / me) ** 0.5 for i in range(3)]
print('w:', w)

e = 4.8 * 10 ** (-10)
r_de = [(k * Te[i] * 10 ** 7 / 4 / 3.1415 / ne[i] / 10 ** 6 / e ** 2) ** 0.5 for i in range(3)]
print('r_de', r_de)

Ti = 300
r_d = [(k * Ti / 4 / 3.1415 / ne[i] / 10 ** 6 / e ** 2) ** 0.5 for i in range(3)]
print('r_d', r_d)

Nd = [4 / 3 * 3.1415 * ne[i] * r_d[i] for i in range(3)]
print('Nd', Nd)

Ip = [5, 3, 1.5]
sigma_T = [.1 * 10 ** 4, .15 * 10 ** 4, .1 * 10 ** 4]
sigma_n = [.6 * 10 ** 16, .4 * 10 ** 16, .2 * 10 ** 16]

fig, ax = plt.subplots()
plt.plot(Ip, np.polyval(np.polyfit(Ip, Te, 1), Ip))
plt.scatter(Ip, Te, s=np.array([2]) * 3)
ax.errorbar(Ip, Te, yerr=sigma_T, fmt='.', linewidth=2, capsize=6)
plt.grid()
plt.xlabel('$I_p$, мА')
plt.ylabel('$T_e$, K')
plt.savefig('31.png')
plt.show()

fig, ax = plt.subplots()
plt.plot(Ip, np.polyval(np.polyfit(Ip, ne, 1), Ip))
plt.scatter(Ip, ne, s=np.array([2]) * 3)
ax.errorbar(Ip, ne, yerr=sigma_n, fmt='.', linewidth=2, capsize=6)
plt.grid()
plt.xlabel('$I_p$, мА')
plt.ylabel('$n_e, м^{-3}$')
plt.savefig('32.png')
plt.show()
