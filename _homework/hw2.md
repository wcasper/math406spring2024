---
layout: page
title: Homework 2
permalink: /homework/hw2
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

* (a) $$xe^{x^2}$$
* (b) $$x^2e^{x^2}$$
* (c) $$\cos(x)$$
* (d) the Heaviside step function
* (e) $$x^n$$

# Problem 2

Prove **Plancherel's Theorem**, which states that if $$f(x)$$ is a real-valued function which is square integrable, then

$$\int_{\mathbb{R}} \lvert f(x)\rvert^2 dx = \int_{\mathbb{R}} \lvert \hat f(k)\rvert^2 dk$$

Hint: start by writing

$$\lvert \hat f(x)\rvert^2 = \int_{\mathbb{R}}\int_{\mathbb{R}} f(x)f(y)e^{-2\pi ikx}e^{2\pi iky}dxdy.$$

# Problem 3

Find a solution of the Cauchy problem

$$T_t = kT_{xx},\quad T(x,0) = f(x)$$

for the piecewise function

$$f(x) = \left\lbrace\begin{array}{cc}
e^{-ax} & x \geq 0\\
0 & x < 0\\
\end{array}\right.$$

# Problem 4

Use the Fourier transform to find a function $$K(x,t)$$ with the property that

$$\int_{\mathbb{R}} K(x-y,t)f(y)dy$$

is a solution of the **heat equation with advection**

$$T_t + vT_x = kT_{xx},\quad T(x,0) = f(x),$$

where here $$v$$ is a constant.





