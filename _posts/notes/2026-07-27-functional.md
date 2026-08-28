---
title: 欧拉-拉格朗日方程复习
date: 2026-07-27
categories:
  - notes
  - physics
tags:
  - classical-mechanics
  - variational-calculus
permalink: /notes/functional.html
math: true
---

## 1. 轨迹

### 1.1 牛顿方程

考虑一个质量为 $m$ 的粒子。它在一维空间中的轨迹记为 $x(t)$，运动时间为

$$
0\leq t\leq \tau.
$$

若粒子受到的合力为 $F$，牛顿第二定律为

$$
F=m\ddot x.
$$

若力为保守力，来自一个不显含时间的势能 $V(x)$，则

$$
m\ddot x(t)
=
-V'\bigl[x(t)\bigr].
$$

这是一个关于时间的微分方程。给定初始位置和初始速度后，求解它便能得到整条轨迹 $x(t)$。

### 1.2 平均动能和平均势能

粒子在时刻 $t$ 的动能是

$$
T\bigl[x(t),\dot x(t)\bigr]
=
\frac12m[\dot x(t)]^2.
$$

沿一条给定轨迹的平均动能为

$$
\bar T[x]
=
\frac1\tau
\int_0^\tau
\frac12m[\dot x(t)]^2\,dt.
$$

平均势能为

$$
\bar V[x]
=
\frac1\tau
\int_0^\tau
V\bigl[x(t)\bigr]\,dt.
$$

瞬时动能 $T$ 和瞬时势能 $V$ 是普通函数：给定某一时刻的位置和速度，它们返回一个数。平均动能 $\bar T[x]$ 和平均势能 $\bar V[x]$ 则不同。要计算它们，必须知道从 $0$ 到 $\tau$ 的整条轨迹。因此，二者都是轨迹的**泛函（functional）**。

若势能不显含时间，则经典轨迹上的总能量守恒：

$$
E=T+V.
$$

在整个运动区间取平均后仍有

$$
E=\bar T+\bar V.
$$

但是 $\bar T$ 与 $\bar V$ 各自怎样随轨迹变化，并不能仅由能量守恒直接看出。这个问题需要泛函导数。

---

## 2. 泛函

### 2.1 函数与泛函

普通函数把一个数映射为另一个数。例如

$$
f(x)=2x+1
$$

把*输入* $x=1$ 映射为*输出* $3$。

泛函把一整个函数映射为一个数。例如

$$
I[f]
=
\int_0^1 f(u)\,du.
$$

当输入函数为

$$
f(u)=u^2
$$

时，泛函的输出为

$$
I[f]
=
\int_0^1u^2\,du
=
\frac13.
$$

因此，方括号 $F[f]$ 用来提醒我们：$F$ 的输入是整条函数 $f$，而不是函数在某一点的取值。对于一个已经确定的输入函数，$F[f]$ 的输出仍然只是一个数。平均动能和平均势能正是这种映射：

$$
x(t)
\longmapsto
\bar T[x],
\qquad
x(t)
\longmapsto
\bar V[x].
$$

### 2.2 一阶变分

设 $F[x]$ 是一个轨迹泛函。取另一条与 $x(t)$ 接近的轨迹，并写成

$$
x(t)+\Delta x(t).
$$

这里的 $\Delta x(t)$ 是两条轨迹之差。因为这个差可以随时间变化，所以 $\Delta x$ 本身也是一条函数。

普通函数在邻近点处可以展开为

$$
f(x+\Delta x)
=
f(x)
+
f'(x)\Delta x
+
O\bigl((\Delta x)^2\bigr).
$$

其中 $f'(x)\Delta x$ 是函数值变化的一阶部分。对泛函也作同样的展开：

$$
F[x+\Delta x]
=
F[x]
+
\delta F[x;\Delta x]
+
O(\Delta^2).
$$

$\delta F[x;\Delta x]$ 称为一阶变分。它是实际变化

$$
\Delta F
\equiv
F[x+\Delta x]-F[x]
$$

中关于 $\Delta x$ 的线性部分。固定原轨迹后，如果把 $\Delta x$ 放大两倍，一阶变分也放大两倍；如果把两种轨迹变化相加，它们的一阶影响也相加。一阶变分依赖于两样东西：从哪一条轨迹开始，以及向哪一条邻近轨迹移动。原轨迹和轨迹变化一旦给定，一阶变分就是一个数。

