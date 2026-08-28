---
title: 群的不可约表示
date: 2026-06-06
categories:
  - notes
  - physics
tags:
  - symmetry
  - group-theory
permalink: /notes/irrep.html
math: true
---

## 总结

* 正交定理： $\boxed{\sum_{R\in G}[D^i(R)_{\mu\nu}]^*D^j(R)_{\mu'\nu'}=\frac{g}{m_i}\delta_{ij}\delta_{\mu\mu'}\delta_{\nu\nu'}}$
* 所有不等价不可约表示的维数的平方和不大于群的阶： $\boxed{\sum_i m_i^2 \le g}$
* 特征标正交关系： $\boxed{\chi^i(R)=\operatorname{Tr}D^i(R)=\sum_\mu D^i(R)_{\mu\mu}}$
* 所有不等价不可约表示个数不大于共轭类个数 $\boxed{\sum_i 1 \le g_c}$
* 两表示等价 $\iff$ 特征标相同
* $\sum_{R\in G}[\chi(R)]^*\chi(R)=g \Longrightarrow$ 不可约表示
* 所有一维表示均不可约，因为 $|\chi(R)|=1$
* 非恒等的不可约表示，根据正交关系，$\sum_R \chi(R)=0$

---

### 不可约表示

设 $D(G)=\{D(R)\}$ 是群 $G$ 在 $n$ 维表示空间 $V_n$ 上的一个表示。如果 $V_n$ 中不存在关于群 $G$ 的非平庸不变子空间 $V_m$，其中 $m<n$ ，那么 $D(G)$ 就是不可约表示。

不变子空间即，对任意 $R\in G$ ，都有 $D(R)V_m\subset V_m$ ，也就是说，群元作用以后，子空间里的矢量不会跑出这个子空间。不存在这样的 $V_m$，表示就是不可约表示。只能在 $V$ 中找到零空间。


对于有限群，若表示可约，则完全可约，也就是可以通过同一个相似变换矩阵 $X$ 化为若干不可约表示的直和：

$$
X^{-1}D(R)X=\bigoplus_j a_jD^j(R)
$$

其中 $a_j$ 是不可约表示 $D^j(R)$ 在 $D(R)$ 中出现的次数，叫重数。

不可约表示不是说每一个 $D(R)$ 单独都不能块对角化，而是说不能用同一个 $X$ 让所有 $D(R)$ 同时块对角化。不排除个别群元在不可约表示中的表示矩阵具有分块对角的形式。

---

## 定理与重要结论

### Schur's Lemma I

设 $D(G)$ 是不可约表示。如果一个非零矩阵 $X$ 满足 $XD(R)=D(R)X, \forall R\in G$ ，那么 $X$ 必为常数矩阵：

$$
X=cI
=
\begin{pmatrix}
c & & \\
& \ddots & \\
& & c \\
\end{pmatrix}
$$

---

说明：

给出一个不可约表示的所有矩阵，找到一个矩阵 $X$ 与它们全部对易，那么 $X$ 就只能为 $cI$ ，强调的是唯一性。 $cI$ 与任意矩阵对易本身是trivial的。

例如， $D_3$ 的二维表示中，

$$
D(r) =
\begin{pmatrix}
    0&-1 \\
    1&0 \\
\end{pmatrix},
D(s) =
\begin{pmatrix}
    1&0\\
    0&-1\\
\end{pmatrix}
$$

若要找一个矩阵只和 $D(r)$ 对易，那么满足 $A=\mathrm{diag}(a,d)$ 即可。但是还要与 $D(s)$ 对易，就必须使得 $a=d$ ，从而满足Schur引理。

---

### Schur's Lemma II

设 $D^i(G)=\{D^i(R)\}$ 和 $D^j(G)=\{D^j(R)\}$ 是群 $G=\{R\}$ 的两个不等价不可约表示，维数分别为 $d_i$ 和 $d_j$。如果 $d_i \times d_j$ 矩阵 $X$ 满足 $D^i(R)X=XD^j(R), \forall R\in G$，那么 $X=0$。

