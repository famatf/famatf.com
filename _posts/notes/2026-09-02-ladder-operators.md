---
title: 量子谐振子的升降算符
date: 2026-09-02
categories:
  - notes
  - physics
tags:
  - quantum-mechanics
  - second-quantization
permalink: /notes/ladder-operators.html
math: true
---

质量为 $m$、劲度系数为 $K$ 的一维谐振子满足 $\omega=\sqrt{K/m}$， $\hat H=\hat p^2/(2m)+m\omega^2\hat x^2/2$。定态薛定谔方程为

$$
\left(-\frac{\hbar^2}{2m}\frac{\mathrm d^2}{\mathrm dx^2}+\frac12m\omega^2x^2\right)\psi_n(x)=E_n\psi_n(x).
$$

令 $\xi=\sqrt{m\omega/\hbar}\,x$，归一化本征函数为

$$
\psi_n(x)=\frac{1}{\sqrt{2^n n!}}\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}H_n(\xi)e^{-\xi^2/2}.
$$

$H_n(\xi)$ 是厄米多项式。能级为 $E_n=(n+1/2)\hbar\omega$，其中 $n=0,1,2,\ldots$。即使处于基态，能量仍为 $E_0=\hbar\omega/2$。

下面引入升降算符求解。

由于 $[\hat x,\hat p]=i\hbar$，$\hat x$ 与 $\hat p$ 的次序不能随意交换。利用这一点可得（把  $\hat H=\hat p^2/(2m)+m\omega^2\hat x^2/2$ 因式分解）

$$
\hat H-\frac12\hbar\omega
=\frac12m\omega^2
\left(\hat x-\frac{i}{m\omega}\hat p\right)
\left(\hat x+\frac{i}{m\omega}\hat p\right).
$$

定义降（湮灭）算符和升（产生）算符：

$$
\begin{aligned}
\hat a&=\sqrt{\frac{m\omega}{2\hbar}}
\left(\hat x+\frac{i}{m\omega}\hat p\right),\\
\hat a^\dagger&=\sqrt{\frac{m\omega}{2\hbar}}
\left(\hat x-\frac{i}{m\omega}\hat p\right).
\end{aligned}
$$

满足 $[\hat a,\hat a^\dagger]=1$。反解出$\hat x$，$\hat p$：

$$
\begin{aligned}
\hat x&=\sqrt{\frac{\hbar}{2m\omega}}(\hat a+\hat a^\dagger),\\
\hat p&=i\sqrt{\frac{m\hbar\omega}{2}}(\hat a^\dagger-\hat a).
\end{aligned}
$$

$\hat H$ 化为 $\hat H=\hbar\omega(\hat a^\dagger\hat a+1/2)$。

对易关系：

$$
\begin{aligned}
{}[\hat a,\hat a^\dagger]
&=\frac{m\omega}{2\hbar}
\left[\hat x+\frac{i\hat p}{m\omega},
\hat x-\frac{i\hat p}{m\omega}\right]
=1,\\
\hat a^\dagger\hat a
&=\frac{\hat H}{\hbar\omega}-\frac12.
\end{aligned}
$$

定义粒子数算符 $\hat n=\hat a^\dagger\hat a$，则 $\hat H=\hbar\omega(\hat n+1/2)$，设 $\hat n\lvert n\rangle=n\lvert n\rangle$。由对易关系可得

$$
\begin{aligned}
\hat n\hat a^\dagger\lvert n\rangle
&=\hat a^\dagger(\hat n+1)\lvert n\rangle
=(n+1)\hat a^\dagger\lvert n\rangle,\\
\hat n\hat a\lvert n\rangle
&=\hat a(\hat n-1)\lvert n\rangle
=(n-1)\hat a\lvert n\rangle.
\end{aligned}
$$

因此，$\hat a^\dagger\lvert n\rangle$ 属于本征值 $n+1$，而 $\hat a\lvert n\rangle$ 属于本征值 $n-1$。

归一化系数由模长决定：$\lVert\hat a^\dagger\lvert n\rangle\rVert^2=n+1$，$\lVert\hat a\lvert n\rangle\rVert^2=n$。所以

$$
\begin{aligned}
\hat a^\dagger\lvert n\rangle&=\sqrt{n+1}\lvert n+1\rangle,\\
\hat a\lvert n\rangle&=\sqrt n\lvert n-1\rangle.
\end{aligned}
$$

