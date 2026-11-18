---
title: "Handout 005: Implicit Diff, Extrema, MVT — Key"
---

# 005: Implicit Differentiation, Critical Points, and the Mean Value Theorem — Answer Key

## Exercises

### Q1

**1.**

> **Stage 1 (Classification & Domain).** The relation $x^2 - xy + y^2 = 7$ defines a rotated ellipse. We seek the derivative $\frac{dy}{dx}$ in terms of $x$ and $y$.
>
> **Stage 2 (Algebraic Preparation).** Treat $y$ as a differentiable function of $x$. Apply the Product Rule to the mixed term $-xy$:
>
> $\displaystyle \frac{d}{dx}[-xy] = -\left(1 \cdot y + x \frac{dy}{dx}\right) = -y - x\frac{dy}{dx}$
>
> **Stage 3 (Core Operation).** Differentiate both sides of $x^2 - xy + y^2 = 7$ with respect to $x$:
>
> $\displaystyle 2x - \left(y + x\frac{dy}{dx}\right) + 2y\frac{dy}{dx} = 0 \;\Longrightarrow\; 2x - y - x\frac{dy}{dx} + 2y\frac{dy}{dx} = 0$
>
> Group terms containing $\frac{dy}{dx}$:
>
> $\displaystyle (2y - x)\frac{dy}{dx} = y - 2x$
>
> Divide by $(2y - x)$:
>
> $\displaystyle \frac{dy}{dx} = \frac{y - 2x}{2y - x} \quad (2y \ne x)$
>
> **Stage 4 (Interpretation & Boundary Check).** The derivative is valid at all points on the ellipse where the tangent is not vertical ($2y - x \ne 0$).
>
> Verified derivative: $\frac{dy}{dx} = \frac{y - 2x}{2y - x}$.

**2.**

> **Stage 1 (Classification & Domain).** Verify that $(2, 3)$ lies on the ellipse: $2^2 - (2)(3) + 3^2 = 4 - 6 + 9 = 7$.
>
> **Stage 2 (Algebraic Preparation).** Evaluate the denominator condition: $2y - x = 2(3) - 2 = 6 - 2 = 4 \ne 0$, so the tangent line exists and is non-vertical.
>
> **Stage 3 (Core Operation).** Evaluate the slope at $(2, 3)$:
>
> $\displaystyle m = \frac{dy}{dx}\Bigg|_{(2, 3)} = \frac{3 - 2(2)}{2(3) - 2} = \frac{3 - 4}{6 - 2} = -\frac{1}{4}$
>
> Write the point-slope equation with $x_1 = 2, y_1 = 3, m = -\frac{1}{4}$:
>
> $\displaystyle y - 3 = -\frac{1}{4}(x - 2)$
>
> Clear the fraction by multiplying both sides by $4$:
>
> $\displaystyle 4(y - 3) = -(x - 2) \;\Longrightarrow\; 4y - 12 = -x + 2 \;\Longrightarrow\; x + 4y = 14$
>
> **Stage 4 (Interpretation & Boundary Check).** Check coordinates $(2, 3)$ in the linear equation: $2 + 4(3) = 2 + 12 = 14$. Slope is $m = -\frac{1}{4}$.
>
> Verified tangent equation: $x + 4y = 14$.

### Q2

**1.**

