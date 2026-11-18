---
title: "Handout 002: Functions & Limits — Answer Key"
---

# 002: Functions, Transformations, and Limits — Answer Key

## Exercises

### Q1

**1.**

> **Stage 1 (Classification & Domain).** Rational function $f(x) = \dfrac{3x - 1}{x^2 - 4x - 12}$; the denominator cannot be zero.
>
> **Stage 2 (Algebraic Preparation).** $x^2 - 4x - 12 = (x - 6)(x + 2) = 0 \;\Rightarrow\; x = -2,\ 6$.
>
> **Stage 3 (Core Operation).** Remove the zeros of the denominator: $(-\infty, -2) \cup (-2, 6) \cup (6, \infty)$.
>
> **Stage 4 (Interpretation & Boundary Check).** The numerator at the excluded points is $3(-2) - 1 = -7$ and $3(6) - 1 = 17$, both nonzero, so each exclusion is a vertical asymptote, not a hole.
>
> Verified domain: $(-\infty, -2) \cup (-2, 6) \cup (6, \infty)$.

**2.**

> **Stage 1 (Classification & Domain).** $g(t) = \sqrt{5 - t} - \sqrt{t + 3}$; both radicands must be non-negative.
>
> **Stage 2 (Algebraic Preparation).** $5 - t \ge 0 \Rightarrow t \le 5$ and $t + 3 \ge 0 \Rightarrow t \ge -3$.
>
> **Stage 3 (Core Operation).** Intersect: $-3 \le t \le 5$, so the domain is $[-3, 5]$.
>
> **Stage 4 (Interpretation & Boundary Check).** $g(-3) = \sqrt{8} - 0 = 2\sqrt{2}$ and $g(5) = 0 - \sqrt{8} = -2\sqrt{2}$, so both endpoints belong (closed brackets).
>
> Verified domain: $[-3, 5]$.

**3.**

> **Stage 1 (Classification & Domain).** $h(x) = \dfrac{2x + 7}{\sqrt[4]{x^2 - 4x}}$; an even root in a denominator needs a strictly positive radicand.
>
> **Stage 2 (Algebraic Preparation).** $x^2 - 4x = x(x - 4) > 0$ with roots $x = 0$ and $x = 4$. A sign test gives positive on $(-\infty, 0)$ and on $(4, \infty)$, negative on $(0, 4)$.
>
> **Stage 3 (Core Operation).** Collect the positive intervals: $(-\infty, 0) \cup (4, \infty)$.
>
> **Stage 4 (Interpretation & Boundary Check).** At $x = 0$ and $x = 4$ the denominator is $0$ (open parentheses).
>
> Verified domain: $(-\infty, 0) \cup (4, \infty)$.

**4.**

> **Stage 1 (Classification & Domain).** Nested fraction $k(u) = \dfrac{u - 2}{2 - \dfrac{6}{u + 1}}$; every denominator at every level must be nonzero.
>
> **Stage 2 (Algebraic Preparation).** Inner denominator: $u + 1 \ne 0 \Rightarrow u \ne -1$. Main denominator:
>
> $\displaystyle 2 - \frac{6}{u + 1} = 0 \;\Rightarrow\; 2(u + 1) - 6 = 0 \;\Rightarrow\; 2u - 4 = 0 \;\Rightarrow\; u = 2$
>
> **Stage 3 (Core Operation).** Exclude $u = -1$ and $u = 2$: $(-\infty, -1) \cup (-1, 2) \cup (2, \infty)$.
>
> **Stage 4 (Interpretation & Boundary Check).** Simplifying gives $\dfrac{u - 2}{\dfrac{2u - 4}{u + 1}} = \dfrac{u + 1}{2}$, which cancels $(u - 2)$, but the original expression is still undefined at $u = 2$ (a hole).
>
> Verified domain: $(-\infty, -1) \cup (-1, 2) \cup (2, \infty)$.

### Q2

**1. Correct answer: B.**

- **A (Incorrect):** Confuses the definition of a limit with continuity; limits depend strictly on behavior near $x = 2$, not at $x = 2$.
- **B (Correct):** Evaluates left-hand limit $\lim_{x \to 2^-} (x^2 - 2x + 3) = 3$ and right-hand limit $\lim_{x \to 2^+} (7 - 2x) = 3$, confirming $\lim_{x \to 2} g(x) = 3$, while noting that $\lim_{x \to 2} g(x) \neq g(2) = 5$ produces a removable discontinuity.
- **C (Incorrect):** Fails to enforce the continuity condition that the limit must equal the evaluated function value at the point.
- **D (Incorrect):** Erroneously evaluates the isolated point $g(2) = 5$ rather than investigating local approaching behavior as $x \to 2$.
- **E (Incorrect):** Contains an arithmetic error in evaluating one-sided limits, falsely asserting that directional limits disagree.

