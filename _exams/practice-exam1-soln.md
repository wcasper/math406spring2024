---
layout: page
title: Practice Exam 1 Solutions
permalink: /exams/practice-exam1-soln
---

### Directions
Solve the following problems and type up your solutions.  
In the actual exam, you will be allowed scratch paper and a pencil, but no calculator or note sheet.


**Problem 1:** Find the general solution of the partial differential equation

$$xu_x + (4y-x^3+x)u_y = 0.$$

**Solution:**

The characteristic curves satisfy

$$\frac{dy}{dx} = \frac{4y-x^3+x}{x} = 4(y/x)-x^2+1.$$

This is a first-order linear ODE, which we rewrite as

$$y' - \frac{4}{x}y = 1-x^2.$$

We multiply this by the integrating factor $$\mu(x) = x^{-4}$$, getting the equation

$$x^{-4}y' - 4x^{-5}y = x^{-4}-x^{-2}.$$

This combines to the equation

$$(x^{-4}y)' = x^{-4}-x^{-2},$$

which we integrate to

$$x^{-4}y = \int x^{-4}-x^{-2} dx = \frac{-1}{3}x^{-3} + x^{-1} + C.$$

The characteristic curves are therefore

$$x^{-4}y + \frac{1}{3}x^{-3} - x^{-1}  = C$$

and the general solution is

$$u = f(x^{-4}y + \frac{1}{3}x^{-3} - x^{-1}).$$

