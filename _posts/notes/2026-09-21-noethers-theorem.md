---
title: Noether's Theorem and Spacetime Symmetries
date: 2026-09-21
categories:
  - notes
  - physics
tags:
  - quantum-field-theory
  - quantum-mechanics
permalink: /notes/noethers-theorem.html
math: true
---


This note is basically based on David Tong's lecture notes and Schwartz's textbook. I use $g_{\mu\nu}=\operatorname{diag}(1,-1,-1,-1)$ and $c=\hbar=1$. Repeated indices are summed. All transformations are kept to first order, and $\delta\phi_a$ denotes the variation at fixed $x$.

## Noether's theorem

This theorem reads:

Every continuous global symmetry of the action gives rise to a conserved current:
$$
\boxed{\partial_\mu j^\mu=0}
$$

when the equations of motion hold.

---
### Proof:

For a set of fields $\phi_a(x)$, the action is

$$
S=\int d^4x\,\mathcal L(\phi_a,\partial_\mu\phi_a).
$$

Consider an infinitesimal transformation

$$
\phi_a\longrightarrow\phi_a+\delta\phi_a,
\qquad
\delta\phi_a=\epsilon X_a,
\qquad
\partial_\mu\epsilon=0.
$$

Using the chain rule,

$$
\delta\mathcal L
=
\frac{\partial\mathcal L}{\partial\phi_a}\delta\phi_a
+
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
\partial_\mu(\delta\phi_a),
$$

where $\delta$ and $\partial_\mu$ commute.

Applying the product rule,

$$
\begin{aligned}
\delta\mathcal L
={}&
\left[
\frac{\partial\mathcal L}{\partial\phi_a}
-
\partial_\mu
\left(
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
\right)
\right]\delta\phi_a\\
&+
\partial_\mu
\left(
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
\delta\phi_a
\right).
\end{aligned}
$$

The fields satisfy the Euler–Lagrange 
equations:

$$
\frac{\partial\mathcal L}{\partial\phi_a}
-
\partial_\mu
\left(
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
\right)
=0.
$$

Therefore, on solutions,

$$
\delta\mathcal L
=
\partial_\mu
\left(
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
\delta\phi_a
\right).
$$

Independently, if the transformation is a symmetry, the Lagrangian density may change by a total divergence:

$$
\boxed{\delta\mathcal L=\partial_\mu F^\mu.}
$$

This symmetry condition is checked without using the equations of motion. It is allowed because

$$
\delta S
=
\int d^4x\,\partial_\mu F^\mu
=
\int_{\partial\Omega}d\Sigma_\mu\,F^\mu
$$

is only a boundary term. If the boundary integral vanishes, $\delta S=0$. Strict invariance of $\mathcal L$ corresponds to choosing $F^\mu=0$.

We now have two expressions for the same variation:

$$
\delta\mathcal L
=
\underbrace{
\partial_\mu
\left(
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
\delta\phi_a
\right)
}_{\text{Euler–Lagrange equations}}
=
\underbrace{\partial_\mu F^\mu}_{\text{symmetry}}.
$$

Subtracting,

$$
\partial_\mu
\left[
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
\delta\phi_a-F^\mu
\right]=0.
$$

Define the Noether current:

$$
j^\mu
\equiv
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
\delta\phi_a-F^\mu.
$$

Then

$$
\partial_\mu j^\mu=0.
$$


### Vanishing $\epsilon$

Since $\delta\phi_a=\epsilon X_a$, write $F^\mu=\epsilon K^\mu$. Thus,

$$
j^\mu
=
\epsilon
\left(
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
X_a-K^\mu
\right),
$$

and

$$
\epsilon\,\partial_\mu
\left(
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
X_a-K^\mu
\right)=0.
$$

Because $\epsilon$ is an arbitrary constant,

$$
\partial_\mu
\left(
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
X_a-K^\mu
\right)=0.
$$

So we can ignore $\epsilon$, $j^\mu$ includes the infinitesimal transformation parameters.

## Translations

Consider the infinitesimal translation

$$
x'^\nu=x^\nu-\epsilon^\nu,
\qquad
\partial_\mu\epsilon^\nu=0.
$$

Since $\phi'_a(x')=\phi_a(x)$,

$$
\phi'_a(x)
=
\phi_a(x+\epsilon)
=
\phi_a(x)+\epsilon^\nu\partial_\nu\phi_a(x).
$$

Therefore,

$$
\delta\phi_a=\epsilon^\nu\partial_\nu\phi_a.
$$

If $\mathcal L$ has no explicit dependence on $x$, similarly,

$$
\delta\mathcal L
=
\epsilon^\nu\partial_\nu\mathcal L.
$$

To express this as a divergence with index $\mu$,