### Q3

**1.**

> **Stage 1 (Classification & Domain).** $f(x) = \sqrt{x}$ with $\operatorname{dom} = [0, \infty)$. Apply: right $3$, vertical stretch $2$, reflect in the $x$-axis, up $5$.
>
> **Stage 2 (Algebraic Preparation).** $h(x) = -2\sqrt{x - 3} + 5 = 5 - 2\sqrt{x - 3}$.
>
> **Stage 3 (Core Operation).** Domain: $x - 3 \ge 0 \Rightarrow [3, \infty)$.
>
> Range: $\sqrt{x - 3} \ge 0 \;\Rightarrow\; -2\sqrt{x - 3} \le 0 \;\Rightarrow\; 5 - 2\sqrt{x - 3} \le 5$, so the range is $(-\infty, 5]$.
>
> **Stage 4 (Interpretation & Boundary Check).** $h(3) = 5$ is the vertex and absolute maximum; $h(x) \to -\infty$ as $x \to \infty$.
>
> Verified: $h(x) = 5 - 2\sqrt{x - 3}$; domain $[3, \infty)$; range $(-\infty, 5]$.

**2.**

> **Stage 1 (Classification & Domain).** $f(x) = \sqrt{x}$ and $g(x) = 9 - x^2$. For $(f \circ g)(x)$ require $x \in \operatorname{dom}(g)$ and $g(x) \in \operatorname{dom}(f)$.
>
> **Stage 2 (Algebraic Preparation).** $(f \circ g)(x) = \sqrt{9 - x^2}$, which requires $9 - x^2 \ge 0$.
>
> **Stage 3 (Core Operation).** $9 - x^2 \ge 0 \;\Rightarrow\; x^2 \le 9 \;\Rightarrow\; -3 \le x \le 3$, so the domain is $[-3, 3]$.
>
> **Stage 4 (Interpretation & Boundary Check).** At the endpoints $(f \circ g)(\pm 3) = \sqrt{0} = 0$; at $x = 0$ the peak is $\sqrt{9} = 3$.
>
> Verified: $(f \circ g)(x) = \sqrt{9 - x^2}$; domain $[-3, 3]$.

**3.**

> **Stage 1 (Classification & Domain).** $f(x) = \sqrt{x}$ with $\operatorname{dom} = [0, \infty)$ is the inner function in $(g \circ f)(x)$, with $g(x) = 9 - x^2$.
>
> **Stage 2 (Algebraic Preparation).** $(g \circ f)(x) = 9 - \left(\sqrt{x}\right)^2$. The inner function forces $x \ge 0$, and for $x \ge 0$ this equals $9 - x$.
>
> **Stage 3 (Core Operation).** The domain is set by the inner root: $[0, \infty)$. On it $9 - x$ decreases from $9$ without bound, so the range is $(-\infty, 9]$.
>
> **Stage 4 (Interpretation & Boundary Check).** Dropping the inner restriction would wrongly give the domain $(-\infty, \infty)$ from the simplified formula $9 - x$.
>
> Verified: $(g \circ f)(x) = 9 - x$ for $x \ge 0$; domain $[0, \infty)$; range $(-\infty, 9]$.

### Q4

**1.**

> **Stage 1 (Classification & Domain).** $\displaystyle \lim_{x \to 3} \frac{2x^2 - 5x - 3}{x^2 - 9}$; direct substitution gives $\dfrac{0}{0}$.
>
> **Stage 2 (Algebraic Preparation).** $2x^2 - 5x - 3 = (2x + 1)(x - 3)$ and $x^2 - 9 = (x + 3)(x - 3)$.
>
> **Stage 3 (Core Operation).** Cancel $(x - 3)$ for $x \ne 3$:
>
> $\displaystyle \lim_{x \to 3} \frac{2x + 1}{x + 3} = \frac{2(3) + 1}{3 + 3} = \frac{7}{6}$
>
> **Stage 4 (Interpretation & Boundary Check).** Numerical check: at $x = 3.01$ the ratio is $\approx 1.168$ and $\frac{7}{6} \approx 1.1667$.
>
> Verified limit: $\dfrac{7}{6}$.

**2.**

> **Stage 1 (Classification & Domain).** $\displaystyle \lim_{t \to 0} \frac{\sqrt{t + 16} - 4}{t}$; direct substitution gives $\dfrac{4 - 4}{0} = \dfrac{0}{0}$.
>
> **Stage 2 (Algebraic Preparation).** Multiply by the conjugate $\sqrt{t + 16} + 4$:
>
> $\displaystyle \frac{(\sqrt{t + 16} - 4)(\sqrt{t + 16} + 4)}{t(\sqrt{t + 16} + 4)} = \frac{t}{t(\sqrt{t + 16} + 4)}$
>
> **Stage 3 (Core Operation).** Cancel $t$ for $t \ne 0$:
>
> $\displaystyle \lim_{t \to 0} \frac{1}{\sqrt{t + 16} + 4} = \frac{1}{4 + 4} = \frac{1}{8}$
>
> **Stage 4 (Interpretation & Boundary Check).** Numerical check: at $t = 0.01$ the value is $\approx 0.12496$ and $\frac{1}{8} = 0.125$.
>
> Verified limit: $\dfrac{1}{8}$.

