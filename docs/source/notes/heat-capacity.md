# 晶格热容的量子理论


当 $T \to 0$ 时，晶格热容满足：

$$
C_V \propto
\begin{cases}
T, & \text{金属中的电子热容} \\
T^3, & \text{绝缘体或半导体中的晶格热容}
\end{cases}
$$

下面主要讨论晶格振动对热容的贡献。

---

晶格振动可以量子化为一组独立的谐振子。第 $i$ 个振动模的能量为：

$$
E_{n_i} = \left(n_i + \frac{1}{2}\right)\hbar\omega_i，n_i = 0,1,2,\cdots
$$

配分函数：

$$
Z_i = \sum_{n_i=0}^{\infty} e^{-\beta n_i \hbar \omega_i}，\beta = \frac{1}{k_B T}
$$

所以晶格振动的平均能量为：

$$
\begin{aligned}
\bar{E}_i(T)
&=
\frac{1}{2}\hbar\omega_i
+
\frac{
\sum_{n_i=0}^{\infty}
n_i\hbar\omega_i e^{-\beta n_i\hbar\omega_i}
}{
\sum_{n_i=0}^{\infty}
e^{-\beta n_i\hbar\omega_i}
} \\
&=
\frac{1}{2}\hbar\omega_i
-
\frac{\partial}{\partial\beta}
\ln\left(
\sum_{n_i=0}^{\infty}
e^{-\beta n_i\hbar\omega_i}
\right)
\end{aligned}
$$

利用级数求和结果 

$$
\sum_{n_i=0}^{\infty} e^{-\beta
n_i\hbar\omega_i}=
\frac{1}
{1-e^{-\beta\hbar\omega_i}}
$$


$$
\Longrightarrow
\bar{E}_i(T)
=
\frac{1}{2}\hbar\omega_i
+
\frac{\hbar\omega_i}{e^{\beta\hbar\omega_i}-1}
$$

平均声子数：

$$
\bar{n}_i
=
\frac{1}{e^{\beta\hbar\omega_i}-1}
$$

$$
\Longrightarrow
\bar{E}_i(T)
=
\frac{1}{2}\hbar\omega_i
+
\bar{n}_i\hbar\omega_i
$$

第一项是零点能，第二项是声子能量。

---

下面求单个振动模对热容的贡献，根据热容的定义为：

$$
C_{V,i}
=
\frac{\partial \bar{E}_i}{\partial T}
$$

代入：

$$
\bar{E}_i(T)
=
\frac{1}{2}\hbar\omega_i
+
\frac{\hbar\omega_i}{e^{\hbar\omega_i/k_B T}-1}
$$

$$
\Longrightarrow
C_{V,i}
=
k_B
\frac{
\left(\frac{\hbar\omega_i}{k_B T}\right)^2
e^{\hbar\omega_i/k_B T}
}{
\left(e^{\hbar\omega_i/k_B T}-1\right)^2
}
$$

低温极限， $k_B T \ll \hbar\omega_i$：

$$
C_{V,i}
\approx
k_B
\left(\frac{\hbar\omega_i}{k_B T}\right)^2
e^{-\hbar\omega_i/k_B T}
\to 0
$$

高温极限， $k_B T \gg \hbar\omega_i$：

$$
C_{V,i}
\to k_B
$$

这就是每个谐振子在高温下给出 $k_B$ 的热容贡献，也就是Dulong-Petit定律。

---

## 1. Einstein 模型

Einstein 模型假设晶体中所有原子都以相同频率 $\omega_E$ 作简正振动。对于含有 $N$ 个原子的晶体，总共有 $3N$ 个振动自由度，因此：

$$
C_V
=
3N k_B
\frac{
\left(\frac{\hbar\omega_E}{k_B T}\right)^2
e^{\hbar\omega_E/k_B T}
}{
\left(e^{\hbar\omega_E/k_B T}-1\right)^2
}
$$

定义 Einstein 温度 $\theta_E = \hbar\omega_E/k_B$ 并代入 $C_V$，

得到：

$$
C_V
=
3N k_B
\frac{
\left(\frac{\theta_E}{T}\right)^2
e^{\theta_E/T}
}{
\left(e^{\theta_E/T}-1\right)^2
}
$$

高温极限：即 $T \gg \theta_E$ 时， $C_V \to 3N k_B$，对应Dulong-Petit 定律。

低温极限： $T \ll \theta_E$ 时，它是一个负指数型的函数，趋于$0$：

