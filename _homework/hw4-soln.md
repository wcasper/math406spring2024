---
layout: page
title: Homework 4 Solutions
permalink: /homework/hw4-soln
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

Determine the expression for the Laplacian operator

$$\Delta = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$$

in spherical coordinates.

**Solution:**

To simplify the calculation, we first convert to cylindrical coordinates, which we already managed in class.
This gives the Laplacian

$$\Delta = \frac{\partial^2}{\partial r^2} + \frac{1}{r}\frac{\partial}{\partial r} + \frac{1}{r^2}\frac{\partial^2}{\partial \theta^2} + \frac{\partial^2}{\partial z^2}.$$

Then to get to spherical coordinates, we need to change $$r$$ and $$z$$ into $$\rho$$ and $$\phi$$, using the conversion

$$z=\rho\cos\phi,\quad\quad r = \rho\sin\phi,$$

equivalently

$$\rho = \sqrt{r^2+z^2},\quad\quad \tan\phi = \frac{r}{z}.$$


Under these coordinate changes,

$$\begin{align}
\frac{\partial}{\partial z}
  & = \frac{\partial \rho}{\partial z}\frac{\partial}{\partial \rho} +  \frac{\partial \phi}{\partial z}\frac{\partial}{\partial \phi}\\
  & = \cos\phi\frac{\partial}{\partial \rho} -  \frac{\sin\phi}{\rho}\frac{\partial}{\partial \phi}\\
\frac{\partial}{\partial r}
  & = \frac{\partial \rho}{\partial r}\frac{\partial}{\partial \rho} +  \frac{\partial \phi}{\partial r}\frac{\partial}{\partial \phi}\\
  & = \sin\phi\frac{\partial}{\partial \rho} +  \frac{\cos\phi}{\rho}\frac{\partial}{\partial \phi}.
\end{align}$$

Therefore

$$\begin{align}
\frac{\partial^2}{\partial z^2}
  & = \left(\cos\phi\frac{\partial}{\partial \rho} -  \frac{\sin\phi}{\rho}\frac{\partial}{\partial \phi}\right)^2\\
  & = \cos^2\phi\frac{\partial^2}{\partial \rho^2} +  \frac{\sin^2\phi}{\rho^2}\frac{\partial^2}{\partial \phi^2}\\
  & - 2\frac{\sin\phi\cos\phi}{\rho}\frac{\partial^2}{\partial \rho\partial \phi} + \frac{\sin\phi\cos\phi}{\rho^2}\frac{\partial}{\partial \phi} + \frac{\sin^2\phi}{\rho}\frac{\partial}{\partial\rho},
\end{align}$$

and also

$$\begin{align}
\frac{\partial^2}{\partial r^2}
  & = \left(\sin\phi\frac{\partial}{\partial \rho} +  \frac{\cos\phi}{\rho}\frac{\partial}{\partial \phi}\right)^2\\
  & = \sin^2\phi\frac{\partial^2}{\partial \rho^2} +  \frac{\cos^2\phi}{\rho^2}\frac{\partial^2}{\partial \phi^2}\\
  & + 2\frac{\sin\phi\cos\phi}{\rho}\frac{\partial^2}{\partial \rho\partial \phi} - \frac{\sin\phi\cos\phi}{\rho^2}\frac{\partial}{\partial \phi} + \frac{\cos^2\phi}{\rho}\frac{\partial}{\partial\rho}.
\end{align}$$

This means

$$
\frac{\partial^2}{\partial r^2} + \frac{\partial^2}{\partial z^2}
   = \frac{\partial^2}{\partial \rho^2} +  \frac{1}{\rho^2}\frac{\partial^2}{\partial \phi^2} + \frac{1}{\rho}\frac{\partial}{\partial\rho}.
$$

and also

$$
\frac{1}{r}\frac{\partial}{\partial r} + \frac{1}{r^2}\frac{\partial^2}{\partial \theta^2}
  = \frac{1}{\rho}\frac{\partial}{\partial \rho} +  \frac{1}{\rho\tan\phi}\frac{\partial}{\partial \phi} + \frac{1}{\rho^2\sin^2\phi}\frac{\partial^2}{\partial \theta^2}
$$

