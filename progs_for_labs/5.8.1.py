import numpy as np
import matplotlib.pyplot as plt

W = np.array([747.4, 727.1, 1142, 1609, 2663, 5070, 7330, 9960, 9917.6])
T = np.array([912.3, 1007., 1112., 1216., 1320., 1424., 1528., 1632., 1736.])
sigma_W = np.array([5.2, 5.1, 6.9, 8.7, 12.8, 19.4, 26.3, 32.9, 32.8])  # мВт
sigma_T = 2.0  # K

sigma_W = sigma_W * 1e-3  # переводим в Вт
W = W * 1e-3  # переводим в Вт

# Логарифмические координаты
lnW = np.log(W)
lnT = np.log(T)

k, b = np.polyfit(lnT, lnW, 1)
print('n =', k)

# Погрешности в логарифмических координатах
sigma_lnW = sigma_W / W
sigma_lnT = sigma_T / T

# Расчет погрешностей коэффициентов
n = len(lnT)
S = np.sum(lnT)
S2 = np.sum(lnT**2)
D = n * S2 - S**2

# Среднеквадратичное отклонение точек от прямой
residuals = lnW - (k * lnT + b)
sigma_res = np.sqrt(np.sum(residuals**2) / (n - 2))

# Погрешности коэффициентов
sigma_k = sigma_res * np.sqrt(n / D)
sigma_b = sigma_res * np.sqrt(S2 / D)

print(f'{sigma_k:.6f}')
print(f'{sigma_b:.6f}')

plt.figure(figsize=(10, 6))
plt.scatter(lnT, lnW, color='#2E86AB', s=80, alpha=0.8, edgecolors='white', linewidth=1)
x_fit = np.linspace(min(lnT), max(lnT), 100)
y_fit = k * x_fit + b

plt.errorbar(lnT, lnW, xerr=sigma_lnT, yerr=sigma_lnW,
             fmt='o', color='#2E86AB', markersize=6, capsize=4, capthick=1.5,
             alpha=0.8, label='Экспериментальные данные', elinewidth=1.5)
plt.plot(x_fit, y_fit, color='#A23B72', linewidth=2.5, linestyle='--',
         label=f'lnW = {k:.3f}·lnT + {b:.3f}')
# Настройки оформления
plt.xlabel('ln(T)', fontsize=12, fontweight='bold')
plt.ylabel('ln(W)', fontsize=12, fontweight='bold')
plt.title('Зависимость ln(W) от ln(T) для проверки закона Стефана-Больцмана',
          fontsize=14, fontweight='bold', pad=20)

plt.grid(True, linestyle='-', linewidth=0.5)
plt.legend(fontsize=11, framealpha=0.9, shadow=True)

plt.annotate(f'n = {k:.3f}',
             xy=(0.05, 0.95), xycoords='axes fraction',
             fontsize=12, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_linewidth(0.5)
plt.gca().spines['bottom'].set_linewidth(0.5)

plt.tight_layout()
plt.savefig('1.png')
plt.show()