> **Stage 1 (Classification & Domain).** The equation $x^3 + y^3 = 3xy$ defines an algebraic curve (Folium of Descartes with parameter $a = 1$).
>
> **Stage 2 (Algebraic Preparation).** Differentiate both sides with respect to $x$:
>
> $\displaystyle 3x^2 + 3y^2\frac{dy}{dx} = 3\left(y + x\frac{dy}{dx}\right) = 3y + 3x\frac{dy}{dx}$
>
> Divide by $3$: $x^2 + y^2\frac{dy}{dx} = y + x\frac{dy}{dx} \;\Longrightarrow\; (y^2 - x)\frac{dy}{dx} = y - x^2 \;\Longrightarrow\; \frac{dy}{dx} = \frac{y - x^2}{y^2 - x}$.
>
> **Stage 3 (Core Operation).** For a horizontal tangent line, set the numerator to zero:
>
> $\displaystyle y - x^2 = 0 \;\Longrightarrow\; y = x^2 \quad (\text{with } y^2 - x \ne 0)$
>
> Substitute $y = x^2$ into the curve equation:
>
> $\displaystyle x^3 + (x^2)^3 = 3x(x^2) \;\Longrightarrow\; x^3 + x^6 = 3x^3 \;\Longrightarrow\; x^6 = 2x^3$
>
> If $x = 0$, then $y = 0$. At $(0, 0)$, both numerator and denominator vanish (singular node with self-intersection).
>
> For $x \ne 0$, divide by $x^3$:
>
> $\displaystyle x^3 = 2 \;\Longrightarrow\; x = 2^{1/3} = \sqrt[3]{2}$
>
> Compute the corresponding $y$-coordinate:
>
> $\displaystyle y = x^2 = (2^{1/3})^2 = 2^{2/3} = \sqrt[3]{4}$
>
> **Stage 4 (Interpretation & Boundary Check).** Check denominator at $(\sqrt[3]{2}, \sqrt[3]{4})$: $y^2 - x = (\sqrt[3]{4})^2 - \sqrt[3]{2} = \sqrt[3]{16} - \sqrt[3]{2} = 2\sqrt[3]{2} - \sqrt[3]{2} = \sqrt[3]{2} \ne 0$.
>
> Verified horizontal tangent point: $(\sqrt[3]{2}, \sqrt[3]{4}) = (2^{1/3}, 2^{2/3})$.

**2.**

> **Stage 1 (Classification & Domain).** Vertical tangents occur where the denominator of $\frac{dy}{dx}$ equals zero while the numerator is non-zero (or equivalently, $\frac{dx}{dy} = 0$).
>
> **Stage 2 (Algebraic Preparation).** Set the denominator of $\frac{dy}{dx} = \frac{y - x^2}{y^2 - x}$ to zero:
>
> $\displaystyle y^2 - x = 0 \;\Longrightarrow\; x = y^2 \quad (\text{with } y - x^2 \ne 0)$
>
> **Stage 3 (Core Operation).** Substitute $x = y^2$ into the original curve equation:
>
> $\displaystyle (y^2)^3 + y^3 = 3(y^2)y \;\Longrightarrow\; y^6 + y^3 = 3y^3 \;\Longrightarrow\; y^6 = 2y^3$
>
> Discarding $y = 0$ (the singular node at the origin), divide by $y^3$:
>
> $\displaystyle y^3 = 2 \;\Longrightarrow\; y = 2^{1/3} = \sqrt[3]{2}$
>
> Compute the corresponding $x$-coordinate:
>
> $\displaystyle x = y^2 = (2^{1/3})^2 = 2^{2/3} = \sqrt[3]{4}$
>
> **Stage 4 (Interpretation & Boundary Check).** Check numerator at $(\sqrt[3]{4}, \sqrt[3]{2})$: $y - x^2 = \sqrt[3]{2} - 2\sqrt[3]{2} = -\sqrt[3]{2} \ne 0$. Thus $\frac{dx}{dy} = 0$, confirming a vertical tangent.
>
> Verified vertical tangent point: $(\sqrt[3]{4}, \sqrt[3]{2}) = (2^{2/3}, 2^{1/3})$.

**3.**

