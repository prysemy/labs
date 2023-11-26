import numpy as np
import matplotlib.pyplot as plt


def read(file):
    data = []
    with open(file, 'r') as file:
        for line in file.readlines():
            data.append(float(line))
    return np.array(data)


def aver(data):
    return np.sum(data) / np.size(data)


mmHg_40 = read('40.txt')
mmHg_80 = read('80.txt')
mmHg_120 = read('120.txt')
mmHg_160 = read('160.txt')

calib_count_arr = np.array([aver(mmHg_40), aver(mmHg_80),
                            aver(mmHg_120), aver(mmHg_160)])
calib_press_arr = np.array([40, 80, 120, 160])


def a(m):
    return np.sum(m) / np.size(m)


u = calib_press_arr
v = calib_count_arr

plt.figure(figsize=(8, 6), dpi=100)
plt.title('Калибровочный график зависимости показаний АЦП от давления')
plt.xlim(0, 2000)
plt.ylim(0, 180)
plt.ylabel("Давление [мм рт.ст.]")
plt.xlabel("Отсчёты АЦП")
plt.grid(which='major', color='#A0A0A0')
plt.minorticks_on()
plt.grid(which='minor', color='#E0E0E0')
plt.scatter(calib_count_arr, calib_press_arr, label='Измерения')
plt.plot(np.linspace(500, 1680, 100), np.linspace(40, 160, 100), label='$p = 0.101 \cdot N - 10.50$ [Па]')
plt.legend()
plt.show()
plt.savefig('kalib.png')