### 2.3 泛函导数

先把时间区间分成 $N$ 个小段，泛函近似成为多元函数

$$
F_N(x_1,x_2,\ldots,x_N).
$$

对于普通多元函数的一阶变化是

$$
\delta F_N
=
\sum_{i=1}^{N}
\frac{\partial F_N}{\partial x_i}
\Delta x_i.
$$

每一个分量都是“对第 $i$ 个分量的变化率”（偏导）乘以“第 $i$ 个分量的实际变化”，总的一阶变化等于所有分量贡献之和。

设分成 $N$ 段，每一段的时间间隔为 $\Delta t$。在每一项中乘除 $\Delta t$，得到

$$
\delta F_N
=
\sum_{i=1}^{N}
\left(
\frac1{\Delta t}
\frac{\partial F_N}{\partial x_i}
\right)
\Delta x_i\,\Delta t.
$$

当分割无限变细时，离散下标 $i$ 变成连续时间 $t$，求和变成积分，括号中的变成关于时间的函数。于是

$$
\delta F[x;\Delta x]
=
\int_0^\tau
G(t)\Delta x(t)\,dt.
$$

这个系数函数定义为泛函导数：

$$
G(t)
\equiv
\frac{\delta F[x]}{\delta x(t)}.
$$

$$
\boxed{
\delta F[x;\Delta x]
=
\int_0^\tau
\frac{\delta F[x]}{\delta x(t)}
\Delta x(t)\,dt
}.
$$

固定原轨迹后，泛函导数 $\delta F[x]/\delta x(t)$ 仍然随时间变化，所以它是一条函数。一阶变分 $\delta F[x;\Delta x]$ 则还包含具体的轨迹变化，并在积分以后成为一个数。二者的关系与普通微积分中的 $f'(x)$ 和 $f'(x)\Delta x$ 相似。

### 2.4 驻定条件

设 $x_*(t)$ 是一条特殊轨迹。如果

$$
\left.
\frac{\delta F[x]}{\delta x(t)}
\right|_{x=x_*}
=0
$$

在每个时刻都成立，泛函导数处处为零，那么对任意允许的 $\Delta x(t)$ 都有

$$
\delta F[x_*;\Delta x]
=
\int_0^\tau
0\cdot\Delta x(t)\,dt
=0,
$$

一阶变分对**所有允许的轨迹**变化都为零。反过来也成立。若泛函导数在某个小区间内不为零，可以选取一条只在这个区间内非零并与它同号的轨迹变化，使积分不为零，从而产生矛盾。

$$
\delta F[x_*;\Delta x]=0
\quad
\text{对所有允许的 }\Delta x
\quad\Longleftrightarrow\quad
\left.
\frac{\delta F[x]}{\delta x(t)}
\right|_{x=x_*}=0
\quad
\text{对每个 }t。
$$

一阶变分为零也不等于泛函的实际变化为零。根据展开式，

$$
F[x_*+\Delta x]-F[x_*]
=
O(\Delta^2).
$$

这只说明实际变化从二阶开始。驻定点可以是极小值、极大值。

---

## 3. 平均能量的泛函导数

比较的所有轨迹都连接相同的起点和终点，并且经历相同的时间。因此轨迹变化满足

$$
\Delta x(0)=\Delta x(\tau)=0.
$$

这个端点条件将在处理平均动能时消去分部积分产生的边界项。

### 3.1 平均势能

沿邻近轨迹的平均势能是

$$
\bar V[x+\Delta x]
=
\frac1\tau
\int_0^\tau
V\bigl[x(t)+\Delta x(t)\bigr]\,dt.
$$

在每个时刻对普通函数 $V$ 作一阶展开：

$$
V(x+\Delta x)
=
V(x)
+
V'(x)\Delta x
+
O(\Delta^2).
$$

代入积分后，平均势能的一阶变分为

$$
\delta\bar V[x;\Delta x]
=
\frac1\tau
\int_0^\tau
V'\bigl[x(t)\bigr]
\Delta x(t)\,dt.
$$

与泛函导数的定义比较，得到

$$
\frac{\delta\bar V[x]}{\delta x(t)}
=
\frac1\tau
V'\bigl[x(t)\bigr].
$$

### 3.2 平均动能

沿邻近轨迹的速度为

