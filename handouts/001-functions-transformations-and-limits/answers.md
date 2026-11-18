---
title: "Handout 001: Functions, Transformations, and Limits — Answer Key"
---

# 001: Functions, Transformations, and Limits — Answer Key

## Exercises

### Q1

**1.**

> **Stage 1 (Classification & Domain).** Rational function $f(x) = \dfrac{3x - 1}{x^2 - 4x - 12}$; the denominator cannot be zero.
>
> **Stage 2 (Algebraic Preparation).** $x^2 - 4x - 12 = (x - 6)(x + 2) = 0 \;\Rightarrow\; x = -2,\ 6$.
>
> **Stage 3 (Core Operation).** Remove the zeros of the denominator: $\mathopen{]}-\infty, -2\mathclose{[} \cup \mathopen{]}-2, 6\mathclose{[} \cup \mathopen{]}6, +\infty\mathclose{[}$.
>
> **Stage 4 (Interpretation & Boundary Check).** The numerator at the excluded points is $3(-2) - 1 = -7$ and $3(6) - 1 = 17$, both nonzero, so each exclusion is a vertical asymptote, not a hole.
>
> Verified domain: $\mathopen{]}-\infty, -2\mathclose{[} \cup \mathopen{]}-2, 6\mathclose{[} \cup \mathopen{]}6, +\infty\mathclose{[}$.

**2.**

> **Stage 1 (Classification & Domain).** $g(t) = \sqrt{5 - t} - \sqrt{t + 3}$; both even radicands must be non-negative.
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
> **Stage 2 (Algebraic Preparation).** $x^2 - 4x = x(x - 4) > 0$ with roots $x = 0$ and $x = 4$. A sign test gives positive on $\mathopen{]}-\infty, 0\mathclose{[}$ and on $\mathopen{]}4, +\infty\mathclose{[}$, negative on $\mathopen{]}0, 4\mathclose{[}$.
>
> **Stage 3 (Core Operation).** Collect the positive intervals: $\mathopen{]}-\infty, 0\mathclose{[} \cup \mathopen{]}4, +\infty\mathclose{[}$.
>
> **Stage 4 (Interpretation & Boundary Check).** At $x = 0$ and $x = 4$ the denominator is $0$, so both ends are excluded.
>
> Verified domain: $\mathopen{]}-\infty, 0\mathclose{[} \cup \mathopen{]}4, +\infty\mathclose{[}$.

**4.**

> **Stage 1 (Classification & Domain).** Nested fraction $k(u) = \dfrac{u - 2}{2 - \dfrac{6}{u + 1}}$; every denominator at every level must be nonzero.
>
> **Stage 2 (Algebraic Preparation).** Inner denominator: $u + 1 \ne 0 \Rightarrow u \ne -1$. Main denominator:
>
> $\displaystyle 2 - \frac{6}{u + 1} = 0 \;\Rightarrow\; 2(u + 1) - 6 = 0 \;\Rightarrow\; 2u - 4 = 0 \;\Rightarrow\; u = 2$
>
> **Stage 3 (Core Operation).** Exclude $u = -1$ and $u = 2$: $\mathopen{]}-\infty, -1\mathclose{[} \cup \mathopen{]}-1, 2\mathclose{[} \cup \mathopen{]}2, +\infty\mathclose{[}$.
>
> **Stage 4 (Interpretation & Boundary Check).** Simplifying gives $\dfrac{u - 2}{\dfrac{2u - 4}{u + 1}} = \dfrac{u + 1}{2}$, which cancels $(u - 2)$, but the original expression is still undefined at $u = 2$ (a hole at $\left(2, \tfrac{3}{2}\right)$).
>
> Verified domain: $\mathopen{]}-\infty, -1\mathclose{[} \cup \mathopen{]}-1, 2\mathclose{[} \cup \mathopen{]}2, +\infty\mathclose{[}$.

**5.**

> **Stage 1 (Classification & Domain).** $m(x) = \sqrt[3]{4 - x^2} + \sqrt{x + 1}$ is a sum of an odd-index radical and an even-index radical.
>
> **Stage 2 (Algebraic Preparation).** The cube root accepts every real radicand, so $4 - x^2$ imposes no condition. The square root needs $x + 1 \ge 0$, so $x \ge -1$.
>
> **Stage 3 (Core Operation).** The only restriction is $x \ge -1$, giving $[-1, +\infty\mathclose{[}$.
>
> **Stage 4 (Interpretation & Boundary Check).** At $x = -1$: $m(-1) = \sqrt[3]{3} + 0$, defined (closed bracket). At $x = 3$: $m(3) = \sqrt[3]{-5} + 2$ is real even though $4 - x^2 < 0$, so requiring $4 - x^2 \ge 0$ (which would give $[-1, 2]$) is wrong.
>
> Verified domain: $[-1, +\infty\mathclose{[}$.

### Q2

**1. Correct answer: D.**

- **A (Incorrect):** Confuses the limit with the function value. A limit depends only on behavior near $x = 2$, so $g(2) \ne 3$ does not prevent the limit from existing.
- **B (Incorrect):** Continuity needs the limit to equal the function value; here $3 \ne g(2) = 5$.
- **C (Incorrect):** Assumes the piecewise formulas disagree at the boundary; the computed one-sided limits are both $3$, so there is no jump.
- **D (Correct):** $\displaystyle \lim_{x \to 2^-} (x^2 - 2x + 3) = 3$ and $\displaystyle \lim_{x \to 2^+} (7 - 2x) = 3$, so $\displaystyle \lim_{x \to 2} g(x) = 3$. Since $g(2) = 5 \ne 3$, the discontinuity is removable.
- **E (Incorrect):** Reads the isolated value $g(2) = 5$ as the limit instead of examining the approaching values.


### Q3

**1.**

> **Stage 1 (Classification & Domain).** Base function $y = |x|$ with domain $\mathopen{]}-\infty, +\infty\mathclose{[}$ and range $[0, +\infty\mathclose{[}$. Apply in order: right $2$, stretch $3$, reflect in the $x$-axis, down $1$.
>
> **Stage 2 (Algebraic Preparation).**
>
> $|x| \;\to\; |x - 2| \;\to\; 3|x - 2| \;\to\; -3|x - 2| \;\to\; h(x) = -3|x - 2| - 1$
>
> **Stage 3 (Core Operation).** No restriction on $x$, so the domain is $\mathopen{]}-\infty, +\infty\mathclose{[}$. Range: $|x - 2| \ge 0 \;\Rightarrow\; -3|x - 2| \le 0 \;\Rightarrow\; h(x) \le -1$, so the range is $\mathopen{]}-\infty, -1]$.
>
> **Stage 4 (Interpretation & Boundary Check).** $h(2) = -1$ is attained, so the bracket at $-1$ is closed. The vertex $(2, -1)$ is the highest point of the graph.
>
> Verified: $h(x) = -3|x - 2| - 1$; domain $\mathopen{]}-\infty, +\infty\mathclose{[}$; range $\mathopen{]}-\infty, -1]$.

**2.**

> **Stage 1 (Classification & Domain).** $p(x) = 3 - 2f(x - 1)$ combines a right shift by $1$, a vertical stretch by $2$, a reflection across the $x$-axis, and an upward shift by $3$.
>
> **Stage 2 (Algebraic Preparation).** Domain: $x - 1$ must lie in $[-2, 4]$, so $-1 \le x \le 5$.
>
> **Stage 3 (Core Operation).** Range, step by step:
>
> $f \in [1, 5] \;\Rightarrow\; 2f \in [2, 10] \;\Rightarrow\; -2f \in [-10, -2] \;\Rightarrow\; 3 - 2f \in [-7, 1]$
>
> **Stage 4 (Interpretation & Boundary Check).** The reflection swaps the ends: the largest value of $f$ gives the smallest value of $p$ ($3 - 10 = -7$), and the smallest value of $f$ gives the largest ($3 - 2 = 1$). A left shift would wrongly give the domain $[-3, 3]$.
>
> Verified: domain $[-1, 5]$; range $[-7, 1]$.

**3.**

> **Stage 1 (Classification & Domain).** $f(x) = \sqrt{x}$ and $g(x) = 9 - x^2$. For $(f \circ g)(x)$ require $x \in \operatorname{dom}(g)$ and $g(x) \in \operatorname{dom}(f)$.
>
> **Stage 2 (Algebraic Preparation).** $(f \circ g)(x) = \sqrt{9 - x^2}$, which requires $9 - x^2 \ge 0$.
>
> **Stage 3 (Core Operation).** $9 - x^2 \ge 0 \;\Rightarrow\; x^2 \le 9 \;\Rightarrow\; -3 \le x \le 3$, so the domain is $[-3, 3]$.
>
> **Stage 4 (Interpretation & Boundary Check).** At the endpoints $(f \circ g)(\pm 3) = \sqrt{0} = 0$, and at $x = 0$ the value is $\sqrt{9} = 3$.
>
> Verified: $(f \circ g)(x) = \sqrt{9 - x^2}$; domain $[-3, 3]$.

**4.**

> **Stage 1 (Classification & Domain).** $f(x) = \sqrt{x}$ with domain $[0, +\infty\mathclose{[}$ is the inner function in $(g \circ f)(x)$, with $g(x) = 9 - x^2$.
>
> **Stage 2 (Algebraic Preparation).** $(g \circ f)(x) = 9 - \left(\sqrt{x}\right)^2$. The inner function forces $x \ge 0$, and for $x \ge 0$ this equals $9 - x$.
>
> **Stage 3 (Core Operation).** The domain is set by the inner root: $[0, +\infty\mathclose{[}$. On it $9 - x$ decreases from $9$ without bound, so the range is $\mathopen{]}-\infty, 9]$.
>
> **Stage 4 (Interpretation & Boundary Check).** Using only the simplified formula $9 - x$ would wrongly give the domain $\mathopen{]}-\infty, +\infty\mathclose{[}$.
>
> Verified: $(g \circ f)(x) = 9 - x$ for $x \ge 0$; domain $[0, +\infty\mathclose{[}$; range $\mathopen{]}-\infty, 9]$.

### Q4

**1.**

> **Stage 1 (Classification & Domain).** $\displaystyle \lim_{x \to 3} \frac{2x^2 - 5x - 3}{x^2 - 9}$; direct substitution gives $\dfrac{0}{0}$, so the Quotient Law does not apply directly.
>
> **Stage 2 (Algebraic Preparation).** $2x^2 - 5x - 3 = (2x + 1)(x - 3)$ and $x^2 - 9 = (x + 3)(x - 3)$.
>
> **Stage 3 (Core Operation).** Cancel $(x - 3)$ for $x \ne 3$:
>
> $\displaystyle \lim_{x \to 3} \frac{2x + 1}{x + 3} = \frac{2(3) + 1}{3 + 3} = \frac{7}{6}$
>
> **Stage 4 (Interpretation & Boundary Check).** Numerical check: at $x = 3.01$ the ratio is $\approx 1.1681$ and $\frac{7}{6} \approx 1.1667$.
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
> **Stage 4 (Interpretation & Boundary Check).** Numerical check: at $t = 0.01$ the value is $\approx 0.12498$ and $\frac{1}{8} = 0.125$.
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
> **Stage 2 (Algebraic Preparation).** Use $\displaystyle \lim_{u \to 0} \frac{\sin u}{u} = 1$. Rescale so the sine argument matches the denominator:
>
> $\displaystyle \frac{\sin(5\theta)}{3\theta} = \frac{5}{3} \cdot \frac{\sin(5\theta)}{5\theta}$
>
> **Stage 3 (Core Operation).** With $u = 5\theta \to 0$ the limit is $\dfrac{5}{3} \cdot 1 = \dfrac{5}{3}$.
>
> **Stage 4 (Interpretation & Boundary Check).** Numerical check: at $\theta = 0.001$, $\dfrac{\sin(0.005)}{0.003} \approx 1.66666$. Dropping the factor $\frac{5}{3}$ would wrongly give $1$.
>
> Verified limit: $\dfrac{5}{3}$.

### Q5

**1.**

> **Stage 1 (Classification & Domain).** Piecewise model $T(t)$ on $[0, 6]$: left piece $2 + 1.5t$ for $t < 2$, right piece $8 - \dfrac{6}{t + 1}$ for $t > 2$.
>
> **Stage 2 (Algebraic Preparation).** Each piece is continuous on its own interval, so each one-sided limit is found by direct substitution.
>
> **Stage 3 (Core Operation).**
>
> $\displaystyle \lim_{t \to 2^-} (2 + 1.5t) = 2 + 1.5(2) = 5 \qquad \lim_{t \to 2^+} \left(8 - \frac{6}{t + 1}\right) = 8 - \frac{6}{3} = 6$
>
> **Stage 4 (Interpretation & Boundary Check).** Left limit $5$ ($500\,^\circ\text{C}$, heating stage); right limit $6$ ($600\,^\circ\text{C}$, firing stage).
>
> Verified: $\displaystyle \lim_{t \to 2^-} T(t) = 5$ and $\displaystyle \lim_{t \to 2^+} T(t) = 6$.

**2.**

> **Stage 1 (Classification & Domain).** The one-sided limits are $5$ (left) and $6$ (right).
>
> **Stage 2 (Algebraic Preparation).** The two-sided limit exists if and only if the one-sided limits are equal.
>
> **Stage 3 (Core Operation).** Since $5 \ne 6$, $\displaystyle \lim_{t \to 2} T(t)$ does not exist. The discontinuity is a jump of size $|6 - 5| = 1$ at $t = 2$.
>
> **Stage 4 (Interpretation & Boundary Check).** The control value $T(2) = 5$ matches the left limit but cannot bridge the jump.
>
> Verified conclusion: the limit does not exist; jump discontinuity of size $1$.

**3.**

> **Stage 1 (Classification & Domain).** On $[0, 6]$ the output rises along each piece: $2 + 1.5t$ increases with $t$, and $8 - \dfrac{6}{t + 1}$ increases with $t$ because $\dfrac{6}{t + 1}$ shrinks.
>
> **Stage 2 (Algebraic Preparation).** Piece 1 on $[0, 2\mathclose{[}$ takes values from $T(0) = 2$ up to (but not reaching) $5$; with $T(2) = 5$ the first part of the range is $[2, 5]$. Piece 2 on $\mathopen{]}2, 6]$ takes values above $6$ (the value $6$ is approached but not reached) up to $T(6) = 8 - \dfrac{6}{7} = \dfrac{50}{7}$.
>
> **Stage 3 (Core Operation).** Range: $[2, 5] \cup \mathopen{]}6, \dfrac{50}{7}]$. The minimum is $2$ at $t = 0$; the maximum is $\dfrac{50}{7}$ at $t = 6$.
>
> **Stage 4 (Interpretation & Boundary Check).** The values in $\mathopen{]}5, 6]$ are never reached because of the jump. In temperature terms, the minimum is $200\,^\circ\text{C}$ and the maximum is about $714\,^\circ\text{C}$.
>
> Verified range: $[2, 5] \cup \mathopen{]}6, \dfrac{50}{7}]$.