Putting this together, we get the Laplacian in spherical coordinates:

$$\begin{align}
\Delta 
  & = \frac{\partial^2}{\partial \rho^2} +  \frac{1}{\rho^2}\frac{\partial^2}{\partial \phi^2} + \frac{2}{\rho}\frac{\partial}{\partial\rho}\\
  & +  \frac{1}{\rho\tan\phi}\frac{\partial}{\partial \phi} + \frac{1}{\rho^2\sin^2\phi}\frac{\partial^2}{\partial \theta^2}
\end{align}$$

# Problem 2

Find the Green's function for the Laplacian and the Poisson kernel for the ball $$B_R(0,0,0) = \{(x,y,z): x^2+y^2+z^2 < R^2\}$$  of radius $$R$$ centered at the origin.

**Solution:**
The fundamental solution for Laplace's equation in $$\mathbb{R}^3$$ is

$$\Phi(x,y,z;x',y',z') = \frac{-1}{4\pi\sqrt{(x-x')^2+(y-y')^2+(z-z')^2}}.$$

This can also be written in spherical coordinates, using the Law of Cosines as:

$$\Phi(\rho,\theta,\phi;\rho',\theta',\phi') = \frac{1}{4\pi\sqrt{\rho^2+(\rho')^2 - 2\rho\rho'\cos(\mu)}},$$

