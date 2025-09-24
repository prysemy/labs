import matplotlib.pyplot as plt
import numpy as np

phi_neon = [2200 - 34, 2200 - 20, 2250 - 38, 2250 - 24, 2254, 2300 - 28, 2300 - 18, 2302, 2350 - 38, 2350 - 16, 2354,
            2400 - 32, 2400 - 20, 2400, 2406, 2450 - 6, 2451, 2500 - 26, 2502, 2550 - 40]
lambda_neon = [5852, 5882, 5945, 5976, 6030, 6074, 6096, 6143, 6164, 6217, 6267, 6305, 6334, 6383, 6402, 6507, 6533,
               6599, 6678, 6717]

phi_rtut = [2150 - 16, 2150 - 26, 1950 - 6, 1550 - 26, 900 - 41, 350 - 32]
lambda_rtut = [579.1, 577.0, 546.1, 491.6, 435.8, 404.7]

# водород
H_alpha = 2466  # красный
# H_betta не видим
H_gamma = 1472  # голубой
H_delta = 836  # фиолетовый

# йод
hnu_10 = 2290
hnu_15 = 2186
hnu_p = 1688


lambda_rtut_angstrom = [l * 10 for l in lambda_rtut]  # 1 нм = 10 Å

# 3. ГРАДУИРОВКА СПЕКТРОМЕТРА
print("=== ГРАДУИРОВКА СПЕКТРОМЕТРА ===")

# Объединяем все данные для градуировки
all_phi = np.array(phi_neon + phi_rtut)
all_lambda = np.array(lambda_neon + lambda_rtut_angstrom)

# Подбираем полином 3-й степени
degree = 3
coefficients = np.polyfit(all_phi, all_lambda, degree)
calibration_poly = np.poly1d(coefficients)

# Рассчитываем коэффициент детерминации R^2
y_pred = calibration_poly(all_phi)
ss_total = np.sum((all_lambda - np.mean(all_lambda))**2)
ss_residual = np.sum((all_lambda - y_pred)**2)
r2 = 1 - (ss_residual / ss_total)

print(f"Коэффициент детерминации R^2: {r2:.6f}")
print(f"Полиномиальная модель: λ(φ) = {coefficients[0]:.6f}φ^3 + {coefficients[1]:.6f}φ^2 + {coefficients[2]:.6f}φ + {coefficients[3]:.6f}")

# Построение градуировочного графика
phi_range = np.linspace(min(all_phi), max(all_phi), 500)
lambda_calibrated = calibration_poly(phi_range)

plt.figure(figsize=(10, 6))
plt.scatter(phi_neon, lambda_neon, color='red', label='Неон', alpha=0.7)
plt.scatter(phi_rtut, lambda_rtut_angstrom, color='blue', label='Ртуть', alpha=0.7)
plt.plot(phi_range, lambda_calibrated, color='green', label=f'Градуировка (полином {degree}-й степени)')
plt.xlabel('Угол φ (деления барабана)')
plt.ylabel('Длина волны λ, Å')
plt.title('Градуировочный график спектрометра УМ-2')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.savefig('gradirovochnyi_grafik.png', dpi=300)
plt.show()

# 4. ОПРЕДЕЛЕНИЕ ДЛИН ВОЛН ВОДОРОДА
print("\n=== ОПРЕДЕЛЕНИЕ ДЛИН ВОЛН ЛИНИЙ ВОДОРОДА ===")

H_alpha_lambda = calibration_poly(H_alpha)
H_gamma_lambda = calibration_poly(H_gamma)
H_delta_lambda = calibration_poly(H_delta)

print("Результаты для линий водорода:")
print(f"H_alpha: φ = {H_alpha}, λ = {H_alpha_lambda:.2f} Å, {H_alpha_lambda/10:.2f} нм")
print(f"H_gamma: φ = {H_gamma}, λ = {H_gamma_lambda:.2f} Å, {H_gamma_lambda/10:.2f} нм")
print(f"H_delta: φ = {H_delta}, λ = {H_delta_lambda:.2f} Å, {H_delta_lambda/10:.2f} нм")