> **Stage 1 (Classification & Domain).** Find the non-zero point where $x = y$:
>
> $\displaystyle x^3 + x^3 = 3x(x) \;\Longrightarrow\; 2x^3 = 3x^2 \;\Longrightarrow\; 2x = 3 \;\Longrightarrow\; x = \frac{3}{2}, \; y = \frac{3}{2}$
>
> **Stage 2 (Algebraic Preparation).** Evaluate the first derivative at $\left(\frac{3}{2}, \frac{3}{2}\right)$:
>
> $\displaystyle \frac{dy}{dx}\Bigg|_{\left(\frac{3}{2}, \frac{3}{2}\right)} = \frac{\frac{3}{2} - \left(\frac{3}{2}\right)^2}{\left(\frac{3}{2}\right)^2 - \frac{3}{2}} = \frac{\frac{3}{2} - \frac{9}{4}}{\frac{9}{4} - \frac{3}{2}} = \frac{-\frac{3}{4}}{\frac{3}{4}} = -1$
>
> **Stage 3 (Core Operation).** Differentiate $\frac{dy}{dx} = \frac{y - x^2}{y^2 - x}$ with respect to $x$ using the Quotient Rule:
>
> $\displaystyle \frac{d^2y}{dx^2} = \frac{\left(\frac{dy}{dx} - 2x\right)(y^2 - x) - (y - x^2)\left(2y\frac{dy}{dx} - 1\right)}{(y^2 - x)^2}$
>
> Substitute $x = \frac{3}{2}, y = \frac{3}{2}$, and $\frac{dy}{dx} = -1$:
>
> $\displaystyle y^2 - x = \left(\frac{3}{2}\right)^2 - \frac{3}{2} = \frac{9}{4} - \frac{6}{4} = \frac{3}{4}$
>
> $\displaystyle y - x^2 = \frac{3}{2} - \left(\frac{3}{2}\right)^2 = \frac{6}{4} - \frac{9}{4} = -\frac{3}{4}$
>
> $\displaystyle \frac{dy}{dx} - 2x = -1 - 2\left(\frac{3}{2}\right) = -1 - 3 = -4$
>
> $\displaystyle 2y\frac{dy}{dx} - 1 = 2\left(\frac{3}{2}\right)(-1) - 1 = -3 - 1 = -4$
>
> Evaluate the numerator:
>
> $\displaystyle (-4)\left(\frac{3}{4}\right) - \left(-\frac{3}{4}\right)(-4) = -3 - 3 = -6$
>
> Evaluate the denominator:
>
> $\displaystyle (y^2 - x)^2 = \left(\frac{3}{4}\right)^2 = \frac{9}{16}$
>
> Compute the quotient:
>
> $\displaystyle \frac{d^2y}{dx^2} = \frac{-6}{\frac{9}{16}} = -6 \cdot \frac{16}{9} = -\frac{96}{9} = -\frac{32}{3}$
>
> **Stage 4 (Interpretation & Boundary Check).** Since $\frac{d^2y}{dx^2} = -\frac{32}{3} < 0$, the curve is strictly concave downward at the loop vertex $\left(\frac{3}{2}, \frac{3}{2}\right)$.
>
> Verified second derivative: $\frac{d^2y}{dx^2} = -\frac{32}{3}$.

### Q3

**1. Correct answer: A.**

