---
layout: page
title: Practice Exam 2 Solutions
permalink: /exams/practice-exam2-soln
---

### Directions
Solve the following problems and type up your solutions.  
In the actual exam, you will be allowed scratch paper and a pencil, but no calculator or note sheet.


**Problem 1:** 

* (A) Show that if $$u(x,y)$$ is harmonic everywhere in $$\mathbb{R}^2$$ and bounded below, then $$u$$ is constant.
* (B) Show that the statement is false when we allow $$u(x,y)$$ to be unbounded.

**Solution:**

* (A) Check out Liouville's Theorem from Homework 3.
* (B) The function $$u(x,y) = x$$ is harmonic, but is unbounded

**Problem 2:** 

Consider the quarter disk (in polar coordinates) $$\Omega = \{(r,\theta): 0 < r < R,\ \ 0 < \theta < \pi/2\}$$.
Find a solution to Laplace's equation 

$$\Delta u = 0,\ \ (r,\theta)\in \Omega$$

with the boundary conditions

$$u(r,0) = 0,\ \ 0 < r < R,\ \ u(r,\pi/2) = 0,\ \ 0 < r < R,\ \ u(R,\theta) = \sin(2\theta).$$

**Solution:**

Using separation of variables, we get solutions of the form

$$u(r,\theta) =  Ar^\lambda\cos(\lambda \theta)) + Br^\lambda(\sin(\lambda \theta).$$

for some $$\lambda\in\mathbb{R}$$.
When we had the periodic boundary condition, we got that $$\lambda\in\mathbb{Z}$$.
In this case, our bouondary condition is different.
Instead, we want $$u(r,\theta)$$ to satisfy $$u(r,0) = 0$$ and $$u(r,\pi/2) = 0$$.
This forces $$A = 0$$ and $$\lambda = 2 n$$, so that we get solutions of the form

$$u(r,\theta) =  Br^{2 n} \sin(2 n\theta).$$

In fact, by the superposition principle,

$$u(r,\theta) = \sum_{n=0}^\infty B_n r^{2n}\sin (2 n\theta),$$

is also a solution of Laplace's equation satisfying $$u(r,0) =0$$ and $$u(r,\pi/2) = 0$$.
Then to make the boundary condition work, we want to choose the $$B_n$$ so that

$$u(R,\theta) = \sum_{n=0}^\infty B_n r^{2n}\sin (2 n\theta) = \sin(2\theta).$$

From this, it makes sense to take $$B_1 = R^{-2}$$ and $$B_n = 0$$ otherwise.
So our solution is

$$u(r,\theta) = (r/R)^2\sin(2\theta).$$

**Problem 3:**

* (A) If $$u(x,y) = f(x/y)$$ is a harmonic function, solve the ODE satisfied by $$f$$.
* (B) Convert your result from (A) to polar coordinates and show that $$\partial u/\partial r = 0$$.  
* (C) As a converse, suppose that $$v(x,y)$$ is any function in the upper half plane with $$\partial u/\partial r = 0$$.  Show that $$v = g(x/y)$$ for some function $$g$$.

**Solution:**

* (A) We calculate

$$u_x = f'(x/y)/y\quad\text{and}\quad u_{xx} = f''(x/y)/y^2.$$

Likewise,

$$u_y = f'(x/y)(-x/y^2)\quad\text{and}\quad u_{yy} = f''(x/y)(x^2/y^4) + f'(x/y)(2x/y^3).$$

This results in 

$$\Delta u = f''(x/y)/y^2 + f''(x/y)(x^2/y^4) + f'(x/y)(2x/y^3) = 0.$$

If we multiply this by $$x^2$$, it becomes

$$f''(x/y)x^2/y^2 + f''(x/y)(x^4/y^4) + f'(x/y)(2x^3/y^3) = 0.$$

Now substituting $$ z = x/y$$, this gives

$$f''(z)(z^2 + z^4) + 2z^3f'(z)  = 0$$.

This is a first-order ODE in $$f'(z)$$.  The general solution is

$$f(x/y) = C_1\tan^{-1}(x/y) + C_2.$$

* (B) If we convert this to polar coordinates, we get

$$u(r,\theta) = C_1\tan^{-1}(\cot(\theta)) + C_2.$$

The solution is independent of $$r$$, so $$u_r=0$$.

Conversely, if $$u_r=0$$ then $$u(r,\theta) = g(\theta) = g(\cot^{-1}(\cot(\theta))) = g(\cot^{-1}(x/y))$$.


**Problem 4:**

Find a solution of Laplace's equation $$\Delta u = 0$$ in the rectangle $$\Omega = (0,L)\times (0,M)$$
with the boundary conditions

$$u(L,y) = y(M-y),\ 0 < y < M,\ \ \ u(0,y) = 0,\ 0 < y < M,$$

$$u(x,0) = 0,\ 0 < x < L,\ \ \ u(x,M) = 0,\ 0 < x < L.$$


**Solution:**

We calculate

$$B_n = \frac{2}{M}\int_0^M y(M-y)\sin(2\pi y/M)dy =  -\frac{4}{n^3\pi^3}((-1)^n-1).$$

Therefore

$$u(x,y) = \sum_{n=1}^\infty -\frac{4}{n^3\pi^3\sinh(n L/M)}((-1)^n-1) \sin(n\pi y/M)\sinh(n \pi x/M)$$

is our solution.

**Problem 5:**

Find the Green's function for the domain consisting of the first octant

$$\Omega = \{(x,y,z): x > 0,\ y > 0,\ z > 0\}.$$

**Solution:** The fundmental solution for $$\mathbb{R}^3$$ is

$$\Phi(x,y,z;x',y',z') = \frac{1}{4\pi \sqrt{(x-x')^2+(y-y')^2+(z-z')^2}}.$$

