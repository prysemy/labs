import matplotlib.pyplot as plt
import numpy as np

I1 = [0.704, 56.26, 71.45, 79.25, 89.72, 106.37, 120.57, 142.94, 157.36]  # мА
k1x = 20  # мВ
k1y = 50  # мВ
K1x = np.array([0, 1.6, 2.5, 3, 2+6.5/5, 3+4.5/5, 4.4, 5, 4+6.5/5]) * k1x
K1y = np.array([0, 0.2, 3.5/5, 6/5, 2, 2+8.5/5, 5, 6.2, 7]) * k1y
print('Для Fe-Ni:\nKx ->', K1x, '\nKy ->', K1y)
print('Средние Kx/y -> Kx:', round(K1x.mean(), 1), ' Ky:', round(K1y.mean(), 1), 'В')

I2 = [0.686, 25.43, 29.5, 35.2, 47.48, 58.65, 74.29, 93.16, 115.16]
k2x = 20  # мВ
k2y = 10  # мВ
K2x = np.array([0, 0.5, 0.6, .8, 1, 1.1, 1.2, 1.4, 1.5]) * k2x
K2y = np.array([0, 0.6, 3.5/5, 1.2, 8.5/5, 2.2, 2.6, 2.8, 3.1]) * k2y
print('Для Ni-Zn:\nKx ->', K2x, '\nKy ->', K2y)
print('Средние Kx/y -> Kx:', round(K2x.mean(), 1), ' Ky:', round(K2y.mean(), 1), 'мВ')

I3 = [.735, 60.05, 79.88, 100.21, 121.35, 144.97, 174.91, 221.14, 285.12, 355.55]
k3x = 50  # мВ
k3y = 50  # мВ
K3x = np.array([0, 0.5, .8, 1, 1.1, 6.5/5, 1.4, 1.6, 1.8, 9.5/5]) * k3x
K3y = np.array([0, .6, 1, 1.4, 1.8, 2, 1+6.5/5, 2.6, 3.9, 4.1]) * k3y
print('Для Fe-Si:\nKx ->', K3x, '\nKy ->', K3y)
print('Средние Kx/y -> Kx:', round(K3x.mean(), 1), ' Ky:', round(K3y.mean(), 1), 'мВ')

R0 = 0.3
Ru = 20000
Cu = 20 * 10 ** (-6)

N01 = 35
Nu1 = 220
S1 = 3.8 / 10 ** 4
R2p1 = 24 / 100
N02 = 40
Nu2 = 400
S2 = 3 / 10 ** 4
R2p2 = 25 / 100
N03 = 40
Nu3 = 400
S3 = 1.2 / 10 ** 4
R2p3 = 10 / 100

Kh1 = N01 / R2p1 / R0
Kh2 = N02 / R2p2 / R0
Kh3 = N03 / R2p3 / R0
H1 = Kh1 * K1x / 10 ** 3
H2 = Kh2 * K2x / 10 ** 3
H3 = Kh3 * K3x / 10 ** 3

print('H ->', round(H1.mean(), 1), H2.mean(), H3.mean())

Kb1 = Ru * Cu / S1 / Nu1
Kb2 = Ru * Cu / S2 / Nu2
Kb3 = Ru * Cu / S3 / Nu3
B1 = Kb1 * K1y / 10 ** 3
B2 = Kb2 * K2y / 10 ** 3
B3 = Kb3 * K3y / 10 ** 3
print('B ->', B1.mean(), B2.mean(), B3.mean())

Bs1 = Kb1 * 3.8 * k1y / 10 ** 3
Bs2 = Kb2 * 3.8 * k2y / 10 ** 3
Bs3 = Kb3 * 3 * k3y / 10 ** 3


Hmax1 = Kh1 * 4 * k1x / 10 ** 3
Hmax2 = Kh2 * 4 * k2x / 10 ** 3
Hmax3 = Kh3 * 4 * k3x / 10 ** 3

print('Hmax ->', Hmax1, Hmax2, Hmax3)
print('Bs ->', Bs1, Bs2, Bs3)

Hc1 = Kh1 * 2 * K1x.max() / 10 ** 3
Hc2 = Kh2 * 2 * K2x.max() / 10 ** 3
Hc3 = Kh3 * 2 * K3x.max() / 10 ** 3

print('Hc ->', Hc1, Hc2, Hc3)

Br1 = Kb1 * 2 * K1y.max() / 10 ** 3
Br2 = Kb2 * 2 * K2y.max() / 10 ** 3
Br3 = Kb3 * 2 * K3y.max() / 10 ** 3
print('Br ->', Br1, Br2, Br3)

plt.scatter(H1, B1)
plt.plot(H1, B1, label='Fe-Ni')
plt.legend()
plt.grid()
plt.xlabel('H, А/м')
plt.ylabel('B, Тл')
plt.savefig('1.png')
plt.show()

plt.scatter(H2, B2)
plt.plot(H2, B2, label='Ni-Zn')
plt.legend()
plt.grid()
plt.xlabel('H, А/м')
plt.ylabel('B, Тл')
plt.savefig('2.png')
plt.show()

plt.scatter(H3, B3)
plt.plot(H3, B3, label='Fe-Si')
plt.legend()
plt.grid()
plt.xlabel('H, А/м')
plt.ylabel('B, Тл')
plt.savefig('3.png')
plt.show()

dBdH1 = [(B1[i] - B1[i - 1]) / (H1[i] - H1[i - 1]) for i in range(1, len(B1))]
dBdH2 = [(B2[i] - B2[i - 1]) / (H2[i] - H2[i - 1]) for i in range(1, len(B2))]
dBdH3 = [(B3[i] - B3[i - 1]) / (H3[i] - H3[i - 1]) for i in range(1, len(B3))]
print('Начальные dB/dH:', dBdH1[0], dBdH2[0], dBdH3[0])
print('Максимальные dB/dH:', max(dBdH1), max(dBdH2), max(dBdH3))