因为 $\langle n\rvert\hat n\lvert n\rangle=\lVert\hat a\lvert n\rangle\rVert^2\geq0$，本征值不能为负。最低态记为 $\lvert 0\rangle$，并满足 $\hat a\lvert 0\rangle=0$。所有激发态都可以从基态产生：

$$
\lvert n\rangle=\frac{(\hat a^\dagger)^n}{\sqrt{n!}}\lvert 0\rangle.
$$

考虑含 $N$ 个相同质量点的一维单原子链模型，相邻质量点由劲度系数为 $K$ 的弹簧连接，并取周期性边界条件 $x_{j+N}=x_j$。哈密顿量为

$$
\hat H=\sum_{j=0}^{N-1}
\left[\frac{\hat p_j^2}{2m}+\frac K2(\hat x_{j+1}-\hat x_j)^2\right].
$$

由于势能中同时含有 $x_j$ 和 $x_{j+1}$，一个项中有两个粒子坐标的乘积，所以$x_j$ 不是独立振动的坐标。

在倒易空间中引入简正坐标 $\hat Q_k$ 和动量 $\hat P_k$：

$$
\begin{aligned}
\hat x_j&=\frac1{\sqrt N}\sum_k\hat Q_k e^{ikja},
&\hat Q_k&=\frac1{\sqrt N}\sum_j\hat x_j e^{-ikja},\\
\hat p_j&=\frac1{\sqrt N}\sum_k\hat P_k e^{ikja},
&\hat P_k&=\frac1{\sqrt N}\sum_j\hat p_j e^{-ikja}.
\end{aligned}
$$

周期边界条件给出 $k=2\pi n/(Na)$。通常只取第一布里渊区中的波矢 $k$。因为 $\hat x_j$、$\hat p_j$ 是厄米算符，所以 $\hat Q_k^\dagger=\hat Q_{-k}$、$\hat P_k^\dagger=\hat P_{-k}$。

