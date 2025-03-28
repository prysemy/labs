import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def linear_model(x, a, b):
    return a * x + b


m = 1 / np.arange(1, 7, 1)
z = 692 - np.array([671, 681, 685, 687, 689, 690])

popt, pcov = curve_fit(linear_model, m, z, sigma=np.array([1] * 6))
a = popt[0]
b = popt[1]
a_err = pcov[0][0]
b_err = pcov[1][1]
y_fit = m * a + b
sigma = np.array([1] * 6)
chi_squared = np.sum(((z - y_fit) / sigma) ** 2)
ndof = len(m) - len(popt)
x_fit = np.array([0, 1.1])
y_fit = linear_model(x_fit, *popt)

fig, ax = plt.subplots()
ax.errorbar(m, z, np.array([1] * 6), fmt='o', elinewidth=1, capsize=3, capthick=0.5, markersize=2.5, color='black')
ax.plot(x_fit, y_fit, color='black')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.minorticks_on()
ax.grid(which="major", color='grey', linewidth=0.7, linestyle='--')
ax.grid(which="minor", color='lightgrey', linewidth=0.7, linestyle='--')
ax.legend(["k=("+str(round(a, 2))+r'$\pm$'+str(round(a_err, 2))+')мм'])
ax.set_ylabel('z, мм')
ax.set_xlabel('1/m')
plt.savefig('graph1.png')
plt.show()

print('k=', a)
print('ширина щели:', 2*(a*58/10**5)**0.5)


m = np.arange(-3, 4, 1)
xm = [-0.54, -0.42, -0.22, 0, 0.22, 0.44, 0.56]
fig, ax = plt.subplots()
coefs = np.polyfit(m, xm, 1)
k = coefs[0]
coef_error = np.sqrt(np.diag(pcov))
k_err = k*1.01167049/100
ax.errorbar(m, xm, np.array([0.02]*len(m)), fmt='o', elinewidth=1, capsize=3, capthick=0.5, markersize=2.5, color='black')
ax.plot(m, np.polyval(np.polyfit(m, xm, 1), m), color='black')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.minorticks_on()
ax.grid(which="major", color='grey', linewidth=0.7, linestyle='--')
ax.grid(which="minor", color='lightgrey', linewidth=0.7, linestyle='--')
ax.legend([r'k=0.195$\pm$0.011 мм'])
ax.set_ylabel(r'$x_m$, мм')
ax.set_xlabel('m')
plt.savefig('graph2.png')
plt.show()

print(coefs, coef_error)