### Q6

**1.**

> **Stage 1 (Classification & Domain).** For $t > 10$: $v(t) = \dfrac{\sqrt{t - 1} - 3}{t - 10} + 5$. The fraction is $\dfrac{0}{0}$ at $t = 10$, so a radical difference calls for the conjugate.
>
> **Stage 2 (Algebraic Preparation).** Multiply by $\sqrt{t - 1} + 3$:
>
> $\displaystyle \frac{(\sqrt{t - 1} - 3)(\sqrt{t - 1} + 3)}{(t - 10)(\sqrt{t - 1} + 3)} = \frac{t - 10}{(t - 10)(\sqrt{t - 1} + 3)}$
>
> **Stage 3 (Core Operation).** Cancel $(t - 10)$ for $t \ne 10$:
>
> $\displaystyle \lim_{t \to 10^+} v(t) = \frac{1}{\sqrt{9} + 3} + 5 = \frac{1}{6} + 5 = \frac{31}{6}\ \text{m/s}$
>
> **Stage 4 (Interpretation & Boundary Check).** Numerical check: at $t = 10.01$, $v \approx 5.16662\ \text{m/s}$ and $\frac{31}{6} \approx 5.16667$.
>
> Verified limit: $\dfrac{31}{6}\ \text{m/s}$.

