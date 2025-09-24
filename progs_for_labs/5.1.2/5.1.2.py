import numpy as np
import matplotlib.pyplot as plt

# Данные
x = np.array([0.0000, 0.0038, 0.0152, 0.0341, 0.0603, 0.1340, 0.2340,
              0.3572, 0.5000, 0.6580, 0.8264, 1.0000, 1.1736, 1.3420])

dx = np.array([0.0000, 0.0015, 0.0030, 0.0045, 0.0060, 0.0087, 0.0112,
               0.0134, 0.0151, 0.0164, 0.0172, 0.0175, 0.0172, 0.0164])

y = np.array([1142.9, 1091.7, 1180.6, 1109.9, 1315.8, 1552.8, 1730.1,
              1976.3, 2217.3, 2531.6, 2849.0, 3225.8, 3401.4, 3703.7])

dy = np.array([0.38, 0.40, 0.54, 0.56, 0.96, 1.30, 1.64,
               2.24, 2.95, 4.04, 5.30, 7.09, 8.14, 9.98])

# Аппроксимация полиномом 1 степени (прямая)
coeffs = np.polyfit(x, y, 1)
k, b = coeffs[0], coeffs[1]
y_fit = np.polyval(coeffs, x)

# Расчет погрешностей параметров аппроксимации
residuals = y - y_fit
chi2 = np.sum((residuals / dy) ** 2)
dof = len(x) - 2  # степени свободы

# Ковариационная матрица параметров
X = np.column_stack([x, np.ones_like(x)])
cov_matrix = np.linalg.inv(X.T @ (X / dy[:, np.newaxis] ** 2))
param_errors = np.sqrt(np.diag(cov_matrix))

dk, db = param_errors[0], param_errors[1]

# Расчет энергии покоя
Eg = 662
dEg = 5  # погрешность энергии фотона

N0 = 1 / b
N90 = 1 / (k + b)
mc2 = Eg * N90 / (N0 - N90)

# Расчет погрешностей методом propagation of errors
# Погрешности N0 и N90
dN0 = db / (b ** 2)
dN90 = np.sqrt((dk / (k + b) ** 2) ** 2 + (db / (k + b) ** 2) ** 2)

# Погрешность разности N0 - N90
diff = N0 - N90
d_diff = np.sqrt(dN0 ** 2 + dN90 ** 2)

# Погрешность mc²
dmc2_dEg = N90 / diff
dmc2_dN90 = Eg / diff - Eg * N90 / (diff ** 2)
dmc2_ddiff = -Eg * N90 / (diff ** 2)

dmc2 = np.sqrt((dmc2_dEg * dEg) ** 2 +
               (dmc2_dN90 * dN90) ** 2 +
               (dmc2_ddiff * d_diff) ** 2)

# График
plt.figure(figsize=(12, 8))

# Экспериментальные точки с погрешностями
plt.errorbar(x, y, xerr=dx, yerr=dy, fmt='o', color='navy',
             markersize=8, capsize=5, capthick=2, elinewidth=2, alpha=0.8,
             markerfacecolor='white', markeredgewidth=2)

# Аппроксимирующая прямая
x_smooth = np.linspace(min(x), max(x), 500)
y_smooth = np.polyval(coeffs, x_smooth)
plt.plot(x_smooth, y_smooth, 'r-', linewidth=3,
         label=f'$y = ({k:.1f} \pm {dk:.1f})x + ({b:.1f} \pm {db:.1f})$')

# Настройки графика
plt.xlabel(r'$1 - \cos\theta$', fontsize=16, fontweight='bold')
plt.ylabel(r'$1/N(\theta)$', fontsize=16, fontweight='bold')

plt.grid(True, alpha=0.7, linestyle='--')
plt.minorticks_on()
plt.grid(which='minor', alpha=0.5, linestyle=':')
plt.legend(fontsize=12, framealpha=0.9)

plt.tight_layout()
plt.savefig('1.png', dpi=300, bbox_inches='tight')
# plt.show()

# Вывод результатов
print("=" * 60)
print("РЕЗУЛЬТАТЫ РАСЧЕТА")
print("=" * 60)
print(f"Параметры аппроксимации:")
print(f"k = {k:.3f} ± {dk:.3f} (отн. погр.: {dk / k * 100:.1f}%)")
print(f"b = {b:.3f} ± {db:.3f} (отн. погр.: {db / b * 100:.1f}%)")
print(f"χ²/dof = {chi2:.1f}/{dof} = {chi2 / dof:.1f}")

print(f"\nРасчетные величины:")
print(f"N₀ = 1/b = {N0:.3f} ± {dN0:.3f}")
print(f"N₉₀ = 1/(k+b) = {N90:.3f} ± {dN90:.3f}")
print(f"N₀ - N₉₀ = {diff:.3f} ± {d_diff:.3f}")

print(f"\nФинальный результат:")
print(f"Энергия покоя: mc² = {mc2:.2f} ± {dmc2:.2f} кэВ")
print(f"Теоретическое значение: 511.0 кэВ")
print(f"Отклонение: {(mc2 - 511) / 511 * 100:.2f}%")
print(f"Относительная погрешность: {dmc2 / mc2 * 100:.2f}%")

print(f"\nВклад погрешностей:")
print(f"От Eγ: {abs(dmc2_dEg * dEg):.1f} кэВ")
print(f"От N₉₀: {abs(dmc2_dN90 * dN90):.1f} кэВ")
print(f"От разности: {abs(dmc2_ddiff * d_diff):.1f} кэВ")
