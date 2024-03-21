import math

import matplotlib.pyplot as plt
import numpy as np

T_hot = [t for t in range(23 + 273, 41 + 273)]
T_cold = [t for t in range(39 + 273, 22 + 273, -1)]
T = T_hot + T_cold
h_hot = [48.29, 52.95, 54.42, 59.37, 61, 65.14, 68.79, 72.38, 76.19, 80.75, 85.28, 89.95, 95.28, 100.13, 105.01, 111.13,
         117.22, 123.94]
h_cold = [123.89, 118.63, 113.03, 107.98, 101.24, 96.59, 91.19, 86.74, 82, 77.94, 74.3, 69.16, 65.88, 62.65, 59.88,
          56.54, 53.26]
h = h_hot + h_cold
P_hot = [136 * h_hot[i] for i in range(len(h_hot))]
P_cold = [136 * h_cold[i] for i in range(len(h_cold))]
P = P_hot + P_cold
plt.scatter(T_hot, P_hot, s=np.array([1.2]) * len(h_hot), color='gray', label='heat')
plt.scatter(T_cold, P_cold, s=np.array([1.2]) * len(h_cold), color='gray', label='cool')
plt.xlabel('T, K')
plt.ylabel('P, Па')
plt.legend()
plt.grid()
plt.savefig('1.png')
plt.show()

lnP_hot = [math.log(P_hot[i], math.e) for i in range(len(P_hot))]
lnP_cold = [math.log(P_cold[i], math.e) for i in range(len(P_cold))]
T1_hot = [1 / T_hot[i] * 1000 for i in range(len(T_hot))]
T1_cold = [1 / T_cold[i] * 1000 for i in range(len(T_cold))]
plt.plot(T1_hot, np.polyval(np.polyfit(T1_hot, lnP_hot, 1), T1_hot), color='gray', label='heat')
plt.scatter(T1_hot, lnP_hot, s=np.array([1.2]) * len(T1_hot), color='gray')
plt.plot(T1_cold, np.polyval(np.polyfit(T1_cold, lnP_cold, 1), T1_cold), color='gray', label='cool')
plt.scatter(T1_cold, lnP_cold, s=np.array([1.2]) * len(T1_cold), color='gray')
plt.xlabel('1/T * 1000')
plt.ylabel('ln P')
plt.legend()
plt.grid()
plt.savefig('2.png')
plt.show()

# вычисление по первой кривой
k_hot = [(P_hot[len(P_hot) - 1] - P_hot[0]) / (T_hot[len(T_hot) - 1] - T_hot[0])] + [
    (P_hot[i] - P_hot[i - 1]) / (T_hot[i] - T_hot[i - 1]) for i in range(1, len(P_hot))]
k_cold = [(P_cold[len(P_cold) - 1] - P_cold[0]) / (T_cold[len(T_cold) - 1] - T_cold[0])] + [
    (P_cold[i] - P_cold[i - 1]) / (T_cold[i] - T_cold[i - 1]) for i in range(1, len(P_cold))]
R = 8.31
L_hot = [round(R * T_hot[i] ** 2 / P_hot[i] * k_hot[i] / 1000, 1) for i in range(len(P_hot))]
L_cold = [round(R * T_cold[i] ** 2 / P_cold[i] * k_cold[i] / 1000, 1) for i in range(len(P_cold))]
L = L_hot + L_cold
L_s = sum(L) / len(L)
plt.scatter(T_hot, L_hot, color='gray', s=np.array([1.2]) * len(T_hot))
plt.scatter(T_cold, L_cold, color='gray', s=np.array([1.2]) * len(T_cold))
plt.plot(T_hot, L_hot, color='gray')
plt.plot(T_cold, L_cold, color='gray')
plt.axhline(y=L_s, color='black', linestyle='-', label='L_s=' + str(round(L_s, 2)) + 'кДж/кг')
plt.grid()
plt.legend()
plt.xlabel('T, K')
plt.ylabel('L, кДж/моль')
plt.savefig('3.png')
plt.show()

# вычисление по прямой
k_new_hot = np.polyfit(T1_hot, lnP_hot, 1)[0]
k_new_cold = -np.polyfit(T1_cold, lnP_cold, 1)[0]
L_new_hot = -R * k_new_hot
L_new_cold = -R * k_new_cold
# print(k_new_hot)
# print(round(L_new_hot, 2))
# print(round(L_new_cold, 2))