$$
C_V
\approx
3N k_B
\left(\frac{\theta_E}{T}\right)^2
e^{-\theta_E/T}
\to 0
$$

Einstein 模型可以解释低温热容趋于零，但它给出的是指数衰减，与实际不符，而实验中许多绝缘体低温下满足：$C_V \propto T^3$ ，引入 Debye 模型。

---

## 2. Debye 模型

Debye 模型把晶格振动看成连续介质中的弹性波。声学支近似满足线性色散关系,也就是 $q$ 很小时，$sin$ 函数趋于线性，即长波极限：

$$
\omega = c q
$$

对于三维情况，

$$
有一个纵波：
\omega = c_l q
$$

$$
两个横波：
\omega = c_t q
$$

三维一个波矢态在 $\mathbf{q}$ 空间中占据的体积为： $\frac{(2\pi)^3}{V}$，因此 $\mathbf{q}$ 空间中的 $\mathbf{q}$ 密度为：$\frac{V}{(2\pi)^3}$。

$\mathbf{q}$ 不是任意取的，允许取的数目是 $\frac{V}{(2\pi)^3}\mathrm{d}\mathbf{k}$。

对于宏观的 $V$ ，把 $\mathbf{q}$ 看成连续的，积分代替求和。

对于包含在 $\omega \to \omega + \mathrm{d}\omega$ 内，

$$
\Delta n = g(\omega) \Delta \omega 
\longrightarrow
\mathrm{d}n = \underbrace{g(\omega)}_{\text{{密度}}} \underbrace{\mathrm{d}\omega}_{\text{区间}}
$$


有 $n$ 个振动模，所以直接积分即可。

$$
C_V(T)
=
k_B
\int \frac{(\hbar\omega/k_BT)^2 e^{\hbar\omega/k_BT}}{(e^{\hbar\omega/k_BT}-1)^2} g(\omega)\mathrm{d}\omega
$$

在线性色散关系下可以求出 $g(\omega)$：

$$
q = \frac{\omega}{c_l} 
\longrightarrow
q + \mathrm{d}q = \frac{\omega+\mathrm{d}\omega}{c_l} = q + \frac{\mathrm{d}\omega}{c_l}
$$

纵波数目为：

$$
\frac{V}{(2\pi)^3}4\pi q^2\mathrm{d}q 
=
\frac{V}{2\pi^2c_l^3}\omega^2\mathrm{d\omega}
$$

同理，横波数目为：

$$
2\times\frac{V}{2\pi^2c_t^3}\omega^2\mathrm{d\omega}
$$



$$\Longrightarrow g(\omega) = \frac{3V}{2\pi^2\bar{c}^3}\omega^2\mathrm{d\omega}
$$

我们发现，对 $\omega^2$ 积分，积分发散，也就是：

$$
\int_0^\infty g(\omega)\mathrm{d}\omega \rightarrow \infty
$$

Debye假设，$\omega$有一个上限的截止频率$\omega_m$，$\omega_m$ 称为Debye频率。超过这个频率的短波不存在。因为一共有 $3N$ 个振动模，所以

$$
\int_0^{\omega_m} g(\omega)\mathrm{d}\omega = 3N
$$

定义Debye温度：$\Theta_D=\frac{\hbar\omega_m}{k_B}$

$$
\Rightarrow
C_V
=
9N k_B
\left(\frac{T}{\theta_D}\right)^3
\int_0^{\theta_D/T}
\frac{x^4 e^x}{(e^x-1)^2}\,\mathrm{d}x
$$

低温极限下，当： $T \ll \theta_D$ 时，积分上限可以近似为无穷大：$\theta_D/T \to \infty$

有：

$$
C_V
\approx
\frac{12\pi^4}{5}
N k_B
\left(\frac{T}{\theta_D}\right)^3
$$

这说明三维晶体在低温下的晶格热容满足：

$$
C_V \sim T^3
$$

这就是 Debye $T^3$ 定律。低温下只有长声学波。


---

## 3. 晶格振动的模式密度

一般地，振动态密度，上面的 $g(\omega)$ 定义为：

$$
g(\omega) = \frac{dn}{d\omega}
$$

更一般地，可以写成等频面上的积分：

$$
g(\omega)
=
\frac{V}{(2\pi)^3}
\int
\frac{dS}{\left|\frac{d\omega}{dq}\right|}
$$

其中 $dS$ 是 $q$ 空间中等频面上的面积元。

