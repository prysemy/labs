import math

import matplotlib.pyplot as plt
import numpy as np

d = [5.25, 3., 3.9]
l3 = [11, 30, 40, 50]
l2 = [6, 20, 20, 30]
l1 = [10.5, 30, 40, 50]
T0 = 23.2 + 273
P0 = 99.97 * 10 ** 3
mu = 29 * 10 ** (-3)
R = 8.31
ro = P0 * mu / R / T0
Recr = 10 ** 3
n__ = 2 * 10 ** (-5)
Qcr = [round(Recr * math.pi * d[i] / 2 * n__ / ro, 3) for i in range(3)]
# print(Qcr)
dPcr1 = [round(8 * n__ * l1[i] / 100 * Qcr[0] * 10 ** (-3) / math.pi / (d[0] * 10 ** (-3) / 2) ** 4, 2) for i in
         range(len(l1))]
dPcr2 = [round(8 * n__ * l2[i] / 100 * Qcr[1] * 10 ** (-3) / math.pi / (d[1] * 10 ** (-3) / 2) ** 4, 2) for i in
         range(len(l2))]
dPcr3 = [round(8 * n__ * l3[i] / 100 * Qcr[2] * 10 ** (-3) / math.pi / (d[2] * 10 ** (-3) / 2) ** 4, 2) for i in
         range(len(l3))]
dPcr1_del = [round(dPcr1[i] / 0.2 / 9.80665) for i in range(len(dPcr1))]
dPcr2_del = [round(dPcr2[i] / 0.2 / 9.80665) for i in range(len(dPcr2))]
dPcr3_del = [round(dPcr3[i] / 0.2 / 9.80665) for i in range(len(dPcr3))]
# print(dPcr1_del, dPcr2_del, dPcr3_del)
l_ust = [0.2 * d[i] / 2 * Recr for i in range(3)]
# print(l_ust)

Pd3l50 = [p * 0.2 * 9.80665 for p in [7, 10, 14, 20, 22, 30, 35, 40, 50, 60, 70, 80, 90, 100]]
Vd3l50 = [0.501, 0.852, 0.526, 1.033, 1.15, 1.01, 1.11, 1.001, 1.003, 1.008, 1.005, .996, 1.012, 1]
td3l50 = [49.45, 60, 26.98, 40.57, 39.35, 26.26, 24.97, 19.71, 16.11, 13.69, 11.85, 10.86, 10.62, 10.04]
Qd3l50 = [Vd3l50[i] / td3l50[i] for i in range(len(Vd3l50))]
k3 = np.polyfit(Pd3l50[:11], Qd3l50[:11], 1)[0]
plt.scatter(Pd3l50, Qd3l50)
plt.plot(Pd3l50[:11], np.polyval(np.polyfit(Pd3l50[:11], Qd3l50[:11], 1), Pd3l50[:11]))
plt.ylabel('Q, л/с')
plt.xlabel('dP, Па')
plt.text(25, 0.08, "d3=3.90 мм")
plt.axvline(x=74 * 0.2 * 9.80665, ymin=0, ymax=1, linestyle="-.")
plt.grid()
# plt.show()

Pd1l50 = [p * 0.2 * 9.80665 for p in [11, 23, 28, 6, 14, 26, 32, 44, 59, 64, 79, 86, 104, 120]]
Vd1l50 = [0.641, 1.068, 1.083, 0.516, 0.64, 0.997, 1.265, 1.022, 0.997, 1.038, 1.008, 2.012, 2.07, 2.407]
td1l50 = [13.10, 10.94, 9.83, 18.22, 11.11, 9.25, 9.85, 7.29, 6.45, 6.50, 5.67, 10.86, 10.02, 10.82]
Qd1l50 = [Vd1l50[i] / td1l50[i] for i in range(len(Vd1l50))]
k1 = np.polyfit(Pd1l50[:7], Qd1l50[:7], 1)[0]
plt.scatter(Pd1l50, Qd1l50)
plt.plot(Pd1l50[:7], np.polyval(np.polyfit(Pd1l50[:7], Qd1l50[:7], 1), Pd1l50[:7]))
plt.ylabel('Q, л/с')
plt.xlabel('dP, Па')
plt.text(70, 0.2, "d1=5.25 мм")
plt.axvline(x=33 * 0.2 * 9.80665, ymin=0, ymax=1, linestyle="-.")
plt.grid()
# plt.show()