正交关系为 $\sum_j e^{i(k+k')ja}=N\delta_{k,-k'}$，于是有

$$
\begin{aligned}
\sum_j\hat p_j^2&=\sum_k\hat P_k\hat P_{-k},\\
\sum_j(\hat x_{j+1}-\hat x_j)^2
&=\sum_k4\sin^2\left(\frac{ka}{2}\right)\hat Q_k\hat Q_{-k}.
\end{aligned}
$$

上式代回哈密顿量，得到
$$
\hat H=\sum_k
{}\left[{}\frac{\hat P_k\hat P_{-k}}{2m}
+\frac12m\omega_k^2\hat Q_k\hat Q_{-k}\right],
$$

其中

$$
\begin{aligned}
\omega_k^2&=\frac{4K}{m}\sin^2\left(\frac{ka}{2}\right),\\
\omega_k&=2\sqrt{\frac Km}\left\lvert\sin\left(\frac{ka}{2}\right)\right\rvert.
\end{aligned}
$$

引入简正坐标后，变换消除了不同 $k$ 之间的交叉项。对于 $k\neq0$，每个独立简正模式都可以量子化为一个频率为 $\omega_k$ 的谐振子。由于实空间位移为厄米算符，复数 Fourier 坐标满足 $Q_k^\dagger=Q_{-k}$，因此 $k$ 与 $-k$ 模式互为共轭。

$$
\begin{aligned}
\hat Q_k&=\sqrt{\frac{\hbar}{2m\omega_k}}
(\hat a_k+\hat a_{-k}^\dagger),\\
\hat P_k&=-i\sqrt{\frac{m\hbar\omega_k}{2}}
(\hat a_k-\hat a_{-k}^\dagger),\\
\hat H&=\frac{\hat P_0^2}{2m}
+\sum_{k\neq0}\hbar\omega_k
\left(\hat a_k^\dagger\hat a_k+\frac12\right).
\end{aligned}
$$

---

在通常的单粒子问题中，先固定粒子数，再写波函数 $\Psi(x_1,\ldots,x_N)$。占据数表象则先选一组单粒子态 $\lvert i\rangle$，然后只记录每个态中有多少粒子。所有允许粒子数的空间合在一起构成 Fock 空间：

$$
\mathcal F=\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2\oplus\cdots.
$$

当体系有许多独立模式时，用 $\lvert n_1,n_2,\ldots\rangle$ 表示各模式的占据数。对玻色子，$n_k=0,1,2,\ldots$，且

$$
\lvert n_1,n_2,\ldots\rangle
=\prod_k\frac{(\hat a_k^\dagger)^{n_k}}{\sqrt{n_k!}}\lvert 0\rangle.
$$

产生、湮灭算符只改变对应模式的占据数：

$$
\begin{aligned}
\hat a_k^\dagger\lvert\ldots,n_k,\ldots\rangle
&=\sqrt{n_k+1}\lvert\ldots,n_k+1,\ldots\rangle,\\
\hat a_k\lvert\ldots,n_k,\ldots\rangle
&=\sqrt{n_k}\lvert\ldots,n_k-1,\ldots\rangle.
\end{aligned}
$$

不同模式满足 $[\hat a_k,\hat a_q]=0$、$[\hat a_k^\dagger,\hat a_q^\dagger]=0$ 和 $[\hat a_k,\hat a_q^\dagger]=\delta_{kq}$。

每个模式的数算符和总数算符分别为 $\hat n_k=\hat a_k^\dagger\hat a_k$ 和 $\hat N=\sum_k\hat n_k$，并满足

$$
\begin{aligned}
\hat n_k\lvert n_1,n_2,\ldots\rangle
&=n_k\lvert n_1,n_2,\ldots\rangle,\\
\hat N\lvert n_1,n_2,\ldots\rangle
&=\left(\sum_kn_k\right)\lvert n_1,n_2,\ldots\rangle.
\end{aligned}
$$

设单粒子态标记为 $p$、单粒子能量为 $E_p$，则

$$
\hat H=\sum_pE_p\hat a_p^\dagger\hat a_p,
$$

并有 $\hat H\lvert n_{p_1},n_{p_2},\ldots\rangle=(\sum_p n_pE_p)\lvert n_{p_1},n_{p_2},\ldots\rangle$。

考虑两个全同粒子分别占据两个不同的单粒子态的情形。在两个不同单粒子态 $p_1,p_2$ 中各放入一个粒子，可以写成 $\hat a_{p_1}^\dagger\hat a_{p_2}^\dagger\lvert 0\rangle$。在三维空间中，连续交换两个全同粒子两次等价于不交换，因此交换本征值满足 $\lambda^2=1$，即 $\lambda=1$ 或 $\lambda=-1$。

玻色子在交换下对称，$\lambda=1$。满足

$$
\begin{aligned}
{}[\hat{a}_i,\hat{a}_j] &= 0,\\
[\hat{a}_i^\dagger,\hat{a}_j^\dagger] &= 0,\\
[\hat{a}_i,\hat{a}_j^\dagger] &= \delta_{ij}.
\end{aligned}
$$

费米子的多粒子态在交换下反对称，对应 $\lambda=-1$。用 $\hat c_i$、$\hat c_i^\dagger$ 表示费米算符，则

$$
\begin{aligned}
\{\hat c_i,\hat c_j\} & =0,\\
\{\hat c_i^\dagger,\hat c_j^\dagger\}&=0,\\
\{\hat c_i,\hat c_j^\dagger\}&=\delta_{ij}.
\end{aligned}
$$

令 $i=j$ 可得 $(\hat c_i^\dagger)^2=0$，所以同一个单粒子态的占据数只能是 $0$ 或 $1$。这就是泡利不相容原理在占据数表象中的形式。

在有限体积中，动量是离散的，右端使用 Kronecker 符号 $\delta_{pq}$。在连续极限中可选归一化，使玻色算符和费米算符分别满足

$$
[\hat a(\boldsymbol p),\hat a^\dagger(\boldsymbol q)]
=\delta^{(3)}(\boldsymbol p-\boldsymbol q),
$$

以及

$$
\{\hat c(\boldsymbol p),\hat c^\dagger(\boldsymbol q)\}
=\delta^{(3)}(\boldsymbol p-\boldsymbol q).
$$

---

在一维中，动量本征方程 $-i\hbar\,\mathrm d\psi_p/\mathrm dx=p\psi_p$ 给出 $\psi_p(x)=Ce^{ipx/\hbar}$。周期条件 $\psi_p(x+L)=\psi_p(x)$ 要求 $e^{ipL/\hbar}=1$，因此 $p=2\pi\hbar n/L$。

推广到边长为 $L$、体积为 $V=L^3$ 的三维周期性边界条件，动量取值为 $\boldsymbol p=2\pi\hbar\boldsymbol n/L$。平面波归一化为

$$
\begin{aligned}
\langle\boldsymbol x\rvert\boldsymbol p\rangle
&=\frac1{\sqrt V}e^{i\boldsymbol p\cdot\boldsymbol x/\hbar},\\
\langle\boldsymbol p\rvert\boldsymbol x\rangle
&=\frac1{\sqrt V}e^{-i\boldsymbol p\cdot\boldsymbol x/\hbar}.
\end{aligned}
$$

对任意态 $\lvert\alpha\rangle$，有

$$
\begin{aligned}
\widetilde\psi_\alpha(\boldsymbol p)
&=\frac1{\sqrt V}\int_V\mathrm d^3x\,
e^{-i\boldsymbol p\cdot\boldsymbol x/\hbar}
\psi_\alpha(\boldsymbol x),\\
\psi_\alpha(\boldsymbol x)
&=\frac1{\sqrt V}\sum_{\boldsymbol p}
e^{i\boldsymbol p\cdot\boldsymbol x/\hbar}
\widetilde\psi_\alpha(\boldsymbol p).
\end{aligned}
$$

正交完备关系为

$$
\begin{aligned}
\int_V\mathrm d^3x\,
e^{i(\boldsymbol p-\boldsymbol q)\cdot\boldsymbol x/\hbar}
&=V\delta_{\boldsymbol p\boldsymbol q},\\
\frac1V\sum_{\boldsymbol p}
e^{i\boldsymbol p\cdot(\boldsymbol x-\boldsymbol y)/\hbar}
&=\delta_V^{(3)}(\boldsymbol x-\boldsymbol y).
\end{aligned}
$$

令体积趋于无穷，可选

$$
\langle\boldsymbol x\rvert\boldsymbol p\rangle
=\frac1{(2\pi\hbar)^{3/2}}
e^{i\boldsymbol p\cdot\boldsymbol x/\hbar}.
$$

于是

$$
\begin{aligned}
\widetilde\psi_\alpha(\boldsymbol p)
&=\frac1{(2\pi\hbar)^{3/2}}
\int\mathrm d^3x\,
e^{-i\boldsymbol p\cdot\boldsymbol x/\hbar}
\psi_\alpha(\boldsymbol x),\\
\psi_\alpha(\boldsymbol x)
&=\frac1{(2\pi\hbar)^{3/2}}
\int\mathrm d^3p\,
e^{i\boldsymbol p\cdot\boldsymbol x/\hbar}
\widetilde\psi_\alpha(\boldsymbol p).
\end{aligned}
$$

动量本征态可写为 $\lvert\boldsymbol p\rangle=\hat a_{\boldsymbol p}^\dagger\lvert 0\rangle$。利用动量完备关系，位置本征态为

$$
\lvert\boldsymbol x\rangle
=\frac1{\sqrt V}\sum_{\boldsymbol p}
e^{-i\boldsymbol p\cdot\boldsymbol x/\hbar}
\lvert\boldsymbol p\rangle.
$$

定义箱归一化的场算符

$$
\begin{aligned}
\hat\psi(\boldsymbol x)
&=\frac1{\sqrt V}\sum_{\boldsymbol p}
e^{i\boldsymbol p\cdot\boldsymbol x/\hbar}
\hat a_{\boldsymbol p},\\
\hat\psi^\dagger(\boldsymbol x)
&=\frac1{\sqrt V}\sum_{\boldsymbol p}
e^{-i\boldsymbol p\cdot\boldsymbol x/\hbar}
\hat a_{\boldsymbol p}^\dagger.
\end{aligned}
$$

于是 $\hat\psi^\dagger(\boldsymbol x)\lvert 0\rangle=\lvert\boldsymbol x\rangle$。因此，$\hat a_{\boldsymbol p}^\dagger$ 在动量态中产生一个粒子，而 $\hat\psi^\dagger(\boldsymbol x)$ 在位置态中产生一个粒子；二者互为傅里叶变换。玻色场满足 $[\hat\psi(\boldsymbol x),\hat\psi^\dagger(\boldsymbol y)]=\delta_V^{(3)}(\boldsymbol x-\boldsymbol y)$；取无限体积极限后，右端变为 $\delta^{(3)}(\boldsymbol x-\boldsymbol y)$。费米场满足相应的反对易关系。场算符不是波函数。$\psi_\alpha(\boldsymbol x)=\langle\boldsymbol x\rvert\alpha\rangle$ 是复数函数，而 $\hat\psi(\boldsymbol x)$ 是作用在整个 Fock 空间上的算符，会使粒子数减少 $1$。

总粒子数算符可以在动量和位置表象中分别写成

$$
\hat N=\sum_{\boldsymbol p}\hat a_{\boldsymbol p}^\dagger\hat a_{\boldsymbol p}
=\int_V\mathrm d^3x\,
\hat\psi^\dagger(\boldsymbol x)\hat\psi(\boldsymbol x).
$$