**2.**

> **Stage 1 (Classification & Domain).** For $t < 10$: $v(t) = \dfrac{kt + 2}{t + 2}$, which is a rational function whose denominator is $12 \ne 0$ at $t = 10$, so substitution is valid.
>
> **Stage 2 (Algebraic Preparation).** Substitute directly and match the right-hand limit:
>
> $\displaystyle \lim_{t \to 10^-} v(t) = \frac{10k + 2}{12} = \frac{31}{6}$
>
> **Stage 3 (Core Operation).** Cross-multiply: $6(10k + 2) = 12 \cdot 31 \;\Rightarrow\; 60k + 12 = 372 \;\Rightarrow\; k = 6$.
>
> **Stage 4 (Interpretation & Boundary Check).** Check: $\dfrac{10 \cdot 6 + 2}{12} = \dfrac{62}{12} = \dfrac{31}{6}\ \text{m/s}$.
>
> Verified parameter: $k = 6$.

**3.**

> **Stage 1 (Classification & Domain).** Continuity at $t = 10$ requires that the limit exists and equals $v(10)$.
>
> **Stage 2 (Algebraic Preparation).** By definition $v(10) = c$. With $k = 6$ both one-sided limits equal $\dfrac{31}{6}$, so $\displaystyle \lim_{t \to 10} v(t) = \dfrac{31}{6}\ \text{m/s}$.
>
> **Stage 3 (Core Operation).** Equate the value and the limit: $c = \dfrac{31}{6}\ \text{m/s}$.
>
> **Stage 4 (Interpretation & Boundary Check).** With $c = \frac{31}{6}$ there is no break in the velocity at $t = 10$.
>
> Verified parameter: $c = \dfrac{31}{6}$.

**4.**

> **Stage 1 (Classification & Domain).** $\bar{a} = \dfrac{v(26) - v(17)}{26 - 17}$; both times lie in $\mathopen{]}10, 30]$, so the right-hand formula applies.
>
> **Stage 2 (Algebraic Preparation).**
>
> $\displaystyle v(17) = \frac{\sqrt{16} - 3}{7} + 5 = \frac{1}{7} + 5 = \frac{36}{7} \qquad v(26) = \frac{\sqrt{25} - 3}{16} + 5 = \frac{1}{8} + 5 = \frac{41}{8}$
>
> **Stage 3 (Core Operation).**
>
> $\displaystyle v(26) - v(17) = \frac{41}{8} - \frac{36}{7} = \frac{287 - 288}{56} = -\frac{1}{56} \qquad \bar{a} = \frac{-1/56}{9} = -\frac{1}{504}\ \text{m/s}^2$
>
> **Stage 4 (Interpretation & Boundary Check).** Numerical check: $\dfrac{5.125 - 5.142857}{9} \approx -0.0019841$ and $-\frac{1}{504} \approx -0.0019841$. The negative sign means a slight deceleration.
>
> Verified acceleration: $-\dfrac{1}{504}\ \text{m/s}^2$.
