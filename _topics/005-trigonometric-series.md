---
layout: page
title: Trigonometric Series
---

Before moving on to how to solve boundary value problems with more general initial conditions, we have to take a bit of a detour into trigonometric series.
A **trigonometric series** is a series of the form

$$A_0 + \sum_{n=1}^\infty A_n\cos\frac{2\pi nx}{L} + B_n\sin\frac{2\pi nx}{L}.$$

Here $$L$$ is a parameter which controls the **period** of the series.
If the above series converges for all values of $$x$$, then it converges to an $$L$$-periodic function.

Typically, we are interested in expression a complicated function as a trigonometric series.
Our motivation for this often is similar to our motivation for Taylor series: it makes things like derivataives and integrals (or even just computing the function) easier to understand.
The most important tool for expressing functions as trigonometric series is **Fourier series**.

## Fourier series

Given an $$L$$-periodic function $$f(x)$$ on $$\mathbb{R}$$, the **Fourier series** of $$f(x)$$ is the trigonometric series

$$A_0 + \sum_{n=1}^\infty A_n\cos\frac{2\pi nx}{L} + B_n\sin\frac{2\pi nx}{L}$$

with coefficients $$A_0 = \frac{1}{L}\int_0^L f(x)dx$$ and more generally

$$A_n = \frac{2}{L} \int_0^L f(x)\cos\frac{2\pi nx}{L}dx\quad\text{and}\quad B_n = \frac{2}{L} \int_0^L f(x)\sin\frac{2\pi nx}{L}dx.$$

:warning: Note the special formula for $$A_n$$ in the case $$n=0$$!

Under sufficiently nice conditions, for example if $$f(x)$$ is continuous, the Fourier series converges pointwise to the function $$f(x)$$

**Theorem:** Suppose that $$f(x)$$ is $$L$$-periodic and continuous on $$\mathbb[r]$$.  Then

$$f(x) = A_0 + \sum_{n=1}^\infty A_n\cos\frac{2\pi nx}{L} + B_n\sin\frac{2\pi nx}{L}.$$

The rate of this convergence is controlled by the regularity of the function: the smoother $$f$$ is, the faster the series will converge.
The coefficient formulas come from is the orthogonality of trigonometric functions.

**Theorem (Trigonometric Orthogonality):**
Let $$m$$ and $$n$$ be integers with $$n>0$$.

$$\begin{align}
\int_0^L \cos\frac{2\pi mx}{L}\cos\frac{2\pi nx}{L}dx = \frac{L}{2}\delta_{mn},\\
\int_0^L \sin\frac{2\pi mx}{L}\cos\frac{2\pi nx}{L}dx = 0,\\
\int_0^L \sin\frac{2\pi mx}{L}\sin\frac{2\pi nx}{L}dx = \frac{L}{2}\delta_{mn}.
\end{align}$$

**Exercise:** Prove these orthogonality relations.

Thus if we are trying to write 

$$f(x) = A_0 + \sum_{n=1}^\infty A_n\cos\frac{2\pi nx}{L} + B_n\sin\frac{2\pi nx}{L},$$

then taking the integral of $$f(x)$$ with $$\sin\frac{2\pi mx}{L}$$ gives

$$\begin{align}
\int_0^L f(x)\sin\frac{2\pi mx}{L}dx
  & = \sum_{n=0}^\infty A_n\int_0^L\cos\frac{2\pi nx}{L}\sin\frac{2\pi mx}{L}dx + \sum_{n=1}^\infty\int_0^L B_n\sin\frac{2\pi nx}{L}\sin\frac{2\pi mx}{L}dx\\
  & = \sum_{n=0}^\infty A_n0 + \sum_{n=1}^\infty\int_0^L B_n\frac{L}{2}\delta_{mn}\\
  & = B_m\frac{L}{2}.
\end{align}$$

This results in the formula for $$B_m$$.  The formulas for $$B_m$$ are obtained similarly.

