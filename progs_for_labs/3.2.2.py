import matplotlib.pyplot as plt
import numpy as np

v_c1 = [31.41, 31.51, 31.6, 31.7, 31.8, 31.9, 32., 32.1, 32.2, 32.3, 32.4, 32.5, 32.6, 32.7, 32.8, 32.9, 33.]
U_c1 = [3.21, 3.49, 3.79, 4.14, 4.51, 4.85, 5.19, 5.35, 5.38, 5.29, 5.09, 4.84, 4.56, 4.23, 3.96, 3.7, 3.46]
v_c5 = [18.7, 18.8, 18.9, 19., 19.1, 19.2, 19.3, 19.4, 19.5, 19.6, 19.7, 19.8, 19.9, 20., 20.1, 20.2, 20.3]
U_c5 = [2.14, 2.33, 2.56, 2.8, 3.04, 3.26, 3.43, 3.5, 3.49, 3.35, 3.18, 2.97, 2.76, 2.55, 2.36, 2.18, 2.02]
# plt.scatter(v_c1, U_c1, s=np.array([1.5]) * len(v_c1), label='C1')
# plt.scatter(v_c5, U_c5, s=np.array([1.5]) * len(v_c5), label='C5')
# plt.grid()
# plt.legend()
# plt.xlabel('$U_c, B$')
# plt.ylabel('$f, кГц$')
# # plt.savefig('1_1.png')
# plt.show()

x_c1 = [i / 32.21 for i in v_c1]
# y_c1 = [i / 5.376 for i in U_c1]
x_c5 = [i / 19.478 for i in v_c5]
# y_c5 = [i / 3.494 for i in U_c5]

# plt.scatter(x_c1, y_c1, s=np.array([1.5]) * len(v_c1), label='C1')
# plt.scatter(x_c5, y_c5, s=np.array([1.5]) * len(v_c5), label='C5')
# plt.grid()
# plt.legend()
# plt.xlabel('$x=\\frac{f}{f_{0n}}$')
# plt.ylabel('$y=\\frac{U_c}{U_0}$')
# plt.savefig('2.png')
# plt.show()


# v_c1_ = [31.41, 31.51, 31.6, 31.7, 31.8, 31.9, 32., 32.1, 32.3, 32.4, 32.5, 32.6, 32.7, 32.8, 32.9, 33.]
# f_c1 = [.47, .54, .57, .7, .76, .86, .99, 1.12, 1.38, 1.46, 1.56, 1.63, 1.73, 1.8, 1.84, 1.91]
# v_c5_ = [18.7, 18.8, 18.9, 19., 19.1, 19.2, 19.3, 19.4, 19.6, 19.7, 19.8, 19.9, 20., 20.1, 20.2, 20.3]
# f_c5 = [.47, .53, .6, .67, .8, .9, 1., 1.16, 1.41, 1.52, 1.64, 1.69, 1.8, 1.87, 1.92, 1.97]
#
# x_c1_ = [i / 32.21 for i in v_c1_]
# y_c1_ = [i / np.pi for i in f_c1]
# x_c5_ = [i / 19.478 for i in v_c5_]
# y_c5_ = [i / np.pi for i in f_c5]
# plt.scatter(x_c1_, y_c1_, s=np.array([1.5]) * len(v_c1), label='C1')
# plt.scatter(x_c5_, y_c5_, s=np.array([1.5]) * len(v_c5), label='C5')
# plt.grid()
# plt.legend()
# plt.xlabel('$x=\\frac{f}{f_{0n}}$')
# plt.ylabel('$y=\\frac{\\phi_c}{\\pi}$')
# plt.savefig('3.png')
# plt.show()

v_0n1 = [32.21, 27.826, 23.282, 21.181, 19.478, 15.87]
Rl1 = [4.23, 4.12, 3.9, 3.8, 3.72, 3.53]
v_0n2 = [32.39, 27.99, 23.39, 21.29, 19.59, 15.95]
Rl2 = [4.14, 3.93, 3.71, 3.63, 3.58, 3.39]
v_0n3 = [32.17, 27.79, 23.23, 21.12, 19.43, 15.82]
Rl3 = [4.39, 4.11, 3.93, 3.81, 3.84, 3.62]
plt.plot([15, 32.5], [3.88, 3.88], color='black')
plt.plot([15, 32.5], [3.73, 3.73], color='red')
plt.plot([15, 32.5], [3.95, 3.95], color='blue')
plt.scatter(v_0n1, Rl1, s=np.array([1.5]) * len(v_0n1), color='black')
plt.plot(v_0n1, np.polyval(np.polyfit(v_0n1, Rl1, 1), v_0n1), label='$\\varepsilon=213мВ$', color='black')
plt.scatter(v_0n2, Rl2, s=np.array([1.5]) * len(v_0n2), color='red')
plt.plot(v_0n2, np.polyval(np.polyfit(v_0n2, Rl2, 1), v_0n2), label='$\\varepsilon=89мВ$', color='red')
plt.scatter(v_0n3, Rl3, s=np.array([1.5]) * len(v_0n3), color='blue')
plt.plot(v_0n3, np.polyval(np.polyfit(v_0n3, Rl3, 1), v_0n3), label='$\\varepsilon=302мВ$', color='blue')
plt.grid()
plt.legend()
plt.xlabel('$\\nu_{0n}, кГц$')
plt.ylabel('$R_L, Ом$')
plt.savefig('4.png')
plt.show()