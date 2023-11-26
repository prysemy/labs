import numpy as np
import matplotlib.pyplot as plt


def read(file):
    data = []
    with open(file, 'r') as file:
        for line in file.readlines():
            data.append(float(line))
    return np.array(data)


rest = read('pot_rest.txt')
rest = [rest[i] * 0.101 - 10.5 for i in range(len(rest))]
time_rest = np.linspace(0, 60, np.size(rest))

plt.figure(figsize=(8, 6), dpi=100)
plt.title('Артериальное давление\nдо физической нагрузки')
plt.xlim(2.5, 30)
plt.ylim(20, 180)
plt.ylabel("Давление [мм рт.ст.]")
plt.xlabel("Время [с]")
plt.grid(which='major', color='#A0A0A0')
plt.minorticks_on()
plt.grid(which='minor', color='#E0E0E0')

plt.plot(time_rest, rest, linewidth=0.7, label='Давление 117/80 [мм рт.ст.]')
plt.scatter([10.1], [117], marker='*', color='red')
plt.text(10.1, 114 + 5, 'Systole')
plt.scatter([19.8], [80], marker='*', color='red')
plt.text(19.8, 80 + 5, 'Diastole')
plt.legend()
plt.savefig('rest.png')

step_pulse = rest[::40]
time_pulse = time_rest[::40]
pulse = [step_pulse[i] - step_pulse[i - 1] for i in range(1, len(step_pulse))]
plt.figure(figsize=(8, 6), dpi=100)
plt.title('Пульс\nдо физической нагрузки')
plt.ylabel("Изменение давления в артерии [мм рт.ст.]")
plt.xlabel("Время [с]")
plt.grid(which='major', color='#A0A0A0')
plt.minorticks_on()
plt.grid(which='minor', color='#E0E0E0')
plt.xlim(10, 30)
plt.plot(time_pulse[:-1], pulse, label='Пульс 63 [уд/мин]')
plt.legend()
plt.savefig('pulse_rest.png')
plt.show()