## Sine and cosine series
The utility of Fourier series in expressing functions as trigonometric series extends beyond the case of periodic functions and to functions defined on an interval.
Specifically, given a function $$f$$ defined only on the interval $$[0,L]$$, we can still express $$f(x)$$ as a trigonometric series
by extending $$f(x)$ periodically outside the interval.
The most naive way to do this is to simply set
$$f(x+kL) = f(x)\quad\text{for all}\ k\in\mathbb{Z}.$$
The corresponding Fourier coefficients would then follow the same formula as above.
However, this turns out to be a **bad idea**, since it tends to introduce discontinuities at the boundaries of the interval $$x=0$$ and $$x=L$$.
As a result the Fourier series begin to exhibit undesireable behavior, like [Gibbs phenomenon](https://en.wikipedia.org/wiki/Gibbs_phenomenon).

Instead, a smarter decision is to first extend $$f(x)$$ to a nice function on the interval $$[-L,L]$$ which then extends to a continous $$2L$$-periodic function on $$\mathbb{R}$$.
In either case, we let $$f(x+2kL) = f(x)$$ for all integers $$k$$, making the function $$2L$$-periodic.
Inside the interval, there are two different but complementary ways to extend $$f(x)$$, depending on whether we want our extension to be even or odd.
We can use either

* the **even extension**

$$f(x) = \left\lbrace\begin{array} f(x)& 0\leq x \leq L\\ f(-x) & -L\leq x \leq 0\end{array}\right.,$$

* or the **odd extension**

$$f(x) = \left\lbrace\begin{array} f(x)& 0\leq x \leq L\\ -f(-x) & -L\leq x \leq 0\end{array}\right..$$

In the even extension case, the function is extended to an even function, which forces $$B_n = 0$$ for all $$n$$.
This means that the Fourier series of $$f(x)$$ will involve only cosines.
A series like that is called a **cosine series**.
Conversely, in the odd case, the extended function is odd.  This makes $$A_n = 0$$ for all $$n$$, which makes the series involve only sines.
This is called a **sine series**.

Typically, the even extension works best when the derivatives of $$f(x)$$ vanish at $$0$$ and $$L$$.
The odd extension works best when the function $$f(x)$$ itself vanishes at $$0$$ and $$L$$.
In particular, if $$f$$ doesn't vanish at $$0$$ and $$L$$, $$f(x)$$ will have jump discontinuities at the boundaries, leading to Gibbs phenomena.

### Sine series
Suppose that $$f(x)$$ is a function on $$[0,L]$$ with $$f(0) = f(L) = 0$$.
The **sine series expansion** for $$f(x)$$ is a sequence of constants $$B_n,\ n\geq 1$$ with the property that

$$f(x) = \sum_{n=1}^\infty B_n\sin\left(\frac{n\pi}{L}x\right),\ \forall x\in [0,L].$$

Using orthogonality of trigonometric integrals, we cn obtain an explicit formula for calculating the constants $$A_n$$.
In particular

$$B_n = \frac{2}{L}\int_0^L \sin\left(\frac{n\pi}{L}x\right)f(x)dx,\quad n\geq 1$$

### Cosine series
Alternatively, if $$f'(0) = f'(L) = 0$$, then we define the **cosine series expansion** of $$f(x)$$ to be a sequence of constants $$A_n,\ n\geq 0$$ with the property that

$$f(x) = \sum_{n=1}^\infty A_n\cos\left(\frac{n\pi}{L}x\right),\ \forall x\in [0,L].$$

In this case
$$A_0 = \frac{1}{L}\int_0^L f(x)dx,$$

and more generally

$$A_n = \frac{2}{L}\int_0^L \sin\left(\frac{n\pi}{L}x\right)f(x)dx,\quad n\geq 1$$

:warning: Notice again the different formulas for $$B_0$$ vs. $$B_n$$!




