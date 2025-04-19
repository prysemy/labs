import matplotlib.pyplot as plt
import numpy as np

m = np.arange(1, 9, 1)
rm = np.array([28, 41, 49, 57, 64, 71, 77, 82])/10

fig, ax = plt.subplots()
fig.set_figwidth(12)
fig.set_figheight(7)
plt.plot(m, np.polyval(np.polyfit(m, rm ** 2, 1), m), linewidth=1, color='black')
ax.errorbar(m, rm ** 2, yerr=np.array([0.4] * len(m)), fmt='o', elinewidth=1, capsize=3, capthick=0.5, markersize=2.5,
            color='black')
plt.scatter(m, rm ** 2, s=np.array([8] * len(m)), color='black')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.minorticks_on()
ax.grid(which="major", color='grey', linewidth=0.7, linestyle='--')
ax.grid(which="minor", color='lightgrey', linewidth=0.7, linestyle='--')
ax.set_ylabel(r'$r_m^2, см^2$')
ax.set_xlabel('m')
plt.savefig('graph1.png')
plt.show()
