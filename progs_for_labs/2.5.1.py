import matplotlib.pyplot as plt
import numpy as np

d = 10 ** (-3)

T = np.arange(296, 331 + 5, 5)
dP = 165
P = [p - dP for p in [478.2, 473.7, 469.6, 465.6, 461, 457.1, 454.5, 446.8]]
sigma = [round(p * d / 4 * 1000, 1) for p in P]
# print(sigma)
plt.scatter(T, sigma, s=np.array([1.3]) * len(T), color='black')
plt.plot(T, np.polyval(np.polyfit(T, sigma, 1), T), color='black')
plt.grid()
plt.xlabel('T, K')
plt.ylabel('sigma, мН/м')
plt.savefig('1.png')
plt.show()
k = np.polyfit(T, sigma, 1)[0]
print(k)
q = [-T[i] * k for i in range(len(T))]
# print([round(q[i], 1) for i in range(len(q))])
U_F = [sigma[i] + q[i] for i in range(len(T))]
# print(U_F)
plt.scatter(T, q, s=np.array([1.3]) * len(T), color='black')
plt.plot(T, np.polyval(np.polyfit(T, q, 1), T))
plt.grid()
plt.xlabel('T, K')
plt.ylabel('q, мН/м')
plt.savefig('2.png')
plt.show()
plt.scatter(T, U_F, s=np.array([1.3]) * len(T), color='black')
plt.plot(T, np.polyval(np.polyfit(T, U_F, 1), T))
plt.grid()
plt.xlabel('T, K')
plt.ylabel('U/F, мН/м')
plt.savefig('3.png')
plt.show()

s_k = 1 / 5 ** 0.5 * (
        (sum(s ** 2 for s in sigma) - sum(sigma) ** 2) / (sum(t ** 2 for t in T) - sum(T) ** 2) - k ** 2) ** 0.5
print(s_k)
