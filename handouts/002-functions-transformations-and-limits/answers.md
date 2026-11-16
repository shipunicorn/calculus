---
title: "Handout 002: Functions & Limits — Answer Key"
---

# 002: Functions, Transformations, and Limits — Answer Key

## Exercises

### Q1

**1.**
```text
Stage 1 (Classification & Domain):
Function family: Rational function f(x) = (3x - 1)/(x^2 - 4x - 12).
Constraint: Denominator cannot be zero: x^2 - 4x - 12 != 0.

Stage 2 (Algebraic Preparation):
Factor quadratic denominator:
x^2 - 4x - 12 = (x - 6)(x + 2).
Set equal to zero to identify excluded singularities:
(x - 6)(x + 2) = 0  ==>  x = 6 or x = -2.

Stage 3 (Core Operation):
Exclude x = -2 and x = 6 from all real numbers:
(-inf, -2) U (-2, 6) U (6, inf).

Stage 4 (Interpretation & Boundary Check):
Numerator at singularities:
At x = -2: 3(-2) - 1 = -7 != 0 (vertical asymptote).
At x = 6: 3(6) - 1 = 17 != 0 (vertical asymptote).
Neither singularity is removable.
Verified domain: (-inf, -2) U (-2, 6) U (6, inf).
```

**2.**
```text
Stage 1 (Classification & Domain):
Function family: Difference of two square root radicals g(t) = sqrt(5 - t) - sqrt(t + 3).
Constraint: Both even-root radicands must be non-negative simultaneously:
5 - t >= 0  and  t + 3 >= 0.

Stage 2 (Algebraic Preparation):
Solve individual inequalities:
5 - t >= 0  ==>  t <= 5.
t + 3 >= 0  ==>  t >= -3.

Stage 3 (Core Operation):
Find the intersection of both solution sets:
-3 <= t <= 5.
In interval notation: [-3, 5].

Stage 4 (Interpretation & Boundary Check):
Check boundary endpoints:
At t = -3: g(-3) = sqrt(5 - (-3)) - sqrt(-3 + 3) = sqrt(8) - 0 = 2*sqrt(2) (valid).
At t = 5: g(5) = sqrt(5 - 5) - sqrt(5 + 3) = 0 - sqrt(8) = -2*sqrt(2) (valid).
Both endpoints are included (closed brackets).
Verified domain: [-3, 5].
```

**3.**
```text
Stage 1 (Classification & Domain):
Function family: Fourth-root radical in the denominator h(x) = (2x + 7)/((x^2 - 4x)^(1/4)).
Constraint: Fourth-root requires non-negative radicand, and denominator position prohibits zero:
x^2 - 4x > 0 (strictly positive).

Stage 2 (Algebraic Preparation):
Factor quadratic radicand:
x(x - 4) > 0.
Critical boundary roots are x = 0 and x = 4.
Test sign across test intervals (-inf, 0), (0, 4), and (4, inf):
For x = -1: (-1)(-5) = +5 > 0 (satisfied).
For x = 2: (2)(-2) = -4 < 0 (not satisfied).
For x = 5: (5)(1) = +5 > 0 (satisfied).

Stage 3 (Core Operation):
Collect positive intervals:
x < 0 or x > 4.
In interval notation: (-inf, 0) U (4, inf).

Stage 4 (Interpretation & Boundary Check):
Check boundary roots x = 0 and x = 4:
At x = 0 and x = 4, the radicand is zero, causing division by zero.
Therefore, both boundaries must be open parentheses.
Verified domain: (-inf, 0) U (4, inf).
```

