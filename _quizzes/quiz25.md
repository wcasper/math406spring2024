---
layout: page
title: Lecture 25 Assessment
permalink: /quizzes/lecture25
---


**Question 1:**  True or false.

To solve the wave equation 

$$u_{tt} = c^2(u_{xx} + u_{yy}),\ \ 0 < x < L,\ 0 < y < M,$$

on a rectangle $$[0,L]\times [0,M]$$ with the initial condition

$$u(x,y,0) = f(x,y),\ \ u_t(x,y) = 0$$

we should first take the two-dimensional sine series expansion of $$f(x,y)$$, ie. 

$$f(x,y) = \sum_{m=1}^\infty \sum_{n=1}^\infty A_{mn}\sin(m\pi x/L)\sin(n\pi y/M).$$


**Question 2:**  Numerical.

Determine the value $$A_{21}$$ in the two-dimensional sine series expansion 

$$f(x,y) = \sum_{m=1}^\infty \sum_{n=1}^\infty A_{mn}\sin(mx)\sin(ny)$$

of the function

$$f(x,y) = xy,\ \ 0 \leq x < \pi,\ \ 0 \leq y < \pi.$$


**Question 3:**  True or false.

The $$n$$'th Fourier-Bessel series expansion of a function $$f(r)$$ on $$(0,R)$$ is given by

$$f(r) = \sum_{k=1}^\infty A_k J_n(s_k^n r/R),$$

where the constants $$A_k$$ are defined by

$$A_k = \frac{2}{R^2 J_{n+1}(s_k^n)^2}\int_0^R f(r)J_n(s_k^nr/R) rdr.$$




