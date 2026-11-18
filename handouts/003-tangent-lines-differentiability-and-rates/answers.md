---
title: "Handout 003: Tangent Lines & Differentiability — Key"
---

# 003: Tangent Lines, Differentiability, and Rates of Change — Answer Key

## Exercises

### Q1

**1.**

> **Stage 1 (Classification & Domain).** The function $f(x) = \frac{2}{x + 3}$ is a rational function with domain $\mathopen{]}-\infty, -3\mathclose{[} \cup \mathopen{]}-3, +\infty\mathclose{[}$. The evaluation point $a = 1$ is an interior domain point with $f(1) = \frac{2}{1 + 3} = \frac{2}{4} = \frac{1}{2}$.
>
> **Stage 2 (Algebraic Preparation).** Set up the difference quotient with increment $h$:
>
> $\displaystyle \frac{f(1 + h) - f(1)}{h} = \frac{\frac{2}{(1 + h) + 3} - \frac{1}{2}}{h} = \frac{\frac{2}{4 + h} - \frac{1}{2}}{h}$
>
> Combine the numerator fractions over the common denominator $2(4 + h)$:
>
> $\displaystyle \frac{2(2) - (4 + h)}{2(4 + h)} = \frac{4 - 4 - h}{2(4 + h)} = \frac{-h}{2(4 + h)}$
>
> Divide by $h$ (valid for $h \ne 0$):
>
> $\displaystyle \frac{\frac{-h}{2(4 + h)}}{h} = \frac{-h}{2h(4 + h)} = \frac{-1}{2(4 + h)}$
>
> **Stage 3 (Core Operation).** Evaluate the limit as $h \to 0$ using limit laws:
>
> $\displaystyle f'(1) = \lim_{h \to 0} \frac{-1}{2(4 + h)} = \frac{-1}{2(4 + 0)} = -\frac{1}{8}$
>
> **Stage 4 (Interpretation & Boundary Check).** The tangent line to $y = \frac{2}{x + 3}$ at $(1, 1/2)$ has negative slope $m = -1/8$, consistent with a decreasing rational branch on $\mathopen{]}-3, +\infty\mathclose{[}$.
>
> Verified value: $f'(1) = -\dfrac{1}{8}$.

**2.**

> **Stage 1 (Classification & Domain).** The function $f(x) = \sqrt{3x + 1}$ requires $3x + 1 \ge 0 \;\Longrightarrow\; x \ge -1/3$. The domain of $f(x)$ is $[-1/3, +\infty\mathclose{[}$.
>
> **Stage 2 (Algebraic Preparation).** Formulate the difference quotient for arbitrary $x > -1/3$:
>
> $\displaystyle \frac{f(x + h) - f(x)}{h} = \frac{\sqrt{3(x + h) + 1} - \sqrt{3x + 1}}{h} = \frac{\sqrt{3x + 3h + 1} - \sqrt{3x + 1}}{h}$
>
> Multiply numerator and denominator by the conjugate radical expression $\sqrt{3x + 3h + 1} + \sqrt{3x + 1}$:
>
> $\displaystyle \frac{(\sqrt{3x + 3h + 1} - \sqrt{3x + 1})(\sqrt{3x + 3h + 1} + \sqrt{3x + 1})}{h(\sqrt{3x + 3h + 1} + \sqrt{3x + 1})} = \frac{(3x + 3h + 1) - (3x + 1)}{h(\sqrt{3x + 3h + 1} + \sqrt{3x + 1})}$
>
> Simplify the algebraic numerator:
>
> $\displaystyle \frac{3h}{h(\sqrt{3x + 3h + 1} + \sqrt{3x + 1})} = \frac{3}{\sqrt{3x + 3h + 1} + \sqrt{3x + 1}} \quad (h \ne 0)$
>
> **Stage 3 (Core Operation).** Evaluate the limit as $h \to 0$:
>
> $\displaystyle f'(x) = \lim_{h \to 0} \frac{3}{\sqrt{3x + 3h + 1} + \sqrt{3x + 1}} = \frac{3}{\sqrt{3x + 1} + \sqrt{3x + 1}} = \frac{3}{2\sqrt{3x + 1}}$
>
> **Stage 4 (Interpretation & Boundary Check).** The derivative denominator requires $3x + 1 > 0$, excluding the endpoint $x = -1/3$ where a vertical tangent forms.
>
> Verified formula: $f'(x) = \dfrac{3}{2\sqrt{3x + 1}}$.
>
> Verified domains: $\operatorname{dom}(f) = [-1/3, +\infty\mathclose{[}$, $\operatorname{dom}(f') = \mathopen{]}-1/3, +\infty\mathclose{[}$.

### Q2

**1.**

> **Stage 1 (Classification & Domain).** The cubic function $f(x) = x^3 - 4x + 1$ is a polynomial with domain $\mathopen{]}-\infty, +\infty\mathclose{[}$. At $x = 2$, $f(2) = 2^3 - 4(2) + 1 = 8 - 8 + 1 = 1$, confirming the point of tangency $(2, 1)$.
>
> **Stage 2 (Algebraic Preparation).** Set up the difference quotient at $a = 2$:
>
> $\displaystyle f(2 + h) = (2 + h)^3 - 4(2 + h) + 1 = (8 + 12h + 6h^2 + h^3) - (8 + 4h) + 1 = 1 + 8h + 6h^2 + h^3$
>
> Subtract $f(2) = 1$ and divide by $h$:
>
> $\displaystyle \frac{f(2 + h) - f(2)}{h} = \frac{8h + 6h^2 + h^3}{h} = 8 + 6h + h^2 \quad (h \ne 0)$
>
> **Stage 3 (Core Operation).** Evaluate the limit as $h \to 0$:
>
> $\displaystyle m = f'(2) = \lim_{h \to 0} (8 + 6h + h^2) = 8 + 0 + 0 = 8$
>
> Apply point-slope form with slope $m = 8$ through $(2, 1)$:
>
> $\displaystyle y - 1 = 8(x - 2)$
>
> Expand into slope-intercept form:
>
> $\displaystyle y - 1 = 8x - 16 \;\Longrightarrow\; y = 8x - 15$
>
> **Stage 4 (Interpretation & Boundary Check).** At $x = 2$, $y = 8(2) - 15 = 1$. The tangent line passes through $(2, 1)$ with slope $8$.
>
> Verified equations: point-slope form $y - 1 = 8(x - 2)$; slope-intercept form $y = 8x - 15$.

**2.**

> **Stage 1 (Classification & Domain).** The linear approximation function $L(x)$ at center $a = 2$ uses the base value $f(2) = 1$ and derivative slope $f'(2) = 8$.
>
> **Stage 2 (Algebraic Preparation).** Assemble the linearization formula:
>
> $\displaystyle L(x) = f(2) + f'(2)(x - 2) = 1 + 8(x - 2) = 8x - 15$
>
> **Stage 3 (Core Operation).** Evaluate $L(x)$ at $x = 2.03$ and $x = 1.97$:
>
> $\displaystyle L(2.03) = 1 + 8(2.03 - 2) = 1 + 8(0.03) = 1 + 0.24 = 1.24$
>
> $\displaystyle L(1.97) = 1 + 8(1.97 - 2) = 1 + 8(-0.03) = 1 - 0.24 = 0.76$
>
> Compute the exact values using $f(x) = x^3 - 4x + 1$:
>
> $\displaystyle f(2.03) = (2.03)^3 - 4(2.03) + 1 = 8.365427 - 8.12 + 1 = 1.245427$
>
> $\displaystyle f(1.97) = (1.97)^3 - 4(1.97) + 1 = 7.645373 - 7.88 + 1 = 0.765373$
>
> Calculate approximation discrepancies:
>
> $\displaystyle |f(2.03) - L(2.03)| = |1.245427 - 1.24| = 0.005427$
>
> $\displaystyle |f(1.97) - L(1.97)| = |0.765373 - 0.76| = 0.005373$
>
> **Stage 4 (Interpretation & Boundary Check).** Because $f''(2) = 6(2) = 12 > 0$, the curve is concave upward at $x = 2$. Consequently, the tangent line lies below the curve locally, making both $L(2.03)$ and $L(1.97)$ slight underestimates.
>
> Verified linear approximation: $L(x) = 1 + 8(x - 2)$; estimates: $L(2.03) = 1.24$ (true: $1.245427$), $L(1.97) = 0.76$ (true: $0.765373$).

### Q3

**1. Correct answer: A.**

- **A (Correct):** The function is continuous everywhere on $\mathbb{R}$ and its difference quotient $\frac{\sqrt[3]{h}}{h} = \frac{1}{h^{2/3}} \to +\infty$ as $h \to 0$, creating a vertical tangent line $x = 0$ while failing differentiability.
- **B (Incorrect):** Incorrectly asserts a jump discontinuity; the function is continuous at $x = 0$ with $\lim_{x \to 0} \sqrt[3]{x} = 0 = f(0)$.
- **C (Incorrect):** Conflates geometric existence of a tangent line with mathematical differentiability; a vertical tangent line has infinite slope, so the derivative does not exist as a finite real number.
- **D (Incorrect):** Misclassifies the geometry as a sharp corner with unequal finite slopes, whereas the slopes blow up to positive infinity from both sides.
- **E (Incorrect):** Assumes the false converse of the differentiability theorem; continuity is necessary but not sufficient for differentiability.


### Q4

**1.**

> **Stage 1 (Classification & Domain).** The position function $s(t) = 2t^3 - 9t^2 + 12t$ is a polynomial defined on the time domain $[0, +\infty\mathclose{[}$.
>
> **Stage 2 (Algebraic Preparation).** Instantaneous velocity is the first derivative $v(t) = s'(t)$; instantaneous acceleration is the second derivative $a(t) = v'(t) = s''(t)$.
>
> **Stage 3 (Core Operation).** Differentiating with respect to $t$:
>
> $\displaystyle v(t) = s'(t) = 6t^2 - 18t + 12 = 6(t^2 - 3t + 2) = 6(t - 1)(t - 2) \quad (\text{m/s})$
>
> Differentiating velocity with respect to $t$:
>
> $\displaystyle a(t) = v'(t) = 12t - 18 = 6(2t - 3) \quad (\text{m/s}^2)$
>
> **Stage 4 (Interpretation & Boundary Check).** Units are verified: position in meters, velocity in meters per second, acceleration in meters per second squared.
>
> Verified formulas: $v(t) = 6t^2 - 18t + 12 = 6(t - 1)(t - 2)\text{ m/s}$, $a(t) = 12t - 18\text{ m/s}^2$.

**2.**

> **Stage 1 (Classification & Domain).** The motion domain is $t \in [0, +\infty\mathclose{[}$. Direction of motion is governed by the sign of velocity $v(t) = 6(t - 1)(t - 2)$.
>
> **Stage 2 (Algebraic Preparation).** Set $v(t) = 0$ to identify stationary points:
>
> $\displaystyle 6(t - 1)(t - 2) = 0 \;\Longrightarrow\; t = 1\text{ s} \quad\text{and}\quad t = 2\text{ s}$
>
> **Stage 3 (Core Operation).** Analyze the sign of $v(t)$ across partition intervals:
> - On $[0, 1\mathclose{[}$: for $t = 0.5$, $v(0.5) = 6(-0.5)(-1.5) = +4.5 > 0$. The particle moves in the positive direction.
> - At $t = 1$: $v(1) = 0$. The particle is temporarily at rest.
> - On $\mathopen{]}1, 2\mathclose{[}$: for $t = 1.5$, $v(1.5) = 6(0.5)(-0.5) = -1.5 < 0$. The particle moves in the negative direction.
> - At $t = 2$: $v(2) = 0$. The particle is temporarily at rest.
> - On $\mathopen{]}2, +\infty\mathclose{[}$: for $t = 3$, $v(3) = 6(2)(1) = +12 > 0$. The particle moves in the positive direction.
>
> **Stage 4 (Interpretation & Boundary Check).** Reversal of velocity sign occurs at $t = 1\text{ s}$ (from forward to backward) and at $t = 2\text{ s}$ (from backward to forward).
>
> Verified positive direction intervals: $[0, 1\mathclose{[} \cup \mathopen{]}2, +\infty\mathclose{[}$.
>
> Verified negative direction interval: $\mathopen{]}1, 2\mathclose{[}$.
>
> Verified resting instants: $t = 1\text{ s}$ and $t = 2\text{ s}$.

**3.**

> **Stage 1 (Classification & Domain).** The time window is $[0, 3]$. Direction reversals occur inside this window at $t = 1$ and $t = 2$.
>
> **Stage 2 (Algebraic Preparation).** Compute positions at boundary times and turning points:
>
> $\displaystyle s(0) = 2(0)^3 - 9(0)^2 + 12(0) = 0\text{ m}$
>
> $\displaystyle s(1) = 2(1)^3 - 9(1)^2 + 12(1) = 2 - 9 + 12 = 5\text{ m}$
>
> $\displaystyle s(2) = 2(2)^3 - 9(2)^2 + 12(2) = 16 - 36 + 24 = 4\text{ m}$
>
> $\displaystyle s(3) = 2(3)^3 - 9(3)^2 + 12(3) = 54 - 81 + 36 = 9\text{ m}$
>
> **Stage 3 (Core Operation).**
> - Net displacement:
>
> $\displaystyle \Delta s = s(3) - s(0) = 9 - 0 = 9\text{ meters}$
>
> - Total distance traveled sums absolute displacements across each monotonic segment:
>
> $\displaystyle d_{\text{total}} = |s(1) - s(0)| + |s(2) - s(1)| + |s(3) - s(2)|$
>
> $\displaystyle d_{\text{total}} = |5 - 0| + |4 - 5| + |9 - 4| = 5 + 1 + 5 = 11\text{ meters}$
>
> **Stage 4 (Interpretation & Boundary Check).** Total distance ($11\text{ m}$) strictly exceeds net displacement ($9\text{ m}$) because the particle moves backward by $1\text{ m}$ (from $s = 5$ to $s = 4$) before resuming forward motion.
>
> Verified net displacement: $9\text{ meters}$; verified total distance: $11\text{ meters}$.

### Q5

**1.**

> **Stage 1 (Classification & Domain).** The function $f(x)$ is defined piecewise by quadratic polynomial $x^2 + 2x$ on $\mathopen{]}-\infty, 1]$ and linear polynomial $mx + b$ on $\mathopen{]}1, +\infty\mathclose{[}$. Both pieces are infinitely differentiable on their open domains; differentiability on $\mathbb{R}$ requires continuity and differentiability at the interface $x = 1$.
>
> **Stage 2 (Algebraic Preparation).**
> - Continuity requirement at $x = 1$: $\lim_{x \to 1^-} f(x) = \lim_{x \to 1^+} f(x) = f(1)$.
>
> $\displaystyle f(1) = 1^2 + 2(1) = 3$
>
> $\displaystyle \lim_{x \to 1^-} (x^2 + 2x) = 3, \qquad \lim_{x \to 1^+} (mx + b) = m(1) + b = m + b$
>
> Setting the limits equal gives the continuity equation:
>
> $\displaystyle m + b = 3 \;\Longrightarrow\; b = 3 - m$
>
> - Differentiability requirement at $x = 1$: one-sided derivatives must match.
>
> For $x < 1$, $\frac{d}{dx}(x^2 + 2x) = 2x + 2 \;\Longrightarrow\; \lim_{x \to 1^-} f'(x) = 2(1) + 2 = 4$.
>
> For $x > 1$, $\frac{d}{dx}(mx + b) = m \;\Longrightarrow\; \lim_{x \to 1^+} f'(x) = m$.
>
> **Stage 3 (Core Operation).** Equate the one-sided derivative limits:
>
> $\displaystyle m = 4$
>
> Substitute $m = 4$ into the continuity equation:
>
> $\displaystyle b = 3 - 4 = -1$
>
> **Stage 4 (Interpretation & Boundary Check).** With $m = 4$ and $b = -1$, the function values match at $x = 1$ ($3 = 3$) and the tangent slopes match ($4 = 4$), ensuring no corner or jump occurs.
>
> Verified parameter values: $m = 4$ and $b = -1$.

**2.**

> **Stage 1 (Classification & Domain).** We verify differentiability from the foundational limit definition with $f(1) = 3$, $m = 4$, and $b = -1$.
>
> **Stage 2 (Algebraic Preparation).**
> - Left-hand difference quotient ($h < 0$, so $1 + h < 1$):
>
> $\displaystyle f(1 + h) = (1 + h)^2 + 2(1 + h) = (1 + 2h + h^2) + (2 + 2h) = 3 + 4h + h^2$
>
> $\displaystyle \frac{f(1 + h) - f(1)}{h} = \frac{(3 + 4h + h^2) - 3}{h} = \frac{4h + h^2}{h} = 4 + h \quad (h \ne 0)$
>
> - Right-hand difference quotient ($h > 0$, so $1 + h > 1$):
>
> $\displaystyle f(1 + h) = 4(1 + h) - 1 = 4 + 4h - 1 = 3 + 4h$
>
> $\displaystyle \frac{f(1 + h) - f(1)}{h} = \frac{(3 + 4h) - 3}{h} = \frac{4h}{h} = 4 \quad (h \ne 0)$
>
> **Stage 3 (Core Operation).** Evaluate one-sided limits as $h \to 0$:
>
> $\displaystyle \lim_{h \to 0^-} \frac{f(1 + h) - f(1)}{h} = \lim_{h \to 0^-} (4 + h) = 4 + 0 = 4$
>
> $\displaystyle \lim_{h \to 0^+} \frac{f(1 + h) - f(1)}{h} = \lim_{h \to 0^+} 4 = 4$
>
> **Stage 4 (Interpretation & Boundary Check).** Because both one-sided difference quotients exist and equal $4$, the two-sided limit exists:
>
> $\displaystyle f'(1) = \lim_{h \to 0} \frac{f(1 + h) - f(1)}{h} = 4$
>
> Verified conclusion: $f'(1) = 4$, rigorously establishing differentiability at $x = 1$ and therefore everywhere on $\mathbb{R}$.

### Q6

**1.**

> **Stage 1 (Classification & Domain).** The first-stage altitude function $y_1(t) = 4t^2$ is defined on $[0, 10]$.
>
> **Stage 2 (Algebraic Preparation).** Set up the difference quotient for $t \in [0, 10]$:
>
> $\displaystyle \frac{y_1(t + h) - y_1(t)}{h} = \frac{4(t + h)^2 - 4t^2}{h} = \frac{4(t^2 + 2th + h^2) - 4t^2}{h} = \frac{8th + 4h^2}{h}$
>
> Factor $h$ for $h \ne 0$: $\frac{h(8t + 4h)}{h} = 8t + 4h$.
>
> **Stage 3 (Core Operation).** Evaluate the limit as $h \to 0$:
>
> $\displaystyle v_1(t) = y'_1(t) = \lim_{h \to 0} (8t + 4h) = 8t \quad (\text{m/s})$
>
> Evaluate velocity and altitude at burnout time $t = 10\text{ s}$:
>
> $\displaystyle v_1(10) = 8(10) = 80\text{ m/s}$
>
> $\displaystyle y_1(10) = 4(10)^2 = 400\text{ meters}$
>
> **Stage 4 (Interpretation & Boundary Check).** At $t = 0$, $v_1(0) = 0\text{ m/s}$ (starts from rest) and $y_1(0) = 0\text{ m}$. At $t = 10$, the rocket attains $400\text{ m}$ altitude and climbs at $80\text{ m/s}$.
>
> Verified burnout values: $v_1(t) = 8t\text{ m/s}$; $v_1(10) = 80\text{ m/s}$; $y_1(10) = 400\text{ meters}$.

**2.**

> **Stage 1 (Classification & Domain).** The upper stage altitude is $y_2(t) = k\sqrt{t - 1} + h_0$ for $t > 10$. Smooth physical flight requires $y(t)$ to be continuous and differentiable at $t = 10\text{ s}$.
>
> **Stage 2 (Algebraic Preparation).**
> - Velocity for $t > 10$:
>
> $\displaystyle v_2(t) = y'_2(t) = \frac{d}{dt}\left(k(t - 1)^{1/2} + h_0\right) = \frac{k}{2\sqrt{t - 1}}$
>
> - Equating velocities at $t = 10\text{ s}$ to prevent infinite acceleration impulses:
>
> $\displaystyle \lim_{t \to 10^+} v_2(t) = v_1(10) \;\Longrightarrow\; \frac{k}{2\sqrt{10 - 1}} = 80 \;\Longrightarrow\; \frac{k}{2(3)} = 80 \;\Longrightarrow\; \frac{k}{6} = 80$
>
> **Stage 3 (Core Operation).** Solve for $k$:
>
> $\displaystyle k = 80 \times 6 = 480$
>
> Now apply the continuity condition for altitude at $t = 10\text{ s}$:
>
> $\displaystyle \lim_{t \to 10^+} y_2(t) = y_1(10) \;\Longrightarrow\; 480\sqrt{10 - 1} + h_0 = 400$
>
> $\displaystyle 480(3) + h_0 = 400 \;\Longrightarrow\; 1440 + h_0 = 400 \;\Longrightarrow\; h_0 = 400 - 1440 = -1040$
>
> **Stage 4 (Interpretation & Boundary Check).** Check: $y_2(10) = 480(3) - 1040 = 1440 - 1040 = 400\text{ m}$, and $v_2(10) = \frac{480}{6} = 80\text{ m/s}$, matching the first-stage terminal conditions exactly.
>
> Verified parameter values: $k = 480$ and $h_0 = -1040$.

**3.**

> **Stage 1 (Classification & Domain).** The linearization center is $t_0 = 10\text{ s}$, with base altitude $y(10) = 400\text{ m}$ and velocity $y'(10) = 80\text{ m/s}$.
>
> **Stage 2 (Algebraic Preparation).** Construct the tangent line equation:
>
> $\displaystyle L(t) = y(10) + y'(10)(t - 10) = 400 + 80(t - 10)$
>
> **Stage 3 (Core Operation).** Evaluate at $t = 10.5\text{ s}$:
>
> $\displaystyle L(10.5) = 400 + 80(10.5 - 10) = 400 + 80(0.5) = 400 + 40 = 440\text{ meters}$
>
> Calculate the true altitude using $y_2(t) = 480\sqrt{t - 1} - 1040$:
>
> $\displaystyle y_2(10.5) = 480\sqrt{10.5 - 1} - 1040 = 480\sqrt{9.5} - 1040$
>
> Since $\sqrt{9.5} \approx 3.082207$:
>
> $\displaystyle y_2(10.5) \approx 480(3.082207) - 1040 \approx 1479.459 - 1040 = 439.459\text{ meters}$
>
> Discrepancy:
>
> $\displaystyle L(10.5) - y_2(10.5) \approx 440 - 439.459 = 0.541\text{ meters}$
>
> **Stage 4 (Interpretation & Boundary Check).** The linear approximation overestimates the true altitude by approximately $0.54\text{ m}$ because the upper stage is decelerating ($y''_2(t) < 0$, concave down).
>
> Verified linearization: $L(t) = 400 + 80(t - 10)$; estimated altitude: $L(10.5) = 440\text{ m}$; true altitude: $y_2(10.5) \approx 439.46\text{ m}$ (discrepancy $+0.54\text{ m}$).

**4.**

> **Stage 1 (Classification & Domain).** Acceleration is the derivative of velocity: $a(t) = v'(t) = y''(t)$.
>
> **Stage 2 (Algebraic Preparation).**
> - For powered ascent $t \in [0, 10\mathclose{[}$:
>
> $\displaystyle v_1(t) = 8t \;\Longrightarrow\; a_1(t) = \frac{d}{dt}(8t) = 8\text{ m/s}^2$
>
> - For unpowered glide $t \in \mathopen{]}10, 26\mathclose{]}$:
>
> $\displaystyle v_2(t) = 240(t - 1)^{-1/2} \;\Longrightarrow\; a_2(t) = 240\left(-\frac{1}{2}\right)(t - 1)^{-3/2} = -\frac{120}{(t - 1)^{3/2}}\text{ m/s}^2$
>
> **Stage 3 (Core Operation).**
> Evaluate acceleration at $t = 17\text{ s}$ ($t - 1 = 16$):
>
> $\displaystyle a_2(17) = -\frac{120}{16^{3/2}} = -\frac{120}{(4)^3} = -\frac{120}{64} = -\frac{15}{8} = -1.875\text{ m/s}^2$
>
> Examine the acceleration limit across the staging boundary $t = 10\text{ s}$:
>
> $\displaystyle \lim_{t \to 10^-} a(t) = 8\text{ m/s}^2$
>
> $\displaystyle \lim_{t \to 10^+} a(t) = -\frac{120}{(10 - 1)^{3/2}} = -\frac{120}{9^{3/2}} = -\frac{120}{27} = -\frac{40}{9} \approx -4.44\text{ m/s}^2$
>
> **Stage 4 (Interpretation & Boundary Check).** Because $\lim_{t \to 10^-} a(t) = 8 \ne -40/9 = \lim_{t \to 10^+} a(t)$, the acceleration function has a jump discontinuity of $\Delta a = -40/9 - 8 = -112/9 \approx -12.44\text{ m/s}^2$ at staging. The vehicle's motion is continuously differentiable ($C^1$), but not twice continuously differentiable ($C^2$), producing a sharp physical jerk at motor burnout.
>
> Verified acceleration formulas: $a(t) = 8\text{ m/s}^2$ on $[0, 10\mathclose{[}$; $a(t) = -\dfrac{120}{(t - 1)^{3/2}}\text{ m/s}^2$ on $\mathopen{]}10, 26\mathclose{]}$.
>
> Verified value at $17\text{ s}$: $a(17) = -\dfrac{15}{8} = -1.875\text{ m/s}^2$. Acceleration is discontinuous at $t = 10\text{ s}$ (jump discontinuity from $+8$ to $-40/9\text{ m/s}^2$).