**4.**
```text
Stage 1 (Classification & Domain):
Function family: Nested compound rational function k(u) = (u - 2)/(2 - 6/(u + 1)).
Constraints: Every denominator at every structural tier must be non-zero simultaneously:
1. Inner denominator: u + 1 != 0.
2. Outer main denominator: 2 - 6/(u + 1) != 0.

Stage 2 (Algebraic Preparation):
Solve inner denominator constraint:
u + 1 != 0  ==>  u != -1.
Simplify and solve main denominator constraint:
2 - 6/(u + 1) = 0  ==>  2(u + 1) - 6 = 0  ==>  2u - 4 = 0  ==>  u = 2.

Stage 3 (Core Operation):
Exclude both singularities u = -1 and u = 2 from real numbers:
(-inf, -1) U (-1, 2) U (2, inf).

Stage 4 (Interpretation & Boundary Check):
Note that although the numerator has a factor (u - 2) which algebraically simplifies
the ratio to (u - 2)/[(2(u - 2))/(u + 1)] = (u + 1)/2 for u != 2,
the input u = 2 remains undefined in the original function definition.
Verified domain: (-inf, -1) U (-1, 2) U (2, inf).
```

### Q2

**1. Correct answer: B.**

- **A (Incorrect):** Confuses the definition of a limit with the definition of continuity; a limit depends strictly on function values near $x = 2$, not at $x = 2$.
- **B (Correct):** Evaluates left-hand limit $\lim_{x \to 2^-} (x^2 - 2x + 3) = 3$ and right-hand limit $\lim_{x \to 2^+} (7 - 2x) = 3$, confirming that $\lim_{x \to 2} g(x) = 3$, while noting that $\lim_{x \to 2} g(x) \neq g(2) = 5$ creates a removable discontinuity.
- **C (Incorrect):** Fails to enforce the continuity requirement that the two-sided limit must equal the evaluated function value at the point.
- **D (Incorrect):** Erroneously evaluates the isolated function point $g(2) = 5$ rather than investigating local approaching behavior as $x \to 2$.
- **E (Incorrect):** Contains an arithmetic sign error when evaluating the one-sided polynomial pieces, incorrectly asserting that the directional limits disagree.

### Q3

**1.**
```text
Stage 1 (Classification & Domain):
Base function: f(x) = sqrt(x), with prototype domain [0, inf) and range [0, inf).
Target transformations:
1. Shift right by 3 units: replace x with (x - 3).
2. Reflect across x-axis: multiply output by -1.
3. Stretch vertically by factor 2: scale by 2 (yielding multiplier -2).
4. Shift upward by 5 units: add 5 to output.

Stage 2 (Algebraic Preparation):
Construct explicit formula:
h(x) = -2 * sqrt(x - 3) + 5 = 5 - 2*sqrt(x - 3).

Stage 3 (Core Operation):
Determine domain and range:
Domain: Radicand condition x - 3 >= 0 ==> x >= 3 ==> [3, inf).
Range: Since sqrt(x - 3) >= 0 for all x >= 3, multiplying by -2 yields
-2*sqrt(x - 3) <= 0. Adding 5 gives 5 - 2*sqrt(x - 3) <= 5.
Range is (-inf, 5].

Stage 4 (Interpretation & Boundary Check):
Boundary evaluation:
At x = 3: h(3) = 5 - 2*sqrt(0) = 5 (attains absolute maximum at (3, 5)).
As x -> inf: h(x) -> -inf.
Verified formula: h(x) = -2*sqrt(x - 3) + 5; Domain: [3, inf); Range: (-inf, 5].
```

**2.**
```text
Stage 1 (Classification & Domain):
Given f(x) = sqrt(x) and g(x) = 9 - x^2.
Outer function f requires input >= 0.
Inner function g(x) has domain (-inf, inf).

Stage 2 (Algebraic Preparation):
Form composite expression:
(f o g)(x) = f(g(x)) = sqrt(9 - x^2).
Enforce composite domain condition:
x in dom(g) and g(x) in dom(f)  ==>  9 - x^2 >= 0.

Stage 3 (Core Operation):
Solve 9 - x^2 >= 0:
x^2 <= 9  ==>  -3 <= x <= 3.
In interval notation: [-3, 3].

Stage 4 (Interpretation & Boundary Check):
Check boundary endpoints:
At x = -3: f(g(-3)) = sqrt(9 - 9) = 0.
At x = 3: f(g(3)) = sqrt(9 - 9) = 0.
At x = 0: f(g(0)) = sqrt(9 - 0) = 3 (maximum).
Verified formula: (f o g)(x) = sqrt(9 - x^2); Domain: [-3, 3].
```