$$
\begin{aligned}
\delta\mathcal L
&=
\epsilon^\nu\delta^\mu{}_\nu\partial_\mu\mathcal L\\
&=
\partial_\mu
\left(
\epsilon^\nu\delta^\mu{}_\nu\mathcal L
\right).
\end{aligned}
$$

We choose

$$
F^\mu=\epsilon^\nu\delta^\mu{}_\nu\mathcal L.
$$

Substitute into the Noether current:

$$
\begin{aligned}
j^\mu
&=
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
\delta\phi_a-F^\mu\\
&=
\epsilon^\nu
\left(
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
\partial_\nu\phi_a
-\delta^\mu{}_\nu\mathcal L
\right).
\end{aligned}
$$

Define the canonical energy–momentum tensor:

$$
T^\mu{}_\nu
\equiv
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
\partial_\nu\phi_a
-\delta^\mu{}_\nu\mathcal L.
$$

Then

$$
j^\mu=\epsilon^\nu T^\mu{}_\nu,
$$

so

$$
0=\partial_\mu j^\mu
=\epsilon^\nu\partial_\mu T^\mu{}_\nu.
$$

The four components of $\epsilon^\nu$ are independent. Their coefficients must vanish separately:

$$
\partial_\mu T^\mu{}_\nu=0,
\qquad \nu=0,1,2,3.
$$

We are comparing coefficients, not dividing by a vector. The index $\nu$ labels the four translation currents.

Raising the second index,

$$
T^{\mu\nu}
=
g^{\nu\rho}T^\mu{}_\rho
=
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}
\partial^\nu\phi_a
-g^{\mu\nu}\mathcal L,
$$

and

$$
\partial_\mu T^{\mu\nu}=0.
$$

The conserved four-momentum is

$$
P^\nu=\int d^3x\,T^{0\nu}.
$$

Indeed,
$$
\frac{dP^\nu}{dt}
=
-\int d^3x\,\partial_iT^{i\nu}
=
-\oint dS_i\,T^{i\nu}
=0,
$$

assuming that the boundary flux vanishes.

In particular,

$$
E=P^0=\int d^3x\,T^{00},
\qquad
P^i=\int d^3x\,T^{0i}.
$$

### Example: the real Klein–Gordon field

The Lagrangian density is

$$
\mathcal L
=
\frac12g^{\alpha\beta}
\partial_\alpha\phi\,\partial_\beta\phi
-\frac12m^2\phi^2.
$$

Then

$$
\begin{aligned}
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}
&=
\frac12g^{\alpha\beta}
\left(
\delta^\mu{}_\alpha\partial_\beta\phi
+
\partial_\alpha\phi\,\delta^\mu{}_\beta
\right)\\
&=g^{\mu\nu}\partial_\nu\phi
=\partial^\mu\phi.
\end{aligned}
$$

Hence,

$$
T^{\mu\nu}
=
\partial^\mu\phi\,\partial^\nu\phi
-g^{\mu\nu}\mathcal L.
$$

For this field, 
$T^{\mu\nu}=T^{\nu\mu}$, and

$$
T^{00}
=
\frac12\dot\phi^{\,2}
+\frac12(\nabla\phi)^2
+\frac12m^2\phi^2.
$$


## Lorentz transformations

Here we consider a scalar field with a Lorentz-invariant Lagrangian, such as the Klein–Gordon field.

An infinitesimal Lorentz transformation is

$$
x'^\mu=\Lambda^\mu{}_\nu x^\nu,
\qquad
\Lambda^\mu{}_\nu=\delta^\mu{}_\nu+\omega^\mu{}_\nu,
$$

where $\omega^\mu{}_\nu$ is infinitesimal and constant.

The Lorentz condition is

$$
\Lambda^\mu{}_\rho g^{\rho\sigma}
\Lambda^\nu{}_\sigma=g^{\mu\nu}.
$$

Expanding to first order,

$$
g^{\mu\nu}+\omega^{\mu\nu}+\omega^{\nu\mu}
=g^{\mu\nu}.
$$

Thus,

$$
\omega^{\mu\nu}=-\omega^{\nu\mu},
\qquad
\omega_{\mu\nu}=-\omega_{\nu\mu}.
$$

In particular,

$$
\omega^\mu{}_\mu=g^{\mu\rho}\omega_{\rho\mu}=0.
$$

For a scalar field,

$$
\phi'(x)=\phi(\Lambda^{-1}x).
$$

Since $\Lambda^{-1}=I-\omega$ to first order,

$$
\phi'(x)
=
\phi(x)-\omega^\rho{}_\sigma x^\sigma\partial_\rho\phi(x).
$$

Therefore,

$$
\delta\phi=-\omega^\rho{}_\sigma x^\sigma\partial_\rho\phi.
$$

