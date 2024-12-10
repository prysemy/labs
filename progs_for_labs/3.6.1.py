import numpy as np
import matplotlib.pyplot as plt

t = np.array([20, 50, 80, 110, 140, 170, 200])
dv = [50.02, 20, 12.5, 8.9, 6.8, 5.5, 5]
plt.scatter(1/t, dv)
plt.plot(1/t, np.polyval(np.polyfit(1/t, dv, 1), 1/t))
plt.grid()
plt.legend(['k='+str(round(np.polyfit(1/t, dv, 1)[0] / 1000, 4))+' Гц*с'])
plt.title(r'Зависимость $\Delta\nu(1/\tau)$')
plt.xlabel(r'$1/\tau, мкс^{-1}$')
plt.ylabel(r'$\Delta\nu$, кГц')
plt.savefig('1.png')
plt.show()

T = np.array([.2, 1, 1.8, 2.6, 3.4, 4.2, 5])
bv = [5.014, 1.003, .548, .38, .284, .225, .201]
plt.scatter(1/T, bv)
plt.plot(1/T, np.polyval(np.polyfit(1/T, bv, 1), 1/T))
plt.grid()
plt.legend(['k='+str(round(np.polyfit(1/T, bv, 1)[0], 4))+' Гц*с'])
plt.title(r'Зависимость $\delta\nu(1/T)$')
plt.xlabel(r'$1/T, мс^{-1}$')
plt.ylabel(r'$\delta\nu$, кГц')
plt.savefig('2.png')
plt.show()

m = np.array([10, 30, 50, 70, 90, 100]) / 100
abao = [0.049, 0.2, 0.25, .35, .45, .52]
plt.scatter(m, abao)
plt.plot(m, np.polyval(np.polyfit(m, abao, 1), m))
plt.grid()
plt.legend(['k='+str(round(np.polyfit(m, abao, 1)[0], 4))])
plt.title(r'Зависимость $\frac{a_{бок}}{a_{осн}}(m)$')
plt.xlabel('m')
plt.ylabel(r'$\frac{a_{бок}}{a_{осн}}$')
plt.savefig('3.png')
plt.show()