**3.**
```text
Stage 1 (Classification & Domain):
Given f(x) = sqrt(x) with dom(f) = [0, inf) and g(x) = 9 - x^2 with dom(g) = (-inf, inf).
Inner function is f(x); outer function is g(x).

Stage 2 (Algebraic Preparation):
Form composite expression:
(g o f)(x) = g(f(x)) = 9 - (sqrt(x))^2.
Enforce composite domain condition:
x must be in dom(f)  ==>  x >= 0.
For x >= 0, (sqrt(x))^2 = x, so (g o f)(x) = 9 - x.

Stage 3 (Core Operation):
Determine domain and range:
Domain is restricted by inner square root: [0, inf).
Range analysis:
For x in [0, inf), output starts at 9 - 0 = 9 and decreases without bound as x -> inf.
Range is (-inf, 9].

Stage 4 (Interpretation & Boundary Check):
Common error check: Writing the formula as 9 - x without restricting x >= 0
would incorrectly claim the domain is (-inf, inf). The inner function f(x) = sqrt(x)
strictly restricts admissible inputs to [0, inf).
Verified formula: (g o f)(x) = 9 - x for x >= 0; Domain: [0, inf); Range: (-inf, 9].
```

### Q4

**1.**
```text
Stage 1 (Classification & Domain):
Rational limit: lim_{x -> 3} (2x^2 - 5x - 3)/(x^2 - 9).
Direct substitution test at x = 3:
Numerator: 2(3)^2 - 5(3) - 3 = 18 - 15 - 3 = 0.
Denominator: 3^2 - 9 = 9 - 9 = 0.
Form is 0/0 (indeterminate).

Stage 2 (Algebraic Preparation):
Factor numerator and denominator:
Numerator: 2x^2 - 5x - 3 = (2x + 1)(x - 3).
Denominator: x^2 - 9 = (x + 3)(x - 3).
Rewrite quotient:
(2x + 1)(x - 3) / [(x + 3)(x - 3)].

Stage 3 (Core Operation):
Cancel common non-zero factor (x - 3) valid for all x != 3:
= (2x + 1) / (x + 3).
Apply Quotient Law with direct substitution:
lim_{x -> 3} (2x + 1)/(x + 3) = (2(3) + 1)/(3 + 3) = 7/6.

Stage 4 (Interpretation & Boundary Check):
Numerical check with x = 3.01:
(2(3.01)^2 - 5(3.01) - 3) / (3.01^2 - 9) = (18.1202 - 15.05 - 3) / (9.0601 - 9)
= 0.0702 / 0.0601 approx 1.16805.
Fraction 7/6 = 1.16667... matches closely.
Verified limit: 7/6.
```

**2.**
```text
Stage 1 (Classification & Domain):
Radical limit: lim_{t -> 0} (sqrt(t + 16) - 4)/t.
Direct substitution test at t = 0:
(sqrt(16) - 4)/0 = (4 - 4)/0 = 0/0 (indeterminate).

Stage 2 (Algebraic Preparation):
Rationalize numerator by multiplying numerator and denominator
by the conjugate (sqrt(t + 16) + 4):
[ (sqrt(t + 16) - 4) * (sqrt(t + 16) + 4) ] / [ t * (sqrt(t + 16) + 4) ]
Expand difference of squares:
[ (t + 16) - 16 ] / [ t * (sqrt(t + 16) + 4) ] = t / [ t * (sqrt(t + 16) + 4) ].

Stage 3 (Core Operation):
Cancel non-zero factor t for t != 0:
= 1 / (sqrt(t + 16) + 4).
Apply Root and Quotient Laws:
lim_{t -> 0} [ 1 / (sqrt(t + 16) + 4) ] = 1 / (sqrt(0 + 16) + 4) = 1 / (4 + 4) = 1/8.

Stage 4 (Interpretation & Boundary Check):
Numerical check with t = 0.01:
(sqrt(16.01) - 4)/0.01 = (4.0012496 - 4)/0.01 = 0.12496.
Value 1/8 = 0.125 matches closely.
Verified limit: 1/8.
```

