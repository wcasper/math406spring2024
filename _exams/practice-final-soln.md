---
layout: page
title: Practice Final Exam Solutions
permalink: /exams/practice-final-soln
---

### Directions
Solve the following problems and type up your solutions.  
In the actual exam, you will be allowed scratch paper and a pencil, but no calculator or note sheet.


**Problem 1:**

Find a solution of the heat equation

$$u_t = ku_{xx}$$

* (A) on the real line  satisfying the initial condition

$$u(x,0) = \frac{1}{\sqrt{4\pi k}}e^{-(x-1)^2/4k}.$$

* (B) on the interval $$(0,L)$$ with Neumann boundary conditions and the initial condition

$$u(x,0) = 3\cos(5x/L) + 4\cos(7x/L).$$

**Solution:**

* (A) The heat kernel 

$$K(x,y,t) = \frac{1}{\sqrt{4\pi kt}}e^{-(x-y)^2/(4kt)}$$

is a solution of the heat equation for any value of $$y$$, so in particular 

$$K(x,1,t) = \frac{1}{\sqrt{4\pi kt}}e^{-(x-1)^2/(4kt)}$$

is a solution.  Also translations of solutions are solutions, so 

$$u(x,t) := K(x,1,t+1) = \frac{1}{\sqrt{4\pi k(t+1)}}e^{-(x-1)^2/(4k(t+1))}$$

is also a solution.  It satisfies the initial condition

$$u(x,0) = \frac{1}{\sqrt{4\pi k}}e^{-(x-1)^2/4k}

$$u(x,1,t+1) = \frac{1}{\sqrt{4\pi k(t+1)}}e^{-(x-1)^2/(4k(t+1))}$$

* (B)

We have a Neumann boundary condition, so we expect a linear combination of solutions of the form

$$u_n(x,t) = e^{-n^2\pi^2 kt/L^2}\cos(n\pi x/L)$$

From the initial condition, we find

$$u(x,t) = 3u_5(x,t) + 4u_7(x,t) = 3e^{-25\pi^2 kt/L^2}\cos(5\pi x/L) + 4e^{-49\pi^2 kt/L^2}\cos(7\pi x/L).$$


**Problem 2:**

Calculate each of the following

* (A) The Fourier transform of $$e^{-\lvert x \rvert}$$
* (B) The Fourier transform of  $$xe^{-x^2}$$
* (C) The sine series of $$x$$ on $$(0,\pi)$$


**Solution:**

* (A) We break up the integral into two pieces to obtain

$$\frac{2}{1 + 4\pi\xi^2}.$$

* (B) We use properties of the Fourier transform to obtain

$$\frac{1}{-2\pi i}\frac{d}{d\xi}\sqrt{\pi}e^{-\pi^2\xi^2} = -i(\pi)^{3/2}\xi e^{-\pi^2\xi^2}$$

* (C) 

$$x = \sum_{n=1}^\infty \frac{2(-1)^{n+1)}{n}\sin(n x),\quad 0 < x < \pi$$


**Problem 3:**

Find a solution of Laplace's equation on the unit square $$(0,1)\times (0,1)$$
with the Neumann boundary conditions

$$u_x(0,y) = 0,\ \ \ u_x(\pi,y) = 0,\quad 0 < y < \pi,$$

$$u_y(x,0) = 0,\ \ \ u_y(x,\pi) = \cos(x),\quad 0 < x < \pi.$$

**Solution:**

Use separation of variables to see that with Neumann boundary conditions, we are looking for a combination of solutions of the form

$$u_n(x,y) = \cos(n x)\cosh(n y).$$

The value of this function on the boundary is

$$u_x(x,\pi) = n \cos(n x)\sinh(n\pi).$$

So

$$u(x,y) = \frac{1}{\sinh(\pi)}u_1(x,y) = \frac{1}{\sinh(\pi)}\cos(x)\cosh(y)$$

solves the problem.


**Problem 4:**

* (A) Find a solution of the wave equation on the real line 

$$u_{tt} = c^2u_{xx}$$

with the iniitial condition

$$u(x,0) = e^{-x^2},\ \ u_t(x,0) = \frac{2}{1+x^2}.$$

**Solution:**

From d'Alembert's formula, we have that the solution is given by

$$u(x,t) = \frac{1}{2}(f(x+ct)+f(x-ct)) + \frac{1}{2c}\int_{x-ct}^{x+ct} sg(s)ds.$$

Therefore 

$$u(x,t) = \frac{1}{2}e^{-(x+ct)^2} + \frac{1}{2}e^{-(x-ct)^2} + \ln(1 + (x+ct)^2) - \ln(1 + (x-ct)^2).$$


**Problem 5:**

* (A) Write down the Poisson kernel for the upper half plane.

* (B) Determine the equation of a harmonic function on the upper half plane satisfying the boundary condition

$$u(x,0) = \left\lbrace\begin{array}{cc}
2, & 0 < x < 5\\
0, & \text{otherwise}
\end{array}\right.$$

**Solution:**

