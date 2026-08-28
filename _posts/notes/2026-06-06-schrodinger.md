---
title: 定态薛定谔方程的有限差分法
date: 2026-06-06
categories:
  - notes
  - physics
  - computing
tags:
  - quantum-mechanics
  - numerical-methods
permalink: /notes/schrodinger.html
math: true
---

定态薛定谔方程如下，$V(x)$为任意给定势能函数：
$$
-\frac{\hbar}{2m}\frac{d^2\psi}{dx}+V(x)\psi(x)=E\psi(x)
$$
发现方程含有对 $x$ 的二阶导，采用差分近似：
$$
\left. \frac{d^2\psi}{dx}\right|_{x=x_i} \approx \frac{\psi_{i+1}-2\psi_i+\psi_{i-1}}{h^2}
$$
推导如下：

$x$区间的总长度为$L$，在$x$上取$N$个小区间，则每个区间的长度为$h=\frac{L}{N}$，设$\psi(x)$在$x_i$附近光滑，其中$x_i$表示第$i$个点的坐标，自然有：
$$
x_i = ih,\quad x_{i+1}=(i+1)h, \quad x_{i-1}=(i-1)h
$$
把$\psi(x_i+h)$和$\psi(x_i-h)$在$x_i$处作泰勒展开：
$$
\psi(x_i+h)=\psi(x_i)+h\psi'(x_i)+\frac{h^2}{2}\psi''(x_i)+\frac{h^2}{3!}\psi'''(x_i)+\frac{h^3}{4!}\psi^{(4)}(x_i)+\cdots
$$

$$
\psi(x_i-h)=\psi(x_i)-h\psi'(x_i)+\frac{h^2}{2}\psi''(x_i)-\frac{h^2}{3!}\psi'''(x_i)+\frac{h^3}{4!}\psi^{(4)}(x_i)+\cdots
$$

二者相加：
$$
\psi(x_i+h)+\psi(x_i-h)=2\psi(x_i)+h^2\psi''(x_i)+\cdots
$$
我们把$\psi(x_i)$写成$\psi_i$，就得到差分法的近似公式：
$$
\psi''_i \approx \frac{\psi_{i+1}-2\psi_i+\psi_{i-1}}{h^2}
$$
把它带入薛定谔方程：
$$
-\frac{\hbar^2}{2m}\frac{\psi_{i+1}-2\psi_i+\psi_{i-1}}{h^2}V_i\psi_i=E\psi_i
$$
其中$V_i=V(x_i)$，令$t=\hbar^2/2mh^2$，则方程可以写成：
$$
-t\psi_{i-1}+(2t+V_i)\psi_i-t\psi_{i+1}=E\psi_i
$$
对应求矩阵本征值的问题：
$$
H\Psi = E\Psi
$$
我们采用Dirichlet边界条件，即$\psi_0=\psi_N=0$，因此未知量只有内部$N-1$个点。矩阵$H$的维数为$N-1$，波函数为列向量：
$$
\Psi=\begin{pmatrix}
\psi_1\\
\psi_2\\
\vdots\\
\psi_{N-1}
\end{pmatrix}
$$
矩阵为三对角形式：
$$
\begin{pmatrix}
2t+V_1 & -t & 0 & \cdots & 0\\
-t & 2t+V_2 & -t & \cdots & 0\\
0 & -t & 2t+V_3 & \cdots & 0\\
\vdots & \vdots & \vdots & \ddots & -t\\
0 & 0 & 0 & -t & 2t+V_{N-1}\
\end{pmatrix}
$$
其中，两条副对角线上的$-t$来自于差分近似，主对角线的$2t$来源于动能项，$V_i$来自势能项。考虑到矩阵的形式，我们在python使用`from scipy.linalg import eigh_tridiagonal`求解，使用方法为`eigh_tridiagonal(d, e)`，`d`为主对角线，`e`为两条相同的副对角线。

只要间隔$N$的数量足够大，就可以求得足够准确的数值解。

