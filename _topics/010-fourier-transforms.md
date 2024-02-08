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


## Basic Properies of the Fourier Transform

**Plancherel's Theorem:**  If $$f(x)$$ is square integrable, then

$$\int_{\mathbb R} \lvert f(x)\rvert^2 dx = \int_{\mathbb R} \lvert \hat f(x)\rvert^2 dx.$$

**Inversion:** If $$f(x)$$ is both integrable and square integrable, then so is $$\widehat f$$ and

$$\check{\hat f} = f\ \text{and}\ \widehat{(\check{f})} = f.$$

In other words, the Fourier transform and inverse Fourier transform are inverse transformations.

In fact, one can show that $$(\widehat{\hat f})(x) = f(-x)$$, that $$\widehat{\widehat{\hat f}} = \check{f}$$, and that $$\widehat{\widehat{\widehat{\hat f}}} = f$$.

## Convolution

**Definition:** The convolution of two functions $$f(x)$$ and $$g(x)$$, if it exists, is defined to be

$$(f * g)(x) := \int_{\mathbb R} f(y)g(x-y)dy.$$

It exists under several circumstances, including when
* both $$f$$ and $$g$$ are square integrable
* both $$f$$ and $$g$$ are *locally* integrable and at least one has compact support
* both $$f$$ and $$g$$ are integrable, one is bounded and the other is vanishes quickly as $$\lvert x\rvert$$ goes to infinity

**Proposition:** If $$f * g$$ exists, then $$g * f$$ exists and $$f * g = g * f$$.

**Theorem:** $$\widehat{f * g} = \widehat f \widehat g$$.