**3.**
```text
Stage 1 (Classification & Domain):
Compound fraction limit: lim_{x -> -2} [ (1/(x + 4) - 1/2) / (x + 2) ].
Direct substitution test at x = -2:
Numerator: 1/(-2 + 4) - 1/2 = 1/2 - 1/2 = 0.
Denominator: -2 + 2 = 0.
Form is 0/0 (indeterminate).

Stage 2 (Algebraic Preparation):
Combine terms in numerator over common denominator 2(x + 4):
1/(x + 4) - 1/2 = [2 - (x + 4)] / [2(x + 4)] = (-x - 2) / [2(x + 4)] = -(x + 2) / [2(x + 4)].
Divide by main denominator (x + 2):
[ -(x + 2) / [2(x + 4)] ] * [ 1 / (x + 2) ].

Stage 3 (Core Operation):
Cancel common non-zero factor (x + 2) for x != -2:
= -1 / [2(x + 4)].
Apply Quotient Law with direct substitution:
lim_{x -> -2} [ -1 / (2(x + 4)) ] = -1 / [2(-2 + 4)] = -1 / [2(2)] = -1/4.

Stage 4 (Interpretation & Boundary Check):
Numerical check with x = -1.99:
(1/2.01 - 0.5) / 0.01 = (0.4975124 - 0.5) / 0.01 = -0.0024876 / 0.01 = -0.2488.
Value -1/4 = -0.25 matches closely.
Verified limit: -1/4.
```

**4.**
```text
Stage 1 (Classification & Domain):
Trigonometric limit: lim_{theta -> 0} sin(5*theta)/(3*theta).
Direct substitution test at theta = 0 gives sin(0)/0 = 0/0 (indeterminate).

Stage 2 (Algebraic Preparation):
Use the fundamental trigonometric limit identity: lim_{u -> 0} sin(u)/u = 1.
Factor constants to isolate sin(5*theta)/(5*theta):
sin(5*theta)/(3*theta) = (5/3) * [ sin(5*theta) / (5*theta) ].

Stage 3 (Core Operation):
Substitute u = 5*theta. As theta -> 0, u -> 0:
lim_{theta -> 0} [ (5/3) * sin(5*theta)/(5*theta) ]
= (5/3) * lim_{u -> 0} [ sin(u)/u ]
= (5/3) * 1 = 5/3.

Stage 4 (Interpretation & Boundary Check):
Numerical check with theta = 0.001 rad:
sin(0.005) / 0.003 = 0.004999979 / 0.003 = 1.66666...
Fraction 5/3 = 1.66667... matches closely.
Verified limit: 5/3.
```

### Q5

**1.**
```text
Stage 1 (Classification & Domain):
Model is piecewise temperature function T(t) over domain [0, 6] hours.
Left approach (t < 2): T(t) = 2 + 1.5t.
Right approach (t > 2): T(t) = 8 - 6/(t + 1).

Stage 2 (Algebraic Preparation):
Both sub-functions are continuous on their respective open sub-intervals.
Direct substitution is valid for directional limits.

Stage 3 (Core Operation):
Evaluate one-sided limits:
Left-hand limit:
lim_{t -> 2^-} T(t) = lim_{t -> 2^-} (2 + 1.5t) = 2 + 1.5(2) = 2 + 3 = 5 (500 deg C).
Right-hand limit:
lim_{t -> 2^+} T(t) = lim_{t -> 2^+} (8 - 6/(t + 1)) = 8 - 6/(2 + 1) = 8 - 2 = 6 (600 deg C).

Stage 4 (Interpretation & Boundary Check):
Left limit represents approach temperature from initial pre-heating stage (500 deg C).
Right limit represents approach temperature from secondary firing stage (600 deg C).
Verified directional limits: lim_{t -> 2^-} T(t) = 5 and lim_{t -> 2^+} T(t) = 6.
```