**3.**

> **Stage 1 (Classification & Domain).** $\displaystyle \lim_{x \to -2} \frac{\dfrac{1}{x + 4} - \dfrac{1}{2}}{x + 2}$; direct substitution gives $\dfrac{0}{0}$.
>
> **Stage 2 (Algebraic Preparation).** Combine the numerator over a common denominator, then divide by $(x + 2)$:
>
> $\displaystyle \frac{1}{x + 4} - \frac{1}{2} = \frac{2 - (x + 4)}{2(x + 4)} = \frac{-(x + 2)}{2(x + 4)} \quad\Longrightarrow\quad \frac{-(x + 2)}{2(x + 4)(x + 2)}$
>
> **Stage 3 (Core Operation).** Cancel $(x + 2)$ for $x \ne -2$:
>
> $\displaystyle \lim_{x \to -2} \frac{-1}{2(x + 4)} = \frac{-1}{2(2)} = -\frac{1}{4}$
>
> **Stage 4 (Interpretation & Boundary Check).** Numerical check: at $x = -1.99$ the value is $\approx -0.2488$ and $-\frac{1}{4} = -0.25$.
>
> Verified limit: $-\dfrac{1}{4}$.

**4.**

> **Stage 1 (Classification & Domain).** $\displaystyle \lim_{\theta \to 0} \frac{\sin(5\theta)}{3\theta}$ has the form $\dfrac{0}{0}$.
>
> **Stage 2 (Algebraic Preparation).** Use $\displaystyle \lim_{u \to 0} \frac{\sin u}{u} = 1$. Rewrite as
>
> $\displaystyle \frac{5}{3} \cdot \frac{\sin(5\theta)}{5\theta}$
>
> **Stage 3 (Core Operation).** With $u = 5\theta \to 0$ the limit is $\dfrac{5}{3} \cdot 1 = \dfrac{5}{3}$.
>
> **Stage 4 (Interpretation & Boundary Check).** Numerical check: at $\theta = 0.001$ rad, $\dfrac{\sin(0.005)}{0.003} \approx 1.66667$.
>
> Verified limit: $\dfrac{5}{3}$.

### Q5

**1.**

> **Stage 1 (Classification & Domain).** Piecewise model $T(t)$ on $[0, 6]$: left piece $2 + 1.5t$ for $t < 2$, right piece $8 - \dfrac{6}{t + 1}$ for $t > 2$.
>
> **Stage 2 (Algebraic Preparation).** Each piece is continuous on its open interval, so each one-sided limit is found by direct substitution.
>
> **Stage 3 (Core Operation).**
>
> $\displaystyle \lim_{t \to 2^-} (2 + 1.5t) = 2 + 1.5(2) = 5 \qquad \lim_{t \to 2^+} \left(8 - \frac{6}{t + 1}\right) = 8 - \frac{6}{3} = 6$
>
> **Stage 4 (Interpretation & Boundary Check).** Left limit $5$ ($500\,^\circ\text{C}$, pre-heating); right limit $6$ ($600\,^\circ\text{C}$, firing stage).
>
> Verified: $\displaystyle \lim_{t \to 2^-} T(t) = 5$ and $\displaystyle \lim_{t \to 2^+} T(t) = 6$.

**2.**

> **Stage 1 (Classification & Domain).** The one-sided limits are $\displaystyle \lim_{t \to 2^-} T(t) = 5$ and $\displaystyle \lim_{t \to 2^+} T(t) = 6$.
>
> **Stage 2 (Algebraic Preparation).** The two-sided limit exists if and only if the one-sided limits are equal.
>
> **Stage 3 (Core Operation).** Since $5 \ne 6$, $\displaystyle \lim_{t \to 2} T(t)$ does not exist (DNE). The discontinuity is a jump of size $|6 - 5| = 1$ at $t = 2$.
>
> **Stage 4 (Interpretation & Boundary Check).** The control value $T(2) = 5$ cannot bridge the jump.
>
> Verified conclusion: the limit DNE; jump discontinuity of size $1$.

**3.**