- **A (Correct):** Satisfies both hypotheses of the Mean Value Theorem (continuous on $[a, b]$ and differentiable on $\mathopen{]}a, b\mathclose{[}$), which guarantees the existence of at least one number $c \in \mathopen{]}a, b\mathclose{[}$ satisfying $f(b) - f(a) = f'(c)(b - a)$.
- **B (Incorrect):** EVT requires a closed and bounded interval $[a, b]$; on the open interval $\mathopen{]}0, 1\mathclose{[}$, the continuous function $f(x) = x$ has neither an absolute maximum nor an absolute minimum because values approach $1$ and $0$ without ever attaining them.
- **C (Incorrect):** A local minimum can occur at a sharp corner or cusp where $f'(c)$ does not exist, such as $f(x) = |x|$ at $c = 0$. Fermat's Theorem requires differentiability as a hypothesis.
- **D (Incorrect):** MVT requires differentiability on the entire open interval $\mathopen{]}-1, 2\mathclose{[}$; a continuous function with a sharp corner such as $f(x) = |x|$ on $[-1, 2]$ does not satisfy MVT because the secant slope is $\frac{2 - 1}{2 - (-1)} = \frac{1}{3}$, while $f'(x)$ is either $-1$ or $1$, never $\frac{1}{3}$.
- **E (Incorrect):** The converse of Fermat's Theorem fails; a stationary point where $f'(c) = 0$ can be an inflection point rather than an extremum, as demonstrated by $f(x) = x^3$ at $c = 0$ where $f'(0) = 0$ but $f$ has no local extremum.


### Q4

**1.**

> **Stage 1 (Classification & Domain).** The function $f(x) = 2\cos(x) + \sin(2x)$ is a sum of trigonometric functions, continuous and differentiable on all of $\mathbb{R}$. The domain is the closed interval $\left[0, \frac{\pi}{2}\right]$.
>
> **Stage 2 (Algebraic Preparation).** Compute the derivative using the Chain Rule on $\sin(2x)$:
>
> $\displaystyle f'(x) = -2\sin(x) + 2\cos(2x)$
>
> Apply the double-angle identity $\cos(2x) = 1 - 2\sin^2(x)$:
>
> $\displaystyle f'(x) = -2\sin(x) + 2(1 - 2\sin^2(x)) = 2 - 2\sin(x) - 4\sin^2(x) = -2(2\sin^2(x) + \sin(x) - 1)$
>
> Factor the quadratic in $\sin(x)$:
>
> $\displaystyle f'(x) = -2(2\sin(x) - 1)(\sin(x) + 1)$
>
> **Stage 3 (Core Operation).** Set $f'(x) = 0$ to find critical numbers:
>
> $\displaystyle 2\sin(x) - 1 = 0 \;\Longrightarrow\; \sin(x) = \frac{1}{2} \;\Longrightarrow\; x = \frac{\pi}{6}$
>
> The factor $\sin(x) + 1 = 0 \;\Longrightarrow\; \sin(x) = -1$ has no solutions in $\left[0, \frac{\pi}{2}\right]$.
>
> Thus, the sole interior critical number in $\mathopen{]}0, \frac{\pi}{2}\mathclose{[}$ is $x = \frac{\pi}{6}$.
>
> Evaluate $f$ at the critical number:
>
> $\displaystyle f\left(\frac{\pi}{6}\right) = 2\cos\left(\frac{\pi}{6}\right) + \sin\left(\frac{\pi}{3}\right) = 2\left(\frac{\sqrt{3}}{2}\right) + \frac{\sqrt{3}}{2} = \sqrt{3} + \frac{\sqrt{3}}{2} = \frac{3\sqrt{3}}{2} \approx 2.598$
>
> Evaluate $f$ at boundary endpoints:
>
> $\displaystyle f(0) = 2\cos(0) + \sin(0) = 2(1) + 0 = 2$
>
> $\displaystyle f\left(\frac{\pi}{2}\right) = 2\cos\left(\frac{\pi}{2}\right) + \sin(\pi) = 2(0) + 0 = 0$
>
> **Stage 4 (Interpretation & Boundary Check).** Compare all values: $\left\{f(0) = 2,\; f\left(\frac{\pi}{6}\right) = \frac{3\sqrt{3}}{2},\; f\left(\frac{\pi}{2}\right) = 0\right\}$.
>
> Since $\frac{3\sqrt{3}}{2} = \sqrt{\frac{27}{4}} = \sqrt{6.75} > \sqrt{4} = 2$:
> - Absolute maximum value is $\frac{3\sqrt{3}}{2}$, occurring at $x = \frac{\pi}{6}$.
> - Absolute minimum value is $0$, occurring at the right endpoint $x = \frac{\pi}{2}$.
>
> Verified extrema: absolute maximum $\frac{3\sqrt{3}}{2}$ at $\left(\frac{\pi}{6}, \frac{3\sqrt{3}}{2}\right)$; absolute minimum $0$ at $\left(\frac{\pi}{2}, 0\right)$.

**2.**

> **Stage 1 (Classification & Domain).** The function $g(x) = x^{2/3}(5 - x)$ is continuous on all of $\mathbb{R}$. The domain is the closed interval $[-1, 5]$.
>
> **Stage 2 (Algebraic Preparation).** Expand $g(x)$ before differentiating:
>
> $\displaystyle g(x) = 5x^{2/3} - x^{5/3}$
>
> Compute $g'(x)$ using the Power Rule:
>
> $\displaystyle g'(x) = 5\left(\frac{2}{3}x^{-1/3}\right) - \frac{5}{3}x^{2/3} = \frac{10}{3x^{1/3}} - \frac{5x^{2/3}}{3} = \frac{10 - 5x}{3x^{1/3}} = \frac{5(2 - x)}{3x^{1/3}}$
>
> **Stage 3 (Core Operation).** Locate all critical numbers in the interior $\mathopen{]}-1, 5\mathclose{[}$:
> - Numerator zero: $5(2 - x) = 0 \;\Longrightarrow\; x = 2$.
> - Denominator zero: $3x^{1/3} = 0 \;\Longrightarrow\; x = 0$ (non-differentiable cusp; $g(0) = 0$ is in domain).
>
> Both $x = 0$ and $x = 2$ lie inside $\mathopen{]}-1, 5\mathclose{[}$.
>
> Evaluate $g$ at interior critical numbers:
>
> $\displaystyle g(0) = (0)^{2/3}(5 - 0) = 0$
>
> $\displaystyle g(2) = (2)^{2/3}(5 - 2) = 3 \cdot 2^{2/3} = 3\sqrt[3]{4} \approx 3(1.5874) \approx 4.762$
>
> Evaluate $g$ at boundary endpoints:
>
> $\displaystyle g(-1) = (-1)^{2/3}(5 - (-1)) = (1)(6) = 6$
>
> $\displaystyle g(5) = (5)^{2/3}(5 - 5) = 0$
>
> **Stage 4 (Interpretation & Boundary Check).** Compare values: $\left\{g(-1) = 6,\; g(0) = 0,\; g(2) = 3\sqrt[3]{4} \approx 4.762,\; g(5) = 0\right\}$.
>
> - The largest value is $6$, attained at the left boundary endpoint $x = -1$.
> - The smallest value is $0$, attained at both the interior non-differentiable critical point $x = 0$ and the right boundary endpoint $x = 5$.
>
> Verified extrema: absolute maximum value is $6$ at $x = -1$; absolute minimum value is $0$ at $x = 0$ and $x = 5$.

### Q5

**1.**

> **Stage 1 (Classification & Domain).** Let $f(x) = 2x^3 + 3x - 5$. As a polynomial, $f$ is continuous and differentiable on all of $\mathbb{R}$.
>
> **Stage 2 (Algebraic Preparation).** Apply the Intermediate Value Theorem to establish existence of at least one real root.
>
> Evaluate $f$ at test values:
>
> $\displaystyle f(0) = 2(0)^3 + 3(0) - 5 = -5 < 0$
>
> $\displaystyle f(2) = 2(2)^3 + 3(2) - 5 = 16 + 6 - 5 = 17 > 0$
>
> (Direct evaluation also shows $f(1) = 2(1) + 3(1) - 5 = 0$).
>
> Since $f(0) < 0$ and $f(2) > 0$, the Intermediate Value Theorem guarantees that there exists at least one real number $c \in \mathopen{]}0, 2\mathclose{[}$ such that $f(c) = 0$.
>
> **Stage 3 (Core Operation).** Apply Rolle's Theorem to prove uniqueness by contradiction.
>
> Assume for contradiction that $f(x) = 0$ has two distinct real roots $a$ and $b$ with $a < b$.
>
> Then $f(a) = f(b) = 0$. Since $f$ is continuous on $[a, b]$ and differentiable on $\mathopen{]}a, b\mathclose{[}$, all hypotheses of Rolle's Theorem are satisfied.
>
> By Rolle's Theorem, there must exist some number $c \in \mathopen{]}a, b\mathclose{[}$ such that $f'(c) = 0$.
>
> Compute the derivative:
>
> $\displaystyle f'(x) = 6x^2 + 3$
>
> For every real number $x$, $x^2 \ge 0$, which implies $6x^2 \ge 0$, and therefore:
>
> $\displaystyle f'(x) = 6x^2 + 3 \ge 3 > 0 \quad\text{for all } x \in \mathbb{R}$
>
> **Stage 4 (Interpretation & Boundary Check).** Because $f'(x) \ge 3$ everywhere, $f'(c) = 0$ has no real solution, contradicting the conclusion of Rolle's Theorem.
>
> Therefore, the assumption of two distinct real roots is false. The equation $2x^3 + 3x - 5 = 0$ has exactly one real root (which is $x = 1$).

**2.**

> **Stage 1 (Classification & Domain).** Let $s(t)$ represent the position of the van in miles at time $t$ in hours, where $t = 0$ corresponds to 1:00 PM.
>
> **Stage 2 (Algebraic Preparation).** Determine the elapsed time and displacement:
>
> $\displaystyle \Delta t = 42\text{ minutes} = \frac{42}{60}\text{ hours} = \frac{7}{10}\text{ hours} = 0.7\text{ hours}$
>
> $\displaystyle \Delta s = s(0.7) - s(0) = 170 - 120 = 50\text{ miles}$
>
> Compute the average velocity over the trip:
>
> $\displaystyle \bar{v} = \frac{s(0.7) - s(0)}{0.7 - 0} = \frac{50}{0.7} = \frac{500}{7} \approx 71.43\text{ mph}$
>
> **Stage 3 (Core Operation).** The position function of a moving vehicle is continuous on the closed time interval $[0, 0.7]$ and differentiable on the open interval $\mathopen{]}0, 0.7\mathclose{[}$.
>
> By the Mean Value Theorem, there exists at least one instant $c \in \mathopen{]}0, 0.7\mathclose{[}$ such that the instantaneous velocity $v(c) = s'(c)$ equals the average velocity:
>
> $\displaystyle v(c) = s'(c) = \frac{500}{7}\text{ mph} \approx 71.43\text{ mph}$
>
> **Stage 4 (Interpretation & Boundary Check).** Because $71.43\text{ mph} > 65\text{ mph}$, the driver's speedometer read at least $71.43\text{ mph}$ at time $c$, proving that the driver exceeded the $65\text{ mph}$ speed limit.

### Q6

**1.**

> **Stage 1 (Classification & Domain).** The Lemniscate of Bernoulli $(x^2 + y^2)^2 = 2a^2(x^2 - y^2)$ with $a > 0$ is an implicit fourth-degree polynomial curve.
>
> **Stage 2 (Algebraic Preparation).** Treat $y$ as a differentiable function of $x$. Differentiate both sides using the Chain Rule on both sides:
>
> $\displaystyle \frac{d}{dx}\left[(x^2 + y^2)^2\right] = 2(x^2 + y^2)\left(2x + 2y\frac{dy}{dx}\right) = 4(x^2 + y^2)\left(x + y\frac{dy}{dx}\right)$
>
> $\displaystyle \frac{d}{dx}\left[2a^2(x^2 - y^2)\right] = 2a^2\left(2x - 2y\frac{dy}{dx}\right) = 4a^2\left(x - y\frac{dy}{dx}\right)$
>
> **Stage 3 (Core Operation).** Equate derivatives and divide by $4$:
>
> $\displaystyle (x^2 + y^2)\left(x + y\frac{dy}{dx}\right) = a^2\left(x - y\frac{dy}{dx}\right)$
>
> Expand both sides:
>
> $\displaystyle x(x^2 + y^2) + y(x^2 + y^2)\frac{dy}{dx} = a^2 x - a^2 y\frac{dy}{dx}$
>
> Group terms containing $\frac{dy}{dx}$ on the left and remaining terms on the right:
>
> $\displaystyle \left[y(x^2 + y^2) + a^2 y\right]\frac{dy}{dx} = a^2 x - x(x^2 + y^2)$
>
> Factor $y$ on the left and $x$ on the right:
>
> $\displaystyle y(x^2 + y^2 + a^2)\frac{dy}{dx} = x\left[a^2 - (x^2 + y^2)\right]$
>
> Isolate $\frac{dy}{dx}$:
>
> $\displaystyle \frac{dy}{dx} = \frac{x\left[a^2 - (x^2 + y^2)\right]}{y\left[a^2 + (x^2 + y^2)\right]}$
>
> **Stage 4 (Interpretation & Boundary Check).** Since $a > 0$ and $x^2 + y^2 \ge 0$, the factor $a^2 + x^2 + y^2 \ge a^2 > 0$. The denominator vanishes only when $y = 0$.
>
> Verified derivative: $\frac{dy}{dx} = \frac{x\left[a^2 - (x^2 + y^2)\right]}{y\left[a^2 + (x^2 + y^2)\right]}$.

**2.**

> **Stage 1 (Classification & Domain).** In the first quadrant, $x > 0$ and $y > 0$. Maximum vertical displacement corresponds to a horizontal tangent line: $\frac{dy}{dx} = 0$.
>
> **Stage 2 (Algebraic Preparation).** Set the numerator of $\frac{dy}{dx}$ to zero:
>
> $\displaystyle x\left[a^2 - (x^2 + y^2)\right] = 0$
>
> Because $x > 0$ in the first quadrant, this simplifies to:
>
> $\displaystyle x^2 + y^2 = a^2$
>
> **Stage 3 (Core Operation).** Substitute $x^2 + y^2 = a^2$ into the lemniscate equation:
>
> $\displaystyle (a^2)^2 = 2a^2(x^2 - y^2) \;\Longrightarrow\; a^4 = 2a^2(x^2 - y^2)$
>
> Divide by $2a^2$:
>
> $\displaystyle x^2 - y^2 = \frac{a^2}{2}$
>
> Solve the simultaneous linear system in $x^2$ and $y^2$:
>
> $\displaystyle x^2 + y^2 = a^2 \quad\text{and}\quad x^2 - y^2 = \frac{a^2}{2}$
>
> Add the two equations:
>
> $\displaystyle 2x^2 = a^2 + \frac{a^2}{2} = \frac{3a^2}{2} \;\Longrightarrow\; x^2 = \frac{3a^2}{4} \;\Longrightarrow\; x = \frac{\sqrt{3}}{2}a$
>
> Subtract the second equation from the first:
>
> $\displaystyle 2y^2 = a^2 - \frac{a^2}{2} = \frac{a^2}{2} \;\Longrightarrow\; y^2 = \frac{a^2}{4} \;\Longrightarrow\; y = \frac{a}{2}$
>
> **Stage 4 (Interpretation & Boundary Check).** At $\left(\frac{\sqrt{3}}{2}a, \frac{a}{2}\right)$, the denominator is $y(a^2 + x^2 + y^2) = \frac{a}{2}(a^2 + a^2) = a^3 \ne 0$.
>
> Verified maximum displacement point: $(x, y) = \left(\frac{\sqrt{3}}{2}a, \frac{a}{2}\right)$.

**3.**

> **Stage 1 (Classification & Domain).** At the critical point $\left(\frac{\sqrt{3}}{2}a, \frac{a}{2}\right)$, $x^2 + y^2 = a^2$ and $\frac{dy}{dx} = 0$.
>
> **Stage 2 (Algebraic Preparation).** Let $N(x, y) = x[a^2 - (x^2 + y^2)] = a^2 x - x^3 - x y^2$ and $D(x, y) = y[a^2 + x^2 + y^2]$.
>
> By the Quotient Rule:
>
> $\displaystyle \frac{d^2y}{dx^2} = \frac{N'(x) D(x) - N(x) D'(x)}{[D(x)]^2}$
>
> At the critical point, $N(x, y) = 0$, so the second term vanishes:
>
> $\displaystyle \frac{d^2y}{dx^2} = \frac{N'(x)}{D(x)}$
>
> **Stage 3 (Core Operation).** Differentiate $N(x, y) = a^2 x - x^3 - x y^2$ with respect to $x$:
>
> $\displaystyle N'(x) = a^2 - 3x^2 - \left(y^2 + 2x y \frac{dy}{dx}\right)$
>
> Since $\frac{dy}{dx} = 0$ at this point:
>
> $\displaystyle N'(x) = a^2 - 3x^2 - y^2$
>
> Substitute $x^2 = \frac{3a^2}{4}$ and $y^2 = \frac{a^2}{4}$:
>
> $\displaystyle N'(x) = a^2 - 3\left(\frac{3a^2}{4}\right) - \frac{a^2}{4} = a^2 - \frac{9a^2}{4} - \frac{a^2}{4} = a^2 - \frac{10a^2}{4} = a^2 - \frac{5a^2}{2} = -\frac{3a^2}{2}$
>
> Evaluate the denominator at the critical point:
>
> $\displaystyle D(x, y) = y[a^2 + (x^2 + y^2)] = \frac{a}{2}[a^2 + a^2] = \frac{a}{2}(2a^2) = a^3$
>
> Compute $\frac{d^2y}{dx^2}$:
>
> $\displaystyle \frac{d^2y}{dx^2} = \frac{-\frac{3a^2}{2}}{a^3} = -\frac{3}{2a}$
>
> **Stage 4 (Interpretation & Boundary Check).** Because $a > 0$, $\frac{d^2y}{dx^2} = -\frac{3}{2a} < 0$, which confirms by the Second Derivative Test that the curve is strictly concave downward at this point, establishing a local maximum for $y(x)$.
>
> Verified second derivative: $\frac{d^2y}{dx^2} = -\frac{3}{2a}$.

**4.**

> **Stage 1 (Classification & Domain).** Find the positive $x$-intercept where $y = 0$:
>
> $\displaystyle (x^2 + 0)^2 = 2a^2(x^2 - 0) \;\Longrightarrow\; x^4 = 2a^2 x^2 \;\Longrightarrow\; x^2 = 2a^2 \;\Longrightarrow\; x = a\sqrt{2}$
>
> The first-quadrant upper loop is defined on the closed interval $[0, a\sqrt{2}]$ with $y(0) = 0$ and $y(a\sqrt{2}) = 0$.
>
> **Stage 2 (Algebraic Preparation).** Verify the three hypotheses of Rolle's Theorem for $y = y(x)$ on $[0, a\sqrt{2}]$:
> - $y(x)$ is continuous on $[0, a\sqrt{2}]$.
> - $y(x)$ is differentiable on $\mathopen{]}0, a\sqrt{2}\mathclose{[}$ (denominator of $\frac{dy}{dx}$ is non-zero since $y > 0$).
> - $y(0) = 0 = y(a\sqrt{2})$.
>
> **Stage 3 (Core Operation).** By Rolle's Theorem, there exists at least one number $c \in \mathopen{]}0, a\sqrt{2}\mathclose{[}$ such that $y'(c) = 0$.
>
> Setting $y'(c) = 0$ requires $c^2 + y(c)^2 = a^2$, which in subpart 2 uniquely yielded:
>
> $\displaystyle c = \frac{\sqrt{3}}{2}a$
>
> Verify that $c$ lies strictly inside the open interval $\mathopen{]}0, a\sqrt{2}\mathclose{[}$:
>
> $\displaystyle c = \frac{\sqrt{3}}{2}a \approx 0.8660 a, \quad\text{and}\quad a\sqrt{2} \approx 1.4142 a$
>
> Since $0 < 0.8660 a < 1.4142 a$, $c \in \mathopen{]}0, a\sqrt{2}\mathclose{[}$.
>
> **Stage 4 (Interpretation & Boundary Check).** Rolle's Theorem guarantees the existence of a horizontal tangent on the loop, and the explicit derivation in subpart 2 identifies that critical value as $c = \frac{\sqrt{3}}{2}a$.
>
> Verified critical value: $c = \frac{\sqrt{3}}{2}a$.