**2.**
```text
Stage 1 (Classification & Domain):
Compare directional limits from subpart 1:
lim_{t -> 2^-} T(t) = 5 != lim_{t -> 2^+} T(t) = 6.

Stage 2 (Algebraic Preparation):
Apply Existence Theorem for two-sided limits:
A two-sided limit exists if and only if both one-sided limits exist and are equal.

Stage 3 (Core Operation):
Because 5 != 6, the two-sided limit lim_{t -> 2} T(t) Does Not Exist (DNE).
Classification:
Because both directional limits are finite real numbers that disagree, the profile
exhibits an essential jump discontinuity of magnitude |6 - 5| = 1 (100 deg C) at t = 2.

Stage 4 (Interpretation & Boundary Check):
The isolated control point T(2) = 5 coincides with the left limit, but cannot eliminate
the abrupt jump transition between the two firing regimes.
Verified conclusion: Limit DNE; jump discontinuity of magnitude 1.
```

**3.**
```text
Stage 1 (Classification & Domain):
Investigate temperature extrema and range across the full domain [0, 6].
Interval 1: [0, 2), where T(t) = 2 + 1.5t.
Boundary point: t = 2, where T(2) = 5.
Interval 2: (2, 6], where T(t) = 8 - 6/(t + 1).

Stage 2 (Algebraic Preparation):
Analyze monotonicity on each segment:
Segment 1: dT/dt = 1.5 > 0, strictly increasing from T(0) = 2 up to lim_{t -> 2^-} T(t) = 5.
Value range on [0, 2): [2, 5).
Point t = 2: T(2) = 5, completing the closed interval [2, 5].
Segment 2: dT/dt = 6/(t + 1)^2 > 0, strictly increasing from lim_{t -> 2^+} T(t) = 6 up to
T(6) = 8 - 6/(6 + 1) = 8 - 6/7 = 50/7 approx 7.14 (714.3 deg C).
Value range on (2, 6]: (6, 50/7].

Stage 3 (Core Operation):
Synthesize full range:
range(T) = [2, 5] U (6, 50/7].
Extrema determination:
Absolute minimum: 2 (200 deg C, attained at initial time t = 0).
Absolute maximum: 50/7 (approx 714.3 deg C, attained at final time t = 6).

Stage 4 (Interpretation & Boundary Check):
Notice the temperature gap (5, 6]: temperatures between 500 deg C and 600 deg C
are skipped instantly due to the jump discontinuity at t = 2 hours.
Verified extrema: Min = 2 at t = 0; Max = 50/7 at t = 6; Range: [2, 5] U (6, 50/7].
```

### Q6

**1.**
```text
Stage 1 (Classification & Domain):
Right-hand velocity for t in (10, 30]: v(t) = (sqrt(t - 1) - 3)/(t - 10) + 15.
Direct substitution of t = 10 into the fraction gives:
(sqrt(9) - 3)/(10 - 10) = (3 - 3)/0 = 0/0 (indeterminate).

Stage 2 (Algebraic Preparation):
Rationalize the radical quotient by multiplying numerator and denominator
by the conjugate (sqrt(t - 1) + 3):
[ (sqrt(t - 1) - 3) * (sqrt(t - 1) + 3) ] / [ (t - 10) * (sqrt(t - 1) + 3) ]
= [ (t - 1) - 9 ] / [ (t - 10) * (sqrt(t - 1) + 3) ]
= (t - 10) / [ (t - 10) * (sqrt(t - 1) + 3) ].

Stage 3 (Core Operation):
Cancel non-zero factor (t - 10) for t > 10:
= 1 / (sqrt(t - 1) + 3).
Evaluate the limit as t -> 10^+:
lim_{t -> 10^+} [ 1 / (sqrt(t - 1) + 3) + 15 ] = 1 / (sqrt(9) + 3) + 15
                                               = 1 / (3 + 3) + 15
                                               = 1/6 + 15 = 91/6 m/s.

Stage 4 (Interpretation & Boundary Check):
Numerical check with t = 10.01:
(sqrt(9.01) - 3)/0.01 + 15 = (3.001666 - 3)/0.01 + 15 = 0.1666 + 15 = 15.1666 m/s.
Matches 91/6 = 15.1667 m/s.
Verified right-hand limit: 91/6 m/s.
```