也就是说，如果两个变换是等价的，那么可以通过相似变换 $D'(R)=X^{-1}D(R)X$ 联系在一起，现在既然不是等价的，也不是可约的，就不能这么做，维数也不满足矩阵的乘法条件。因此，就把 $X$ 乘到左边，因此只能有 $X=0$ 。


---

### Great Orthogonality Theorem

Schur引理的推论。

设群 $G$ 的阶为 $g$ ，两个不等价不可约幺正表示为 $D^i(G), D^j(G)$ ,维数分别为 $m_i, m_j$ ，

则矩阵元满足：

$$
\sum_{R\in G}
[D^i(R)_{\mu\nu}]^*
D^j(R)_{\mu'\nu'}
=
\frac{g}{m_i}
\delta_{ij}\delta_{\mu\mu'}\delta_{\nu\nu'}
$$

这就是正交定理。

这里可以把每个矩阵元

$$
D^i(R)_{\mu\nu}
$$

看成一个关于群元 $R$ 的群函数。所以它等价于一个 $g$ 维向量：

$$
\begin{pmatrix}
D^i(R_1)_{\mu\nu},
D^i(R_2)_{\mu\nu},
\dots,
D^i(R_g)_{\mu\nu}
\end{pmatrix}
$$

正交定理就是说：不同不可约表示、不同矩阵元，对应的这些 $g$ 维向量彼此正交，也就是：

$$
\begin{pmatrix}
D^i(R_1)_{\mu\nu},
D^i(R_2)_{\mu\nu},
\dots,
D^i(R_g)_{\mu\nu}
\end{pmatrix}^*
\begin{pmatrix}
D^j(R_1)_{\mu\nu}\\
D^j(R_2)_{\mu\nu}\\
\vdots\\
D^j(R_g)_{\mu\nu}\\
\end{pmatrix}
=
\frac{g}{m_i}\delta_{ij}\delta_{\mu\mu'}\delta_{\nu\nu'}
$$

---

### GOT 推论 1 ：维数平方和不大于群的阶

一个 $m_i$ 维不可约表示 $D^i(G)$ 有 $m_i^2$ 个矩阵元：

$$
D^i(R)_{\mu\nu},\qquad \mu,\nu=1,\dots,m_i
$$

每一个矩阵元都给出一个群空间矢量，也就是把这些矩阵元当作空间的基矢。正交定理说明这些矢量彼此正交，所以它们线性无关。群空间维数是群的阶 $g$ ，因此所有不等价不可约表示提供的线性无关矢量总数不能超过 $g$：

$$
\sum_i m_i^2\le g
$$

加入完备性条件可得：

$$
\sum_i m_i^2=g
$$

---

### GOT 推论 2 ：不可约表示的特征标正交

正交定理，令 $\mu=\nu,\mu'=\nu'$ ，再对 $\mu,\mu'$ 求和，就得到特征标正交关系：

$$
\sum_{R\in G}
[\chi^i(R)]^*
\chi^j(R)
=
g\delta_{ij}
$$

特征标就是表示矩阵的trace，

$$
\chi^i(R)=\operatorname{Tr}D^i(R)
=\sum_\mu D^i(R)_{\mu\mu}
$$

也就是把 $\chi^i(R)$ 看作群空间的基矢，是正交的。


除恒等表示外，有限群任何不可约表示的特征标对群元求和都等于零。
恒等表示的特征标是 $\chi^i(R)\equiv 1$ ，若 $\chi^j(R)$ 是任意非恒等不可约表示的特征标，则 $i\ne j$。由特征标正交关系：

$$
\sum_{R\in G}
[\chi^i(R)]^*
\chi^j(R)
=
g\delta_{ij}=0
$$

因为 $\chi^i(R)=1$ ，所以 $\sum_{R\in G}\chi^j(R)=0$ 。


---

### GOT 推论 3 ：不等价不可约表示个数不大于共轭类个数

有限群不等价不可约表示的个数不能大于群的类的个数 $g_c$ ，即：

$$
\sum_i 1 \le g_c
$$

由于特征标是类函数，同一共轭类中的元素特征标相同。若第 $\alpha$ 类中任一元素的特征标为 $\chi_\alpha^i$ ，则对第 $i$ 个不可约表示，构造特征标矢量：