where here $$\mu$$ is the angle between the vectors $$(x,y,z)$$ and $$(x',y',z')$$, defined by

$$\cos\mu = \sin^2\phi(\cos^2\theta+\sin^2\theta) + \cos^2\phi.$$

Using the method of reflections and our motivation from the Green's function for the disk, we guess that the Green's function has the form

$$\begin{align}
G(\rho,\theta,\phi;\rho',\theta',\phi')
  & = \Phi(\rho,\theta,\phi;\rho',\theta',\phi') - \frac{R}{\rho'}\Phi(\rho,\theta,\phi;R^2/\rho',\theta',\phi')\\
  & = \frac{-1}{4\pi\sqrt{\rho^2+(\rho')^2 - 2\rho\rho'\cos(\mu)}} + \frac{R}{\rho'}\frac{1}{4\pi\sqrt{\rho^2+(R^2/\rho')^2 - 2R^2\rho/\rho'\cos(\mu)}}\\
  & = \frac{-1}{4\pi\sqrt{\rho^2+(\rho')^2 - 2\rho\rho'\cos(\mu)}} + \frac{1}{4\pi\sqrt{\rho^2(\rho'/R)^2 + R^2 - 2\rho\rho'\cos(\mu)}}.
\end{align}$$

This is a linear combination of solutions to Poisson's equation, and satisfies

$$\Delta G = \delta(\rho-\rho')\delta(\theta-\theta')\delta(\phi-\phi'),\ \ \ 0 < \rho < R,$$

and when $$\rho = R$$, the expression is identically zero, so it is a Green's function for $$B_R(0,0,0)$$.

The Poisson equation is then

$$\begin{align}
P
  & = \nabla' G\cdot \hat n' = \nabla' G\cdot \hat{\rho'} = \frac{\partial}{\partial \rho'}G\\
  & = \frac{\rho'-\rho\cos(\mu)}{4\pi[\rho^2+(\rho')^2 - 2\rho\rho'\cos(\mu)]^{3/2}} - \frac{\rho'\rho^2/R^2-\rho\cos(\mu)}{4\pi[\rho^2(\rho'/R)^2 + R^2 - 2\rho\rho'\cos(\mu)]^{3/2}}.
\end{align}$$

We are interested the value on the boundary only, ie. where $$\rho' = R$$.  Plugging this in, we get the Poisson kernel

$$
P  = \frac{1}{4\pi R}\frac{R^2 - \rho^2}{[\rho^2+R^2 - 2\rho R\cos(\mu)]^{3/2}}
$$

# Problem 3

Find a Green's function for each of the following operators

* (a) The differential operator $$L = \partial_x^3$$ on the domain $$\Omega = (0,\infty) \subseteq \mathbb R$$
* (b) The diffusion operator $$L = \partial_t - \partial_x^2$$ on the domain $$\Omega = \{(x,t): 0 < x < L,\ \ 0 < t < \infty\}$$.

**Solution:**

* (a) We want to find $$G(x,t)$$ with $$G(0,t) = 0$$ and

$$G'''(x,t) = \delta(x-t).$$

Integrating this once, we get

$$G''(x,t) = \int_0^x  \delta(y-t)dy = H(x-t)$$

Doing this again, we get

$$G'(x,t) = \int_0^x  1_{[0,\infty)}(y-t)dy = (x-t)H(x-t)$$

and finally

$$G(x,t) = \int_0^x  1_{[0,\infty)}(y-t)dy = \frac{1}{2}(x-t)^2 H(x-t)$$

* (b)  A solution of

$$LG(x,t;x',t') = \delta(x-x')\delta(t-t')$$

on $$\Omega$$ is determined by our usual method of solving the nonhomogeneous heat equation.

First we write 

$$\delta(x-x')\delta(t-t') = \sum_{n=1}^\infty \phi_n(t)\sin(n\pi x/L)$$

where here

$$\phi_n(t) = \frac{2}{L}\int_0^L \delta(x-x')\delta(t-t') \sin(n\pi x/L) dx = \frac{2}{L}\delta(t-t')\sin(n\pi x'/L).$$

Then we calculate

$$\begin{align}
A_n(t)
  & = e^{-\frac{n^2\pi^2}{L^2}t} \int_0^t \phi_n(s)e^{\frac{n^2\pi^2}{L^2}s}ds\\
  & = \frac{2}{L}\sin(n\pi x'/L)e^{-\frac{n^2\pi^2}{L^2}t} \int_0^t \delta(s-t')e^{\frac{n^2\pi^2}{L^2}s}ds\\
  & = \frac{2}{L}\sin(n\pi x'/L)e^{-\frac{n^2\pi^2}{L^2}t}e^{\frac{n^2\pi^2}{L^2}kt'} H(t-t')\\
  & = \frac{2}{L}e^{-\frac{n^2\pi^2}{L^2}(t-t')}H(t-t')\sin(n\pi x'/L) 
\end{align}$$

Then our final solution is

$$\begin{align}
G
  & = \sum_{n=1}^\infty A_n(t)\sin\left(\frac{n\pi x}{L}\right)\\
  & = \frac{2}{L}\sum_{n=1}^\infty e^{-\frac{n^2\pi^2}{L^2}k(t-t')}H(t-t')\sin\left(\frac{n\pi x'}{L}\right)\sin\left(\frac{n\pi x}{L}\right)
\end{align}$$


# Problem 4

An **eigenfunction of the Laplacian** on a domain $$\Omega\subseteq \mathbb{R}^n$$ is a function $$u(\vec x)$$ satisfying

$$\Delta u = \lambda u,\ \ \vec x\in\Omega$$
$$u(\vec x) = 0,\ \ \vec x\in\partial\Omega$$

If such a function exists, then the associated value $$\lambda$$ is called an eigenvalue of $$\Delta$$.

* (a) Look up and explain what Bessel functions of the first and second kind are.
* (b) Use separation of variables to find the eigenfunctions and eigenvalues of the Laplacian on the disk $$\Omega = \{(x,y): x^2+y^2 < R^2\}$$.  Your answer should involve Bessel functions.
* (c) Use (b) to find an example of a nonconstant solution of the wave equation on the disk

$$u_{tt} = c^2(u_{xx}+u_{yy}),\ \ (x,y)\in \Omega,$$
$$u(x,y,t) = 0,\ \ (x,y)\in \partial\Omega.$$

**Solution:**  

See the notes on wave on a disk
* <a target="_parent" href="https://wcasper.github.io/math406spring2024/topics/029-waves-on-a-disk.html">Waves on a disk (link)</a>

# Problem 5

Find all the three dimensional plane waves, ie. all solutions of

$$u_{tt} = k^2(u_{xx}+u_{yy} + u_{zz})$$

in $$\mathbb{R}^3$$ which are of the form

$$u(x,y,z,t) = f(ax+by+cz - kt)$$

for some single-variable function.


**Solution:** This is a solution for any twice differentiable function $$f(x)$$ and any numbers $$a,b,c$$ with $$a^2+b^2 + c^2 = 1$$.