下面的程序$N=2000$，求解了四种势场：一维无限深势阱、谐振子势、$\delta$函数势和有限深势阱。对于$\delta$函数，数值上无法表示无穷高，使用一个网格点代替：
$$
V_\delta[i_\delta] = \frac{\text{intensity}}{h}
$$
下面的程序运行后画出前五个态的能量与波函数。

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal

# Use dimensionless units: hbar = m = 1.
hbar = 1.0
m = 1.0

N = 2000
number_of_states = 5
levels = np.arange(1, number_of_states + 1)

omega = 1.0
delta_strength = -10.0
delta_position = 0.0
well_width = 1.0
well_depth = 20.0


def make_grid(x_min, x_max):
    """Create a grid whose endpoints are fixed boundary points."""
    h = (x_max - x_min) / (N + 1)
    x = np.linspace(x_min + h, x_max - h, N)
    return x, h


def infinite_well(x, h):
    """The infinite walls come from the fixed endpoints of the grid."""
    return np.zeros_like(x)


def harmonic_oscillator(x, h):
    return 0.5 * m * omega**2 * x**2


def delta_potential(x, h):
    """Approximate a Dirac delta by putting its area on one grid point."""
    V = np.zeros_like(x)
    delta_index = np.argmin(np.abs(x - delta_position))
    V[delta_index] = delta_strength / h
    return V


def finite_square_well(x, h):
    V = np.zeros_like(x)
    V[np.abs(x) <= well_width / 2] = -well_depth
    return V


def solve_schrodinger(V_x, h):
    """Build and diagonalize the finite-difference Hamiltonian."""
    n = len(V_x)
    t = hbar**2 / (2 * m * h**2)
    d = 2 * t + V_x
    e = -t * np.ones(n - 1)
    E, psi = eigh_tridiagonal(
        d,
        e,
        select='i',
        select_range=(0, number_of_states - 1),
    )
    return E, psi / np.sqrt(h)


def plot_potential(ax, name, x, V_x):
    """Draw V(x); use a vertical line for the delta potential display."""
    if name == 'Delta Potential':
        ax.plot(x, np.zeros_like(x), color='black', linewidth=1.5, label='V(x)')
        ax.vlines(delta_position, delta_strength, 0, color='black', linewidth=2.0)
    else:
        ax.plot(x, V_x, color='black', linewidth=1.5, label='V(x)')


potentials = [
    ('Infinite Well', infinite_well, -1.0, 1.0),
    ('Harmonic Oscillator', harmonic_oscillator, -5.0, 5.0),
    ('Delta Potential', delta_potential, -5.0, 5.0),
    ('Finite Square Well', finite_square_well, -5.0, 5.0),
]

results = []
for name, potential, x_min, x_max in potentials:
    x, h = make_grid(x_min, x_max)
    V_x = potential(x, h)
    E, psi = solve_schrodinger(V_x, h)
    results.append((name, x, x_min, x_max, V_x, E, psi))

# Make one large figure for each potential. Each figure has three subplots:
# potential, energy levels, and the first five wave functions.
for name, x, x_min, x_max, V_x, E, psi in results:
    fig, axes = plt.subplots(3, 1, figsize=(10, 10))
    fig.suptitle(name)

    ax_potential, ax_energy, ax_wave = axes

    plot_potential(ax_potential, name, x, V_x)
    ax_potential.set_title('Potential')
    ax_potential.set_xlabel('Position x')
    ax_potential.set_ylabel('V(x)')
    ax_potential.set_xlim(x_min, x_max)
    ax_potential.legend()

    ax_energy.bar(levels, E, color='steelblue')
    ax_energy.set_title('Energy Levels')
    ax_energy.set_xlabel('State Number')
    ax_energy.set_ylabel('Energy')
    ax_energy.set_xticks(levels)

    for i in range(number_of_states):
        ax_wave.plot(x, psi[:, i], label=f'n = {i + 1}')
    ax_wave.set_title('Wave Functions')
    ax_wave.set_xlabel('Position x')
    ax_wave.set_ylabel('psi(x)')
    ax_wave.set_xlim(x_min, x_max)
    ax_wave.legend()

    fig.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()


```

---

图片

---

参考：

* https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigh_tridiagonal.html

* https://www.youtube.com/watch?v=ay0zZ8SUMSk
