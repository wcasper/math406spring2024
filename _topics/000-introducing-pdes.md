---
layout: page
title: Introducing Parial Differential Equations
---

### Basic Equations

A **partial differential equation** is a differential equation which defines a relationship between a function and its **partial derivatives**.
While we will be interested in general with establishing a general theory of these equations, we will be especially interested in three main examples whose origins come from the physics of heat transfer, wave motion, and electrodynamics.

Notationally, there are many different ways of expressing partial derivatives and in practice we will use many of these interchangeably.  For example $\frac{\partial u}{\partial x}$, $\partial_x u$, $\frac{\partial}{\partial x}u$ and $u_x$ will all be ways that we express partial derivatives.

## The Heat Equation

The **heat equation** describes how the temperature of a material $T(x,y,z,t)$ in three dimensional space at position $(x,y,z)$ and time $t$ changes.  Intuitively, heat spreads out from very hot spots and migrates toward very cold spots, so in particular the value of $T$ will change over time.  Exactly how this change happens is described by **Fourier's Law**, which says that the change will be proporional to the negative temperature gradient.

$$T_t = -k (T_{xx} + T_{yy} + T_{zz})$$

This sort of equation arises in many more contexts then heat, such as Brownian motion in probability theory.

## The Wave Equation

The **wave equation** describes how 

