import matplotlib.pyplot as plt
import numpy as np
import math

P1 = [1.1, 1.2, 1.4, 1.6, 1.7, 1.9, 2, 2.2, 2.4, 2.5, 2.7, 2.8, 3, 3.2, 3.4, 3.5, 3.7, 3.9, 4, 4.2, 4.3, 4.5, 4.6, 4.8,
      5, 5.2, 5.3, 5.5, 5.7, 5.8, 6, 6.2, 6.4, 6.5, 6.7, 6.9, 7, 7.2, 7.4]
P1_ = [1.1, 1.2, 1.3, 1.5, 1.7, 1.9, 2, 2.2, 2.4, 2.5, 2.7, 2.9, 3, 3.2, 3.4, 3.5, 3.7, 3.9, 4, 4.2, 4.4, 4.6, 4.7, 5,
       5.2, 5.4, 5.6, 5.7, 5.9, 6.1, 6.3, 6.4, 6.6, 6.8, 7, 7.1, 7.3, 7.5, 7.4]
P2 = [7.4, 7.2, 6.5, 5.1, 3.6, 2.9, 2.2, 1.9, 1.8, 1.6, 1.5, 1.4, 1.3, 1.3, 1.3, 1.3, 1.2, 1.2]
P2_ = [7.4, 6.2, 4.7, 3.3, 2.7, 2.5, 2, 1.8, 1.6, 1.5, 1.4, 1.4, 1.4, 1.3, 1.3, 1.3, 1.3, 1.3]

t1 = np.arange(0, 78, 2)
t2 = np.arange(0, 36, 2)

plt.scatter(t1, P1, color='black')
plt.plot(t1, np.polyval(np.polyfit(t1, P1, 1), t1), color='black')
plt.grid()
plt.xlabel('t, c')
plt.ylabel('P, мм.рт.ст * 10^(-4)')
plt.savefig('11.png')
# plt.show()
plt.cla()
plt.clf()

plt.scatter(t1, P1_, color='black')
plt.plot(t1, np.polyval(np.polyfit(t1, P1_, 1), t1), color='black')
plt.xlabel('t, c')
plt.ylabel('P, мм.рт.ст * 10^(-4)')
plt.grid()
plt.savefig('21.png')
# plt.show()
plt.cla()
plt.clf()

plt.scatter(t2, P2, color='black')
plt.xlabel('t, c')
plt.ylabel('P, мм.рт.ст * 10^(-4)')
plt.grid()
plt.savefig('12.png')
# plt.show()
plt.cla()
plt.clf()

plt.scatter(t2, P2_, color='black')
plt.xlabel('t, c')
plt.ylabel('P, мм.рт.ст * 10^(-4)')
plt.grid()
plt.savefig('22.png')
# plt.show()
plt.cla()
plt.clf()

# ln(P/P0)=-W/V t
P0 = 98.58 * 1000
# апроксимация для нахождения W
plt.scatter(t2[2:8], np.log([p / P0 for p in P2[2:8]]))
plt.plot(t2[2:8], np.polyval(np.polyfit(t2[2:8], np.log([p / P0 for p in P2[2:8]]), 1), t2[2:8]))
# plt.show()
Vfv = 2093.8 * 10 ** (-3)
k = np.polyfit(t2[2:8], np.log([p * 10 ** (-4) / P0 for p in P2[2:8]]), 1)[0]
W = -Vfv * k
# print(k)
# print(W)

a = np.polyfit(t1, [p * 10 ** (-4) for p in P1], 1)[0]
Vvv = 1241.2 * 10 ** (-3)
Ppr = 10 ** (-4)
Qn = Ppr * W - a * Vvv
# print(a)
# print(Qn)

r = 0.4 * 10 ** (-3)
L = 10.8 / 100
T = 299
mu = 29 * 10 ** (-3)
Ctr = 4 / 3 * r ** 3 / L * (2 * 3.1415 * 8.31 * T / mu) ** 0.5
print(Ctr * 1000)

Pfv = 4.5 * 10 ** (-3)
Pust = 2.4 * 10 ** (-4)
Wt = Ctr * (Pfv - Pust) / Ppr
print(Wt)
