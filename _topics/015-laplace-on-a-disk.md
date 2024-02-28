---
layout: page
title: Laplace on a Disk
---



We want to find a solution of the Dirichlet boundary value problem for Laplace's equation on a disk

$$u_{xx} + u_{yy} = 0,\ \ x^2+y^2 < R,$$

$$u(x,y) = f(x,y),\ \ x^2+y^2 = R.$$

To solve this problem, we must convert the Laplacian operator to polar coordiates.
Then, when we are in polar coordinates, we can again use separation of variables.

## Laplacian in polar

The relationship between polar coordinates $$(r,\theta)$$ and Cartesian coordinates $$(x,y)$$ is

$$x = r\cos\theta,\ \ y = r\sin\theta$$

or alternatively

$$r = \sqrt{x^2+y^2},\ \ \theta = \tan^{-1}(y/x).$$

It follows from the chain rule in two dimensions that

$$\begin{align}
\frac{\partial}{\partial_x}
  & = \frac{\partial r}{\partial x}\frac{\partial}{\partial r} + \frac{\partial\theta}{\partial x}\frac{\partial}{\partial\theta}\\
  & = \frac{x}{\sqrt{x^2+y^2}}\frac{\partial}{\partial r} + \frac{-y}{x^2+y^2}\frac{\partial}{\partial\theta}\\
  & = \cos\theta\frac{\partial}{\partial r} - \frac{1}{r}\sin\theta\frac{\partial}{\partial\theta}
\end{align}$$

and also

$$\begin{align}
\frac{\partial}{\partial_y}
  & = \frac{\partial r}{\partial y}\frac{\partial}{\partial r} + \frac{\partial\theta}{\partial x}\frac{\partial}{\partial\theta}\\
  & = \frac{y}{\sqrt{x^2+y^2}}\frac{\partial}{\partial r} + \frac{x}{x^2+y^2}\frac{\partial}{\partial\theta}\\
  & = \sin\theta\frac{\partial}{\partial r} + \frac{1}{r}\cos\theta\frac{\partial}{\partial\theta}.
\end{align}$$

Therefore

$$\begin{align}
\frac{\partial^2}{\partial x^2}
 & = \left(\cos\theta\frac{\partial}{\partial r} - \frac{1}{r}\sin\theta\frac{\partial}{\partial\theta}\right)^2\\
 & = \cos\theta\frac{\partial}{\partial r}\cos\theta\frac{\partial}{\partial r} - \cos\theta\frac{\partial}{\partial r}\frac{1}{r}\sin\theta\frac{\partial}{\partial\theta}\\
 & - \frac{1}{r}\sin\theta\frac{\partial}{\partial\theta}\cos\theta\frac{\partial}{\partial r} + \frac{1}{r}\sin\theta\frac{\partial}{\partial\theta}\frac{1}{r}\sin\theta\frac{\partial}{\partial\theta}\\
 & = \cos^2\theta\frac{\partial^2}{\partial r^2} - \frac{2}{r}\sin\theta\cos\theta\frac{\partial}{\partial r}\frac{\partial}{\partial\theta} + \frac{2}{r^2}\sin\theta\cos\theta\frac{\partial}{\partial\theta} + \frac{1}{r}\sin^2\theta\frac{\partial}{\partial r} + \frac{1}{r^2}\sin^2\theta\frac{\partial^2}{\partial\theta^2},
\end{align}$$

and also

