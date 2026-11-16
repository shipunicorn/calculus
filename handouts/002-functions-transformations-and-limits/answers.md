---
title: "Handout 002: Functions & Limits — Answer Key"
---

# 002: Functions, Transformations, and Limits — Answer Key

## Exercises

### Q1

**1.**
```text
Stage 1 (Classification & Domain):
Rational function f(x) = (3x - 1)/(x^2 - 4x - 12). Denominator cannot be zero.

Stage 2 (Algebraic Preparation):
Factor quadratic: x^2 - 4x - 12 = (x - 6)(x + 2) = 0  ==>  x = -2, 6.

Stage 3 (Core Operation):
Exclude singularities from real numbers: (-inf, -2) U (-2, 6) U (6, inf).

Stage 4 (Interpretation & Boundary Check):
Numerator at roots: f(-2) -> -7/0, f(6) -> 17/0. Both are vertical asymptotes.
Verified domain: (-inf, -2) U (-2, 6) U (6, inf).
```

**2.**
```text
Stage 1 (Classification & Domain):
Difference of radicals g(t) = sqrt(5 - t) - sqrt(t + 3). Radicands must be non-negative.

Stage 2 (Algebraic Preparation):
Solve individual inequalities: 5 - t >= 0 ==> t <= 5; t + 3 >= 0 ==> t >= -3.

Stage 3 (Core Operation):
Intersect requirements: -3 <= t <= 5, which in interval notation is [-3, 5].

Stage 4 (Interpretation & Boundary Check):
At t = -3: g(-3) = sqrt(8) - 0 = 2*sqrt(2). At t = 5: g(5) = -2*sqrt(2).
Both endpoints are included (closed brackets). Verified domain: [-3, 5].
```

**3.**
```text
Stage 1 (Classification & Domain):
Fourth-root in denominator h(x) = (2x + 7)/((x^2 - 4x)^(1/4)). Radicand must be strictly positive.

Stage 2 (Algebraic Preparation):
Factor: x(x - 4) > 0. Roots are x = 0 and x = 4. Testing signs shows positive on (-inf, 0) and (4, inf).

Stage 3 (Core Operation):
Collect positive intervals: (-inf, 0) U (4, inf).

Stage 4 (Interpretation & Boundary Check):
At x = 0 and x = 4, division by zero occurs (open parentheses).
Verified domain: (-inf, 0) U (4, inf).
```

**4.**
```text
Stage 1 (Classification & Domain):
Nested fraction k(u) = (u - 2)/(2 - 6/(u + 1)). All denominators must be non-zero simultaneously.

Stage 2 (Algebraic Preparation):
Inner denominator: u + 1 != 0 ==> u != -1.
Main denominator: 2 - 6/(u + 1) = 0 ==> 2(u + 1) - 6 = 0 ==> 2u - 4 = 0 ==> u = 2.

Stage 3 (Core Operation):
Exclude singularities u = -1 and u = 2: (-inf, -1) U (-1, 2) U (2, inf).

Stage 4 (Interpretation & Boundary Check):
Simplifying (u - 2)/[(2u - 4)/(u + 1)] = (u + 1)/2 cancels (u - 2), but u = 2 remains a hole.
Verified domain: (-inf, -1) U (-1, 2) U (2, inf).
```

### Q2

**1. Correct answer: B.**

- **A (Incorrect):** Confuses the definition of a limit with continuity; limits depend strictly on behavior near $x = 2$, not at $x = 2$.
- **B (Correct):** Evaluates left-hand limit $\lim_{x \to 2^-} (x^2 - 2x + 3) = 3$ and right-hand limit $\lim_{x \to 2^+} (7 - 2x) = 3$, confirming $\lim_{x \to 2} g(x) = 3$, while noting that $\lim_{x \to 2} g(x) \neq g(2) = 5$ produces a removable discontinuity.
- **C (Incorrect):** Fails to enforce the continuity condition that the limit must equal the evaluated function value at the point.
- **D (Incorrect):** Erroneously evaluates the isolated point $g(2) = 5$ rather than investigating local approaching behavior as $x \to 2$.
- **E (Incorrect):** Contains an arithmetic error in evaluating one-sided limits, falsely asserting that directional limits disagree.

### Q3

**1.**
```text
Stage 1 (Classification & Domain):
Base f(x) = sqrt(x). Apply right shift 3, vertical stretch 2, x-axis reflection, up shift 5.

Stage 2 (Algebraic Preparation):
Formula: h(x) = -2*sqrt(x - 3) + 5 = 5 - 2*sqrt(x - 3).

Stage 3 (Core Operation):
Domain: x - 3 >= 0 ==> x >= 3 ==> [3, inf).
Range: sqrt(x - 3) >= 0 ==> -2*sqrt(x - 3) <= 0 ==> 5 - 2*sqrt(...) <= 5 ==> (-inf, 5].

Stage 4 (Interpretation & Boundary Check):
At x = 3: h(3) = 5 (vertex maximum). As x -> inf, h(x) -> -inf.
Verified formula: h(x) = -2*sqrt(x - 3) + 5; Domain: [3, inf); Range: (-inf, 5].
```

