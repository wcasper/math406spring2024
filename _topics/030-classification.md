---
layout: page
title: Classification of PDEs
---

Our course has emphasized solving the three classical PDEs: the heat equation, Poisson's equation, and the wave equation.
Each of these represents a certain type or characteristic of PDE that we can fit all second-order PDEs with constant coefficients into.
In particular, all PDEs break down into three classes:
* elliptic, like Poisson's equation
* parabolic (or diffusive), like the heat equation
* hyperbolic, like the wave equation

The classes themselves feature certain properties which are characteristic of their type.
For example, elliptic PDEs should feature some type of mean value property, extreme value theorem, and Harnack-type inequality
Parabolic PDEs feature smoothing, Gaussian-like properties and infinite propogation speeds, and decay on the order of $$t^{-n/2}$$ (for $$n$$ the physical dimension).
Hyperbolic PDEs feature *finite* propogation speed and some flavor of conservation of energy.

So if we are faced with a "wild" PDE, such as

$$u_{tt} - 4u_{xt} + 2u_{xx} = 0,$$

if we can classify it, we will be able to start to understand qualitative behavior of solutions or even how to solve it in general.
The secret to classification is to impose a linear coordinate transformation

$$
\widetilde x = ax + bt,\ \ \ 
\widetilde t = cx + dt,\ \ \ 
$$

where here $$a,b,c,d\in\mathbb{R}$$.
Under this transformation

$$\begin{align}
\frac{\partial}{\partial x}
  & = \frac{\partial \widetilde x}{\partial x}\frac{\partial}{\partial \widetilde x} + \frac{\partial \widetilde t}{\partial x}\frac{\partial}{\partial \widetilde t}\\
  & = a\frac{\partial}{\partial \widetilde x} + c\frac{\partial}{\partial \widetilde t}
\frac{\partial}{\partial t}
  & = \frac{\partial \widetilde x}{\partial t}\frac{\partial}{\partial \widetilde x} + \frac{\partial \widetilde t}{\partial t}\frac{\partial}{\partial \widetilde t}\\
  & = b\frac{\partial}{\partial \widetilde x} + d\frac{\partial}{\partial \widetilde t}
\end{align}$$

so that 

$$\begin{align}
\frac{\partial^2}{\partial x^2} &= a^2\frac{\partial^2}{\partial \widetilde x^2} + 2ac\frac{\partial^2}{\partial \widetilde x \partial \widetilde t} + c^2\frac{\partial^2}{\partial \widetilde t^2},\\
\frac{\partial^2}{\partial x\partial t} &= ab\frac{\partial^2}{\partial \widetilde x^2} + (ad+bc)\frac{\partial^2}{\partial \widetilde x \partial \widetilde t} + cd\frac{\partial^2}{\partial \widetilde t^2},\\
\frac{\partial^2}{\partial t^2} &= b^2\frac{\partial^2}{\partial \widetilde x^2} + 2bd\frac{\partial^2}{\partial \widetilde x \partial \widetilde t} + d^2\frac{\partial^2}{\partial \widetilde t^2}.
\end{align}$$

The previous equation then becomes

$$
b^2u_{\widetilde x\widetilde x} + 2bdu_{\widetilde x\widetilde t} + d^2u_{\widetilde t\widetilde t}
- 4(abu_{\widetilde x\widetilde x} + (ad+bc)u_{\widetilde x\widetilde t} + cdu_{\widetilde t\widetilde t})
+ 2(a^2u_{\widetilde x\widetilde x} + 2acu_{\widetilde x\widetilde t} + c^2u_{\widetilde t\widetilde t})
= 0
$$

which we rewrite as

$$(b^2-4ab+2a^2)u_{\widetilde x\widetilde x} + (2bd-4ad-4bc+4ac)u_{\widetilde x\widetilde t} + (d^2-4cd+2c^2)u_{\widetilde t\widetilde t} =0.$$

Then if we take $$d = 0$$, $$c=1/\sqrt{2}$$, and $$a=b=1$$, this results in the usual wave equation

$$ u_{\widetilde t\widetilde t} = u_{\widetilde x\widetilde x}.$$

Thus we would expect to classify this equation as hyperbolic, and its solutions will be an affine transformation of solutions to the one dimensional wave equation.
More generally, we have the following definition

**Definition:**  Let $$u(x_0,x_1,\dots, x_n)$$ be a function of $$n+1$$ variables and let $$(A_{jk})$$ be an $$(n+1)\times (n+1)$$ symmetric matrix, $$\vec b = (b_j)$$ a vector, and $$c$$ real numbers.
Consider the generic second order PDE with constant coefficients

$$\sum_{j,k=0}^n A_{jk} u_{x_jx_k} + \sum_{j=1}^n b_j u_{x_j} + cu = 0.$$

Under **Hadamard's classification**, the equation is called
* **ellipic** if all of the eigenvalues of $$A$$ are nonzero and have the same sign
* **hyperbolic** if all but one of the eigenvalues of $$A$$ are nonzero and have the same sign
* **parabolic** if all the eigenvalues of $$A$$ are nonzero and have the same sign, except for one which is zero
* **ultrahyperbolic** if all of the eigenvalues of $$A$$ are nonzero, and there are at least two positive and two negative ones

:warning: some authors use parabolic for whenever there is *any* number of zero eigenvalues.

We can do the change of coordinates 

$$\vec y = T\vec x,$$

from which 

$$\frac{\partial}{\partial x_j} = \sum_{a=0}^n \frac{\partial y_a}{\partial x_j}\frac{\partial }{\partial y_a} = \sum_{a=0}^n T_{aj}\frac{\partial }{\partial y_a}.$$

and

$$\frac{\partial^2}{\partial x_j\partial x_k} = \sum_{a,b=0}^n T_{aj}T_{bk} \frac{\partial^2 }{\partial y_ay_b}$$

Thus the original PDE becomes

$$\sum_{a,b=0}^n\sum_{j,k=0}^n A_{jk}T_{aj}T_{bk}u_{y_ay_b} + \sum_{j=0}^n b_jT_{aj} u_{y_a} + Cu = 0.$$

This can be rewritten as

$$\sum_{a,b=0}^n (TAT^t)_{ab} u_{y_ay_b}  + \sum_{a=0}^n (T\vec b)_a u_{y_a} + Cu =0

If we take $$Q$$ to be a matrix whose columns form an orthonormal basis of eigenvectors of $$A$$ and

$$\Lambda = \text{diag}(\lambda_0,\lambda_1,\dots,\lambda_n)$$

to be the associated diagonal matrix of eigenvalues, then letting

$$T^t = Q\text{diag}(\lvert\lambda_0\rvert^{-1/2},\lvert\lambda_1\rvert^{-1/2},\dots,\lvert\lambda_n\rvert^{-1/2})$$

we get

$$\sum_{a=0}^n (\text{sign}(\lambda_a) u_{y_ay_a}  + (T\vec b)_a u_{y_a}) + Cu =0,$$

where here $$\text{sign}(x)$$ is $$\pm 1$$ or $$0$$, depending on whether $$x$$ is positive or negative or zero$$.


### Additional sources

* this lecture has a recording

{% include youtube.html id="MbfDTK1wmuc;" %}