$$\begin{align}
\frac{\partial^2}{\partial y^2}
  & = \left(\sin\theta\frac{\partial}{\partial r} + \frac{1}{r}\cos\theta\frac{\partial}{\partial\theta}\right)^2\\
  & = \sin\theta\frac{\partial}{\partial r}\sin\theta\frac{\partial}{\partial r} + \sin\theta\frac{\partial}{\partial r}\frac{1}{r}\cos\theta\frac{\partial}{\partial\theta}\\
  & + \frac{1}{r}\cos\theta\frac{\partial}{\partial\theta}\sin\theta\frac{\partial}{\partial r} + \frac{1}{r}\cos\theta\frac{\partial}{\partial\theta}\frac{1}{r}\cos\theta\frac{\partial}{\partial\theta}\\
 & = \sin^2\theta\frac{\partial^2}{\partial r^2} + \frac{2}{r}\sin\theta\cos\theta\frac{\partial}{\partial r}\frac{\partial}{\partial\theta} - \frac{2}{r^2}\sin\theta\cos\theta\frac{\partial}{\partial\theta} + \frac{1}{r}\cos^2\theta\frac{\partial}{\partial r} + \frac{1}{r^2}\cos^2\theta\frac{\partial^2}{\partial\theta^2}.
\end{align}$$

Adding these together, we find the expression for the Laplacian in polar coordinates

$$ \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} = 
\frac{\partial^2}{\partial r^2} + \frac{1}{r}\frac{\partial}{\partial r} + \frac{1}{r^2}\frac{\partial^2}{\partial\theta^2}.$$

Using this, we can reexpress our Dirichlet problem for Laplace's equation on a disk as

$$u_{rr} + \frac{1}{r}u_r + \frac{1}{r^2}u_{\theta\theta} = 0,\ \ 0 < r < R$$

with the boundary condition that

$$u(R,\theta) = h(\theta)$$ 

for some function $$h(\theta)$$ related to the original boundary condition function by $$h(\theta) = f(R\cos\theta,R\sin\theta)$$.

## Solving Dirichlet on a Disk

Now to solve the Dirichlet problem on the disk

$$u_{rr} + \frac{1}{r}u_r + \frac{1}{r^2}u_{\theta\theta} = 0,\ \ 0 < r < R,\ \ u(R,\theta) = h(\theta)$$

we again apply separation of variables.  We look for a solution of the form $$u(r,\theta) = F(r)G(\theta)$$.  Inserting this into the equation, we geta

$$F''(r)G(\theta) + \frac{1}{r}F'(r)G(\theta) + \frac{1}{r^2}F(r)G''(\theta) = .$$

Dividing above by $$F(r)G(\theta)$$, we obtain

