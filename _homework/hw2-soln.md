---
layout: page
title: Homework 2 Solution
permalink: /homework/hw2-soln
---

### Directions
Solve the following problems and write up your solutions.  Your solutions should be provided in one of the following formats (in order of preference)
* typed up in $$\LaTeX$$ and submitted as a PDF on Canvas
* written legibly on blank paper, scanned into a PDF and then uploaded on Canvas
* written on ancient parchement with a quill and then flown to the instructor via owl post like in Harry Potter

If you go with the first strategy, you may wish to check out Overleaf which is a free and intuitive website for generating $$\LaTeX$$ documents online.
If you wish to use the second method and don't own a scanner at home, you can check out the numerous scanning apps available for smartphones.

You will be graded based on *completion* of all of the assigned problems, along with in-depth grading of *select* problems which will not be revealed until after the homework is graded.

**Remember:** Success in any math class is based on *practice*.  The assigned homework problems are the **bare minimum**.  You should strive to do as many problems as possible from the textbook.

# Problem 1

Determine the Fourier transform of each of the following functions.

* (a) $$xe^{-x^2}$$
* (b) $$x^2e^{-x^2}$$
* (c) $$\cos(x)$$
* (d) $$x^n$$

**Solution:**

We calculate

$$\begin{align}
\int_{\mathbb R} xe^{-x^2}e^{-2\pi i \xi x}dx
  & = \frac{1}{-2\pi i}\frac{\partial}{\partial \xi} \int_{\mathbb R} e^{-x^2}e^{-2\pi i \xi x}dx\\
  & = \frac{1}{-2\pi i}\frac{\partial}{\partial \xi} \sqrt{\pi}e^{-\pi^2\xi^2}\\
  & = - \pi^{3/2}\xi e^{-\pi^2\xi^2}.
\end{align}$$

and also

$$\begin{align}
\int_{\mathbb R} x^2e^{-x^2}e^{-2\pi i \xi x}dx
  & = \frac{1}{(-2\pi i)^2}\frac{\partial^2}{\partial \xi^2} \int_{\mathbb R} e^{-x^2}e^{-2\pi i \xi x}dx\\
  & = \frac{1}{(-2\pi i)^2}\frac{\partial^2}{\partial \xi^2} \sqrt{\pi}e^{-\pi^2\xi^2}\\
  & = \frac{1}{(-2\pi i)^2}\sqrt{\pi} (4\pi^4 \xi^2 -2\pi^2) e^{-\pi^2\xi^2}\\
  & = -\sqrt{\pi} (\frac{1}{2}\pi^2 \xi^2 - 1) e^{-\pi^2\xi^2}
\end{align}$$

Moreover, for any test function $$\varphi$$

$$\begin{align}
\int_{\mathbb R} \varphi(\xi) \hat\cos(\xi)d \xi\\
 &  = \int_{\mathbb R} \hat \varphi(\xi) \cos(\xi)d\xi\\
 &  = \frac{1}{2}\int_{\mathbb R} \hat \varphi(\xi) (e^{i\xi} + e^{-i\xi})d\xi\\
 &  = \frac{1}{2}\int_{\mathbb R} \hat \varphi(\xi) e^{i\xi} d\xi + \frac{1}{2}\int_{\mathbb R} \hat \varphi(\xi) e^{-i\xi})d\xi\\
 &  = \frac{1}{2}(\hat \varphi)^\vee(1/2\pi) + \frac{1}{2}(\hat \varphi)^\vee(-1/2\pi)\\
 &  = \frac{1}{2}\varphi(1/2\pi) + \frac{1}{2}\varphi(1/2\pi).
\end{align}$$

It follows that

$$\hat\cos(\xi) = \frac{1}{2}\delta\left(\xi-\frac{1}{2\pi}\right) + \frac{1}{2}\delta\left(\xi+\frac{1}{2\pi}\right\).$$

Likewise, for $$f(x) = x^n$$ we get

