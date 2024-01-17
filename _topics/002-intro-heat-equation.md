---
layout: page
title: Introduction to the Heat Equation
---

# The Heat Equation / Diffusion Equation

In this section, we will introduce the **heat equation**, also known as the **diffusion equation**.

## Heat

Everything in the physical world is made up of atom which are constantly bouncing around, vibrating, and interacting with nearby atoms at length scales that are on an atomic level.
The **temperature** of a gas, liquid, or solid material is a measure of how much all the atoms are scurrying about *on average* in a small region of space.
Since we are talking about the average behavior, this is actually something we can observe on a macroscopic level, using things like thermometers.
More accurately, the temperature measures the **average kinetic energy** of the molecules which make up the physical matter.

For example, consider a metal fire poker whose point we have just stuck into a fire.

<p align="center"><img widtth=300 src="fig/fire-poker.webp"/></p>

The tip will be very hot, but the length of the poker will initially be cool.
Put another way, the atoms at the tip will be vibrating very quickly, but the other atoms won't initially be affected.
However, as time goes on collisions between the fast moving atoms near the tip and the slow moving atoms in the rest of the rod will cause the latter atoms to start to move faster.
This causes heat transfer from the hot part of the rod to the cold part.

In many situations, the rate of this transfer is modeled well by **Fourier's Law**, which says that the change in temperature is proportional to its gradient.
Mathematically, we can represent different points on the fire poker with points in a finite interval $$[0,L]$$, where $$0$$ is the base of the rod and $$L$$ is the tip.
The temperature $$T(x,t)$$ of the rod at the point $$x$$ and time $$t$$ satisfies

$$T_t = kT_{xx}.$$

Here $$k$$ is a constant, which we call the coefficient of thermal conductivity, and which is a property of the material itself.
This equation is called the **one-dimensional heat equation**.

In the situation we have described, the solution to the heat equation we are looking for might be something like

$$T(x,t) = T_0 + \frac{T_1-T_0}{L}x + \sum_{k=0}^\infty c_ne^{-kn^2\pi^2t/L^2}\sin(n\pi x/L),$$

for some sequnce of values $$c_0,c_1,\dots$$ determined by the initial temperure state of the rod.

## Diffusion

A similar situation occurs when we think about **diffusion processes**.
Imagine putting a bit of dye uniformly on the surface of a long tube.
Microscopic motions of the individual water particles will cause the dye to slowly spread downwards.
The warmer the water is, the faster this expansion will take place.

If $$\rho(x,t)$$ represents the density of the dye at depth $$x$$ and time $$t$$ then $$\rho$$ satisfies the diffusion equation

$$\rho_t = D\rho_{xx},$$

where here $$D$$ is the **diffusion coefficient**, a constant whose value has to
do with the temperture and other properties of the fluid.

For the situation we just described, the initial concentration of the dye might be reasonably approximated by a Gaussian function centered at the origin

$$\rho(x,y,0) = \frac{1}{c}e^{-\frac{1}{4Dc}((x^2+y^2)},$$

where $$c$$ is a constant which adjusts how concentrated the dye is initially.

Our solution of the dispersion equation might then be something like

$$\rho(x,y,t) = \frac{1}{t+c}e^{-\frac{1}{4D(t+c)}((x^2+y^2)}.$$

{% include youtube.html id="LN0UeifPCzw?start=225&end=230;" %}


# Higher Dimensional Heat Equations

For temperature variation on a flat surface, we can instead use the **two-dimensional heat equation**

$$T_t = k(T_{xx}+T_{yy}).$$

Likewise, for temperature variation in three dimensional space, we use the **three-dimensional heat equation**

$$T_t = k(T_{xx}+T_{yy}+T_{zz}).$$

In general, we could imagine ourselves trying to solve the **$$n$$-dimensional heat equation**

$$u_t = \alpha \sum_{k=1}^n \frac{\partial^2 u}{\partial x_k^2}$$

