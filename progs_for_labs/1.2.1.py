# m = [0.5030, 0.5150, 0.5109, 0.5100, 0.4982]
# dx = [11.6, 11.0, 10.7, 11.0, 11.5]
# M = 2915
# L = 2.218
# g = 9.81
# u = [M / m[i] * (g / L) ** 0.5 * dx[i] / 1000 for i in range(5)]
# print(u)
# g_M = 5 / 1000
# g_m = 0.1 / 1000
# g_L = 0.2 / 100
# g_dx = 0.25 / 1000
# g_sist = (g_M ** 2 + g_m ** 2 + g_L ** 2 / 4) ** 0.5
# u_s = sum(u) / 5
# print(g_sist * u_s)
# g_sluch = (1 / 20 * sum((u[i] - u_s) ** 2 for i in range(5))) ** 0.5
# print(g_sluch)
# g = (g_sist ** 2 + g_sluch ** 2) ** 0.5
# print(g)

x = [4.9 / 100, 4.6 / 100, 4.0 / 100, 4.9 / 100, 4.2 / 100]
d = 128 / 100
phi = [x[i] / 2 / d for i in range(5)]
print(phi)
R = 33.6 / 100
r = 20 / 100
M_g = (730.7 + 713.4) / 2 / 1000
m_2 = [0.5103 / 1000, 0.5037 / 1000, 0.5105 / 1000, 0.5028 / 1000, 0.4978 / 1000]
t1 = [6.43, 6.45, 6.45, 6.45, 6.47]
t2 = [4.74, 4.62, 4.68, 4.75, 4.72]
ki = [4 * 3.1415 * M_g * R ** 2 * t1[i] / (t1[i] ** 2 - t2[i] ** 2) for i in range(5)]
print(sum(ki) / 5)
u = [phi[i] * ki[i] / m_2[i] / r for i in range(5)]
u_s = sum(u) / 5
print('u=', u)
print(u_s)
g = [u[i] * (0.001 ** 2 + 0.001 ** 2 + 0.00348 ** 2 + 0.001 ** 2) ** 0.5 for i in range(5)]
print(g)
print(sum(g)/5)
g_s = (1 / 20 * sum((u[i] - u_s) ** 2 for i in range(5))) ** 0.5
print(g_s)
print((g_s ** 2 + 0.24 ** 2) ** 0.5)
