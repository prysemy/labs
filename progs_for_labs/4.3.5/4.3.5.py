import matplotlib.pyplot as plt
import numpy as np

m = np.arange(1, 10, 1)
rm = np.array([0.831, 2.697, 4.796, 6.528, 8.526, 10.79, 13.32, 16.12, 17.61])

fig, ax = plt.subplots()
fig.set_figwidth(12)
fig.set_figheight(7)
k = np.polyfit(m, rm, 1)[0]
print(k)
er = np.array([0.046, 0.148, 0.263, 0.358, 0.467, 0.591, 0.730, 0.883, 0.965])
plt.plot(m, np.polyval(np.polyfit(m, rm, 1), m), linewidth=1, color='black',
         label=r'$k=(2.14\pm 0.10) мм^2$')
ax.errorbar(m, rm, yerr=er, fmt='o', elinewidth=1, capsize=3, capthick=0.5, markersize=2.5,
            color='black')
plt.scatter(m, rm, s=np.array([8] * len(m)), color='black')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.minorticks_on()
ax.grid(which="major", color='grey', linewidth=0.7, linestyle='--')
ax.grid(which="minor", color='lightgrey', linewidth=0.7, linestyle='--')
ax.set_ylabel(r'$r_m^2, мм^2$')
ax.set_xlabel('m')
plt.legend()
plt.savefig('graph1.png')
plt.show()