# 5. ВЫЧИСЛЕНИЕ ПОСТОЯННОЙ РИДБЕРГА
print("\n=== ВЫЧИСЛЕНИЕ ПОСТОЯННОЙ РИДБЕРГА ===")

# Функция для расчета R_H
def calculate_rydberg(lambda_angstrom, n):
    term = (1/4 - 1/(n**2))
    R_H = 1e10 / (lambda_angstrom * term)
    return R_H

# n_values для линий серии Бальмера
n_values = {'alpha': 3, 'beta': 4, 'gamma': 5, 'delta': 6}

# Расчет R_H для каждой линии
R_H_list = []
line_names = []
lambda_list_angstrom = []
balmer_terms = []
inv_lambda_list = []

# H_alpha
n = n_values['alpha']
R_H_alpha = calculate_rydberg(H_alpha_lambda, n)
R_H_list.append(R_H_alpha)
line_names.append('H_alpha')
lambda_list_angstrom.append(H_alpha_lambda)
balmer_terms.append(1/4 - 1/n**2)
inv_lambda_list.append(1e10 / H_alpha_lambda)
print(f"R_H из H_alpha (n={n}): {R_H_alpha:.2f} м⁻¹")

# H_gamma
n = n_values['gamma']
R_H_gamma = calculate_rydberg(H_gamma_lambda, n)
R_H_list.append(R_H_gamma)
line_names.append('H_gamma')
lambda_list_angstrom.append(H_gamma_lambda)
balmer_terms.append(1/4 - 1/n**2)
inv_lambda_list.append(1e10 / H_gamma_lambda)
print(f"R_H из H_gamma (n={n}): {R_H_gamma:.2f} м⁻¹")

# H_delta
n = n_values['delta']
R_H_delta = calculate_rydberg(H_delta_lambda, n)
R_H_list.append(R_H_delta)
line_names.append('H_delta')
lambda_list_angstrom.append(H_delta_lambda)
balmer_terms.append(1/4 - 1/n**2)
inv_lambda_list.append(1e10 / H_delta_lambda)
print(f"R_H из H_delta (n={n}): {R_H_delta:.2f} м⁻¹")

# Статистическая обработка
R_H_mean = np.mean(R_H_list)
R_H_std = np.std(R_H_list, ddof=1)

print(f"\nСреднее значение постоянной Ридберга: <R_H> = {R_H_mean:.2f} м⁻¹")
print(f"Стандартное отклонение: ± {R_H_std:.2f} м⁻¹")
print(f"Относительная погрешность: ± {R_H_std/R_H_mean*100:.2f}%")
print(f"Теоретическое значение: R_H_theory ≈ 10967758.1 м⁻¹")
print(f"Относительное расхождение: {abs(R_H_mean - 10967758.1)/10967758.1*100:.2f}%")

# 6. ПРОВЕРКА ФОРМУЛЫ БАЛЬМЕРА
print("\n=== ПРОВЕРКА ФОРМУЛЫ БАЛЬМЕРА ===")

# Линейная аппроксимация 1/λ = R_H * (1/4 - 1/n²)
slope, intercept = np.polyfit(balmer_terms, inv_lambda_list, 1)
print(f"Наклон прямой (экспериментальный R_H): {slope:.2f} м⁻¹")
print(f"Свободный член (должен быть близок к 0): {intercept:.2f} м⁻¹")

# Построение графика проверки формулы Бальмера
plt.figure(figsize=(8, 5))
plt.scatter(balmer_terms, inv_lambda_list, s=80)
x_fit = np.linspace(min(balmer_terms), max(balmer_terms), 100)
y_fit = slope * x_fit + intercept
plt.plot(x_fit, y_fit, 'r--', label=f'1/λ = {slope:.0f}·term + {intercept:.1f}')

# Подписи точек
for i, (x, y, name) in enumerate(zip(balmer_terms, inv_lambda_list, line_names)):
    plt.annotate(name, (x, y), xytext=(5, 5), textcoords='offset points')

plt.xlabel('(1/4 - 1/n²)')
plt.ylabel('1/λ, м⁻¹')
plt.title('Проверка формулы Бальмера (1/λ = R_H · (1/4 - 1/n²))')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('balmer_check.png', dpi=300)
plt.show()