$$
\dot x(t)+\Delta\dot x(t),
\qquad
\Delta\dot x(t)
=
\frac{d}{dt}\Delta x(t).
$$

将它代入平均动能：

$$
\bar T[x+\Delta x]
=
\frac1\tau
\int_0^\tau
\frac12m
\bigl[\dot x(t)+\Delta\dot x(t)\bigr]^2dt.
$$

展开平方，只保留一阶项：

$$
\delta\bar T[x;\Delta x]
=
\frac m\tau
\int_0^\tau
\dot x(t)\Delta\dot x(t)\,dt.
$$

由于目标是把一阶变分写成某个函数乘以 $\Delta x(t)$ 的积分，对上式分部积分：

$$
\begin{aligned}
\delta\bar T[x;\Delta x]
&=
\frac m\tau
\left[
\dot x(t)\Delta x(t)
\right]_0^\tau
\\
&\quad
-
\frac m\tau
\int_0^\tau
\ddot x(t)\Delta x(t)\,dt.
\end{aligned}
$$

端点固定，所以边界项为零：

$$
\left[
\dot x(t)\Delta x(t)
\right]_0^\tau
=0.
$$

于是

$$
\delta\bar T[x;\Delta x]
=
-
\frac m\tau
\int_0^\tau
\ddot x(t)\Delta x(t)\,dt.
$$

因此

$$
\frac{\delta\bar T[x]}{\delta x(t)}
=
-
\frac m\tau
\ddot x(t).
$$

负号来自分部积分。结果中出现加速度，是因为这里对位置轨迹求泛函导数，而平均动能依赖于位置轨迹的时间导数。

---

## 4. 作用量 $S$

### 4.1 牛顿定律的结果

对牛顿定律，左右同除以 $\tau$

$$
-\frac m\tau
\ddot x(t)
=
\frac1\tau
V'\bigl[x(t)\bigr].
$$

利用上一节的结果便得到

$$
\boxed{
\frac{\delta\bar T[x]}{\delta x(t)}
=
\frac{\delta\bar V[x]}{\delta x(t)}
}
$$

其中等式只在满足牛顿方程的经典轨迹上成立。

注意，这个等式不表示

$$
\bar T=\bar V.
$$

它只能表示：从经典轨迹出发，选取同一条允许的轨迹变化 $\Delta x(t)$ 时，平均动能和平均势能的一阶变分相等：

$$
\delta\bar T[x_{\mathrm{cl}};\Delta x]
=
\delta\bar V[x_{\mathrm{cl}};\Delta x].
$$

二者可能同时增加，也可能同时减少；等式只要求它们的一阶变化量相同。因而它们的差没有一阶变化：

$$
\delta
\bigl(
\bar T-\bar V
\bigr)
=0.
$$

### 4.2 拉格朗日量与作用量

由于上面的这个性质很特殊，我们把瞬时动能和势能之差定义为拉格朗日量：

$$
\boxed{
L(x,\dot x,t)
=
T(x,\dot x,t)-V(x,t)
}.
$$

对当前的一维粒子，

$$
L(x,\dot x)
=
\frac12m\dot x^2-V(x).
$$

拉格朗日量沿时间的积分定义为作用量：

$$
S[x]
=
\int_0^\tau
L\bigl[x(t),\dot x(t),t\bigr]\,dt.
$$

作用量的输入是一整条轨迹，所以 $S[x]$ 是泛函；它的量纲是能量乘时间（和普朗克常数同）。

利用平均能量的定义，

$$
S[x]
=
\tau
\bigl(
\bar T[x]-\bar V[x]
\bigr).
$$

所以在经典轨迹上，

$$
\begin{aligned}
\frac{\delta S[x]}{\delta x(t)}
&=
\tau
\left(
\frac{\delta\bar T[x]}{\delta x(t)}
-
\frac{\delta\bar V[x]}{\delta x(t)}
\right)
\\
&=0.
\end{aligned}
$$

这就是作用量所满足的条件，也叫作哈密顿原理：

$$
\boxed{
\left.
\frac{\delta S[x]}{\delta x(t)}
\right|_{x=x_{\mathrm{cl}}}
=0
}.
$$

泛函导数是关于时间的函数，而一阶变分是将它与具体的轨迹变化配对后得到的数。在经典轨迹上，