Pd2l20 = [p * 0.2 * 9.80665 for p in [10, 23, 45, 40, 52, 58, 72, 78, 87, 110, 124, 137, 146, 173]]
Vd2l20 = [0.517, 1.012, 1.028, 1.045, 1.167, 1.057, 1.067, 1.075, 1.504, 1.136, 1.104, 1.120, 1.286, 1.1004]
td2l20 = [16.47, 15.87, 10.57, 11.19, 9.81, 9.08, 7.76, 7.62, 9.82, 6.53, 5.99, 5.74, 6.28, 4.43]
Qd2l20 = [Vd2l20[i] / td2l20[i] for i in range(len(Vd2l20))]
k2 = np.polyfit(Pd2l20[:6], Qd2l20[:6], 1)[0]
plt.scatter(Pd2l20, Qd2l20)
plt.plot(Pd2l20[:6], np.polyval(np.polyfit(Pd2l20[:6], Qd2l20[:6], 1), Pd2l20[:6]))
plt.ylabel('Q, л/с')
plt.xlabel('dP, Па')
plt.text(40, 0.2, "d2=3.00 мм")
plt.axvline(x=60 * 0.2 * 9.80665, ymin=0, ymax=1, linestyle="-.")
plt.grid()
# plt.show()

ld2 = [6, 26, 46]
Pld2 = [p * 0.2 * 9.80665 for p in [20, 49, 70]]

ld3 = [11, 41, 81]
Pld3 = [p * 0.2 * 9.80665 for p in [18, 36, 60]]

ld1 = [10.5, 40.5, 80.5]
Pld1 = [p * 0.2 * 9.80665 for p in [8, 16, 26]]

n_1 = math.pi * (d[0] / 2000) ** 4 / 8 / (50 / 100) / (k1 / 1000)
# print(n_1)
n_2 = math.pi * (d[1] / 2000) ** 4 / 8 / (11.4 / 100) / (k2 / 1000)
# print(n_2)
n_3 = math.pi * (d[2] / 2000) ** 4 / 8 / (50 / 100) / (k3 / 1000)
# print(n_3)

u1 = Qcr[0] / 1000 / (math.pi * (d[0] / 2000) ** 2)
Re1 = ro * u1 * (d[0] / 2000) / n_1
# print(Re1)
u2 = Qcr[1] / 1000 / (math.pi * (d[1] / 2000) ** 2)
Re2 = ro * u2 * (d[1] / 2000) / n_2
# print(Re2)
u3 = Qcr[2] / 1000 / (math.pi * (d[2] / 2000) ** 2)
Re3 = ro * u3 * (d[2] / 2000) / n_3
# print(Re3)

plt.cla()
plt.clf()
plt.scatter(ld1, Pld1, color='red')
plt.plot(ld1, np.polyval(np.polyfit(ld1, Pld1, 1), ld1), color='red', label='d1=5.25 мм')
plt.scatter(ld2, Pld2, color='green')
plt.plot(ld2, np.polyval(np.polyfit(ld2, Pld2, 1), ld2), color='green', label='d2=3.00 мм')
plt.scatter(ld3, Pld3, color='black')
plt.plot(ld3, np.polyval(np.polyfit(ld3, Pld3, 1), ld3), color='black', label='d1=3.90 мм')
plt.plot([30, 30], [80, 120], linestyle='-.', color='green')
plt.plot([39, 39], [50, 80], linestyle='-.', color='black')
plt.plot([52.5, 52.5], [30, 50], linestyle='-.', color='red')
plt.legend()
plt.grid()
plt.xlabel('l, см')
plt.ylabel('P, Па')
# plt.savefig("1.png")
# plt.show()
plt.cla()
plt.clf()

