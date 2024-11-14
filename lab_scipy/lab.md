## Эпизод 1
Задана матрица 9х9:

$$\begin{bmatrix}0 & 0 & 0 & -\frac{1}{\ro} & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & -\frac{1}{\ro} & 0 & 0 & 0 & 0 \\\
0 & 0 & 0 & 0 & 0 & -\frac{1}{\ro} & 0 & 0 & 0 \\\
-(\lambda + 2\mu) & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\\
0 & -\mu & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\\
0 & 0 & -\mu & 0 & 0 & 0 & 0 & 0 & 0 \\\
-\lambda & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\\
-\lambda & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\end{bmatrix}$$

Найдите её собственные значения в символьном виде:
```Python
import numpy as np
import sympy

ro = sympy.Symbol("ro")
l = sympy.Symbol("l")
m = sympy.Symbol("m")
z1 = np.zeros((3, 3))
nz1 = np.diag((-l-2*m, -m, -m))
nz2 = np.array([[-l, 0, 0], [0, 0, 0], [-l, 0, 0]])
matrix1 = np.concatenate((z1, nz1, nz2), axis=0)
nz3 = np.diag((-1/ro, -1/ro, -1/ro))
z2 = np.zeros((6, 3))
matrix2 = np.concatenate((nz3, z2), axis=0)
matrix3 = np.zeros((9, 3))
matrix = np.concatenate((matrix1, matrix2, matrix3), axis=1)

matrix = sympy.Matrix(matrix)
print('Собственные значения:', list(matrix.eigenvals().keys()))
```

Вывод программы:
```
Собственные значения: [-1.0*sqrt(m/ro), 1.0*sqrt(m/ro), -1.4142135623731*sqrt(0.5*l/ro + m/ro), 1.4142135623731*sqrt(0.5*l/ro + m/ro), 0]
```

То есть полученные собственные значения: $-\sqrt{\frac{\mu}{\ro}}$, $\sqrt{\frac{\mu}{\ro}}$, $-\sqrt{2}\sqrt{0.5\frac{\lambda}{\ro} + \frac{\mu}{\ro}}$, $\sqrt{2}\sqrt{0.5\frac{\lambda}{\ro} + \frac{\mu}{\ro}}$