* (A) It is given by


$$P(x,y,t) = \frac{1}{\pi} \frac{y}{(x-t)^2+y^2}$$


* (B) We calculate

$$\begin{align}
u(x,y)
  & = \frac{1}{\pi} \int_{\mathbb{R}}\frac{y}{(x-t)^2+y^2} u(t,0) dt\\
  & = \frac{2}{\pi} \int_0^5\frac{y}{(x-t)^2+y^2} dt\\
  & = \frac{2}{\pi} \int_{-x}^{5-x}\frac{y}{t^2+y^2} dt\\
  & = \frac{2}{\pi} \left(\tan^{-1}((5-x)/y) + \tan^{-1}(x/y)\right)
\end{align}$$


**Problem 6:**

* (A) Classify the type of the differential equation 

$$u_{xx} + 2u_{xy} + 5u_{yy} = 0$$

* (B) Use separation of variables to determine a fundamental set of solutions of

$$u_{xx} + u_{yy} + u_x + u_y = 0$$

on the interval $$[0,L]\times [0,M]$$ with Dirichlet boundary conditions, which are zero on each side of the boundary except the side where $$x=L$$.


**Solution:**

The eigenvalues of the associated matrix are given by the roots of the polynomial

$$(1-\lambda)(5-\lambda)-4 = \lambda^2-6\lambda + 1$$

which are $$3\pm 2\sqrt{2}$$ and both positive.  Therefore it is elliptic.

* (B) We write $$u(x,y) = F(x)G(y)$$ and then calculate

$$F''/F + G''/G + F'/F  + G'/G = 0.$$

This says

$$F'' + F' - \lambda F = 0.$$

$$G'' + G' + \lambda G = 0.$$


This gives us the solutions

$$F(x) =  Ae^{-x/2}\cosh(\sqrt{\lambda+1/4} x) + Be^{-x/2}\sinh(\sqrt{\lambda+1/4} x)$$

$$G(y) =  Ce^{-y/2}\cos(\sqrt{\lambda-1/4} y) + De^{-y/2}\sin(\sqrt{\lambda-1/4} y)$$


Then initial conditions impliy that $$C=0$$, $$A=0$$, and $$\sqrt{\lambda-1/4} = n\pi$$ for some integer $$n$$.  This means $$\lambda = n^2\pi^2+1/4$$
Then without loss of generality, we can take $$B=D=1$$.  This gives us the fundamental family of solutions

$$u_n(x,y) = e^{-(x+y)/2}\sinh(\sqrt{n^2\pi^2 + 1/2}x)\sin(n\pi y).$$


**Problem 7:**

* (A) State Kirchhoff's Formula

* (B) Determine the spherical mean of 

$$f(x,y,z) = x^4 + xyz.$$

**Solution:**

* (A) $$u(x,y,z,t) = \overline f(x,y,z,ct) + ct\overline f_r(x,y,z,ct) + t\overline g(x,y,z,ct).$$

* (B) Since $$xyz$$ is harmonic, it is its own spherical mean.  Moreover

$$\begin{align}
\overline{x^4}
  &= \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi (x + r\sin\phi\cos\theta)^4 \sin\phi d\phi d\theta\\
  &= \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi x^4\sin\phi + 4x^3r\sin^2\phi\cos\theta + 6x^2r^2\sin^3\phi\cos^2\theta + 4xr^3\sin^4\phi\cos^3\theta + r^4\sin^5\phi\cos^4\theta d\phi d\theta\\
  &= \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi x^4\sin\phi + 6x^2r^2\sin^3\phi\cos^2\theta + r^4\sin^5\phi\cos^4\theta d\phi d\theta\\
  &= \frac{1}{4\pi}\int_0^\pi 2\pi x^4\sin\phi + \pi 6x^2r^2\sin^3\phi + (3\pi/4)r^4\sin^5\phi d\phi d\theta\\
  &= x^4 + 2x^2r^2 + r^4/5
\end{align}$$

**Problem 8:**

* (A) Write down the Green's function for the Laplacian on the unit disk 

* (B) Use (A) and the method of virtual images to determine a Greens function for the upper half unit disk

$$\Omega = \{(r,\theta): 0 < r < 1,\ \ 0 < \theta < \pi\}.$$

**Solution:**

* (A) A Green's function for the unit disk is

$$G(r,\theta; r',\theta')
= (\frac{1}{2\pi}\ln \left[\sqrt{r^2 + (r')^2 - 2rr'\cos(\theta-\theta')}\right]
- (\frac{1}{2\pi}\ln \left[\sqrt{r^2 + (1/r')^2 - 2r(1/r')\cos(\theta-\theta')}\right]
$$

* (B) Using the Green's function of the previous paragraph, we can make a gren's function for the upper half disk by combining the Green's function for the point $$(r',\theta')$$ and the virtual point $$(r',-\theta')$$ reflected across the $$y$$-axis.
Therefore a Green's function is given by

$$G(r,\theta; r',\theta') - G(r,\theta; r',-\theta').$$