$$\frac{F''(r)}{F(r)}  + \frac{1}{r}\frac{F'(r)}{F(r)} + \frac{1}{r^2}\frac{G''(\theta)}{G(\theta)} = 0.$$

Putting all of the $$\theta$$ terms on the right side of the equality leads to

$$r^2\frac{F''(r)}{F(r)}  + r\frac{F'(r)}{F(r)} = - \frac{G''(\theta)}{G(\theta)}.$$

It follows that both sides must be equal to a constant $$\lambda^2$$.  Equivalently

$$G''(\theta) + \lambda^2G(\theta) = 0$$

and also

$$r^2F''(r) + rF'(r) = \lambda^2 F(r).$$

If $$\lambda\neq 0$$, then the general solutions of each equation are

$$G(\theta) = A\cos(\lambda\theta) + B\sin(\lambda\theta)$$

and also

$$F(r) = Cr^\lambda + Dr^{-\lambda}.$$

Not all values of $$\lambda$$ are possible.  Since we are on a circle, our solutions must be periodic in $$\theta$$ with period $$2\pi$$, so $$\lambda = n$$ for some integer $$n$$.
Also, our solution should be continuous inside the disk, so we must have $$D=0$$.

In the special case that $$\lambda = 0$$, the general solution is

$$G(\theta) = A + B\theta$$

and also

$$F(r) = C + D\ln r.$$

By periodicity and continuity, we see $$B=0$$ and $$D=0$$.
This leads to the collection of **fundamental solutions on the disk**

$$r^{n}\cos(n\theta),\ \ \ r^n\sin(n\theta),\ \ n\in\mathbb{N}.$$

By the superposition principle, an arbitrary linear combination of these fundamental solutions

$$u(r,\theta) = \sum_{n=0}^\infty \widetilde A_n r^n\cos(n\theta) + \sum_{n=1}^\infty \widetilde B_nr^n\sin(n\theta)$$

is also a solution of Laplace's equation on the disk.
The value of this solution the boundary is 

$$u(R,\theta) = \sum_{n=0}^\infty \widetilde A_n R^n\cos(n\theta) + \sum_{n=1}^\infty \widetilde B_nr^n\sin(n\theta).$$

If we take $$A_n$$ and $$B_n$$ to be the coefficients in the Fourier series expansion of $$h(\theta)$$

$$h(\theta) = \sum_{n=0}^\infty A_n\cos(n\theta) + \sum_{n=1}^\infty B_n\sin(n\theta),$$

then taking $$\widetilde A_n = A_n/R^n$$ and $$\widetilde B_n = B_n/R^n$$ gives us a solution of the Dirichlet problem for Laplace's equation on the disk


$$u(r,\theta) = \sum_{n=0}^\infty A_n (r/R)^n\cos(n\theta) + \sum_{n=1}^\infty B_n(r/R)^n\sin(n\theta).$$


## Poisson Summation Formula

It turns out that there's a beautiful way to express solutions of the Dirichlet problem for Laplace's equation on a disk using a convolution-type integral with a certain function called the Poisson kernel.
To see this, recall the expressions for the coefficients in the sine and cosine series expansions of $$h(\theta)$$:

$$A_n = \frac{1}{2\pi}\int_0^{2\pi}h(\phi)\cos(n\phi)d\phi\ \ \text{and}\ \ B_n = \frac{1}{2\pi}\int_0^{2\pi}h(\phi)\sin(n\phi)d\phi.$$

Inserting this into our solution above

$$\begin{align}
u(r,\theta)
  & = \sum_{n=0}^\infty A_n (r/R)^n\cos(n\theta) + \sum_{n=1}^\infty B_n(r/R)^n\sin(n\theta)\\
  & = \sum_{n=0}^\infty \frac{1}{2\pi}\int_0^{2\pi}h(\phi)\cos(n\phi)d\phi\cdot (r/R)^n\cos(n\theta) + \sum_{n=1}^\infty \frac{1}{2\pi}\int_0^{2\pi}h(\phi)\sin(n\phi)d\phi\cdot (r/R)^n\sin(n\theta)\\
  & = \frac{1}{2\pi}\int_0^{2\pi} \left(1 + \sum_{n=1}^\infty (r/R)^n(\cos(n\phi)\cos(n\theta) + \sin(n\phi)\sin(n\theta))\right)h(\phi)d\phi\\
  & = \frac{1}{2\pi}\int_0^{2\pi} \left(1 + \sum_{n=1}^\infty (r/R)^n\cos(n(\phi-\theta))\right)h(\phi)d\phi\\
  & = \frac{1}{2\pi}\int_0^{2\pi} \text{Re}\left(1 + \sum_{n=1}^\infty (r/R)^ne^{in(\phi-\theta)}\right)h(\phi)d\phi\\
  & = \frac{1}{2\pi}\int_0^{2\pi} \text{Re}\frac{1}{1-(r/R)e^{i(\phi-\theta)}}h(\phi)d\phi\\
  & = \frac{1}{2\pi}\int_0^{2\pi} \text{Re}\frac{R^2-r^2}{R^2 -2rR\cos(\theta-\phi) + r^2}h(\phi)d\phi
\end{align}$$

In other words, for the **Poisson kernel**

$$P(r,\theta) = \frac{1}{2\pi}\frac{1-r^2}{1 -2r\cos(\theta) + r^2}$$

the solution of Laplace's equation on the disk

$$u_{rr} + \frac{1}{r}u_r + \frac{1}{r^2}u_{\theta\theta} = 0,\ \ 0 < r < R,\ \ u(R,\theta) = h(\theta)$$

is given by the convolution

$$u(r,\theta) = \int_{0}^{2\pi} P(r/R,\theta-\phi)h(\phi)d\phi.$$