r = [_ / 2000 for _ in [5.85, 5.2, 3, 4.1]]
Q = [0.16, 0.11, 0.012, 0.041]
lnr = [math.log(ri, math.e) for ri in r]
lnq = [math.log(qi / 1000, math.e) for qi in Q]
plt.scatter(lnr, lnq)
plt.plot(lnr, np.polyval(np.polyfit(lnr, lnq, 1), lnr))
plt.grid()
plt.xlabel('lnR')
plt.ylabel('lnQ')
# plt.savefig('2.png')
# plt.show()
plt.cla()
plt.clf()

b = np.polyfit(lnr, lnq, 1)[0]
# print(b)

plt.scatter(Pd1l50, Qd1l50)
plt.plot(Pd1l50[6:], np.polyval(np.polyfit(Pd1l50[6:], Qd1l50[6:], 1), Pd1l50[6:]))
plt.ylabel('Q, л/с')
plt.xlabel('dP, Па')
plt.text(70, 0.2, "d1=5.25 мм")
plt.axvline(x=33 * 0.2 * 9.80665, ymin=0, ymax=1, linestyle="-.")
plt.grid()
# plt.savefig('1.png')
# plt.show()

plt.scatter(Pd2l20, Qd2l20)
plt.plot(Pd2l20[5:], np.polyval(np.polyfit(Pd2l20[5:], Qd2l20[5:], 1), Pd2l20[5:]))
plt.ylabel('Q, л/с')
plt.xlabel('dP, Па')
plt.text(40, 0.2, "d2=3.00 мм")
plt.axvline(x=60 * 0.2 * 9.80665, ymin=0, ymax=1, linestyle="-.")
plt.grid()
# plt.savefig('2.png')
# plt.show()

plt.scatter(Pd3l50, Qd3l50)
plt.plot(Pd3l50[10:], np.polyval(np.polyfit(Pd3l50[10:], Qd3l50[10:], 1), Pd3l50[10:]))
plt.ylabel('Q, л/с')
plt.xlabel('dP, Па')
plt.text(25, 0.08, "d3=3.90 мм")
plt.axvline(x=74 * 0.2 * 9.80665, ymin=0, ymax=1, linestyle="-.")
plt.grid()
# plt.savefig('3.png')
# plt.show()
plt.cla()
plt.clf()

kt1 = np.polyfit(Pd1l50[6:], Qd1l50[6:], 1)[0]
n_t1 = math.pi * (d[0] / 2000) ** 4 / 8 / (50 / 100) / (kt1 / 1000)
kt2 = np.polyfit(Pd2l20[5:], Qd2l20[5:], 1)[0]
n_t2 = math.pi * (d[0] / 2000) ** 4 / 8 / (50 / 100) / (kt2 / 1000)
kt3 = np.polyfit(Pd3l50[10:], Qd3l50[10:], 1)[0]
n_t3 = math.pi * (d[0] / 2000) ** 4 / 8 / (50 / 100) / (kt3 / 1000)
# print(n_t1, n_t2, n_t3)

ut1 = [i / 1000 / (math.pi * (d[0] / 2000) ** 2) for i in Qd1l50]
Ret1 = [ro * i * (d[0] / 2000) / n_t1 for i in ut1]
ut2 = [i / 1000 / (math.pi * (d[1] / 2000) ** 2) for i in Qd2l20]
Ret2 = [ro * i * (d[1] / 2000) / n_t2 for i in ut2]
ut3 = [i / 1000 / (math.pi * (d[2] / 2000) ** 2) for i in Qd3l50]
Ret3 = [ro * i * (d[2] / 2000) / n_t3 for i in ut3]

psi1 = [(d[0] / 2000) / 0.5 * Pd1l50[i] / ro / ut1[i] ** 2 for i in range(len(ut1))]
psi2 = [(d[0] / 2000) / 0.5 * Pd2l20[i] / ro / ut2[i] ** 2 for i in range(len(ut2))]
psi3 = [(d[0] / 2000) / 0.5 * Pd3l50[i] / ro / ut3[i] ** 2 for i in range(len(ut3))]

plt.scatter(Ret1, psi1, label='d1=5.25 мм')
plt.scatter(Ret2, psi2, label='d2=3.00 мм')
plt.scatter(Ret3, psi3, label='d3=3.90 мм')
plt.grid()
plt.xlabel('Re')
plt.ylabel('psi')
plt.legend()
plt.savefig('1.png')
plt.show()