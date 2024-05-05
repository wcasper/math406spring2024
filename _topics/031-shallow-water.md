---
layout: page
title: Shallow Water Equations
---

So far, the linear theory of second-order partial differential equations, in particular in the case of constant coefficients, has been shown to be well-understood.




The **one dimensional shallow water equations** are given by

$$\begin{align}
h_t + ((H+h)u)_x &= 0,\\
u_t + uu_x &= -gh_x, 
\end{align}$$

which we can rewrite as

$$
\left[\begin{array}{cc}
H+h & u\\
u   & g
\end{array}\right]\binom{u_x}{h_x} + 
\left[\begin{array}{cc}
1 & 0\\
0 & 1
\end{array}\right]\binom{u_t}{h_t}
 = \binom{0}{0}.
$$

We imagine a solution $$u(x,t)$$ and $$h(x,t)$$, which is defined implicitly by a system of equations of the form

$$\begin{align}
\vec\psi = \vec C,\quad\text{or equiv.}\quad \binom{\psi_1}{\psi_2} = \binom{C_1}{C_2}.
\end{align}$$

Then performing implicit partial differenttition, treating $$h$$ and $$u$$ as functions of $$x$$ and $$t$$, we obtain the relations

$$\begin{align}
\vec\psi_x + \vec\psi_u u_x + \vec\psi_h h_x & = 0,\\
\vec\psi_t + \vec\psi_u u_t + \vec\psi_h h_t & = 0.
\end{align}$$

Therefore if we let 

$$Q = [\vec\psi_u\ \ \vec \psi_h]$$

be the $$2\times 2$$ matrix whose columns are $$\vec\psi_u$$ and $$\vec \psi_h$$, then
the above equations can be expressed as

$$\vec\psi_x + Q\binom{u_x}{h_x}=0,\quad\vec\psi_t + Q\binom{u_t}{h_t}=0.$$

Using this, the one-dimensional shallow water equations can be reexpressed as

$$
Q\left[\begin{array}{cc}
H+h & u\\
u   & g
\end{array}\right]Q^{-1}\vec\psi_x + 
\vec \psi_t
= \binom{0}{0}.
$$

If we diagonalize by taking

$$Q =
\left[\begin{array}{cc}
H+h-g + \sqrt{(H+h+g)^2+4u^2 & 2u\\
2u & g-H-h - \sqrt{(H+h+g)^2+4u^2
\end{array}\right],
$$

then the one-dimensional shallow water equations become

$$
\frac{1}{2}(H+h+g+\sqrt{(H+h+g)^2+4u^2})\psi_{1x} + \psi_{1t} &= 0,\\
\frac{1}{2}(H+h+g-\sqrt{(H+h+g)^2+4u^2})\psi_{2x} + \psi_{2t} &= 0.
$$

The eigenvalues of this matrix are










