import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optimize


def sine_func(x, a, b, c, d):
    return a * np.sin(b * x + c) + d


def fit_sin(x_data, y_data):
    a_guess = (np.max(y_data) - np.min(y_data)) / 2
    period_guess = 2 * np.pi
    b_guess = 2 * np.pi / period_guess
    c_guess = 0
    d_guess = np.mean(y_data)

    initial_guess = [a_guess, b_guess, c_guess, d_guess]

    try:
        params, params_covariance = optimize.curve_fit(
            sine_func, x_data, y_data, p0=initial_guess
        )
        return params, params_covariance
    except RuntimeError:
        print("Ошибка: Не удалось найти оптимальные параметры.")
        return None, None


I = np.array([8.3, 19.2, 30.8, 52.5, 67.5, 53.3, 71.7, 99.2, 100, 73.3, 59.2, 35.8, 28.3, 16.7])
I_ = np.array([8.3, 19.2, 30.8, 52.5, 67.5, 99.2, 100, 73.3, 59.2, 35.8, 28.3, 16.7])
a_ = np.array(np.arange(20, 61, 10).tolist() + np.arange(90, 151, 10).tolist())
a = np.arange(20, 151, 10)

sI = np.array([0.8, 0.8, 0.9, 0.9, 1.0, 0.9, 1.0, 1.2, 1.2, 1.0, 1.0, 0.9, 0.9, 0.8])

# params, params_covariance = fit_sin(a_, I_)
# y_fit = sine_func(a_, *params)
a_guess = (np.max(I_) - np.min(I_)) / 2
period_guess = 360 # Предположим, период близок к 360 (полный круг)
b_guess = 2 * np.pi / period_guess
c_guess = 0
d_guess = np.mean(I_)
initial_guess = [a_guess, b_guess, c_guess, d_guess]

params, params_covariance = optimize.curve_fit(sine_func, a_, I_, p0=initial_guess)
print(f"a = {params[0]}, b = {params[1]}, c = {params[2]}, d = {params[3]}")
a_fit = np.linspace(min(a_), max(a_), 1000)
I_fit = sine_func(a_fit, *params)

# plt.plot(a_, np.polyval(np.polyfit(a_, I_, 4), a_))
plt.plot(a_fit, I_fit, '-')
plt.errorbar(a, I, yerr=sI, fmt='o', capsize=4, ms=2)
plt.scatter(a, I, s=np.array([6]*len(a)))
plt.scatter(a_, I_, color='red', s=np.array([6]*len(a_)))
plt.grid()
plt.xlabel(r'$\alpha$')
plt.ylabel('Относительная интенсивность, %')
plt.savefig('graph1.png')
plt.show()