$$\begin{align}
\int_{\mathbb R} \varphi(\xi) \hat f(\xi)d \xi\\
 &  = \int_{\mathbb R} \hat \varphi(\xi) \xi^nd\xi\\
 &  = \frac{1}{(2\pi i)^n}\int_{\mathbb R} \hat \varphi(\xi) (-2\pi i\xi)^nd\xi\\
 &  = \frac{1}{(2\pi i)^n}\int_{\mathbb R} \hat {\varphi^{(n)}}(\xi)\\
 &  = \frac{1}{(2\pi i)^n}(\hat {\varphi^{(n)}})^\vee (0)\\
 &  = \frac{1}{(2\pi i)^n}\varphi^{(n)}(0)
\end{align}$$

It follows that $$\hat f(\xi) = \frac{1}{(2\pi i)^n}\delta^{(n)}(\xi)$$.

# Problem 2

Prove **Plancherel's Theorem**, which states that if $$f(x)$$ is a real-valued function which is square integrable, then

$$\int_{\mathbb{R}} \lvert f(x)\rvert^2 dx = \int_{\mathbb{R}} \lvert \hat f(k)\rvert^2 dk$$

Hint: start by writing

$$\lvert \hat f(k)\rvert^2 = \int_{\mathbb{R}}\int_{\mathbb{R}} f(x)f(y)e^{-2\pi ikx}e^{2\pi iky}dxdy.$$

**Solution:**

Recall from our work with the heat kernel that

$$\lim_{t\rightarrow 0+} K(x,t) = \delta(x)$$,

where the limit is viewed as a limit of distributions (ie. a weak limit).
Consider the special case where here $$K(x,t)$$ is the heat kernel with coefficient of diffusivity $$k = \frac{1}{4\pi^2}$$.
Using this, we calculate

$$\begin{align}
\int_{\mathbb R}\lvert \hat f(\xi )\rvert^2 d\xi 
  & = \int_{\mathbb{R}}\int_{\mathbb{R}}\int_{\mathbb{R}} f(x)f(y)e^{-2\pi i\xi x}e^{2\pi i\xi y}dxdyd\xi \\
  & = \lim_{a\rightarrow 0}\int_{\mathbb{R}}e^{-a\xi^2}\int_{\mathbb{R}}\int_{\mathbb{R}} f(x)f(y)e^{-2\pi i\xi x}e^{2\pi i\xi y}dxdyd\xi \\
  & = \lim_{a\rightarrow 0}\int_{\mathbb{R}}\int_{\mathbb{R}}\int_{\mathbb{R}} f(x)f(y)e^{-2\pi i\xi (x-y)}e^{-a\xi^2}d\xi dydx\\
  & = \lim_{a\rightarrow 0}\int_{\mathbb{R}}\int_{\mathbb{R}} f(x)f(y)\sqrt{\frac{\pi}{a}}e^{-\pi^2(x-y)^2/a}dydx\\
  & = \int_{\mathbb{R}}f(x)\lim_{a\rightarrow 0}\int_{\mathbb{R}}K(x-y,a)f(y)dydx\\
  & = \int_{\mathbb{R}}f(x)\int_{\mathbb{R}}\delta(x-y)f(y)dydx\\
  & = \int_{\mathbb{R}}f(x)^2dx.
\end{align}


# Problem 3

Find a solution of the Cauchy problem

$$T_t = kT_{xx},\quad T(x,0) = f(x)$$

for the piecewise function

$$f(x) = \left\lbrace\begin{array}{cc}
e^{-ax} & x \geq 0\\
0 & x < 0\\
\end{array}\right.$$

**Solution:**

We use the heat kernel to calculate

$$\begin{align}
T(x,t)
  & = \int_0^\infty e^{-ay}K(x-y,t)dy\\
  & = \sqrt{\frac{1}{4\pi kt}} \int_0^\infty e^{-(x-y)^2/(4kt)}e^{-ay}dy\\
  & = \sqrt{\frac{1}{4\pi kt}} e^{a^2kt-ax}\int_0^\infty e^{-(x-2akt-y)^2/(4kt)}dy\\
  & = \sqrt{\frac{1}{4\pi kt}} e^{a^2kt-ax}\sqrt{4kt}\int_{(-x+2akt)/\sqrt{4kt}}^\infty e^{-z^2}dz\\
  & = \sqrt{\frac{1}{4\pi kt}} e^{a^2kt-ax}\sqrt{4kt} \text{erf}(z)\vert_{(-x+2akt)/\sqrt{4kt}}^\infty\\
  & = \sqrt{\frac{1}{4\pi kt}} e^{a^2kt-ax}\sqrt{4kt} (1-\text{erf}((-x+2akt)/\sqrt{4kt}))
