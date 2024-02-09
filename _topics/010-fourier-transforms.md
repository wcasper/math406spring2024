---
layout: page
title: Fourier Transforms
---

We want to move our theory toward the heat kernel, unbound solutions of the heat equation and distributions.
To do so, its worth introducing one of the most powerful tools of mathematics found after the invention of calculus: the Fourier transform.

**Definition:** Let $$f(x)$$ be an integrable function $$\mathbb R$$.  The **Fourier transform** of $$f(x)$$, is the function $$\widehat{f}(k)$$ on $$\mathbb{R}$$ defined by

$$\hat{f}(k) = \int_{\mathbb{R}} e^{-2\pi i kx}f(x)dx.$$

Similarly, if $$g(k)$$ is an integrable function on $$\mathbb{R}$$, the **inverse Fourier transform** is defined to be

$$\check{f}(k) = \int_{\mathbb{R}} e^{2\pi i kx}f(x)dx.$$

Physically speaking, we can think about the Fourier transform and its inverse as describing the same quantity in two different ways.
* in **physical space** we are saying what the value of the function is at any particular position
* in **frequency space** we are saying if we expressed $$f(x)$$ as a sum of waves, what amplitude it would have for each frequency

### Important special cases

The **Heaviside step function**

$$H(x) = \left\lbrace\begin{array}{cc}0 & x < 0\\ 1/2 & x = 0\\ & 1 & x = 1\end{array}\right.$$

and the **sinc** function

$$\sinc(x) = \left\lbrace\begin{array}{cc}\sin(x)/x & x \neq 0\\ 1 & x = 0\end{array}\right.$$

are related via the Fourier transform.

**Prop:**

$$\hat H(x) = \sinc(x).$$

The **Gaussian function** also plays an important role in the study of Fourier transforms

**Prop:**  If $$f(x) = e^{-ax^2}$$ then

$$\hat f(k) = \sqrt{\frac{\pi}{a}}e^{-\pi^2k^2/a}.$$


## Basic Properies of the Fourier Transform

Assume that $$f(x)$$ is integrable on $$\mathbb{R}$$.

**Fourier Transforms of Translations:** Let $$a\in\mathbb{R}$$.  If $$g(x) = f(x+a)$$ then

$$\hat g(k) = e^{2\pi i ka}\hat f(k).$$

**Fourier Transforms of Rescalings:**  Let $$r\neq 0$$.  If $$g(x) = f(ra)$$ then

$$\hat g(k) = \frac{1}{r}\hat f(k/r).$$

**Fourier Transforms of Derivatives:**  Assume that $$f'(x)$$ exists for all $$x\in\mathbb{R}$$ and is integrable on $$\mathbb{R}$$.  Then

$$\hat{f'}(k) = 2\pi i k\hat f(k).$$

## Fourier Inversion

**Inversion:** If $$f(x)$$ is continuous and integrable.  Then

$$\check{\hat f} = f.$$

In other words, the Fourier transform and inverse Fourier transform are inverse transformations.

**Proof:**

For any $$\epsilon > 0$$, define $$g_\epsilon(k) = e^{-4\pi\epsilon^2k^2}.$$
We calculate

$$\begin{align}
\check{g_\epsilon\hat f}(x)
  & = \int_{\mathbb{R}}\int_{\mathbb{R}} e^{2\pi i kx}e^{-2\pi i kt}f(t)e^{-4\pi\epsilon^2k^2}dtdk\\
  & = \int_{\mathbb{R}}\int_{\mathbb{R}} e^{2\pi i kx}e^{-2\pi i kt}f(t)e^{-4\pi\epsilon^2k^2}dkdt\\
  & = \int_{\mathbb{R}}f(t)\int_{\mathbb{R}} e^{-2\pi i k(t-x)}e^{-\pi\epsilon^2k^2}dkdt\\
  & = \int_{\mathbb{R}}f(t)\frac{1}{\epsilon}e^{-\pi(t-x)^2/\epsilon^2}dt\\
  & = \int_{\mathbb{R}}f(t+x)\frac{1}{\epsilon}e^{-\pi t^2/\epsilon^2}dt\\
  & = f(x) + \int_{\mathbb{R}}(f(t+x)-f(x)\frac{1}{\epsilon}e^{-\pi t^2/\epsilon^2}dt\\
\end{align}$$

We break this last integral into three separate ones

$$\int_{\mathbb{R}}(f(t+x)-f(x))\frac{1}{\epsilon}e^{-\pi t^2/\epsilon^2}dt = I_-(x;\epsilon) + I_0(x;\epsilon) + I_+(x;\epsilon), $$

where

$$\begin{align}
I_-(x;\epsilon) &= \int_{-\infty}^{-\epsilon} (f(t+x)-f(x))\frac{1}{\epsilon}e^{-\pi t^2/\epsilon^2}dt,\\
I_0(x;\epsilon) &= \int_{-\epsilon}^\epsilon (f(t+x)-f(x))\frac{1}{\epsilon}e^{-\pi t^2/\epsilon^2}dt,\\
I_+(x;\epsilon) &= \int_{\epsilon}^\infty (f(t+x)-f(x))\frac{1}{\epsilon}e^{-\pi t^2/\epsilon^2}dt.
\end{align}$$

Now if $$C = \int_{\mathbb{R}} \lvert f(x)\rvert dx$$ then

$$\lim_{\epsilon\rightarrow0+} I_\pm(x;\epsilon) \leq \lim_{\epsilon\rightarrow0+} 2C\frac{1}{\epsilon}e^{-\pi/\epsilon} = 0.$$

Moreover, by the Mean Value Theorem for Integrals, for all $$\epsilon > 0$$ there exists $$t_\epsilon \in [-\epsilon,\epsilon]$$ with

$$I_0(x;\epsilon) = 2(f(t_\epsilon+x)-f(x))e^{-\pi t_\epsilon^2/\epsilon^2}.$$

Since $$f$$ continuous, it follows that $$\lim_{\epsilon\rightarrow 0+} I_0(x;\epsilon) = 0.$$

Thus we conclude

$$\check{\hat f}(x) = \lim_{\epsilon\rightarrow0+} \check{g_\epsilon\hat f}(x) = f(x).$$

:black_square_button:

## Convolution

**Definition:** The convolution of two functions $$f(x)$$ and $$g(x)$$, if it exists, is defined to be

$$(f * g)(x) := \int_{\mathbb R} f(y)g(x-y)dy.$$

It exists under several circumstances, including when
* both $$f$$ and $$g$$ are square integrable
* both $$f$$ and $$g$$ are *locally* integrable and at least one has compact support
* both $$f$$ and $$g$$ are integrable, one is bounded and the other is vanishes quickly as $$\lvert x\rvert$$ goes to infinity

**Proposition:** If $$f * g$$ exists, then $$g * f$$ exists and $$f * g = g * f$$.

**Theorem:** $$\widehat{f * g} = \hat f \hat g$$ and $$\check(f * g) = \check f \check g$$.

**Corollary:**  $$\widehat{fg} =  \hat f * \hat g$$ and $$\check{fg} = \check f * \check g$$.


