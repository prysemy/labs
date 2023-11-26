import numpy as np
import matplotlib.pyplot as plt


def read(file):
    data = []
    with open(file, 'r') as file:
        for line in file.readlines():
            data.append(float(line))
    return np.array(data)


fitness = read('pot_fit.txt')
fitness = [fitness[i] * 0.101 - 10.5 for i in range(len(fitness))]
time_fitness = np.linspace(0, 60, np.size(fitness))

plt.figure(figsize=(8, 6), dpi=100)
plt.title('Артериальное давление\nпосле физической нагрузки')
plt.xlim(2, 35)
plt.ylim(20, 180)
plt.ylabel("Давление [мм рт.ст.]")
plt.xlabel("Время [с]")
plt.grid(which='major', color='#A0A0A0')
plt.minorticks_on()
plt.grid(which='minor', color='#E0E0E0')

plt.plot(time_fitness, fitness, linewidth=0.7, label='Давление 131/78 [мм рт.ст.]')
plt.scatter([6.2], [131], marker='*', color='red')
plt.text(6.2, 131 + 5, 'Systole')
plt.scatter([18.1], [75], marker='*', color='red')
plt.text(18.1, 75 + 5, 'Diastole')
plt.legend()
plt.savefig('fitness.png')

step_pulse = fitness[::40]
time_pulse = time_fitness[::40]
pulse = [step_pulse[i] - step_pulse[i - 1] for i in range(1, len(step_pulse))]
plt.figure(figsize=(8, 6), dpi=100)
plt.title('Пульс\nпосле физической нагрузки')
plt.ylabel("Изменение давления в артерии [мм рт.ст.]")
plt.xlabel("Время [с]")
plt.grid(which='major', color='#A0A0A0')
plt.minorticks_on()
plt.grid(which='minor', color='#E0E0E0')
plt.xlim(10, 30)
plt.plot(time_pulse[:-1], pulse, label='Пульс 66 [уд/мин]')
plt.legend()
plt.show()
plt.savefig('pulse_fitness.png')