\end{align}$$


# Problem 4

Use the Fourier transform to find a function $$K(x,t)$$ with the property that

$$\int_{\mathbb{R}} K(x-y,t)f(y)dy$$

is a solution of the **heat equation with advection**

$$T_t + vT_x = kT_{xx},\quad T(x,0) = f(x),$$

where here $$v$$ is a constant.


**Solution:**

We take the Fourier transform $$\hat T(\xi , t)$$ of $$T$$ to find

$$\hat T_t + 2\pi i \xi v \hat T = -4\pi^2\xi^2 k\hat T,\quad \hat T(\xi, 0) = \hat f(\xi).$$

Therefore

$$\hat T_t + (2\pi i \xi v + 4\pi^2\xi^2 k)\hat T = 0.$$

The solution of this equation shows

$$\hat T(\xi,t) = \hat f(\xi)e^{-2\pi i\xi vt - 4\pi^2\xi^2 kt}.$$

Then by taking the inverse Fourier transform, we get the convolution expression

$$T(x,t) = \int_{\mathbb{R}} K(x-y,t) f(y)dy$$

wherer here $$K(x,t)$$ is given by

$$\begin{align}
K(x,t)
  & = \int_{\mathbb{R}} e^{-2\pi i\xi vt - 4\pi^2\xi^2 kt} e^{2\pi i \xi x} d\xi\\
  & = \int_{\mathbb{R}} e^{-4\pi^2\xi^2 kt} e^{2\pi i \xi (x-vt)} d\xi\\
  & = \frac{1}{\sqrt{4\pi kt}}e^{-(x-vt)^2/(4kt)}
\end{align}$$

# Problem 5 (BONUS)

In this problem, we calculate the Fourier transform of the Heaviside step function

$$H(x) = \left\lbrace\begin{array}{cc}0 & x < 0,\\ 1 & x > 0\end{array}\right.$$

* (a) Explain why

$$\int_{\mathbb R} \varphi(\xi)\hat H(\xi) d\xi =  \int_{\mathbb R} \hat\varphi(x)H(x)dx.$$

* (b) Use the fact that $$\lim_{\epsilon\rightarrow 0+} 1_{[0,\infty)} e^{-\epsilon x}$$ converges to $$H(x)$$ as a distribution to prove

$$\int_{\mathbb R} \hat\varphi(x)H(x)dx = \lim_{\epsilon\rightarrow 0+} \int_{\mathbb R} \varphi(\xi)\frac{1}{\epsilon + 2\pi i\xi}d\xi.$$

* (c) Use (b) to show that

$$\int_{\mathbb R} \hat\varphi(x)H(x)dx = \lim_{\epsilon\rightarrow 0+} I(\epsilon) + \lim_{\epsilon\rightarrow 0+} I(\epsilon)$$

where here

$$\begin{align}
I_\epsilon &= \int_{\mathbb R} \varphi(\xi)\frac{\epsilon}{\epsilon^2 + 4\pi^2\xi^2}d\xi,\\
J_\epsilon &= \int_{\mathbb R} \varphi(\xi)\frac{-2\pi i\xi}{\epsilon^2 + 4\pi^2\xi^2}d\xi.
\end{align}$$

* (d) Prove that

$$\lim_{\epsilon\rightarrow 0+} I_\epsilon = \frac{1}{2}\varphi(0)$$

* (e) Prove that 

$$\lim_{\epsilon\rightarrow 0+} J_\epsilon = \int_{\mathbb{R}} (\varphi(\xi)-\varphi(0))\frac{1}{2\pi i \xi} d\xi.$$

This expression on the right hand side is called the **principal value** of the integral $$\int_{\mathbb{R}}\varphi(\xi)\frac{1}{2\pi i \xi} d\xi$$.
We write $$\text{PV}\left[\frac{1}{2\pi i \xi}\right]$$ to denote this distribution.

* (f) Conclude that 

$$\hat H(\chi) = \frac{1}{2}\delta(\xi) + \text{PV}\left[\frac{1}{2\pi i \xi}\right].$$


