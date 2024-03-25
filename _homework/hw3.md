---
layout: page
title: Homework 3
permalink: /homework/hw3
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

Solve Laplace's equation

$$u_{xx} + u_{yy} = 0$$

on the rectangle $$0 < x < L$$ and $$0 < y < M$$

with the Dirichlet boundary conditions

$$u(x,0) = x(L-x),\ \ u(x,M) = x(L-x),\ \ u(0,y) = y(M-y),\ \ y(L,y) = y(M-y).$$

Then use a computer to create a contour plot of your solution and include the plot with your answer.
Hint: for this part, you might consider using MATLAB or Python or potentially adapting the code from lecture.

# Problem 2

Solve Laplace's equation 

$$u_{xx} + u_{yy} = 0$$

ono the disk $$x^2 + y^2\leq R^2$$ with the Dirichlet boundary condition 

$$u = 1 + 3\sin\theta - 5\cos(2\theta)$$

Then use a computer to create a contour plot of your solution and include the plot with your answer.

Hint: use the fundamental solutions in polar coordinates.

# Problem 3

Solve Laplace's equation 

$$u_{xx} + u_{yy} = 0$$

ono the disk $$x^2 + y^2\leq R$$ with the Dirichlet boundary condition 

$$u = \left\lbrace\begin{array}{cc}1 & 0\leq\theta\leq\pi\\0 & \pi <\theta<2\pi\end{array}\right.$$

Then use a computer to create a contour plot of your solution and include the plot with your answer.

Hint: use Poisson's kernel

# Problem 4

Prove **Harnack's Inequality** which states that if
$$u(x,y)$$ is a non-negative harmonic in a domain $$\Omega\subseteq\mathbb{R}^2$$ containing the disk

$$D_R(a,b) = \{(x,y)\in\mathbb R^2: (x-a)^2 + (y-b)^2 < R^2\}$$

and if $$u(x,y)$$ extends to a continuous function on the boundary of the disk, then for any  $$(x,y)\in D_R(a,b)$$ we have

$$\frac{1-r/R}{1 + r/R} u(a,b)\leq u(x,y)\leq \frac{1+r/R}{1 - r/R} u(a,b)$$

where here $$r = \sqrt{(x-a)^2+(y-b)^2}$$.

Hint: use both the Poisson kernel and the Mean Value Property.

# Problem 5

Use Harnack's inequality to prove **Liouville's Theorem** which states that if $$u(x,y)$$ is a harmonic function on all of $$\mathbb{R}^2$$ and $$u(x,y)$$ is either bounded above or bounded below, then $$u(x,y)$$ is constant.



