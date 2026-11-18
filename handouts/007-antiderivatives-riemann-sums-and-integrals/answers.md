---
title: "Handout 007: Antiderivatives & Integrals — Answer Key"
---

# 007: Antiderivatives, Riemann Sums, and the Definite Integral — Answer Key

## Exercises

### Q1

**1.**

> **Stage 1 (Classification & Domain).** Combination of power, reciprocal, and trigonometric terms on the open interval $\mathopen{]}0, \pi/2\mathclose{[}$. On this domain, $x > 0$ so $|x| = x$, and $\cos(x) \ne 0$ so $\sec^2(x)$ is continuous.
>
> **Stage 2 (Algebraic Preparation).** Rewrite radicals and quotients in standard power and catalog forms:
>
> $\displaystyle f(x) = 4x^{-1/2} - 3x^{-1} + 2\sec^2(x)$
>
> **Stage 3 (Core Operation).** Antidifferentiate term by term using the Power Rule for $x^{-1/2}$, the Logarithmic Rule for $x^{-1}$, and the Trigonometric Rule for $\sec^2(x)$:
>
> $\displaystyle F(x) = 4\left(\frac{x^{-1/2 + 1}}{-1/2 + 1}\right) - 3\ln|x| + 2\tan(x) + C = 4\left(\frac{x^{1/2}}{1/2}\right) - 3\ln(x) + 2\tan(x) + C$
>
> $\displaystyle F(x) = 8\sqrt{x} - 3\ln(x) + 2\tan(x) + C$
>
> **Stage 4 (Interpretation & Boundary Check).** Differentiating $F(x)$ recovers $f(x)$:
>
> $\displaystyle F'(x) = 8\left(\frac{1}{2\sqrt{x}}\right) - \frac{3}{x} + 2\sec^2(x) + 0 = \frac{4}{\sqrt{x}} - \frac{3}{x} + 2\sec^2(x) = f(x)$
>
> Verified general antiderivative: $F(x) = 8\sqrt{x} - 3\ln(x) + 2\tan(x) + C$.

**2.**

> **Stage 1 (Classification & Domain).** Second-order polynomial initial value problem on $\mathopen{]}-\infty, +\infty\mathclose{[}$ with initial slope condition $f'(0) = 5$ and function boundary condition $f(1) = 8$.
>
> **Stage 2 (Algebraic Preparation).** The polynomial $f''(x) = 12x^2 + 6x - 4$ is already in power form.
>
> **Stage 3 (Core Operation).** First integration recovers the first derivative $f'(x)$:
>
> $\displaystyle f'(x) = \int (12x^2 + 6x - 4)\,dx = 12\left(\frac{x^3}{3}\right) + 6\left(\frac{x^2}{2}\right) - 4x + C_1 = 4x^3 + 3x^2 - 4x + C_1$
>
> Apply $f'(0) = 5$:
>
> $\displaystyle f'(0) = 4(0)^3 + 3(0)^2 - 4(0) + C_1 = 5 \;\Longrightarrow\; C_1 = 5$
>
> So $f'(x) = 4x^3 + 3x^2 - 4x + 5$. Second integration recovers the function $f(x)$:
>
> $\displaystyle f(x) = \int (4x^3 + 3x^2 - 4x + 5)\,dx = 4\left(\frac{x^4}{4}\right) + 3\left(\frac{x^3}{3}\right) - 4\left(\frac{x^2}{2}\right) + 5x + C_2$
>
> $\displaystyle f(x) = x^4 + x^3 - 2x^2 + 5x + C_2$
>
> Apply $f(1) = 8$:
>
> $\displaystyle f(1) = (1)^4 + (1)^3 - 2(1)^2 + 5(1) + C_2 = 1 + 1 - 2 + 5 + C_2 = 5 + C_2 = 8 \;\Longrightarrow\; C_2 = 3$
>
> **Stage 4 (Interpretation & Boundary Check).** Direct verification: $f(1) = 1 + 1 - 2 + 5 + 3 = 8$, $f'(0) = 5$, and $f''(x) = 12x^2 + 6x - 4$.
>
> Verified unique particular solution: $f(x) = x^4 + x^3 - 2x^2 + 5x + 3$.

### Q2

**1.**

> **Stage 1 (Classification & Domain).** Continuous piecewise linear rate function $f(x)$ on $[-3, 5]$. By the Fundamental Theorem of Calculus, $F'(x) = f(x)$ and $F''(x) = f'(x)$ wherever the derivative exists.
>
> **Stage 2 (Algebraic Preparation).** Identify the zero crossings and monotonicity of $f(x)$:
>
> - Zero crossings: $f(-2) = 0$, $f(2) = 0$, and $f(5) = 0$.
> - Sign of $f(x)$: negative on $[-3, -2\mathclose{[}$, positive on $\mathopen{]}-2, 2\mathclose{[}$, negative on $\mathopen{]}2, 5\mathclose{[}$.
> - Slope of $f(x)$: positive ($m = 2$) on $\mathopen{]}-3, -1\mathclose{[}$, zero ($m = 0$) on $\mathopen{]}-1, 1\mathclose{[}$, negative ($m = -2$) on $\mathopen{]}1, 3\mathclose{[}$, positive ($m = 1$) on $\mathopen{]}3, 5\mathclose{[}$.
>
> **Stage 3 (Core Operation).** Classify critical points and inflection points:
>
> - **Local Minimum at $x = -2$:** $f(x) = F'(x)$ changes from negative to positive at $x = -2$, so $F(x)$ transitions from decreasing to increasing.
> - **Local Maximum at $x = 2$:** $f(x) = F'(x)$ changes from positive to negative at $x = 2$, so $F(x)$ transitions from increasing to decreasing.
> - **Inflection Points:** Inflection points occur where concavity changes sign, meaning where $F''(x) = f'(x)$ changes sign (extrema of $f$).
>   - At $x = 3$: $f(x)$ attains a local minimum (value $-2$), transitioning from decreasing ($f' < 0$, $F$ concave downward) to increasing ($f' > 0$, $F$ concave upward). Thus, $x = 3$ is an inflection point of $F$.
>   - At $x = -1$ and $x = 1$: the rate curve exhibits corners transitioning to and from a constant line ($f' = 0$, zero curvature).
>
> **Stage 4 (Interpretation & Boundary Check).** Confirms First and Second Derivative Test geometric behavior.
>
> Verified extrema and inflection: local minimum at $x = -2$, local maximum at $x = 2$, and inflection point at $x = 3$.

**2.**

> **Stage 1 (Classification & Domain).** Evaluation of $F(x) = -2 + \int_0^x f(t)\,dt$ across integer grid points $x \in \{-3, -2, -1, 0, 1, 2, 3, 4, 5\}$.
>
> **Stage 2 (Algebraic Preparation).** Compute the signed geometric areas of individual sub-regions between the graph of $f$ and the horizontal axis:
>
> - Triangle on $[-3, -2]$: base $1$, height $-2$, signed area $\frac{1}{2}(1)(-2) = -1$.
> - Triangle on $[-2, -1]$: base $1$, height $2$, signed area $\frac{1}{2}(1)(2) = +1$.
> - Rectangle on $[-1, 0]$: base $1$, height $2$, signed area $1 \times 2 = +2$.
> - Rectangle on $[0, 1]$: base $1$, height $2$, signed area $1 \times 2 = +2$.
> - Triangle on $[1, 2]$: base $1$, height $2$, signed area $\frac{1}{2}(1)(2) = +1$.
> - Triangle on $[2, 3]$: base $1$, height $-2$, signed area $\frac{1}{2}(1)(-2) = -1$.
> - Trapezoid on $[3, 4]$: bases $-2$ and $-1$, width $1$, signed area $\frac{-2 + (-1)}{2}(1) = -1.5$.
> - Triangle on $[4, 5]$: base $1$, height $-1$, signed area $\frac{1}{2}(1)(-1) = -0.5$.
>
> **Stage 3 (Core Operation).** Accumulate values starting from initial condition $F(0) = -2$:
>
> - Forward accumulation ($x > 0$):
>   - $F(1) = F(0) + \int_0^1 f(t)\,dt = -2 + 2 = 0$.
>   - $F(2) = F(1) + \int_1^2 f(t)\,dt = 0 + 1 = 1$.
>   - $F(3) = F(2) + \int_2^3 f(t)\,dt = 1 + (-1) = 0$.
>   - $F(4) = F(3) + \int_3^4 f(t)\,dt = 0 + (-1.5) = -1.5$.
>   - $F(5) = F(4) + \int_4^5 f(t)\,dt = -1.5 + (-0.5) = -2$.
> - Backward accumulation ($x < 0$):
>   - $F(-1) = F(0) - \int_{-1}^0 f(t)\,dt = -2 - 2 = -4$.
>   - $F(-2) = F(-1) - \int_{-2}^{-1} f(t)\,dt = -4 - 1 = -5$.
>   - $F(-3) = F(-2) - \int_{-3}^{-2} f(t)\,dt = -5 - (-1) = -4$.
>
> **Stage 4 (Interpretation & Boundary Check).** Notice that $F(-2) = -5$ is the absolute minimum on $[-3, 0]$, matching the local minimum found in subpart 1. $F(2) = 1$ is the absolute maximum, matching the local maximum.
>
> Verified grid values: $F(-3) = -4$, $F(-2) = -5$, $F(-1) = -4$, $F(0) = -2$, $F(1) = 0$, $F(2) = 1$, $F(3) = 0$, $F(4) = -1.5$, $F(5) = -2$.

### Q3

**1. Correct answer: B.**

- **A (Incorrect):** The definite integral evaluates to a strictly negative real number whenever the integrand lies beneath the horizontal axis ($f(x) < 0$) on $[a, b]$ with $b > a$.
- **B (Correct):** The bounding property establishes that if a continuous function is bounded between $m$ and $M$ on $[a, b]$, its definite integral is bounded between the inscribed rectangle $m(b - a)$ and the circumscribed rectangle $M(b - a)$; furthermore, integration preserves inequalities between functions.
- **C (Incorrect):** A zero definite integral requires only that the signed areas above and below the horizontal axis balance to zero ($A_{\text{above}} = A_{\text{below}}$), as demonstrated by $\int_{-\pi}^\pi \sin(x)\,dx = 0$ for a non-zero function.
- **D (Incorrect):** Reversing the limits of integration inverts the sign of the infinitesimal width $\Delta x = \frac{a - b}{n} = -\frac{b - a}{n}$, so $\int_b^a f(x)\,dx = -\int_a^b f(x)\,dx$.
- **E (Incorrect):** Integration is a linear operator, not a multiplicative one; in general, $\int_a^b [f(x)]^2\,dx \ne \left[\int_a^b f(x)\,dx\right]^2$, as shown by $f(x) = 1$ on $[0, 2]$, where $\int_0^2 1^2\,dx = 2$ but $(\int_0^2 1\,dx)^2 = 2^2 = 4$.


### Q4

**1.**

> **Stage 1 (Classification & Domain).** Left endpoint Riemann sum approximation from discrete telemetry data over $[0, 8]$ hours with $n = 4$ uniform subintervals of width $\Delta t = \frac{8 - 0}{4} = 2$ hours.
>
> **Stage 2 (Algebraic Preparation).** The four subintervals are $[0, 2]$, $[2, 4]$, $[4, 6]$, and $[6, 8]$. The corresponding left endpoints are $t_0 = 0$, $t_1 = 2$, $t_2 = 4$, and $t_3 = 6$. The logged rates are:
>
> $\displaystyle r(0) = 120, \quad r(2) = 145, \quad r(4) = 170, \quad r(6) = 160$
>
> **Stage 3 (Core Operation).** Sum the left-endpoint products:
>
> $\displaystyle L_4 = \Delta t \sum_{i=0}^3 r(t_i) = 2 \cdot [r(0) + r(2) + r(4) + r(6)]$
>
> $\displaystyle L_4 = 2 \cdot [120 + 145 + 170 + 160] = 2 \cdot [595] = 1190\text{ liters}$
>
> **Stage 4 (Interpretation & Boundary Check).** Dimensional consistency: rate in $\text{L/min}$ multiplied by hours converted or scaled directly as flow integral proxy. Units match total volume accumulated.
>
> Verified Left sum: $L_4 = 1190\text{ liters}$.

**2.**

> **Stage 1 (Classification & Domain).** Right endpoint Riemann sum approximation over $[0, 8]$ hours with $n = 4$ uniform subintervals of width $\Delta t = 2$ hours.
>
> **Stage 2 (Algebraic Preparation).** The right endpoints of the four subintervals $[0, 2]$, $[2, 4]$, $[4, 6]$, and $[6, 8]$ are $t_1 = 2$, $t_2 = 4$, $t_3 = 6$, and $t_4 = 8$. The logged rates are:
>
> $\displaystyle r(2) = 145, \quad r(4) = 170, \quad r(6) = 160, \quad r(8) = 130$
>
> **Stage 3 (Core Operation).** Sum the right-endpoint products:
>
> $\displaystyle R_4 = \Delta t \sum_{i=1}^4 r(t_i) = 2 \cdot [r(2) + r(4) + r(6) + r(8)]$
>
> $\displaystyle R_4 = 2 \cdot [145 + 170 + 160 + 130] = 2 \cdot [605] = 1210\text{ liters}$
>
> **Stage 4 (Interpretation & Boundary Check).** The difference $R_4 - L_4 = 2 \cdot [r(8) - r(0)] = 2 \cdot [130 - 120] = 20\text{ liters}$, exactly matching the boundary difference formula $\Delta t [r(b) - r(a)]$.
>
> Verified Right sum: $R_4 = 1210\text{ liters}$.

**3.**

> **Stage 1 (Classification & Domain).** Midpoint Riemann sum approximation over $[0, 8]$ hours partitioned into $n = 2$ subintervals of width $\Delta t' = \frac{8 - 0}{2} = 4$ hours.
>
> **Stage 2 (Algebraic Preparation).** The two 4-hour subintervals are $[0, 4]$ and $[4, 8]$. The midpoints are $\bar{t}_1 = \frac{0 + 4}{2} = 2$ hours and $\bar{t}_2 = \frac{4 + 8}{2} = 6$ hours. The logged midpoint rates are:
>
> $\displaystyle r(\bar{t}_1) = r(2) = 145, \quad r(\bar{t}_2) = r(6) = 160$
>
> **Stage 3 (Core Operation).** Sum the midpoint products:
>
> $\displaystyle M_2 = \Delta t' \sum_{i=1}^2 r(\bar{t}_i) = 4 \cdot [r(2) + r(6)] = 4 \cdot [145 + 160] = 4 \cdot [305] = 1220\text{ liters}$
>
> **Stage 4 (Interpretation & Boundary Check).** The midpoint estimate $1220\text{ L}$ provides an independent approximation consistent with the $L_4$ ($1190\text{ L}$) and $R_4$ ($1210\text{ L}$) bounds.
>
> Verified Midpoint sum: $M_2 = 1220\text{ liters}$.

### Q5

**1.**

> **Stage 1 (Classification & Domain).** Uniform partition of interval $[a, b] = [1, 4]$ into $n$ equal subintervals.
>
> **Stage 2 (Algebraic Preparation).** Apply standard grid formulas:
>
> $\displaystyle \Delta x = \frac{b - a}{n} = \frac{4 - 1}{n} = \frac{3}{n}$
>
> $\displaystyle x_i = a + i\Delta x = 1 + i\left(\frac{3}{n}\right) = 1 + \frac{3i}{n}$
>
> **Stage 3 (Core Operation).** State formulas for index $i \in \{1, 2, \dots, n\}$.
>
> **Stage 4 (Interpretation & Boundary Check).** Check boundaries: for $i = 0$, $x_0 = 1 + 0 = 1 = a$; for $i = n$, $x_n = 1 + \frac{3n}{n} = 1 + 3 = 4 = b$.
>
> Verified partition formulas: $\Delta x = \frac{3}{n}$ and $x_i = 1 + \frac{3i}{n}$.

**2.**

> **Stage 1 (Classification & Domain).** Quadratic polynomial integrand $f(x) = 2x^2 - 3x + 1$ evaluated at right endpoints $x_i = 1 + \frac{3i}{n}$.
>
> **Stage 2 (Algebraic Preparation).** Expand $f(x_i)$ algebraically:
>
> $\displaystyle f(x_i) = 2\left(1 + \frac{3i}{n}\right)^2 - 3\left(1 + \frac{3i}{n}\right) + 1$
>
> $\displaystyle f(x_i) = 2\left(1 + \frac{6i}{n} + \frac{9i^2}{n^2}\right) - 3 - \frac{9i}{n} + 1 = 2 + \frac{12i}{n} + \frac{18i^2}{n^2} - 2 - \frac{9i}{n} = \frac{3i}{n} + \frac{18i^2}{n^2}$
>
> **Stage 3 (Core Operation).** Set up $R_n = \sum_{i=1}^n f(x_i)\Delta x$ and distribute $\Delta x = \frac{3}{n}$:
>
> $\displaystyle R_n = \sum_{i=1}^n \left(\frac{3i}{n} + \frac{18i^2}{n^2}\right)\frac{3}{n} = \sum_{i=1}^n \left(\frac{9i}{n^2} + \frac{54i^2}{n^3}\right) = \frac{9}{n^2}\sum_{i=1}^n i + \frac{54}{n^3}\sum_{i=1}^n i^2$
>
> Substitute sigma identities $\sum_{i=1}^n i = \frac{n(n + 1)}{2}$ and $\sum_{i=1}^n i^2 = \frac{n(n + 1)(2n + 1)}{6}$:
>
> $\displaystyle R_n = \frac{9}{n^2}\left[\frac{n(n + 1)}{2}\right] + \frac{54}{n^3}\left[\frac{n(n + 1)(2n + 1)}{6}\right] = \frac{9(n + 1)}{2n} + \frac{9(n + 1)(2n + 1)}{n^2}$
>
> $\displaystyle R_n = \frac{9}{2}\left(1 + \frac{1}{n}\right) + 9\left(1 + \frac{1}{n}\right)\left(2 + \frac{1}{n}\right)$
>
> **Stage 4 (Interpretation & Boundary Check).** Expanding into a single rational fraction:
>
> $\displaystyle R_n = \frac{9n + 9}{2n} + \frac{18n^2 + 27n + 9}{n^2} = \frac{9n^2 + 9n + 36n^2 + 54n + 18}{2n^2} = \frac{45n^2 + 63n + 18}{2n^2}$
>
> Verified expanded Riemann sum: $R_n = \frac{9}{2}\left(1 + \frac{1}{n}\right) + 9\left(1 + \frac{1}{n}\right)\left(2 + \frac{1}{n}\right) = \frac{45n^2 + 63n + 18}{2n^2}$.

**3.**

> **Stage 1 (Classification & Domain).** Evaluation of the limit of $R_n$ as $n \to \infty$.
>
> **Stage 2 (Algebraic Preparation).** Use the factored form: $R_n = \frac{9}{2}\left(1 + \frac{1}{n}\right) + 9\left(1 + \frac{1}{n}\right)\left(2 + \frac{1}{n}\right)$.
>
> **Stage 3 (Core Operation).** Apply limit laws with $\lim_{n \to \infty} \frac{1}{n} = 0$:
>
> $\displaystyle \lim_{n \to \infty} R_n = \lim_{n \to \infty} \left[\frac{9}{2}\left(1 + \frac{1}{n}\right) + 9\left(1 + \frac{1}{n}\right)\left(2 + \frac{1}{n}\right)\right]$
>
> $\displaystyle \lim_{n \to \infty} R_n = \frac{9}{2}(1 + 0) + 9(1 + 0)(2 + 0) = \frac{9}{2} + 18 = \frac{9}{2} + \frac{36}{2} = \frac{45}{2} = 22.5$
>
> **Stage 4 (Interpretation & Boundary Check).** Verify by standard antiderivative evaluation:
>
> $\displaystyle \int_1^4 (2x^2 - 3x + 1)\,dx = \left[ \frac{2}{3}x^3 - \frac{3}{2}x^2 + x \right]_1^4$
>
> At $x = 4$: $\frac{2}{3}(64) - \frac{3}{2}(16) + 4 = \frac{128}{3} - 24 + 4 = \frac{128}{3} - 20 = \frac{68}{3}$.
>
> At $x = 1$: $\frac{2}{3}(1) - \frac{3}{2}(1) + 1 = \frac{2}{3} - \frac{1}{2} = \frac{1}{6}$.
>
> Difference: $\frac{68}{3} - \frac{1}{6} = \frac{136 - 1}{6} = \frac{135}{6} = \frac{45}{2}$. Exact agreement.
>
> Verified limit: $\lim_{n \to \infty} R_n = \frac{45}{2} = 22.5$.

### Q6

**1.**

> **Stage 1 (Classification & Domain).** Two-stage piecewise continuous acceleration kinematic system on $[0, +\infty\mathclose{[}$ with launch from rest $v(0) = 0$.
>
> **Stage 2 (Algebraic Preparation).** Powered stage: $a(t) = 40 - 2t$ for $0 \le t \le 10$. Coasting stage: $a(t) = -9.8$ for $t > 10$.
>
> **Stage 3 (Core Operation).** Integrate each stage:
>
> - Powered burn ($0 \le t \le 10$):
>   $\displaystyle v(t) = \int (40 - 2t)\,dt = 40t - t^2 + C_1$
>   Applying initial condition $v(0) = 0$ yields $C_1 = 0$, so $v(t) = 40t - t^2$.
> - Coasting phase ($t > 10$):
>   $\displaystyle v(t) = \int -9.8\,dt = -9.8t + C_2$
>   Enforcing continuity of velocity at the stage boundary $t = 10$:
>   $\displaystyle v(10) = 40(10) - (10)^2 = 400 - 100 = 300\text{ m/s}$
>   $\displaystyle -9.8(10) + C_2 = 300 \;\Longrightarrow\; -98 + C_2 = 300 \;\Longrightarrow\; C_2 = 398$
>   Therefore, for $t \ge 10$, $v(t) = 398 - 9.8t = 300 - 9.8(t - 10)$.
>
> **Stage 4 (Interpretation & Boundary Check).** Both pieces evaluate to $300\text{ m/s}$ at $t = 10$, ensuring $v(t)$ is continuous.
>
> Verified piecewise velocity:
>
> $\displaystyle v(t) = \begin{cases} 40t - t^2 & \text{if } 0 \le t \le 10 \\ 398 - 9.8t & \text{if } t > 10 \end{cases}$

**2.**

> **Stage 1 (Classification & Domain).** Burnout evaluation at $t = 10$ and determination of apogee (zero vertical velocity) during coasting flight ($t > 10$).
>
> **Stage 2 (Algebraic Preparation).** At apogee, the vehicle reaches its highest trajectory point and pauses momentarily before descending: $v(t_{\text{apogee}}) = 0$.
>
> **Stage 3 (Core Operation).**
>
> - Burnout velocity at $t = 10$:
>   $\displaystyle v(10) = 40(10) - (10)^2 = 300\text{ m/s}$
> - Apogee time from coasting formula:
>   $\displaystyle 398 - 9.8t_{\text{apogee}} = 0 \;\Longrightarrow\; 9.8t_{\text{apogee}} = 398 \;\Longrightarrow\; t_{\text{apogee}} = \frac{398}{9.8} = \frac{3980}{98} = \frac{1990}{49}\text{ s} \approx 40.6122\text{ s}$
>   Alternatively, elapsed coasting time is $\Delta t_{\text{coast}} = \frac{300}{9.8} = \frac{1500}{49}\text{ s} \approx 30.6122\text{ s}$, giving $t_{\text{apogee}} = 10 + \frac{1500}{49} = \frac{1990}{49}\text{ s}$.
>
> **Stage 4 (Interpretation & Boundary Check).** The sounding rocket powered motor burns for $10\text{ s}$, followed by $30.61\text{ s}$ of gravitational deceleration before reaching apogee at $40.61\text{ s}$.
>
> Verified values: burnout velocity $v(10) = 300\text{ m/s}$ and apogee time $t_{\text{apogee}} = \frac{1990}{49}\text{ s} \approx 40.61\text{ s}$.

**3.**

> **Stage 1 (Classification & Domain).** Definite integrals for vertical displacements $s_1$ (powered ascent) and $s_2$ (coasting ascent). Since $v(t) \ge 0$ throughout $[0, t_{\text{apogee}}]$, total distance equals net vertical displacement.
>
> **Stage 2 (Algebraic Preparation).** Set up the two definite integrals:
>
> $\displaystyle s_1 = \int_0^{10} (40t - t^2)\,dt, \qquad s_2 = \int_{10}^{1990/49} [300 - 9.8(t - 10)]\,dt$
>
> **Stage 3 (Core Operation).** Evaluate $s_1$:
>
> $\displaystyle s_1 = \left[ 20t^2 - \frac{t^3}{3} \right]_0^{10} = 20(100) - \frac{1000}{3} = 2000 - \frac{1000}{3} = \frac{5000}{3}\text{ m} \approx 1666.67\text{ m}$
>
> Evaluate $s_2$ using substitution $u = t - 10$, $du = dt$, with bounds $u \in [0, \frac{1500}{49}]$:
>
> $\displaystyle s_2 = \int_0^{1500/49} (300 - 9.8u)\,du = \left[ 300u - 4.9u^2 \right]_0^{1500/49}$
>
> Geometrically, this is the area of a right triangle with base $b = \frac{1500}{49}\text{ s}$ and height $h = 300\text{ m/s}$:
>
> $\displaystyle s_2 = \frac{1}{2}\left(\frac{1500}{49}\right)(300) = \frac{225000}{49}\text{ m} \approx 4591.84\text{ m}$
>
> Sum the two stages to obtain maximum altitude $s_{\text{max}}$:
>
> $\displaystyle s_{\text{max}} = s_1 + s_2 = \frac{5000}{3} + \frac{225000}{49} = \frac{5000 \cdot 49 + 225000 \cdot 3}{147} = \frac{245000 + 675000}{147} = \frac{920000}{147}\text{ m} \approx 6258.50\text{ m}$
>
> **Stage 4 (Interpretation & Boundary Check).** Physics check: work-energy theorem for coasting stage gives $m g s_2 = \frac{1}{2} m v^2 \implies s_2 = \frac{v^2}{2g} = \frac{300^2}{2(9.8)} = \frac{90000}{19.6} = \frac{225000}{49}\text{ m}$. Exact match.
>
> Verified maximum altitude: $s_{\text{max}} = \frac{920000}{147}\text{ m} \approx 6258.50\text{ m}$.
