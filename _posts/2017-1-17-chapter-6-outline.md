---
layout: post
title: "Chapter 6 Outline"
categories: [content]
tags: [content]
description: Applications of Integration
---
* [Section 6.1 - Areas Between Curves](#s1)
* [Section 6.2 - Volumes](#s2)
* [Section 6.3 - Volumes by Cylindrical Shells](#s3)
* [Section 6.4 - Work](#s4)
* [Section 6.5 - Average Value of a Function](#s5)

<div id='s1'/>
# Section 6.1 - Areas Between Curves
In the simplest case, we have $0\leq g(x)\leq f(x)$ on the interval $(a,b)$. Then the area between the curves $y=g(x)$, $y=f(x)$, $x=a$, and $x=b$ is given by $\int_a^b (f(x)-g(x))\,dx$. This also works without the assumption that $0\leq f(x)$ because we can approximate the area with a Riemann sum by partitioning the interval $(a,b)$. The height of each rectangle will be $f(x_i)-g(x_i)$ and so $A_i = (f(x_i)-g(x_i))\Delta x$, as depicted in the picture below. The total area is approximated as $\sum_{i=1}^n A_i$, and as $\Delta x\to 0$ (i.e. as $n\to\infty$), this Riemann sum turns into the integral previously described.

{% include image.html path="6.1.02.png" path-detail="6.1.02.hd.png" alt="Diagram of the area between two curves." %}

### Integrating an absolute value
Often it is not the case that one function is larger than the other on the entire interval. In this case, the height of the rectangle is given by $\vert f(x_i)-g(x_i)\vert$. There is no shortcut for integrating $\int_a^b\vert f(x)-g(x)\vert\,dx$. We have to break up $(a,b)$ into all the intervals where $f(x)\leq g(x)$ and all the intervals where $g(x)\leq f(x)$. This can be done by solving $f(x)=g(x)$ and either (a) making a sign chart, or (b) looking at the graph. See the figure below.

{% include image.html path="6.1.03.png" path-detail="6.1.03.hd.png" alt="Diagram of the area between two curves." %}

In the above, $a=0$, $b=4\pi$, $f(x)=x^2\sin(x)$ and $g(x)=x^2$. Solving $f(x)=g(x)$ yields $x=0,\pi,2\pi,3\pi,4\pi$. So the area between the curves is given by:

$$\int_0^\pi (f(x)-g(x))\,dx + \int_\pi^{2\pi} (g(x)-f(x))\,dx + \int_{2\pi}^{3\pi} (f(x)-g(x))\,dx + \int_{3\pi}^{4\pi} (g(x)-f(x))\,dx$$

### Integrating along the $y$-axis
In some situations, a region is better described by considering $x$ as a function of $y$. Consider *Example 6* from your book. We want to find the area enclosed by the line $y = x-1$ and the parabola $y^2 = 2x+6$.

{% include image.html path="6.1.04.png" path-detail="6.1.04.hd.png" alt="Example 6 integrating on the x-axis." %}

We *could* set this integral up using $f(x) = \sqrt{2x+6}$, $g(x)=-\sqrt{2x+6}$ and $h(x)=x-1$.

{% include image.html path="6.1.04.png" path-detail="6.1.04.hd.png" alt="Example 6 integrating on the x-axis." %}

The area bound by the curves is then given by:

$$\int_{-3}^{-1}(f(x)-g(x))\,dx + \int_{-1}^4 (f(x)-h(x))\,dx.$$

But we can simplify the whole process by integrating along the $y$-axis instead of the $x$-axis.

{% include image.html path="6.1.05.png" path-detail="6.1.05.hd.png" alt="Example 6 integrating on the y-axis." %}

Then the area bound by the curves is given by the much simpler integral:

$$\int_{-2}^4 \left((y+1) - (\frac{y^2}{2} - 3)\right)\,dy$$

<div id='s2'/>
# Section 6.2 - Volumes
{% include image.html path="6.2.01.png" path-detail="6.2.01.hd.png" alt="Solid of revolution." %}
{% include image.html path="6.2.02.png" path-detail="6.2.02.hd.png" alt="Solid of revolution." %}
{% include image.html path="6.2.03.png" path-detail="6.2.03.hd.png" alt="Solid of revolution." %}

<div id='s3'/>
# Section 6.3 - Volumes by Cylindrical Shells
{% include image.html path="6.3.01.png" path-detail="6.3.01.hd.png" alt="Method of cylindric shells." %}

<div id='s4'/>
# Section 6.4 - Work

<div id='s5'/>
# Section 6.5 - Average Value of a Function