**2.**
```text
Stage 1 (Classification & Domain):
Given f(x) = sqrt(x) and g(x) = 9 - x^2. Enforce x in dom(g) and g(x) in dom(f).

Stage 2 (Algebraic Preparation):
Composite formula: (f o g)(x) = sqrt(9 - x^2). Condition: 9 - x^2 >= 0.

Stage 3 (Core Operation):
Solve 9 - x^2 >= 0 ==> x^2 <= 9 ==> -3 <= x <= 3 ==> [-3, 3].

Stage 4 (Interpretation & Boundary Check):
Endpoints: (f o g)(+-3) = sqrt(0) = 0. Peak at x = 0: sqrt(9) = 3.
Verified formula: (f o g)(x) = sqrt(9 - x^2); Domain: [-3, 3].
```

**3.**
```text
Stage 1 (Classification & Domain):
Given f(x) = sqrt(x) with dom [0, inf) and g(x) = 9 - x^2. Inner function is f(x).

Stage 2 (Algebraic Preparation):
Formula: (g o f)(x) = 9 - (sqrt(x))^2. Enforce x in dom(f) ==> x >= 0. For x >= 0, formula is 9 - x.

Stage 3 (Core Operation):
Domain is restricted by inner root: [0, inf). Range: 9 - x decreases from 9 to -inf: (-inf, 9].

Stage 4 (Interpretation & Boundary Check):
Omitting the inner restriction x >= 0 would falsely yield domain (-inf, inf).
Verified formula: (g o f)(x) = 9 - x for x >= 0; Domain: [0, inf); Range: (-inf, 9].
```

### Q4

**1.**
```text
Stage 1 (Classification & Domain):
Limit: lim_{x -> 3} (2x^2 - 5x - 3)/(x^2 - 9). Direct evaluation gives 0/0 (indeterminate).

Stage 2 (Algebraic Preparation):
Factor: 2x^2 - 5x - 3 = (2x + 1)(x - 3); x^2 - 9 = (x + 3)(x - 3).

Stage 3 (Core Operation):
Cancel (x - 3) for x != 3: (2x + 1)/(x + 3).
Evaluate: lim_{x -> 3} (2x + 1)/(x + 3) = (2(3) + 1)/(3 + 3) = 7/6.

Stage 4 (Interpretation & Boundary Check):
Numerical check: At x = 3.01, ratio approx 1.168; 7/6 = 1.1667. Verified limit: 7/6.
```

**2.**
```text
Stage 1 (Classification & Domain):
Limit: lim_{t -> 0} (sqrt(t + 16) - 4)/t. Direct evaluation gives (4 - 4)/0 = 0/0.

Stage 2 (Algebraic Preparation):
Multiply by conjugate: [(sqrt(t+16)-4)(sqrt(t+16)+4)] / [t(sqrt(t+16)+4)] = t / [t(sqrt(t+16)+4)].

Stage 3 (Core Operation):
Cancel t for t != 0: 1 / (sqrt(t + 16) + 4).
Evaluate: 1 / (sqrt(0 + 16) + 4) = 1 / (4 + 4) = 1/8.

Stage 4 (Interpretation & Boundary Check):
Numerical check: At t = 0.01, value approx 0.12496; 1/8 = 0.125. Verified limit: 1/8.
```

**3.**
```text
Stage 1 (Classification & Domain):
Limit: lim_{x -> -2} [(1/(x + 4) - 1/2)/(x + 2)]. Direct evaluation gives 0/0.

Stage 2 (Algebraic Preparation):
Combine numerator: [2 - (x + 4)] / [2(x + 4)] = -(x + 2) / [2(x + 4)].
Divide by (x + 2): -(x + 2) / [2(x + 4)(x + 2)].

Stage 3 (Core Operation):
Cancel (x + 2) for x != -2: -1 / [2(x + 4)].
Evaluate: -1 / [2(-2 + 4)] = -1 / 4.

Stage 4 (Interpretation & Boundary Check):
Numerical check: At x = -1.99, value approx -0.2488; -1/4 = -0.25. Verified limit: -1/4.
```

**4.**
```text
Stage 1 (Classification & Domain):
Trigonometric limit: lim_{theta -> 0} sin(5*theta)/(3*theta). Form is 0/0.

Stage 2 (Algebraic Preparation):
Use identity lim_{u -> 0} sin(u)/u = 1. Rewrite: (5/3) * [sin(5*theta)/(5*theta)].

Stage 3 (Core Operation):
With u = 5*theta, limit becomes (5/3) * 1 = 5/3.

Stage 4 (Interpretation & Boundary Check):
Numerical check: At theta = 0.001 rad, sin(0.005)/0.003 approx 1.66667. Verified limit: 5/3.
```

### Q5

