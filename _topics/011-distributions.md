---
layout: page
title: Distributions
---

Currently Fourier transforms of a lot of functions aren't defined.
For example, if we wanted to do the Fourier transform of a simple exponential function $$e^{i ax}$$, it doesn't really exist as a function.
However, it is still convenient to be able to make sense of Fourier transformations of functions like this.
To do so, we will introduce the notion of a **distribution**.

## Distributions

A **distribution** on $$\mathbb{R}$$ is a linear transformation $$\chi: C_c^{\infty}(\mathbb{R})\rightarrow \mathbb{R}$$ with the property that for any sequence of functions $$\{f_n(x)\}\in C_c^\infty(\mathbb{R})$$ with $$f_n^{(k)}(x)\rightarrow 0$$ uniformly for all $k$, we must have $$\chi(f_n)\rightarrow 0$$.
A transformation $$\chi$$ defined this way is also called a **bounded linear functional** on $$C_c^\infty(\mathbb{R})$$.

The simplest distributions are functions themselves.  Specifically, if $$f(x)$$ is a bounded function on $$\mathbb{R}$$, then 

$$ C_c^\infty(\mathbb{R})\rightarrow \mathbb{R},\ \ \varphi(x)\mapsto \int_{\mathbb R} f(x)\varphi(x)dx$$

is a distribution.  In this sense, distributions can be thought of as *generalizations* of regular functions.

**Notation:** If $$\chi$$ is a distribution, we write $$\int \varphi(x) \chi(x)dx$$ to mean $$\chi(\varphi)$$.  This notation naturally extends the idea of distributions as generalizations of functions.

The simplest examples of distributions are the **Dirac delta distribution** and it's distributional derivatives $$\delta_a(x),\delta_a'(x),\dots$$ defined by

$$\int_{\mathbb{R}} f(x)\delta_a^{(k)}(x) dx = f^{(k)}(a).$$

As a special case, we write $$\delta^{(k)}(x)$$ in place of $$\delta_0^{(k)}(x)$$.
Note that linear combinations of distributions are also disributions, so they form a vector space.

We say that a sequence of distributions $$\chi_n$$ **converges weakly** or **converges in distribution** to $$\chi$$ if for all test functions $$\varphi$$ we have

$$\lim \int_{\mathbb{R}} \varphi(x)\chi_n(x)dx = \int_{\mathbb{R}}\varphi(x)\chi(x).$$

## Fourier Transforms of Distributions

**Definition:** The Fourier transform of a distribution $$\chi$$ is the distribution $$\hat\chi$$ defined by

$$\int_{\mathbb{R}} \varphi(x)\hat{\chi}(x)dx = \int_{\mathbb{R}} \hat\varphi(k)\chi(k)dk.$$

This notion allows us to take Fourier transforms of more functions, such as bounded functions, viewing them as *distributions*.

**Theorem:** The Fourier transform of the Heaviside step function is

$$\hat H (k) = \frac{1}{2}\delta(k) - \frac{i}{2\pi k}.$$

**Theorem:** The Fourier transform of $$e^{2\pi i ax}$$ is $$\delta_a(k)$$.

**Proof:**

Start with the distribution $$\chi(x) = e^{2\pi i ax}$$.
We calculate

$$\int_{\mathbb R}\varphi(x)\hat{\chi}(x) dx = \int_{\mathbb R} \hat\varphi(k)\chi(k)dk = \int_{\mathbb R} \hat\varphi_a(k)dk$$

for $$\varphi_a(x) = \varphi(x+a).$$
Now by Fourier Inversion

$$\varphi_a(x) = \int_{\mathbb{R}}\hat\varphi_a(k)e^{2\pi i kx}dk.$$

Using the special case of $$x=0$$:

$$\int_{\mathbb R}\varphi(x)\hat{\chi}(x) dx = \varphi_a(0) = \varphi(a) = \int_{\mathbb R} \varphi(x)\delta_a(x)dx.$$

:black_square_button:



