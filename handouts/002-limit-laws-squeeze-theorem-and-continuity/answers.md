---
title: "Handout 002: Limit Laws & Continuity — Key"
---

# 002: Limit Laws, Squeeze Theorem, Continuity, and the IVT — Answer Key

## Exercises

### Q1

**1.**

> **Stage 1 (Classification & Domain).** Direct substitution of $x = 3$ gives $\frac{3^3 - 2(3^2) - 9}{3^2 - 2(3) - 3} = \frac{27 - 18 - 9}{9 - 6 - 3} = \frac{0}{0}$, an indeterminate form of rational type.
>
> **Stage 2 (Algebraic Preparation).** Factor numerator and denominator. Since both vanish at $x = 3$, $(x - 3)$ is a common factor:
>
> $\displaystyle x^3 - 2x^2 - 9 = (x - 3)(x^2 + x + 3)$
>
> $\displaystyle x^2 - 2x - 3 = (x - 3)(x + 1)$
>
> For $x \neq 3$, cancel $(x - 3)$:
>
> $\displaystyle \frac{x^3 - 2x^2 - 9}{x^2 - 2x - 3} = \frac{(x - 3)(x^2 + x + 3)}{(x - 3)(x + 1)} = \frac{x^2 + x + 3}{x + 1} \quad (x \neq 3)$
>
> **Stage 3 (Core Operation).** Apply the Quotient Law to the simplified rational function:
>
> $\displaystyle \lim_{x \to 3} \frac{x^2 + x + 3}{x + 1} = \frac{3^2 + 3 + 3}{3 + 1} = \frac{9 + 3 + 3}{4} = \frac{15}{4}$
>
> **Stage 4 (Interpretation & Boundary Check).** At $x = 3$, the original expression has a removable discontinuity with limiting value $\frac{15}{4} = 3.75$.

**2.**

> **Stage 1 (Classification & Domain).** Direct substitution of $x = 2$ gives $\frac{\sqrt{2^2 + 12} - 4}{2 - 2} = \frac{\sqrt{16} - 4}{0} = \frac{0}{0}$, an indeterminate form involving a radical difference.
>
> **Stage 2 (Algebraic Preparation).** Multiply numerator and denominator by the conjugate radical factor $\sqrt{x^2 + 12} + 4$:
>
> $\displaystyle \frac{\sqrt{x^2 + 12} - 4}{x - 2} \cdot \frac{\sqrt{x^2 + 12} + 4}{\sqrt{x^2 + 12} + 4} = \frac{(x^2 + 12) - 16}{(x - 2)(\sqrt{x^2 + 12} + 4)} = \frac{x^2 - 4}{(x - 2)(\sqrt{x^2 + 12} + 4)}$
>
> Factor the difference of squares in the numerator: $x^2 - 4 = (x - 2)(x + 2)$. For $x \neq 2$, cancel $(x - 2)$:
>
> $\displaystyle \frac{(x - 2)(x + 2)}{(x - 2)(\sqrt{x^2 + 12} + 4)} = \frac{x + 2}{\sqrt{x^2 + 12} + 4} \quad (x \neq 2)$
>
> **Stage 3 (Core Operation).** Evaluate the simplified limit as $x \to 2$:
>
> $\displaystyle \lim_{x \to 2} \frac{x + 2}{\sqrt{x^2 + 12} + 4} = \frac{2 + 2}{\sqrt{2^2 + 12} + 4} = \frac{4}{\sqrt{16} + 4} = \frac{4}{4 + 4} = \frac{4}{8} = \frac{1}{2}$
>
> **Stage 4 (Interpretation & Boundary Check).** The limit represents the instantaneous slope of $y = \sqrt{x^2 + 12}$ at $x = 2$. Verified value: $\frac{1}{2}$.

**3.**

> **Stage 1 (Classification & Domain).** Direct substitution of $x = -1$ yields $\frac{\frac{2}{-1 + 3} - 1}{-1 + 1} = \frac{1 - 1}{0} = \frac{0}{0}$, an indeterminate form containing a compound fraction.
>
> **Stage 2 (Algebraic Preparation).** Combine the numerator terms over common denominator $x + 3$:
>
> $\displaystyle \frac{2}{x + 3} - 1 = \frac{2 - (x + 3)}{x + 3} = \frac{2 - x - 3}{x + 3} = \frac{-(x + 1)}{x + 3}$
>
> Divide by the denominator $(x + 1)$:
>
> $\displaystyle \frac{\frac{-(x + 1)}{x + 3}}{x + 1} = \frac{-(x + 1)}{(x + 1)(x + 3)} = -\frac{1}{x + 3} \quad (x \neq -1)$
>
> **Stage 3 (Core Operation).** Evaluate the simplified limit as $x \to -1$:
>
> $\displaystyle \lim_{x \to -1} \left(-\frac{1}{x + 3}\right) = -\frac{1}{-1 + 3} = -\frac{1}{2}$
>
> **Stage 4 (Interpretation & Boundary Check).** Natural domain requires $x \neq -3$ and $x \neq -1$. As $x \to -1$, the function approaches $-\frac{1}{2}$.

### Q2

**1.**

> **Stage 1 (Classification & Domain).** Evaluate one-sided limits and function values from coordinate grids of $f$ and $g$ with origin at the axes intersection and grid scale $u = 24\text{ px}$.
>
> **Stage 2 (Algebraic Preparation).** Locate target coordinates:
>
> For $g(x)$ near $x = 1$: Left curve approaches open circle at $(1, 2)$. Right curve begins at solid point at $(1, 1)$.
>
> For $f(x)$ near $x = 2$: Curve from left and right converges to open hole at $(2, 2)$, with displaced isolated point at $(2, 1)$.
>
> **Stage 3 (Core Operation).** Read individual values:
>
> (a) Left-hand limit: $\lim_{x \to 1^-} g(x) = 2$.
>
> (b) Right-hand limit: $\lim_{x \to 1^+} g(x) = 1$.
>
> (c) Two-sided limit: $\lim_{x \to 1} g(x)$ does not exist (DNE) because $\lim_{x \to 1^-} g(x) = 2 \neq 1 = \lim_{x \to 1^+} g(x)$.
>
> (d) Two-sided limit: $\lim_{x \to 2} f(x) = 2$, since both directional approaches converge to the hole at $(2, 2)$.
>
> (e) Function evaluation: $f(2) = 1$ (the solid dot at $x = 2$).
>
> **Stage 4 (Interpretation & Boundary Check).** At $x = 1$, $g(x)$ possesses a jump discontinuity of magnitude $|2 - 1| = 1$. At $x = 2$, $f(x)$ possesses a removable discontinuity because $\lim_{x \to 2} f(x) = 2 \neq 1 = f(2)$.

**2.**

> **Stage 1 (Classification & Domain).** The function $h(x)$ contains absolute value factor $|x - 3|$, which changes definition at $x = 3$. Directional limits must be analyzed separately.
>
> **Stage 2 (Algebraic Preparation).** Split $|x - 3|$ into directional branches:
>
> For $x < 3$: $x - 3 < 0 \implies |x - 3| = -(x - 3)$.
>
> $\displaystyle \frac{x^2 - 9}{|x - 3|} = \frac{(x - 3)(x + 3)}{-(x - 3)} = -(x + 3) \quad (x < 3)$
>
> For $x > 3$: $x - 3 > 0 \implies |x - 3| = x - 3$.
>
> $\displaystyle \frac{x^2 - 9}{|x - 3|} = \frac{(x - 3)(x + 3)}{x - 3} = x + 3 \quad (x > 3)$
>
> **Stage 3 (Core Operation).** Evaluate directional limits:
>
> $\displaystyle \lim_{x \to 3^-} h(x) = \lim_{x \to 3^-} [-(x + 3)] = -(3 + 3) = -6$
>
> $\displaystyle \lim_{x \to 3^+} h(x) = \lim_{x \to 3^+} (x + 3) = 3 + 3 = 6$
>
> **Stage 4 (Interpretation & Boundary Check).** Because $\lim_{x \to 3^-} h(x) = -6 \neq 6 = \lim_{x \to 3^+} h(x)$, the two-sided limit $\lim_{x \to 3} h(x)$ does not exist (DNE). The function has a jump discontinuity of size $|6 - (-6)| = 12$ at $x = 3$.

### Q3

**1. Correct answer: E.**

- **A (Incorrect):** The Squeeze Theorem requires the lower and upper bounding functions to approach the exact same limiting value $L$. When the bounding limits differ ($\lim (1 - x) = 1$ and $\lim (2 + x^2) = 2$), the Squeeze Theorem provides no information, and averaging the bounds is mathematically invalid.
- **B (Incorrect):** A jump discontinuity requires both one-sided limits to exist as finite real numbers. If either directional limit diverges to $+\infty$ or $-\infty$, the discontinuity is classified as an infinite discontinuity (vertical asymptote).
- **C (Incorrect):** The Quotient Law applies only when the limit of the denominator is non-zero ($\lim g(x) \neq 0$). When both limits vanish, $0/0$ is an indeterminate form that can frequently be simplified by algebraic cancellation to yield a finite limit.
- **D (Incorrect):** The Intermediate Value Theorem is an existence theorem, not a uniqueness theorem. It guarantees that there exists at least one root $c \in \mathopen{]}0, 4\mathclose{[}$, but there may be multiple roots if the curve oscillates across zero repeatedly.
- **E (Correct):** The Squeeze Theorem hypotheses are fully satisfied: $2 - x^2 \le g(x) \le 2\cos(x)$ on an open interval containing $0$, and evaluating the limits of both bounds gives $\lim_{x \to 0} (2 - x^2) = 2 - 0 = 2$ and $\lim_{x \to 0} (2\cos x) = 2(1) = 2$. Because both outer limits equal $2$, the trapped function $g(x)$ must converge to $2$.


### Q4

**1.**

> **Stage 1 (Classification & Domain).** The function $f(x) = \frac{(x^2 - 1)(x - 3)}{(x - 1)(x - 3)^2 (x + 2)}$ is a rational function. A rational function is continuous on its natural domain and discontinuous wherever its denominator vanishes.
>
> **Stage 2 (Algebraic Preparation).** Set the denominator equal to zero: $(x - 1)(x - 3)^2 (x + 2) = 0 \implies x = 1, \; x = 3, \; x = -2$.
>
> Factor the numerator completely: $(x^2 - 1)(x - 3) = (x - 1)(x + 1)(x - 3)$.
>
> Rewrite $f(x)$ showing all linear factors:
>
> $\displaystyle f(x) = \frac{(x - 1)(x + 1)(x - 3)}{(x - 1)(x - 3)^2 (x + 2)}$
>
> **Stage 3 (Core Operation).** Classify each point of discontinuity:
>
> - **At $x = 1$:** The factor $(x - 1)$ cancels completely from the denominator:
>
>   $\displaystyle \lim_{x \to 1} f(x) = \lim_{x \to 1} \frac{x + 1}{(x - 3)(x + 2)} = \frac{1 + 1}{(1 - 3)(1 + 2)} = \frac{2}{(-2)(3)} = -\frac{1}{3}$
>
>   Because the limit exists as a finite real number ($-\frac{1}{3}$) while $f(1)$ is undefined, $x = 1$ is a **removable discontinuity**.
>
> - **At $x = 3$:** Cancelling one $(x - 3)$ factor leaves one $(x - 3)$ in the denominator:
>
>   $\displaystyle \lim_{x \to 3} \frac{x + 1}{(x - 3)(x + 2)}$
>
>   The numerator approaches $3 + 1 = 4 \neq 0$, while the denominator approaches $0 \cdot 5 = 0$. Thus the one-sided limits diverge to $\pm\infty$:
>
>   $\displaystyle \lim_{x \to 3^-} f(x) = -\infty \quad \text{and} \quad \lim_{x \to 3^+} f(x) = +\infty$
>
>   Therefore, $x = 3$ is an **infinite discontinuity** (vertical asymptote $x = 3$).
>
> - **At $x = -2$:** The factor $(x + 2)$ appears only in the denominator:
>
>   $\displaystyle \lim_{x \to -2} \frac{x + 1}{(x - 3)(x + 2)}$
>
>   Numerator approaches $-2 + 1 = -1 \neq 0$, while denominator approaches $(-5) \cdot 0 = 0$. Thus the limits diverge to $\pm\infty$.
>
>   Therefore, $x = -2$ is an **infinite discontinuity** (vertical asymptote $x = -2$).
>
> **Stage 4 (Interpretation & Boundary Check).** Summary of discontinuities: $x = 1$ is removable; $x = 3$ is infinite; $x = -2$ is infinite. There are no jump discontinuities.

**2.**

> **Stage 1 (Classification & Domain).** The function $g(x)$ is defined piecewise on $\mathbb{R}$. For $x < 1$, $g(x) = k x^2 + 2x - 1$ is a polynomial, continuous everywhere. For $x > 1$, $g(x) = \frac{\sqrt{x + 3} - 2}{x - 1} + 3$ is continuous on its domain ($x + 3 \ge 0$ and $x \neq 1$, which holds for all $x > 1$). Therefore, $g(x)$ is continuous on all of $\mathbb{R}$ if and only if it is continuous at the interface $x = 1$.
>
> **Stage 2 (Algebraic Preparation).** Evaluate the right-hand limit as $x \to 1^+$ using conjugate rationalization:
>
> $\displaystyle \frac{\sqrt{x + 3} - 2}{x - 1} \cdot \frac{\sqrt{x + 3} + 2}{\sqrt{x + 3} + 2} = \frac{(x + 3) - 4}{(x - 1)(\sqrt{x + 3} + 2)} = \frac{x - 1}{(x - 1)(\sqrt{x + 3} + 2)}$
>
> For $x > 1$, cancel $(x - 1)$:
>
> $\displaystyle \frac{1}{\sqrt{x + 3} + 2} \quad (x > 1)$
>
> **Stage 3 (Core Operation).** Compute directional limits and equate to function value $g(1) = m$:
>
> Right-hand limit:
>
> $\displaystyle \lim_{x \to 1^+} g(x) = \lim_{x \to 1^+} \left[\frac{1}{\sqrt{x + 3} + 2} + 3\right] = \frac{1}{\sqrt{1 + 3} + 2} + 3 = \frac{1}{2 + 2} + 3 = \frac{1}{4} + 3 = \frac{13}{4}$
>
> Left-hand limit:
>
> $\displaystyle \lim_{x \to 1^-} g(x) = \lim_{x \to 1^-} (k x^2 + 2x - 1) = k(1)^2 + 2(1) - 1 = k + 1$
>
> For continuity at $x = 1$, the left-hand limit, right-hand limit, and function value must all be equal:
>
> $\displaystyle k + 1 = \frac{13}{4} \;\Longrightarrow\; k = \frac{13}{4} - 1 = \frac{9}{4}$
>
> $\displaystyle m = g(1) = \lim_{x \to 1} g(x) = \frac{13}{4}$
>
> **Stage 4 (Interpretation & Boundary Check).** With $k = \frac{9}{4}$ and $m = \frac{13}{4}$, $\lim_{x \to 1^-} g(x) = \frac{9}{4} + 1 = \frac{13}{4}$, $\lim_{x \to 1^+} g(x) = \frac{13}{4}$, and $g(1) = \frac{13}{4}$. All three continuity conditions hold, making $g(x)$ continuous on $\mathbb{R} = \mathopen{]}-\infty, +\infty\mathclose{[}$.

### Q5

**1.**

> **Stage 1 (Classification & Domain).** Let $f(x) = x^3 - 3x + 1$. The equation $x^3 - 3x + 1 = 0$ corresponds to finding roots where $f(x) = 0$.
>
> **Stage 2 (Algebraic Preparation).** Verify IVT hypotheses on $[1, 2]$:
>
> Hypothesis 1: As a polynomial, $f$ is continuous on the entire real line $\mathbb{R}$, and therefore $f$ is continuous on the closed bounded interval $[1, 2]$.
>
> **Stage 3 (Core Operation).** Evaluate $f$ at the interval endpoints:
>
> $\displaystyle f(1) = (1)^3 - 3(1) + 1 = 1 - 3 + 1 = -1$
>
> $\displaystyle f(2) = (2)^3 - 3(2) + 1 = 8 - 6 + 1 = 3$
>
> Check IVT Hypothesis 2: Target value $u = 0$ lies strictly between $f(1) = -1$ and $f(2) = 3$:
>
> $\displaystyle f(1) = -1 < 0 < 3 = f(2)$
>
> **Stage 4 (Interpretation & Boundary Check).** Both hypotheses of the Intermediate Value Theorem are satisfied. Therefore, by the IVT, there exists at least one real number $c \in \mathopen{]}1, 2\mathclose{[}$ such that $f(c) = 0$.

**2.**

> **Stage 1 (Classification & Domain).** Apply the bisection method to isolate the root of $f(x) = x^3 - 3x + 1$ on $[1, 2]$ until the interval width $w \le 0.25$.
>
> **Stage 2 (Algebraic Preparation).** Initial interval $[a_0, b_0] = [1, 2]$ with $f(1) = -1 < 0$ and $f(2) = 3 > 0$. Width $w_0 = 2 - 1 = 1.0$.
>
> **Stage 3 (Core Operation).** Execute successive bisections:
>
> - **Iteration 1:** Midpoint $m_1 = \frac{1 + 2}{2} = 1.5 = \frac{3}{2}$.
>
>   Evaluate $f(1.5)$:
>
>   $\displaystyle f(1.5) = (1.5)^3 - 3(1.5) + 1 = 3.375 - 4.5 + 1 = -0.125 = -\frac{1}{8} < 0$
>
>   Since $f(1.5) < 0$ and $f(2) > 0$, the sign change occurs on $[1.5, 2]$. New width: $w_1 = 2 - 1.5 = 0.5$.
>
> - **Iteration 2:** Midpoint $m_2 = \frac{1.5 + 2}{2} = 1.75 = \frac{7}{4}$.
>
>   Evaluate $f(1.75)$:
>
>   $\displaystyle f(1.75) = \left(\frac{7}{4}\right)^3 - 3\left(\frac{7}{4}\right) + 1 = \frac{343}{64} - \frac{21}{4} + 1 = \frac{343 - 336 + 64}{64} = \frac{71}{64} > 0$
>
>   Since $f(1.5) < 0$ and $f(1.75) > 0$, the root is trapped in the subinterval $[1.5, 1.75]$.
>
>   New width: $w_2 = 1.75 - 1.5 = 0.25 \le 0.25$.
>
> **Stage 4 (Interpretation & Boundary Check).** The root is guaranteed to lie in the open interval $\mathopen{]}1.5, 1.75\mathclose{[}$ (or in fractional Bourbaki notation, $\mathopen{]}\frac{3}{2}, \frac{7}{4}\mathclose{[}$).

### Q6

**1.**

> **Stage 1 (Classification & Domain).** For $x > 2$, $P(x) = \frac{\sqrt{3x + 10} - 4}{x - 2} + 7$. Direct substitution of $x = 2$ into the quotient gives $\frac{\sqrt{16} - 4}{0} = \frac{0}{0}$, an indeterminate radical difference.
>
> **Stage 2 (Algebraic Preparation).** Multiply numerator and denominator by the conjugate $\sqrt{3x + 10} + 4$:
>
> $\displaystyle \frac{\sqrt{3x + 10} - 4}{x - 2} \cdot \frac{\sqrt{3x + 10} + 4}{\sqrt{3x + 10} + 4} = \frac{(3x + 10) - 16}{(x - 2)(\sqrt{3x + 10} + 4)} = \frac{3x - 6}{(x - 2)(\sqrt{3x + 10} + 4)}$
>
> Factor the numerator: $3x - 6 = 3(x - 2)$. For all $x > 2$, cancel the common factor $(x - 2)$:
>
> $\displaystyle \frac{3(x - 2)}{(x - 2)(\sqrt{3x + 10} + 4)} = \frac{3}{\sqrt{3x + 10} + 4} \quad (x > 2)$
>
> **Stage 3 (Core Operation).** Evaluate the downstream limit as $x \to 2^+$:
>
> $\displaystyle \lim_{x \to 2^+} P(x) = \lim_{x \to 2^+} \left[\frac{3}{\sqrt{3x + 10} + 4} + 7\right] = \frac{3}{\sqrt{3(2) + 10} + 4} + 7 = \frac{3}{4 + 4} + 7 = \frac{3}{8} + 7 = \frac{59}{8} = 7.375\text{ kPa}$
>
> **Stage 4 (Interpretation & Boundary Check).** Downstream pressure near the membrane interface approaches $\frac{59}{8}\text{ kPa}$.

**2.**

> **Stage 1 (Classification & Domain).** Upstream pressure for $x < 2$ is rational function $P(x) = \frac{\alpha x^2 + 8x}{x + 2}$. Since $x + 2 \ge 2 > 0$ for $x \in [0, 2]$, the denominator never vanishes on the upstream channel.
>
> **Stage 2 (Algebraic Preparation).** Evaluate the upstream limit as $x \to 2^-$ by direct substitution:
>
> $\displaystyle \lim_{x \to 2^-} P(x) = \frac{\alpha(2)^2 + 8(2)}{2 + 2} = \frac{4\alpha + 16}{4} = \alpha + 4$
>
> **Stage 3 (Core Operation).** For the pressure profile to avoid an abrupt jump at $x = 2$, directional limits must agree:
>
> $\displaystyle \lim_{x \to 2^-} P(x) = \lim_{x \to 2^+} P(x) \;\Longrightarrow\; \alpha + 4 = \frac{59}{8}$
>
> Solve for $\alpha$:
>
> $\displaystyle \alpha = \frac{59}{8} - 4 = \frac{59 - 32}{8} = \frac{27}{8} = 3.375$
>
> For continuity at $x = 2$, the membrane interface pressure $P(2) = \beta$ must equal this common limit:
>
> $\displaystyle \beta = \lim_{x \to 2} P(x) = \frac{59}{8} = 7.375\text{ kPa}$
>
> **Stage 4 (Interpretation & Boundary Check).** Tuning $\alpha = \frac{27}{8}$ eliminates the shear stress jump at the filter interface, establishing continuity across the membrane boundary.

**3.**

> **Stage 1 (Classification & Domain).** On the interval $[0, 2]$, the continuous pressure formula is $P(x) = \frac{\frac{27}{8} x^2 + 8x}{x + 2}$. The target pressure is $u = 5.0\text{ kPa}$.
>
> **Stage 2 (Algebraic Preparation).** Evaluate endpoint pressures:
>
> At inlet $x = 0$: $P(0) = \frac{0 + 0}{0 + 2} = 0\text{ kPa}$.
>
> At interface $x = 2$: $P(2) = \beta = \frac{59}{8} = 7.375\text{ kPa}$.
>
> Verify IVT hypotheses: $P(x)$ is continuous on $[0, 2]$ because it is a rational function with non-zero denominator ($x + 2 \ge 2 > 0$).
>
> Target value $u = 5.0\text{ kPa}$ lies strictly between $P(0) = 0$ and $P(2) = 7.375$:
>
> $\displaystyle P(0) = 0 < 5.0 < 7.375 = P(2)$
>
> By the Intermediate Value Theorem, there exists at least one trigger location $x_c \in \mathopen{]}0, 2\mathclose{[}$ such that $P(x_c) = 5.0\text{ kPa}$.
>
> **Stage 3 (Core Operation).** Set $P(x_c) = 5$ and solve for $x_c$:
>
> $\displaystyle \frac{\frac{27}{8} x_c^2 + 8x_c}{x_c + 2} = 5$
>
> Clear denominators by multiplying by $8(x_c + 2)$:
>
> $\displaystyle 27 x_c^2 + 64 x_c = 40(x_c + 2) = 40 x_c + 80$
>
> Rearrange into standard quadratic form:
>
> $\displaystyle 27 x_c^2 + 24 x_c - 80 = 0$
>
> Compute the discriminant:
>
> $\displaystyle D = 24^2 - 4(27)(-80) = 576 + 8640 = 9216 = 96^2$
>
> Solve for $x_c$ using the quadratic formula:
>
> $\displaystyle x_c = \frac{-24 \pm 96}{2(27)} = \frac{-24 \pm 96}{54}$
>
> Two algebraic roots:
>
> $\displaystyle x_{c,1} = \frac{-24 + 96}{54} = \frac{72}{54} = \frac{4}{3} \approx 1.333\text{ mm}$
>
> $\displaystyle x_{c,2} = \frac{-24 - 96}{54} = \frac{-120}{54} = -\frac{20}{9} \approx -2.222\text{ mm}$
>
> **Stage 4 (Interpretation & Boundary Check).** Physical channel boundary requires $x_c \in [0, 2]$. The negative root $-\frac{20}{9}$ is extraneous to the physical domain. The unique trigger location in the channel is:
>
> $\displaystyle x_c = \frac{4}{3}\text{ mm} \in \mathopen{]}0, 2\mathclose{[}$
>
> Verification: $P(4/3) = \frac{\frac{27}{8}(16/9) + 8(4/3)}{4/3 + 2} = \frac{6 + 32/3}{10/3} = \frac{50/3}{10/3} = 5.0\text{ kPa}$. Verified exact solution: $x_c = \frac{4}{3}\text{ mm}$.