Similarly,

$$
\delta\mathcal L
=
-\omega^\mu{}_\nu x^\nu\partial_\mu\mathcal L.
$$

Using the product rule,

$$
\begin{aligned}
\delta\mathcal L
&=
-\partial_\mu
\left(\omega^\mu{}_\nu x^\nu\mathcal L\right)
+\omega^\mu{}_\nu(\partial_\mu x^\nu)\mathcal L\\
&=
-\partial_\mu
\left(\omega^\mu{}_\nu x^\nu\mathcal L\right)
+\omega^\mu{}_\mu\mathcal L\\
&=
-\partial_\mu
\left(\omega^\mu{}_\nu x^\nu\mathcal L\right).
\end{aligned}
$$

Thus, we may choose

$$
F^\mu=-\omega^\mu{}_\nu x^\nu\mathcal L.
$$

Substitute into the Noether current:

$$
\begin{aligned}
j^\mu
&=
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}
\delta\phi-F^\mu\\
&=
-\omega^\rho{}_\sigma x^\sigma
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}
\partial_\rho\phi
+\omega^\mu{}_\sigma x^\sigma\mathcal L\\
&=
-\omega^\rho{}_\sigma x^\sigma
\left(
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}
\partial_\rho\phi
-\delta^\mu{}_\rho\mathcal L
\right)\\
&=
-\omega^\rho{}_\sigma x^\sigma T^\mu{}_\rho\\
&=
-\omega_{\rho\sigma}x^\sigma T^{\mu\rho}.
\end{aligned}
$$

Interchanging the dummy indices and using antisymmetry,

$$
-\omega_{\rho\sigma}x^\sigma T^{\mu\rho}
=
\omega_{\rho\sigma}x^\rho T^{\mu\sigma}.
$$

Averaging these two forms gives

$$
j^\mu
=
\frac12\omega_{\rho\sigma}
\left(
x^\rho T^{\mu\sigma}-x^\sigma T^{\mu\rho}
\right).
$$

Define

$$
J^{\mu\rho\sigma}
\equiv
x^\rho T^{\mu\sigma}-x^\sigma T^{\mu\rho}.
$$

Then
$$
j^\mu=\frac12\omega_{\rho\sigma}J^{\mu\rho\sigma},
\qquad
J^{\mu\rho\sigma}=-J^{\mu\sigma\rho}.
$$

The factor $1/2$ avoids counting each antisymmetric pair twice:

$$
j^\mu
=
\sum_{\rho<\sigma}\omega_{\rho\sigma}J^{\mu\rho\sigma}.
$$

Since $\partial_\mu j^\mu=0$,

$$
\sum_{\rho<\sigma}
\omega_{\rho\sigma}\partial_\mu J^{\mu\rho\sigma}=0.
$$

There are six independent parameters,

$$
\omega_{01},\ \omega_{02},\ \omega_{03},\
\omega_{12},\ \omega_{13},\ \omega_{23}.
$$

Their coefficients vanish separately:

$$
\partial_\mu J^{\mu\rho\sigma}=0,
\qquad \rho<\sigma.
$$

The index $\mu$ is the current index, while the pair $(\rho,\sigma)$ labels the six Lorentz currents. Antisymmetry leaves

$$
4\times 6=24
$$

component slots: six four-component currents. Contracting $\mu$ in the divergence gives six conservation equations.

The conserved charges are

$$
Q^{\rho\sigma}
=
\int d^3x\,J^{0\rho\sigma}
=
\int d^3x
\left(
x^\rho T^{0\sigma}-x^\sigma T^{0\rho}
\right),
$$

again assuming vanishing boundary fluxes.

For spatial rotations,

$$
Q^{ij}
=
\int d^3x
\left(
x^iT^{0j}-x^jT^{0i}
\right).
$$

These are the angular-momentum components:

$$
L^1=Q^{23},
\qquad
L^2=Q^{31},
\qquad
L^3=Q^{12}.
$$

The other three charges correspond to boosts:

$$
Q^{0i}
=
tP^i-\int d^3x\,x^iT^{00}.
$$

For the Klein–Gordon field, we can check conservation directly:

$$
\begin{aligned}
\partial_\mu J^{\mu\rho\sigma}
&=
T^{\rho\sigma}-T^{\sigma\rho}
+x^\rho\partial_\mu T^{\mu\sigma}
-x^\sigma\partial_\mu T^{\mu\rho}\\
&=0,
\end{aligned}
$$

using $T^{\rho\sigma}=T^{\sigma\rho}$ and $\partial_\mu T^{\mu\nu}=0$.

For vector or spinor fields, the canonical Lorentz current generally also includes a spin term. The expression above is the scalar-field result.