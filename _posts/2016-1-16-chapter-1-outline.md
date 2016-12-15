---
layout: post
title: "Chapter 5 Outline"
categories: [content]
tags: [content]
description: Integrals
---
* [Section 5.1 - Areas and Distances](#s1)
* [Section 5.2 - The Definite Integral](#s2)
* [Section 5.3 - The Fundamental Theorem of Calculus](#s3)
* [Section 5.4 - Indefinite Integrals and the Net Change Theorem](#s4)
* [Section 5.5 - The Substitution Rule](#s5)

<div id='s1'/>
# Section 5.1 - Areas and Distances
* Areas of complex shapes are generally found by approximating with smaller, simpler shapes.
* Suppose that $f$ is continuous on $[a,b]$ and that for any given $n$, $x_0,\dots,x_n$ is a partition of $[a,b]$ into subintervals of equal size. We define $\Delta x = x_1-x_0 = \frac{b-a}{n}$. Then the area of the region that lies under the graph of $f$ is
	* $ A = \lim_{n\to\infty}R_n = \lim_{n\to\infty}\left(f(x_1)\Delta x + \dots + f(x_n)\Delta x\right) $
	* $ A = \lim_{n\to\infty}L_n = \lim_{n\to\infty}\left(f(x_0)\Delta x + \dots + f(x_{n-1})\Delta x\right) $
* Written in sigma notation, the above are:
	$$ A = \lim_{n\to\infty}\sum_{i=1}^n f(x_i)\Delta x = \lim_{n\to\infty}\sum_{i=0}^{n-1} f(x_i)\Delta x $$
* Distances under constant velocity are computed as $d = v \times t$. If velocity is allowed to vary, then we compute distance travelled using a Riemann sum.
	$$ d = \lim_{n\to\infty}\sum_{i=1}^n v(t_i) \Delta t $$

<div id='s2'/>
# Section 5.2 - The Definite Integral
* Suppose that $f$ is defined for $a\leq x\leq b$. For each $n$, divide the interval into $n$ subintervals of equal width $\Delta x = \frac{b-a}{n}$ and choose sample points $x_i*$ from each subinterval $[x_{i-1},x_i]$. The definite integral of $f$ from $a$ to $b$ is defined as the following limit, provided that the limit exists and gives the same value for any choice of representatives.
	$$ \int_a^b f(x)\,dx = \lim_{n\to\infty}\sum_{i=1}^n f(x_i*)\Delta x $$
	* The definite integral is a number, not a function of $x$.
	* It is possible to generalize this definition by removing the requirement that subintervals have equal width.
	* If $f$ takes on negative values, then $\int_a^b f(x)\,dx$ is a *signed* area.
	* The definitel integral of $f$ is not always defined.
* **Theorem** if $f$ is continuous on $[a,b]$ or has only a finite number of jump discontinuities, then $\int_a^b f(x)\,dx$ exists.
* **Theorem** if $f$ is integrable on $[a,b]$, then we can use the right-endpoints as representatives when computing a definite integral. I.e. $x_i* = x_i$.
* The Midpoint Rule: When a limit of Riemann sums is difficult or impossible to compute, it may be advantageous to approximate the definite integral with a large Riemann sum. In these cases it is usually better to use a midpoint as a representative instead of the right endpoint. I.e. $x_i* = \overline{x_i} = (x_{i-1} + x_i)/2$.
* **Theorem** Properties of the definite integral:
	* $\int_a^b c\, dx = c(b-a)$
	* $\int_a^b \left(f(x) \pm g(x)\right)\,dx = \int_a^b f(x)\,dx \pm \int_a^b g(x)\,dx$
	* $\int_a^b c\cdot f(x)\,dx = c\int_a^b f(x)\,dx$
	* if $f(x)\geq g(x)$ for $a\leq x\leq b$ then $\int_a^b f(x)\,dx \geq \int_a^b g(x)\,dx$
	* if $m\leq f(x)\leq M$ for $a\leq x\leq b$ then $m(b-a)\leq \int_a^b f(x)\,dx\leq M(b-a)$

<div id='s3'/>
# Section 5.3 - The Fundamental Theorem of Calculus
* An **accumulation function** for the function $f$ is a function of the form $F(x) = \int_a^x f(t)\,dt$.
* If $F$ is an accumulation function for $f$, then $\int_a^b f(x)\,dx = F(b) - F(a)$.
* **Fundamental Theorem Part 1** If $f$ is continuous on $[a,b]$, then its accumulation function is continuous and differentiable. Moreover $F'(x) = f(x)$.
* **Fundamental Theorem Part 2** If $f$ is continuous on $[a,b]$, then $\int_a^b f(x)\,dx = F(b)-F(a)$ where $F$ is any antiderivative of $f$.

<div id='s4'/>
# Section 5.4 - Indefinite Integrals and the Net Change Theorem
* $\int f(x)\,dx = F(x) + C$ means that $F'(x) = f(x)$.
* The indefinite integral is always a family of functions.
* **Net Change Theorem** The integral of a rate of change is the net change:
	$$ \int_a^b F'(x) = F(b) - F(a) $$
* See the table on page 398 of your book for several indefinite integrals that you should know.

<div id='s5'/>
# Section 5.5 - The Substitution Rule
* Let $u = g(x)$ be a differentiable function so that $du=g'(x)dx$. If the range of $u$ is an interval $I$ and $f$ is differentiable on $I$, then the substitution rule states that $\int f(u)\,du = F(u) + C$ where $F$ is an antiderivative of $f$.
* If $u = g(x)$ where $g'(x)$ is continuous on $[a,b]$ and $f is continuous on the range of $u=g(x)$, then $\int_a^b f(g(x))g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$.
* Suppose that $f$ is continuous on $[-a,a]$.
	* If $f$ is an even function then $\int_{-a}^a f(x)\,dx = 2\int_0^a f(x)\,dx$.
	* If $f$ is an odd function then $\int_{-a}^a f(x)\,dx = 0$.