$$
\begin{aligned}
\delta S[x_{\mathrm{cl}};\Delta x]
&=
\int_0^\tau
\left.
\frac{\delta S[x]}{\delta x(t)}
\right|_{x=x_{\mathrm{cl}}}
\Delta x(t)\,dt
\\
&=
\int_0^\tau
0\cdot\Delta x(t)\,dt
\\
&=0.
\end{aligned}
$$

但是不要忘了我们还有二阶项，因此实际的作用量差一般不为零：

$$
\begin{aligned}
S[x_{\mathrm{cl}}+\Delta x]
-
S[x_{\mathrm{cl}}]
&=
\delta S[x_{\mathrm{cl}};\Delta x]
+
O(\Delta^2)
\\
&=
O(\Delta^2).
\end{aligned}
$$

我们可以选择牛顿方程作为基本原理（first principle），再推出作用量驻定；也可以选择 $\delta S = 0$ 作为基本原理，再推出运动方程。两种表述等价。

---

## 5. 欧拉-拉格朗日方程

下面选择 $\delta S = 0$ 作为基本原理，再推出运动方程。设一般拉格朗日量依赖于位置、速度和时间：

$$
L=L(x,\dot x,t).
$$

附近轨迹的作用量为

$$
S[x+\Delta x]
=
\int_0^\tau
L
\bigl(
x+\Delta x,
\dot x+\Delta\dot x,
t
\bigr)
dt.
$$

将被积函数展开到一阶：

$$
L
\bigl(
x+\Delta x,
\dot x+\Delta\dot x,
t
\bigr)=
L(x,\dot x,t)
+
\frac{\partial L}{\partial x}\Delta x
+
\frac{\partial L}{\partial\dot x}\Delta\dot x
+
O(\Delta^2).
$$

所以作用量的一阶变分为

$$
\delta S[x;\Delta x]
=
\int_0^\tau
\left(
\frac{\partial L}{\partial x}\Delta x
+
\frac{\partial L}{\partial\dot x}\Delta\dot x
\right)dt.
$$

对含有 $\Delta\dot x$ 的项分部积分：

$$
\int_0^\tau
\frac{\partial L}{\partial\dot x}
\Delta\dot x\,dt
=
\left[
\frac{\partial L}{\partial\dot x}
\Delta x
\right]_0^\tau
-
\int_0^\tau
\frac{d}{dt}
\left(
\frac{\partial L}{\partial\dot x}
\right)
\Delta x\,dt.
$$

由于端点固定，第一项消失。得出

$$
\boxed{
\delta S[x;\Delta x]
=
\int_0^\tau
\left[
\frac{\partial L}{\partial x}
-
\frac{d}{dt}
\left(
\frac{\partial L}{\partial\dot x}
\right)
\right]
\Delta x(t)\,dt
}.
$$

这时可以直接读出作用量的泛函导数：

$$
\frac{\delta S[x]}{\delta x(t)}
=
\frac{\partial L}{\partial x}
-
\frac{d}{dt}
\left(
\frac{\partial L}{\partial\dot x}
\right).
$$

根据刚刚推得的条件，上式为零，得到著名的欧拉-拉格朗日方程：

$$
\boxed{
\frac{d}{dt}
\left(
\frac{\partial L}{\partial\dot x}
\right)
-
\frac{\partial L}{\partial x}
=0
}.
$$

一个经典粒子的拉格朗日量可以写作：

$$
L
=
\frac12m\dot x^2-V(x),
$$

把

$$
\frac{\partial L}{\partial\dot x}
=
m\dot x,
\qquad
\frac{\partial L}{\partial x}
=
-V'(x).
$$

代入欧拉—拉格朗日方程：

$$
m\ddot x+V'(x)=0,
$$

得到牛顿第二定律。

---

## 6. 不那么经典的力学

### 6.1 拉格朗日密度

单个粒子的自由度由有限多个坐标描述；连续场则在空间的每一点都有一个自由度。例如一条弦的横向位移（偏离平衡位置的位移）可以写成

$$
\psi=\psi(x,t).
$$

此时普通拉格朗日量是空间各处贡献的总和，因此可以写成拉格朗日密度 $\mathcal L$ 的积分：

$$
L(t)
=
\int dx\,\mathcal L.
$$

作用量写作：

$$
S[\psi]
=
\int dt\,L(t)
=
\int dt\,dx\,\mathcal L.
$$

