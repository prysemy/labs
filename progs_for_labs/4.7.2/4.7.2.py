import matplotlib.pyplot as plt
import numpy as np

m = np.arange(1, 9, 1)
rm = np.array([2.7, 3.8, 4.7, 5.5, 6.0, 6.6, 7.2, 7.6])

fig, ax = plt.subplots()
fig.set_figwidth(12)
fig.set_figheight(7)
k = np.polyfit(m, rm ** 2, 1)[0]
print(k)
er = np.array([.54, .76, .94, 1.1, 1.2, 1.32, 1.44, 1.52])
plt.plot(m, np.polyval(np.polyfit(m, rm ** 2, 1), m), linewidth=1, color='black',
         label=r'$k=(7.27\pm 0.39) см^2$')
ax.errorbar(m, rm ** 2, yerr=er, fmt='o', elinewidth=1, capsize=3, capthick=0.5, markersize=2.5,
            color='black')
plt.scatter(m, rm ** 2, s=np.array([8] * len(m)), color='black')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.minorticks_on()
ax.grid(which="major", color='grey', linewidth=0.7, linestyle='--')
ax.grid(which="minor", color='lightgrey', linewidth=0.7, linestyle='--')
ax.set_ylabel(r'$r_m^2, см^2$')
ax.set_xlabel('m')
plt.legend()
plt.savefig('graph1.png')
plt.show()