**2.**
```text
Stage 1 (Classification & Domain):
Left-hand velocity for t in [0, 10): v(t) = (a*t^2 + 12t)/(t + 4).
Denominator at t = 10 is 10 + 4 = 14 != 0.
The rational expression is continuous at t = 10, so direct substitution applies.

Stage 2 (Algebraic Preparation):
Evaluate left-hand limit by direct substitution:
lim_{t -> 10^-} v(t) = (a(10)^2 + 12(10)) / (10 + 4) = (100a + 120) / 14 = (50a + 60) / 7.
Enforce existence condition for two-sided limit:
lim_{t -> 10^-} v(t) = lim_{t -> 10^+} v(t) = 91/6.

Stage 3 (Core Operation):
Solve linear equation for parameter a:
(50a + 60) / 7 = 91 / 6
6 * (50a + 60) = 7 * 91
300a + 360 = 637
300a = 277  ==>  a = 277/300.

Stage 4 (Interpretation & Boundary Check):
Back-substitute a = 277/300 into left limit:
[50(277/300) + 60] / 7 = [277/6 + 360/6] / 7 = (637/6) / 7 = 91/6 m/s.
Both directional limits match exactly at 91/6 m/s.
Verified parameter value: a = 277/300.
```

**3.**
```text
Stage 1 (Classification & Domain):
Definition of continuity at t = 10 requires three conditions:
1. v(10) is defined: v(10) = b.
2. lim_{t -> 10} v(t) exists: lim_{t -> 10} v(t) = 91/6 m/s (established in subparts 1 and 2).
3. lim_{t -> 10} v(t) = v(10).

Stage 2 (Algebraic Preparation):
Equate the two-sided limit value to the assigned function value:
b = lim_{t -> 10} v(t).

Stage 3 (Core Operation):
Substitute known limit value:
b = 91/6 m/s.

Stage 4 (Interpretation & Boundary Check):
Physical meaning: Setting b = 91/6 ensures that the velocity telemetry does not
exhibit a single-frame pulse discontinuity or sudden velocity surge at t = 10 seconds.
Verified parameter value: b = 91/6.
```

**4.**
```text
Stage 1 (Classification & Domain):
Average acceleration over [17, 26] is defined by:
a_bar = (v(26) - v(17)) / (26 - 17).
Both evaluation points t = 17 and t = 26 lie strictly in the interval (10, 30],
where v(t) = (sqrt(t - 1) - 3)/(t - 10) + 15.

Stage 2 (Algebraic Preparation):
Compute v(17):
v(17) = (sqrt(17 - 1) - 3)/(17 - 10) + 15 = (sqrt(16) - 3)/7 + 15
      = (4 - 3)/7 + 15 = 1/7 + 15 = 106/7 m/s.
Compute v(26):
v(26) = (sqrt(26 - 1) - 3)/(26 - 10) + 15 = (sqrt(25) - 3)/16 + 15
      = (5 - 3)/16 + 15 = 2/16 + 15 = 1/8 + 15 = 121/8 m/s.

Stage 3 (Core Operation):
Compute velocity change Delta v:
Delta v = v(26) - v(17) = 121/8 - 106/7.
Common denominator 56:
121 * 7 = 847,  106 * 8 = 848.
Delta v = (847 - 848) / 56 = -1/56 m/s.
Divide by elapsed time Delta t = 26 - 17 = 9 seconds:
a_bar = (-1/56) / 9 = -1 / 504 m/s^2.

Stage 4 (Interpretation & Boundary Check):
Numerical check:
v(17) = 15.142857 m/s.
v(26) = 15.125000 m/s.
Delta v = 15.125 - 15.142857 = -0.017857 m/s.
a_bar = -0.017857 / 9 = -0.0019841 m/s^2.
Fraction -1/504 = -0.001984126... matches exactly.
Negative sign indicates the shuttle is experiencing subtle deceleration across this window.
Verified average acceleration: -1/504 m/s^2.
```