举个例子，对于弦的振动，设弦的线密度为 $\rho$，张力为 $T$。拉格朗日密度为

$$
\mathcal L
=
\frac{\rho}{2}
\left(
\frac{\partial\psi}{\partial t}
\right)^2
-
\frac{T}{2}
\left(
\frac{\partial\psi}{\partial x}
\right)^2.
$$

第一项是动能密度，第二项对应弦发生形变所储存的势能密度。对场作变分并在时间和空间上分部积分，可以得到场的欧拉-拉格朗日方程：

$$
\frac{\partial\mathcal L}{\partial\psi}
-
\frac{\partial}{\partial t}
\left[
\frac{\partial\mathcal L}
{\partial(\partial_t\psi)}
\right]
-
\frac{\partial}{\partial x}
\left[
\frac{\partial\mathcal L}
{\partial(\partial_x\psi)}
\right]
=0.
$$

对于上面的拉格朗日密度求下面这三个偏导

$$
\frac{\partial\mathcal L}{\partial\psi}=0,
$$

$$
\frac{\partial\mathcal L}
{\partial(\partial_t\psi)}
=
\rho\,\partial_t\psi,
$$

$$
\frac{\partial\mathcal L}
{\partial(\partial_x\psi)}
=
-T\,\partial_x\psi.
$$

然后代入上式，得到

$$
T\frac{\partial^2\psi}{\partial x^2}
-
\rho
\frac{\partial^2\psi}{\partial t^2}
=0.
$$

就是标准的波动方程：

$$
\frac{\partial^2\psi}{\partial t^2}
=
v^2
\frac{\partial^2\psi}{\partial x^2}.
$$

### 6.2 四维拉格朗日方程

把时间和三维空间统一写成四维时空坐标：

$$
x^\mu
=
(t,\mathbf x).
$$

闵氏度规定义为

$$
\eta_{\mu\nu}
=
\operatorname{diag}(1,-1,-1,-1).
$$

就可以把刚才的换成四维形式，把轨迹换成实标量场 $\phi(x)$，拉格朗日密度就依赖于场和它的一阶时空导数：

$$
\mathcal L
=
\mathcal L
\bigl(
\phi,\partial_\mu\phi
\bigr).
$$

作用量为

$$
S[\phi]
=
\int d^4x\,
\mathcal L
\bigl(
\phi,\partial_\mu\phi
\bigr).
$$

作用量的一阶变分为

$$
\delta S
=
\int d^4x
\left[
\frac{\partial\mathcal L}{\partial\phi}
-
\partial_\mu
\left(
\frac{\partial\mathcal L}
{\partial(\partial_\mu\phi)}
\right)
\right]
\Delta\phi.
$$

要求它对所有允许的 $\Delta\phi$ 都为零，得到四维欧拉—拉格朗日方程：

$$
\boxed{
\frac{\partial\mathcal L}{\partial\phi}
-
\partial_\mu
\left(
\frac{\partial\mathcal L}
{\partial(\partial_\mu\phi)}
\right)
=0
}.
$$

对照一下之前的拉格朗日方程：
$$
\frac{\partial L}{\partial x}
-
\frac{d}{dt}
\left(
\frac{\partial L}{\partial\dot x}
\right)
=
0.
$$
本质上就是做了如下推广：
$$
x(t)\longrightarrow\phi(x^\mu),
$$

$$
\dot x\longrightarrow\partial_\mu\phi,
$$

$$
\frac{d}{dt}\longrightarrow\partial_\mu,
$$

$$
\int dt\longrightarrow\int d^4x,
$$

$$
L\longrightarrow\mathcal L.
$$

---

又例如，考虑一种特定情形，我们会把拉格朗日密度取为

$$
\mathcal L
=
\frac12
\partial_\mu\phi\,
\partial^\mu\phi
-
\frac12m^2\phi^2.
$$

分别求偏导：

$$
\frac{\partial\mathcal L}{\partial\phi}
=
-m^2\phi,
$$

$$
\frac{\partial\mathcal L}
{\partial(\partial_\mu\phi)}
=
\partial^\mu\phi.
$$

代入四维欧拉—拉格朗日方程：

$$
-m^2\phi
-
\partial_\mu\partial^\mu\phi
=0.
$$

整理后可以得到一个**很著名的方程**。哈哈，故事结束！
$$
(\partial^2+m^2)\phi
=0.
$$