$$
V_i=\sum_{R\in G}\chi^i(R)R
$$

因为同一类中的元素特征标相同，所以可以把它按类合并，把 $V_i$ 写成类矢量 $L_\alpha$ 的展开：

$$
V_i
=
\sum_{\alpha=1}^{g_c}\chi_\alpha^i L_\alpha
$$

其中 $L_\alpha=R+R'+\dots$ 表示第 $\alpha$ 个类中所有群元的和。

因此，$V_i$ 不只是群空间中的矢量，也是类空间中的矢量。类空间的基可以取为 $L_1,L_2,\dots,L_{g_c}$ ，于是类空间的维数为 $g_c$ 。

另一方面，由特征标正交关系：

$$
\sum_{R\in G}[\chi^i(R)]^*\chi^j(R)=g\delta_{ij}
$$

可知不同不可约表示对应的特征标矢量 $V_i$ 彼此正交。正交的矢量必定线性无关，一个不可约表示 $D^i(G)$ 提供一个特征标矢量 $V_i$ 。如果不等价不可约表示有很多个，就会提供同样多个线性无关的 $V_i$ 。

$V_i$ 全部都在 $g_c$ 维类空间里，所以它们的个数不能超过类空间维数，也就是：不等价不可约表示个数 $\le g_c$

$$
\sum_i 1\le g_c
$$

---

总结：

$$
\chi^i(R)\text{ 是类函数}
\Rightarrow
V_i=\sum_\alpha \chi_\alpha^i L_\alpha
$$

所以 $V_i$ 属于 $g_c$ 维类空间。

又因为

$$
\sum_R[\chi^i(R)]^*\chi^j(R)=g\delta_{ij}
$$

所以不同 $V_i$ 正交，因而线性无关。

---

### 两个表示等价和特征标完全相同是充要条件

有限群的任意表示是完全可约表示：

$$
X^{-1}D(R)X=\bigoplus_j a_jD^j(R)
$$

取trace，因为取trace后乘法顺序可以调换，就得到

$$
\chi(R)=\sum_j a_j\chi^j(R)
$$

都乘以 $[\chi^i(R)]^*$ ，并对 $R$ 求和， 然后代入正交关系 $\sum_{R\in G}[\chi^i(R)]^*\chi^j(R)=g\delta_{ij}$ ，可以求出重数 $a_j$ ,

$$
a_j=
\frac{1}{g}
\sum_R
[\chi^j(R)]^*
\chi(R)
$$

$a_j$ 完全由特征标决定。所以如果两个表示 $D(R)$ 和 $D'(R)$ 的特征标相同：

$$
\chi(R)=\chi'(R),\qquad \forall R\in G
$$

那么它们分解成不可约表示时，每个不可约表示的重数都相同，所以两个表示等价。

反过来，如果两个表示等价：

$$
D'(R)=X^{-1}D(R)X
$$

那么相似变换不改变迹，所以 $\chi'(R)=\chi(R)$ ，于是：

$$
D(R)\simeq D'(R)
\iff
\chi(R)=\chi'(R),\ \forall R\in G
$$

---

### 用特征标判断表示是否可约


$$
\sum_R\chi^*(R)\chi(R)=g
\Rightarrow D(R)\text{ 不可约}
$$

$$
\sum_R\chi^*(R)\chi(R)>g
\Rightarrow D(R)\text{ 可约}
$$

例如 $D_3$ 的某个二维表示特征标为

$$
\chi(E)=2,\qquad
\chi(D)=\chi(F)=-1,\qquad
\chi(A)=\chi(B)=\chi(C)=0
$$

所以

$$
\sum_R\chi^*(R)\chi(R)
=
2^2+(-1)^2+(-1)^2+0^2+0^2+0^2
=6
$$

而 $D_3$ 的阶为

$$
g=6
$$

所以这个二维表示是不可约表示。

如果某个三维表示满足

$$
\sum_R\chi^*(R)\chi(R)=12>6
$$

它就是可约表示。事实上，所有三维表示都是可约的。根据推论1，维数平方和不大于群的阶， $D_3$ 群有 $6$ 个群元，所以最高维数的不可约表示为二维表示。