> **Stage 1 (Classification & Domain).** On $[0, 6]$ both pieces are increasing: segment 1 on $[0, 2)$ has $\dfrac{dT}{dt} > 0$, and segment 2 on $(2, 6]$ has $\dfrac{dT}{dt} > 0$.
>
> **Stage 2 (Algebraic Preparation).** Segment 1 covers $[2, 5)$, and $T(2) = 5$ closes it to $[2, 5]$. Segment 2 covers $\left(6, \dfrac{50}{7}\right]$.
>
> **Stage 3 (Core Operation).** Range: $[2, 5] \cup \left(6, \dfrac{50}{7}\right]$. The minimum is $2$ at $t = 0$; the maximum is $\dfrac{50}{7}$ at $t = 6$.
>
> **Stage 4 (Interpretation & Boundary Check).** The interval $(5, 6]$ is skipped because of the jump discontinuity.
>
> Verified range: $[2, 5] \cup \left(6, \dfrac{50}{7}\right]$.

### Q6

**1.**

> **Stage 1 (Classification & Domain).** For $t > 10$: $v(t) = \dfrac{\sqrt{t - 1} - 3}{t - 10} + 15$, whose fraction part is $\dfrac{0}{0}$ at $t = 10$.
>
> **Stage 2 (Algebraic Preparation).** Multiply by the conjugate $\sqrt{t - 1} + 3$:
>
> $\displaystyle \frac{(\sqrt{t - 1} - 3)(\sqrt{t - 1} + 3)}{(t - 10)(\sqrt{t - 1} + 3)} = \frac{t - 10}{(t - 10)(\sqrt{t - 1} + 3)}$
>
> **Stage 3 (Core Operation).** Cancel $(t - 10)$:
>
> $\displaystyle \lim_{t \to 10^+} v(t) = \frac{1}{\sqrt{9} + 3} + 15 = \frac{1}{6} + 15 = \frac{91}{6}\ \text{m/s}$
>
> **Stage 4 (Interpretation & Boundary Check).** Numerical check: at $t = 10.01$, $v \approx 15.1666\ \text{m/s}$.
>
> Verified limit: $\dfrac{91}{6}\ \text{m/s}$.

**2.**

> **Stage 1 (Classification & Domain).** For $t < 10$: $v(t) = \dfrac{at^2 + 12t}{t + 4}$, continuous at $t = 10$ because the denominator is $14 \ne 0$.
>
> **Stage 2 (Algebraic Preparation).** Substitute directly, then match the right-hand limit:
>
> $\displaystyle \lim_{t \to 10^-} v(t) = \frac{100a + 120}{14} = \frac{50a + 60}{7} = \frac{91}{6}$
>
> **Stage 3 (Core Operation).** Cross-multiply: $6(50a + 60) = 7(91) \;\Rightarrow\; 300a + 360 = 637 \;\Rightarrow\; a = \dfrac{277}{300}$.
>
> **Stage 4 (Interpretation & Boundary Check).** Check: $\dfrac{50 \cdot \frac{277}{300} + 60}{7} = \dfrac{637/6}{7} = \dfrac{91}{6}\ \text{m/s}$.
>
> Verified parameter: $a = \dfrac{277}{300}$.

**3.**

> **Stage 1 (Classification & Domain).** Continuity at $t = 10$ requires $v(10) = \displaystyle \lim_{t \to 10} v(t)$.
>
> **Stage 2 (Algebraic Preparation).** By definition $v(10) = b$, and the two-sided limit is $\displaystyle \lim_{t \to 10} v(t) = \dfrac{91}{6}\ \text{m/s}$.
>
> **Stage 3 (Core Operation).** Equate the values: $b = \dfrac{91}{6}\ \text{m/s}$.
>
> **Stage 4 (Interpretation & Boundary Check).** With $b = \frac{91}{6}$ there is no velocity discontinuity at $t = 10$.
>
> Verified parameter: $b = \dfrac{91}{6}$.

**4.**

> **Stage 1 (Classification & Domain).** $\bar{a} = \dfrac{v(26) - v(17)}{26 - 17}$; both times lie in $(10, 30]$, so the right-hand formula applies.
>
> **Stage 2 (Algebraic Preparation).**
>
> $\displaystyle v(17) = \frac{\sqrt{16} - 3}{7} + 15 = \frac{1}{7} + 15 = \frac{106}{7} \qquad v(26) = \frac{\sqrt{25} - 3}{16} + 15 = \frac{1}{8} + 15 = \frac{121}{8}$
>
> **Stage 3 (Core Operation).**
>
> $\displaystyle \Delta v = \frac{121}{8} - \frac{106}{7} = \frac{847 - 848}{56} = -\frac{1}{56} \qquad \bar{a} = \frac{-1/56}{9} = -\frac{1}{504}\ \text{m/s}^2$
>
> **Stage 4 (Interpretation & Boundary Check).** Numerical check: $\dfrac{15.125 - 15.142857}{9} \approx -0.0019841$ and $-\frac{1}{504} \approx -0.0019841$. The negative sign means slight deceleration.
>
> Verified acceleration: $-\dfrac{1}{504}\ \text{m/s}^2$.