Note: A summary of how to solve first-order ODEs can be found [here (link)](https://wcasper.github.io/math207spring2024/topics/008-first-order-linear.html).

**Problem 2:** Use the method of separation of variables to find the solution of the BVP

$$u_{t} = 9tu_{xx}$$

with the boundary conditions

$$u(0,t) = 0,\ \ u(L,t) = 0,\ \ u(x,0) = \sin(2\pi x/L) + \sin(5\pi x/L).$$

**Solution:** We write $$u(x,t) = F(x)G(t)$$.  Then

$$F(x)G'(t) = 9tF''(x)G(t)$$.

It follows that

$$\frac{1}{8t}G'(t)/G(t) = F''(x)/F(x),$$

and therefore both expressions are constant.

We write

$$\frac{1}{8t}G'(t)/G(t) = -\lambda,\ \  F''(x)/F(x) = -\lambda.$$

Then solving these equations, we find

$$F(x) = A\cos(\sqrt{\lambda} x) + B\sin(\sqrt{\lambda} x)$$

and also

$$G(t) = Ce^{-4\lambda t^2}.$$

The boundary conditions imply $$A=0$$ and $$\lambda = \frac{n^2\pi^2}{L^2}$$ so that we have the sequence of fundamental solutions

$$u_n(x,t) = e^{-4 n^2\pi ^2 t^2/L^2}\sin\left(\frac{n\pi x}{L}\right).$$

To satisfy the initial condition, we take

$$u(x,t) = u_2(x,t) + u_5(x,t) = e^{-16\pi ^2 t^2/L^2}\sin\left(\frac{2\pi x}{L}\right) + e^{-100\pi ^2 t^2/L^2}\sin\left(\frac{5\pi x}{L}\right).$$

**Problem 3:**

* (a) Determine the cosine series expansion of $$f(x) = \sin(x)$$ on $$[0,\pi]$$.
* (b) Find a solution of the BVP

$$u_t = ku_{xx},\ \ t > 0$$

with the boundary conditions

$$u_x(0,t) = 0,\ \ u_x(\pi,t) = 0,\ \ u(x,0) = \sin(x).$$

**Solution:**

* (a)  We calculate

$$\begin{align}
A_0 & = \frac{1}{\pi}\int_0^\pi \sin(x)dx = \frac{2}{\pi}\\
A_1 & = \frac{2}{\pi}\int_0^\pi \sin(x)\cos(x)dx = \frac{1}{\pi}\sin^2(x)\rvert_0^\pi = 0
\end{align}$$


and for $$n > 1$$

$$\begin{align}
A_n
  & = \frac{2}{\pi}\int_0^\pi \sin(x)\cos(n x)dx\\
  & = \frac{1}{\pi}\int_0^\pi \sin((n+1)x) - \sin((n-1)x) dx\\
  & = \frac{1}{\pi}\left( \frac{-1}{n+1}\cos((n+1)x) + \frac{1}{n-1} \cos((n-1)x) \right\rvert_0^\pi\\
  & = \frac{2}{\pi} \frac{(-1)^{n-1}-1}{(n-1)(n+1)}
\end{align}$$

Therefore

$$\sin(x) = \frac{2}{\pi} + \sum_{n=2}^\infty \frac{2}{\pi} \frac{(-1)^{n-1}-1}{(n-1)(n+1)}\cos(nx),\ \ \ 0 < x < \pi$$

* (b) From (b) and the fundamental solutions we get

$$u(x,t) = \frac{2}{\pi} + \sum_{n=2}^\infty \frac{2}{\pi} \frac{(-1)^{n-1}-1}{(n-1)(n+1)}e^{-n^2kt}\cos(nx).$$


**Problem 4:**

Prove each of the following properties of the Fourier transform

* (a) if $$g(x) = f(x+x_0)$$, then $$\hat g(\xi) = e^{2\pi i\xi x_0}f(\xi)$$
* (b) if $$g(x) = f'(x)$$, then $$\hat g(\xi) = 2\pi i\xi \hat f(\xi)$$
* (c) if $$h(x) = f(x)g(x)$$, then $$\hat h(\xi) = (\hat f * \hat g)(\xi)$$
* (d) if $$\hat f(\xi) = \delta_2'(\xi)$$, then $$f(x) = 2\pi i x e^{4\pi i x}$$

**Solution:**

* (a)

$$\begin{align}
\hat g(\xi)
  & = \int_{\mathbb{R}} f(x+x_0)e^{-2\pi i x\xi}dx = \int_{\mathbb{R}} f(x)e^{-2\pi i (x-x_0)\xi}dx\\
  & = e^{2\pi i \xi x_0}\int_{\mathbb{R}} f(x)e^{-2\pi i (x-x_0)\xi}dx = e^{2\pi i \xi x_0}\hat f(\xi)
\end{align}$$

* (b) 

$$\begin{align}
\hat g(\xi)
  & = \int_{\mathbb{R}} f'(x)e^{-2\pi i x\xi}dx\\
  & = -\frac{1}{2\pi i \xi} f(x)e^{-2\pi i x\xi} \rvert_{-\infty}^\infty +2\pi i \xi \int_{\mathbb{R}} f(x)e^{-2\pi i x\xi}dx\\
  & = 2\pi i \xi \int_{\mathbb{R}} f(x)e^{-2\pi i x\xi}dx = 2\pi i \xi \hat f(\xi).
\end{align}$$

* (c)

$$\begin{align}
\hat h(\xi)
  & = \int_{\mathbb{R}} f(x)g(x)e^{-2\pi i x\xi}dx\\
  & = \int_{\mathbb{R}}\int_{\mathbb{R}}\int_{\mathbb{R}} \hat f(s)\hat g(t)e^{-2\pi i x(\xi-s-t)}dsdtdx\\
  & = \int_{\mathbb{R}}\int_{\mathbb{R}}\int_{\mathbb{R}} \hat f(s)\hat g(t)e^{-2\pi i x(\xi-s-t)}dxdsdt\\
  & = \int_{\mathbb{R}}\int_{\mathbb{R}} \hat f(s)\hat g(t)\delta(\xi-s-t)dsdt\\
  & = \int_{\mathbb{R}}\int_{\mathbb{R}} \hat f(\xi-t)\hat g(t)dt = (\hat f * \hat g)(\xi)
\end{align}$$

* (d)

$$\begin{align}
 f(x)
  & = \int_{\mathbb{R}} \hat f(\xi)e^{2\pi i x\xi}d\xi\\
  & = \int_{\mathbb{R}} \delta_2'(\xi)e^{2\pi i x\xi}d\xi\\
  & = \frac{d}{d\xi}\rvert_{\xi=2}e^{2\pi i x\xi} = 2\pi i x e^{4\pi i x}
\end{align}$$


**Problem 5:**

Find a solution of the following nonhomogeneous heat equation

$$u_t = 8u_{xx} + (1-x/\pi)\cos(t) + e^t\sin(3x),\ \ 0\leq x\leq \pi,\ t>0$$

with the nonhomogeneous boundary conditions

$$u(0,t) = \sin(t),\ \ \ u(\pi,t) = 0,\ \ \ u(x,0) = 0.$$

**Solution:**

We propose a solution of the form

$$u(x,t) = (1-x/\pi)\sin(t) + v(x,t).$$

Then $$u(x,0) = v(x,0)$$, $$u(0,t) = \sin(t) + v(0,t)$$ and $$u(\pi,t) = v(\pi,t)$$, so for $$u(x,t)$$ to satisfy the boundary conditions, we want 

$$v(0,t) = 0,\ \ \ v(\pi,t) = 0,\ \ \ v(x,0) = 0.$$

Also $$u_t = (1-x/\pi)\cos(t) + v_t$$ and $$u_{xx} = v_{xx}$$ so to solve the nonhomogeneous heat equation, we need

$$v_t = 8v_{xx} + e^t\sin(3x),\ \ 0\leq x\leq \pi,\ t>0.$$

To solve this, we first find the sine series expansion of the nonhomogeneous component on $$[0,\pi]$$

$$e^t\sin(3x) = \sum_{n=1}^\infty \phi_n(t)\sin (n x),$$

which gives $$\phi_3(t) = e^t$$ and $$\phi_n(t) = 0$$ for $$n\neq 3$$.
We also need the sine series expansion of the initial condition on the interval $$[0,\pi]$$

$$v(x,0) = \sum_{n=1}^\infty b_n\sin(n\pi).$$

Since $$v(x,0) = 0$$, this gives $$b_n = 0$$ for all $$n$$.

Then the final form for $$v(x,t)$$ is

$$u(x,t) = \sum_{n=1}^\infty B_n(t) \sin(n \pi x)$$

where here $$B_n(t) = 0$$ for $$n\neq 0$$ and otherwise

$$B_3(t) =  e^{-72t}\left(\int_0^t e^{s}e^{72s}ds + 0\right) =  e^{-72t}\left(\int_0^t e^{73s}ds\right) =  \frac{1}{73}\left(e^{t}-e^{-72t}\right).$$

Therefore  $$v(x,t) = \frac{1}{73}\left(e^{t}-e^{-72t}\right)\sin(3\pi x)$$ and 

$$u(x,t) = (1-x/\pi) \sin(t) + \frac{1}{73}\left(e^{t}-e^{-72t}\right)\sin(3\pi x).$$


**Problem 6:**

* (a) Determine the value of $$\int_{\mathbb{R}} xe^{-ax^2}dx$$.  [Hint: odd]
* (b) Determine the value of $$\int_{\mathbb{R}} x^2e^{-ax^2}dx$$.  [Hint: differentiation under the integral]
* (c) Find a solution of the Cauchy problem

$$u_t = ku_{xx},\ \ u(x,0) = x^2.$$

**Solution:**

* (a) Since it is odd, the integral is zero.
* (b) We use differentiation under the integral

$$\begin{align}
\int_{\mathbb{R}} x^2e^{-ax^2}dx
  & = \int_{\mathbb{R}} -\frac{\partial}{\partial a}e^{-ax^2}dx\\
  & = -\frac{\partial}{\partial a}\int_{\mathbb{R}} e^{-ax^2}dx\\
  & = -\frac{\partial}{\partial a}\sqrt{\frac{\pi}{a}}\\
  & = \frac{1}{2a}\sqrt{\frac{\pi}{a}}
\end{align}$$

* (c) Using the heat kernel

$$\begin{align}
u(x,t)
  & = \int_{\mathbb{R}} K(x-y,t)y^2 dy\\
  & = \int_{\mathbb{R}} \frac{1}{\sqrt{4\pi k t}} e^{-(x-y)^2/(4kt)}y^2dy\\
  & = \int_{\mathbb{R}} \frac{1}{\sqrt{4\pi k t}} e^{-y^2/(4kt)}(y-x)^2dy\\
  & = \int_{\mathbb{R}} \frac{1}{\sqrt{4\pi k t}} e^{-y^2/(4kt)}(y^2-2xy+x^2)dy\\
\end{align}$$

This last kernel we break up into three separate kernels using parts (a) and (b) above:

$$\begin{align}
u(x,t)
  & = x^2 + 0 + 2kt.
\end{align}$$


