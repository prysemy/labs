import matplotlib.pyplot as plt
import numpy as np

# все в СГС
r_max = 2.2
g = 980.66
m = 0.845

Pm = (m * g * r_max ** 4 / 6) ** 0.5
sig_Pm = (0.001 ** 2 / 0.845 ** 2 + 0.25 * 0.1 ** 2 / 2.2 ** 2) ** 0.5
print('Pm =', round(Pm, 2), '+-', round(sig_Pm, 2), 'эрг/Гс')

d = .69
V = 4 / 3 * 3.1415 * d ** 3 / 8
pm = Pm / V
sig_pm = (sig_Pm ** 2 / Pm ** 2 + 3 * .01 ** 2 / d ** 2) ** 0.5
print('pm=', round(pm, 2), '+-', round(sig_pm, 2), 'Гс')

Bp = 2 * Pm / (d / 2) ** 3
sig_Bp = (sig_Pm ** 2 / Pm + 3 * .01 ** 2 / d ** 2) ** 0.5
print('Bp=', round(Bp, 2), '+-', round(sig_Bp, 2), 'Гс')

Br = 4 * 3.1415 * pm
print('Br=', round(Br, 2), '+-', round(sig_pm, 2), 'Гс')

M = 268.188
F = M * g
sig_F = (0.001 ** 2 / M ** 2 + 0.01 ** 2 / g ** 2) ** 0.5
print('F=', round(F, 2), 'дин')

F0 = F / 1.08
print('F0=', round(F0, 2), 'дин')

Pm_2 = (F0 * d ** 4 / 6) ** 0.5
sig_Pm_2 = (0.5 * 0.01 ** 2 / F0 ** 2 + 2 * 0.01 ** 2 / d ** 2) ** 0.5
print('Pm=', round(Pm_2, 2), '+-', round(sig_Pm_2, 2), 'эрг/Гс')

Bp_2 = 2 * Pm_2 / (d / 2) ** 3
sig_Bp_2 = (sig_Pm_2 ** 2 / Pm_2 + 3 * .01 ** 2 / d ** 2) ** 0.5
print('Bp=', round(Bp_2, 2), '+-', round(sig_Bp_2, 2), 'Гс')

T0 = 127.53
print('T0=', T0, '+-', '0.15', 'c')

n_1 = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
Tn_1 = [39.03, 36., 34.13, 29.75, 26.19, 23.5, 20.25, 17.03, 15.11, 10.04]
T_1 = [t / 10 for t in Tn_1]
print('T_1=', T_1)

yer = [0.3] * len(T_1)
fig, ax = plt.subplots()
plt.scatter(n_1, T_1, s=np.array([4]) * len(n_1))
plt.plot(n_1, np.polyval(np.polyfit(n_1, T_1, 1), n_1))
ax.errorbar(n_1, T_1, yerr=yer, fmt='.', linewidth=2, capsize=5)
plt.xlabel('n')
plt.ylabel('T, c')
plt.grid()
plt.savefig('1.png')
plt.show()

k = np.polyfit(n_1, T_1, 1)[0]
print('угловой коэффициент k=', k, 'c')

Bh = 3.1415 ** 2 * m * d ** 2 / 3 / k ** 2 / Pm_2
sig_Bh = (0.001 ** 2 / m ** 2 + .5 * 0.01 ** 2 / d ** 2 + 0.5 * 0.02 ** 2 / k ** 2 + sig_Pm_2 ** 2 / Pm_2 ** 2) ** 0.5
print('Bh=', round(Bh, 3), '+-', round(sig_Bh, 3), 'Гс')

n_2 = [12, 10, 8, 6, 4]
m_p = [.173, .197, .221, .263, .352]
l = [5 * d, 4 * d, 3 * d, 2 * d, d]
M = [m_p[i] * g * l[i] for i in range(len(l))]
print('M=', M, 'дин*см')

plt.scatter(n_2, M)
plt.plot(n_2, np.polyval(np.polyfit(n_2, M, 1), n_2))
plt.xlabel('n')
plt.ylabel('M, дин*cм')
plt.grid()
plt.savefig('2.png')
plt.show()

A = np.polyfit(n_2, M, 1)[0]
print('A=', A, 'дин*см')

Bv = A / Pm_2
sig_Bh = (0.02 ** 2 / A ** 2 + sig_Pm_2 ** 2 / Pm_2 ** 2) ** 0.5
print('Bv=', round(Bv, 3), '+-', round(sig_Bh, 3), 'Гс')