**1.**
```text
Stage 1 (Classification & Domain):
Piecewise model T(t) on [0, 6]. Left: 2 + 1.5t (t < 2); Right: 8 - 6/(t + 1) (t > 2).

Stage 2 (Algebraic Preparation):
Sub-functions are continuous on respective open intervals; evaluate directly.

Stage 3 (Core Operation):
Left-hand limit: lim_{t -> 2^-} (2 + 1.5t) = 2 + 1.5(2) = 5 (500 deg C).
Right-hand limit: lim_{t -> 2^+} (8 - 6/(t + 1)) = 8 - 6/3 = 6 (600 deg C).

Stage 4 (Interpretation & Boundary Check):
Left limit: 500 deg C (pre-heating). Right limit: 600 deg C (firing stage).
Verified limits: lim_{t -> 2^-} T(t) = 5 and lim_{t -> 2^+} T(t) = 6.
```

**2.**
```text
Stage 1 (Classification & Domain):
Directional limits: lim_{t -> 2^-} T(t) = 5 != lim_{t -> 2^+} T(t) = 6.

Stage 2 (Algebraic Preparation):
Two-sided limit exists if and only if one-sided limits are equal.

Stage 3 (Core Operation):
Since 5 != 6, lim_{t -> 2} T(t) Does Not Exist (DNE).
Classification: Essential jump discontinuity of magnitude |6 - 5| = 1 at t = 2.

Stage 4 (Interpretation & Boundary Check):
Control point T(2) = 5 cannot bridge the abrupt firing jump transition.
Verified conclusion: Limit DNE; jump discontinuity of magnitude 1.
```

**3.**
```text
Stage 1 (Classification & Domain):
Monotonicity on [0, 6]: Segment 1 [0, 2) has dT/dt > 0; Segment 2 (2, 6] has dT/dt > 0.

Stage 2 (Algebraic Preparation):
Segment 1 spans [2, 5); T(2) = 5 closes [2, 5]. Segment 2 spans (6, 50/7].

Stage 3 (Core Operation):
Range: [2, 5] U (6, 50/7]. Min: 2 at t = 0; Max: 50/7 at t = 6.

Stage 4 (Interpretation & Boundary Check):
Interval (5, 6] is omitted due to jump discontinuity. Verified range: [2, 5] U (6, 50/7].
```

### Q6

**1.**
```text
Stage 1 (Classification & Domain):
Right velocity v(t) = (sqrt(t - 1) - 3)/(t - 10) + 15 for t > 10. Form is 0/0 at 10.

Stage 2 (Algebraic Preparation):
Multiply by conjugate: [(sqrt(t-1)-3)(sqrt(t-1)+3)] / [(t-10)(sqrt(t-1)+3)] = (t-10)/[(t-10)(sqrt(t-1)+3)].

Stage 3 (Core Operation):
Cancel (t - 10): 1 / (sqrt(t - 1) + 3). Limit as t -> 10^+ is 1/6 + 15 = 91/6 m/s.

Stage 4 (Interpretation & Boundary Check):
Numerical check: At t = 10.01, v(t) approx 15.1666 m/s. Verified limit: 91/6 m/s.
```

**2.**
```text
Stage 1 (Classification & Domain):
Left velocity v(t) = (a*t^2 + 12t)/(t + 4) for t < 10. Continuous at 10 (denominator 14 != 0).

Stage 2 (Algebraic Preparation):
Direct substitution: lim_{t -> 10^-} v(t) = (100a + 120)/14 = (50a + 60)/7.
Equate to right limit: (50a + 60)/7 = 91/6.

Stage 3 (Core Operation):
Cross-multiply: 6(50a + 60) = 7(91) ==> 300a + 360 = 637 ==> a = 277/300.

Stage 4 (Interpretation & Boundary Check):
Check: [50(277/300) + 60]/7 = (637/6)/7 = 91/6 m/s. Verified parameter: a = 277/300.
```

**3.**
```text
Stage 1 (Classification & Domain):
Continuity at t = 10 requires v(10) = lim_{t -> 10} v(t).

Stage 2 (Algebraic Preparation):
From definition, v(10) = b. Two-sided limit is lim_{t -> 10} v(t) = 91/6 m/s.

Stage 3 (Core Operation):
Equate values: b = 91/6 m/s.

Stage 4 (Interpretation & Boundary Check):
Setting b = 91/6 eliminates any velocity discontinuity at t = 10.
Verified parameter: b = 91/6.
```

**4.**
```text
Stage 1 (Classification & Domain):
Average acceleration a_bar = (v(26) - v(17)) / (26 - 17). Both points lie in (10, 30].

Stage 2 (Algebraic Preparation):
v(17) = (sqrt(16) - 3)/7 + 15 = 1/7 + 15 = 106/7 m/s.
v(26) = (sqrt(25) - 3)/16 + 15 = 2/16 + 15 = 1/8 + 15 = 121/8 m/s.

Stage 3 (Core Operation):
Delta v = 121/8 - 106/7 = (847 - 848)/56 = -1/56 m/s.
Divide by Delta t = 9 s: a_bar = (-1/56) / 9 = -1/504 m/s^2.

Stage 4 (Interpretation & Boundary Check):
Numerical check: (15.125 - 15.142857)/9 = -0.0019841 m/s^2; -1/504 = -0.0019841.
Negative sign indicates slight deceleration. Verified acceleration: -1/504 m/s^2.
```