Considering the Method of Images, we imagine electrons at $$(x',y',-z')$$, $$(x',-y',z')$$, and $$(-x',y',z')$$, along with protons at $$(-x',-y',z)$$, $$(-x', y', -z')$$, and $$(x', -y',z')$$, and a further electron at $$(-x',-y',-z')$$.

The combined potential field is 

$$\begin{align}
G(x,y,z;x',y',z')
  & = \frac{1}{4\pi \sqrt{(x-x')^2+(y-y')^2+(z-z')^2}} -\frac{1}{4\pi \sqrt{(x+x')^2+(y-y')^2+(z-z')^2}}\\
  & - \frac{1}{4\pi \sqrt{(x-x')^2+(y+y')^2+(z-z')^2}} - \frac{1}{4\pi \sqrt{(x-x')^2+(y-y')^2+(z+z')^2}}\\
  & +\frac{1}{4\pi \sqrt{(x+x')^2+(y+y')^2+(z-z')^2}} + \frac{1}{4\pi \sqrt{(x+x')^2+(y-y')^2+(z+z')^2}}\\
  & + \frac{1}{4\pi \sqrt{(x-x')^2+(y+y')^2+(z+z')^2}} - \frac{1}{4\pi \sqrt{(x+x')^2+(y+y')^2+(z+z')^2}}.
\end{align}$$

We see explicitly that

$$G(x,y,z;0,y',z') = 0,\ \ G(x,y,z;x',0,z') = 0,\ \ \text{and}\ \ G(x,y,z;x',y',0) = 0.$$

Moreover for $$(x,y,z)\in \Omega$$, 

$$\Delta G(x,y,z;x',y',z') = \delta(x-x')\delta(y-y')\delta(z-z').$$

Thus $$G(x,y,z;x',y',z')$$ is a Green's function for $$\Omega$$.

**Problem 6:**

Consider the differential equation

$$u_{tt}-2u_{tx} + u_{xx}=0.$$

Following our methodology for the wave equation, find a d'Alembert style
solution to the PDE on the whole real line satisfying the initial condition

$$u(x,0) = f(x),\ \ u_t(x,0) = g(x).$$

**Solution:**

Using the same idea as we did for the previous d'Alembert's formula, we get

$$\left\lbrace\begin{array}{cc}
w_t-w_x &= 0,\\
u_t-u_x &= w.
\end{array}\right.

Solving the first equation, we get $$w(x,t) = h(x+t)$$ for some arbitrary function $$h$$.
Then setting

$$u(x,t) = v(x,t) + th(x+t)$$

we get that

$$u_t-u_x = v_t -v_x + w,$$

and therefore

$$u_t-u_x = w$$ if and only if $$v_t-v_x = 0$$.

Thus $$v(x,t) = q(x+t)$$ for some function $$q$$ and

$$u(x,t) = h(x+t) + tq(x+t).$$

The initial condition implies that

$$h(x) = f(x),\ \ h'(x) + q(x) = g(x).$$

Thus our solution is

$$u(x,t) = f(x+t) + t(g(x+t)-f'(x+t)).$$



