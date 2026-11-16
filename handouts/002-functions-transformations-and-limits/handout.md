---
title: "Handout 002: Functions, Transformations, and Limits"
---

# 002: Functions, Transformations, and Limits

Calculus investigates continuous change and instantaneous rates of change. Before determining slopes of tangent lines or areas beneath curves, continuous mathematics requires a rigorous foundation in functions, their admissible inputs and outputs, graph transformations, and the limiting behavior of functions near points of interest.

A calculus problem frequently requires evaluating function behavior at or near singular boundaries—such as removable holes, vertical asymptotes, or piecewise transition interfaces. This handout provides a foundational toolkit covering algebraic domain determination, geometric graph reading, transformation catalogs, one-sided and two-sided limits, fundamental limit laws, and systematic techniques for resolving indeterminate forms.

## Functions, domain, and range

A **function** $f$ is a mathematical rule that assigns to each element $x$ in a specified set $D$ (called the **domain**) exactly one output element $f(x)$ in a target set $E$. The **range** of $f$ is the set of all realized output values:

$$\operatorname{range}(f) = \{f(x) \mid x \in D\}$$

In real single-variable calculus, functions are assumed to have real inputs and real outputs ($D, E \subseteq \mathbb{R}$). When a function is defined by an algebraic expression without an explicit domain, the **natural domain** is the largest subset of real numbers for which the formula produces a well-defined real number.

### Natural domain restrictions

Three primary algebraic constraints govern the natural domain of elementary functions:

| Constraint type | General expression | Domain condition | Mathematical justification |
| :--- | :--- | :--- | :--- |
| **Non-zero denominator** | $\frac{P(x)}{Q(x)}$ | $Q(x) \neq 0$ | Division by zero is undefined in real arithmetic. |
| **Even-index radical** | $\sqrt[2n]{g(x)}$ | $g(x) \ge 0$ | Even roots of negative numbers are not real numbers. |
| **Radical in denominator** | $\frac{P(x)}{\sqrt[2n]{g(x)}}$ | $g(x) > 0$ | Radicand must be non-negative, and denominator cannot be zero. |
| **Odd-index radical** | $\sqrt[2n+1]{g(x)}$ | $\operatorname{dom}(g)$ | Odd roots are defined for all real numbers (positive, negative, and zero). |
| **Nested fractions** | $\frac{A(x)}{B(x) + \frac{C(x)}{D(x)}}$ | $D(x) \neq 0$ and $B(x) + \frac{C(x)}{D(x)} \neq 0$ | Every denominator at every hierarchical level must be non-zero simultaneously. |

### Visual representation of domain and range

When graphed in the Cartesian coordinate plane, a function's domain and range correspond directly to geometric shadows (projections) onto the coordinate axes:

- The **domain** is the projection of the continuous curve onto the horizontal $x$-axis.
- The **range** is the projection of the continuous curve onto the vertical $y$-axis, spanning from its absolute minimum value to its absolute maximum value.

![Domain and Range Projections](figures/sec1_domain_range.svg)

### Reading function features from coordinate grids

On a scaled coordinate grid, function values, intercepts, extrema, and interval domains can be read directly:

![Graph of Function on Coordinate Grid](figures/sec1_graph_reading.svg)

From the coordinate grid above:
- **Evaluation at specific inputs:** The function value $f(0) = 1$, $f(1) = 3$, and $f(4) = 1$.
- **Extrema:** A local maximum occurs near $(1.8, 3.8)$ with peak value approximately $3.8$; a local minimum occurs near $(6.8, -2.2)$ with trough value approximately $-2.2$.
- **Intercepts:** The vertical $y$-intercept is $(0, 1)$; horizontal $x$-intercepts occur near $x \approx 4.5$ and at the right boundary $(8, 0)$.
- **Domain and range:** The domain is the closed interval $[0, 8]$; the range spans the vertical interval $[-2.2, 3.8]$.

## Graph transformations and combinations

Constructing new functions from basic prototype curves is a core skill in calculus modeling. Given a known base graph $y = f(x)$ and a positive real constant $c > 0$, transformations alter the position, orientation, or scale of the graph without changing its fundamental geometry.

### Transformation catalog

| Transformation formula | Geometric effect | Coordinate rule | Domain / Range impact |
| :--- | :--- | :--- | :--- |
| $y = f(x) + c$ | Shift upward by $c$ units | $(x, y) \to (x, y + c)$ | Domain unchanged; range shifts up by $c$. |
| $y = f(x) - c$ | Shift downward by $c$ units | $(x, y) \to (x, y - c)$ | Domain unchanged; range shifts down by $c$. |
| $y = f(x - c)$ | Shift right by $c$ units | $(x, y) \to (x + c, y)$ | Domain shifts right by $c$; range unchanged. |
| $y = f(x + c)$ | Shift left by $c$ units | $(x, y) \to (x - c, y)$ | Domain shifts left by $c$; range unchanged. |
| $y = c f(x)$ ($c > 1$) | Stretch vertically by factor $c$ | $(x, y) \to (x, c y)$ | Domain unchanged; vertical distances scaled by $c$. |
| $y = \frac{1}{c} f(x)$ ($c > 1$) | Compress vertically by factor $c$ | $(x, y) \to (x, \frac{1}{c} y)$ | Domain unchanged; vertical distances compressed. |
| $y = -f(x)$ | Reflect across the horizontal $x$-axis | $(x, y) \to (x, -y)$ | Domain unchanged; range values inverted across $0$. |
| $y = f(-x)$ | Reflect across the vertical $y$-axis | $(x, y) \to (-x, y)$ | Domain inverted across $0$; range unchanged. |

![Graph Transformations](figures/sec2_transformations.svg)

### Function composition and domain criteria

Given two functions $f$ and $g$, the **composite function** $(f \circ g)(x)$ is defined by:

$$(f \circ g)(x) = f(g(x))$$

The domain of $f \circ g$ requires two simultaneous conditions:
- **Condition 1:** The input $x$ must lie in the domain of the inner function $g$: $x \in \operatorname{dom}(g)$.
- **Condition 2:** The intermediate output $g(x)$ must lie in the domain of the outer function $f$: $g(x) \in \operatorname{dom}(f)$.

Failure to enforce both conditions produces false domain conclusions, particularly when simplifying algebraic formulas such as $(\sqrt{x})^2 = x$, where the domain remains $x \ge 0$ rather than all real numbers.

## The limit of a function

The fundamental concept separating calculus from precalculus algebra is the **limit**. Limits allow the analysis of local function trends near a point, even when direct algebraic evaluation at that exact point is impossible or indeterminate.

### Intuitive definition and three fundamental cases

We write:

$$\lim_{x \to a} f(x) = L$$

and say "the limit of $f(x)$, as $x$ approaches $a$, equals $L$," if we can make the output values $f(x)$ arbitrarily close to the real number $L$ by taking $x$ sufficiently close to $a$ on both sides of $a$, without ever requiring $x = a$.

The critical insight is that the limit depends strictly on function values **near** $a$, never **at** $a$. Consider the three fundamental cases:

![Three Limit Cases](figures/sec3_limit_cases.svg)

- **Case A (Continuous at $a$):** $f(a)$ is defined and $f(a) = L$. The curve passes smoothly through $(a, L)$ without a break.
- **Case B (Displaced isolated point):** $f(a)$ is defined, but $f(a) \neq L$. The graph contains a removable hole at $(a, L)$ and an isolated point at $(a, f(a))$. The limit remains $\lim_{x \to a} f(x) = L$.
- **Case C (Undefined at $a$):** $f(a)$ is completely undefined. The graph contains a hole at $(a, L)$. The limit remains $\lim_{x \to a} f(x) = L$.

### One-sided limits and existence

Directional limits analyze function approach from a single side:

- **Left-hand limit:** $\lim_{x \to a^-} f(x) = L_1$ means $x$ approaches $a$ through values strictly less than $a$ ($x < a$).
- **Right-hand limit:** $\lim_{x \to a^+} f(x) = L_2$ means $x$ approaches $a$ through values strictly greater than $a$ ($x > a$).

### Existence theorem for two-sided limits

$$\lim_{x \to a} f(x) = L \iff \lim_{x \to a^-} f(x) = L \quad\text{and}\quad \lim_{x \to a^+} f(x) = L$$

If the left-hand and right-hand limits differ ($L_1 \neq L_2$), the two-sided limit **does not exist (DNE)**, indicating a **jump discontinuity**.

![Piecewise Function and One-Sided Limits](figures/sec3_piecewise_limits.svg)

In the figure above:
- At $x = 2$: $\lim_{x \to 2^-} g(x) = 3$, whereas $\lim_{x \to 2^+} g(x) = 1$. Because $3 \neq 1$, $\lim_{x \to 2} g(x)$ does not exist (jump discontinuity).
- At $x = 5$: $\lim_{x \to 5^-} g(x) = 2$ and $\lim_{x \to 5^+} g(x) = 2$. Therefore, the two-sided limit exists: $\lim_{x \to 5} g(x) = 2$, even though the isolated function value is $g(5) \approx 1.25$ (removable discontinuity).

## Calculating limits using limit laws

When limits of individual components exist, they combine predictably through algebraic properties.

### Fundamental limit laws

Suppose $c$ is a constant and both limits $\lim_{x \to a} f(x)$ and $\lim_{x \to a} g(x)$ exist.

| Limit law | Statement | Application condition |
| :--- | :--- | :--- |
| **Sum Law** | $\lim_{x \to a} [f(x) + g(x)] = \lim_{x \to a} f(x) + \lim_{x \to a} g(x)$ | Both individual limits exist. |
| **Difference Law** | $\lim_{x \to a} [f(x) - g(x)] = \lim_{x \to a} f(x) - \lim_{x \to a} g(x)$ | Both individual limits exist. |
| **Constant Multiple** | $\lim_{x \to a} [c f(x)] = c \lim_{x \to a} f(x)$ | Individual limit exists; $c \in \mathbb{R}$. |
| **Product Law** | $\lim_{x \to a} [f(x) g(x)] = \left(\lim_{x \to a} f(x)\right) \cdot \left(\lim_{x \to a} g(x)\right)$ | Both individual limits exist. |
| **Quotient Law** | $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}$ | Both limits exist, and $\lim_{x \to a} g(x) \neq 0$. |
| **Power Law** | $\lim_{x \to a} [f(x)]^n = \left[\lim_{x \to a} f(x)\right]^n$ | $n$ is a positive integer. |
| **Root Law** | $\lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{\lim_{x \to a} f(x)}$ | $n$ is a positive integer; if $n$ is even, assume $\lim f(x) > 0$. |

### Direct substitution and indeterminate forms

If $f$ is a polynomial or a rational function and $a$ lies within the domain of $f$, then:

$$\lim_{x \to a} f(x) = f(a)$$

However, when direct evaluation yields the **indeterminate form** $\frac{0}{0}$, the limit cannot be determined by direct substitution. Algebraic preparation is mandatory to expose and cancel the zero-producing factor $(x - a)$:

- **Factoring and cancellation:** For rational functions, factor polynomials in numerator and denominator, then cancel the common factor $(x - a)$ valid for all $x \neq a$.
- **Conjugate rationalization:** For expressions with square root differences $(\sqrt{A} - B)$, multiply numerator and denominator by the conjugate $(\sqrt{A} + B)$ using $(u - v)(u + v) = u^2 - v^2$.
- **Clearing compound fractions:** Multiply numerator and denominator by the common denominator of all inner fractions to collapse multiple division tiers.
- **Trigonometric limit identity:** For trigonometric expressions, use the fundamental limit $\lim_{\theta \to 0} \frac{\sin\theta}{\theta} = 1$ ($\theta$ in radians).

## Strategy routines

Apply this four-stage routine to resolve continuous analysis problems systematically:

- **S1 Classify & Domain:** Identify the function category (polynomial, rational, radical, composite, piecewise). Check natural domain restrictions ($Q(x) \neq 0$, radicand $\ge 0$). In limit problems, test direct substitution first.
- **S2 Algebraic Preparation:** If direct substitution produces $\frac{0}{0}$, classify the structure. Choose the algebraic tool: factor quadratics, multiply by radical conjugates, clear compound fraction denominators, or apply trigonometric identities.
- **S3 Core Operation:** Apply the primary calculus operation (cancel common factors, apply limit laws component by component, or evaluate one-sided limits).
- **S4 Interpretation & Boundary Check:** Verify that canceled factors satisfy domain caveats ($x \neq a$). Contrast the limit value $L$ against the actual function value $f(a)$ to classify continuity or discontinuity type (removable vs jump vs infinite).

## Mistakes, edge cases & strategies

The table below summarizes common diagnostic pitfalls encountered when analyzing functions, transformations, and limits.

| Trap | Correct reasoning | Strategy |
| :--- | :--- | :--- |
| **Canceling terms across sums** | In $\frac{x^2 - 4}{x - 2}$, terms cannot be canceled individually across addition or subtraction. | Factor polynomials completely into products before attempting any algebraic cancellation: $\frac{(x-2)(x+2)}{x-2} = x + 2$. |
| **Horizontal shift direction confusion** | The transformation $f(x - c)$ shifts the graph **right**, whereas $f(x + c)$ shifts **left**. | Find the new input that yields $0$: solving $x - c = 0$ gives $x = c > 0$, proving the curve shifts in the positive (rightward) direction. |
| **Misapplying the Quotient Limit Law** | The Quotient Law $\lim \frac{f}{g} = \frac{\lim f}{\lim g}$ requires $\lim g(x) \neq 0$. If $\lim g(x) = 0$, the law is invalid. | Check the denominator limit first. If the denominator approaches $0$, do not divide; inspect for $\frac{0}{0}$ algebraic preparation or vertical asymptotes. |
| **Confusing limit value with function value** | $\lim_{x \to a} f(x)$ measures behavior **near** $a$, whereas $f(a)$ is the evaluated output **at** $a$. | Draw an open circle at the limiting coordinate $(a, L)$. The limit exists regardless of whether a point exists at $(a, f(a))$ or is displaced. |
| **Overlooking inner domain in composition** | The domain of $(f \circ g)(x)$ is not simply the domain of the simplified algebraic formula. | Enforce two independent criteria: $x$ must be in $\operatorname{dom}(g)$, and $g(x)$ must be in $\operatorname{dom}(f)$. Never rely solely on the simplified formula. |
| **Confusing even and odd radical domains** | Even roots ($\sqrt{x}, \sqrt[4]{x}$) require non-negative radicands ($x \ge 0$). Odd roots ($\sqrt[3]{x}$) accept all real numbers. | Inspect the index of the radical. Odd indices impose no sign constraints on their radicands. |
| **Assuming one-sided limits are always equal** | Piecewise definitions often exhibit jump discontinuities where left-hand and right-hand limits differ. | Compute left-hand ($x \to a^-$) and right-hand ($x \to a^+$) limits independently before concluding whether a two-sided limit exists. |

## Worked examples

### Example 1: Domain determination of composite radical and rational function

Determine the natural domain of the function $f(x) = \frac{\sqrt{9 - x^2}}{x - 2}$ and express the result in interval notation.

```text
Stage 1 (Classification & Domain):
Identify function family: combination of an even radical (numerator) and a rational denominator.
Identify algebraic domain constraints:
1. Even radical in numerator requires non-negative radicand: 9 - x^2 >= 0.
2. Rational denominator cannot be zero: x - 2 != 0.

Stage 2 (Algebraic Preparation):
Solve radicand inequality:
9 - x^2 >= 0  ==>  x^2 <= 9  ==>  -3 <= x <= 3  ==>  [-3, 3].
Solve denominator constraint:
x - 2 != 0  ==>  x != 2.

Stage 3 (Core Operation):
Intersect both domain requirements:
x in [-3, 3] and x != 2.
Express as union of disjoint intervals:
[-3, 2) U (2, 3].

Stage 4 (Interpretation & Boundary Check):
Check boundary endpoints:
At x = -3: f(-3) = sqrt(0)/(-5) = 0 (valid, closed bracket).
At x = 3: f(3) = sqrt(0)/(1) = 0 (valid, closed bracket).
At x = 2: denominator is zero (vertical asymptote, open parentheses).
Final verified domain: [-3, 2) U (2, 3].
```

### Example 2: Sequential graph transformations and domain/range identification

Given the prototype square root function $y = \sqrt{x}$ with domain $[0, \infty)$ and range $[0, \infty)$, determine the explicit formula, domain, and range for the function $g(x)$ formed by shifting the prototype left by $4$ units, stretching vertically by a factor of $2$, reflecting across the $x$-axis, and shifting upward by $3$ units.

```text
Stage 1 (Classification & Domain):
Base function: y = sqrt(x), domain [0, inf), range [0, inf).
Sequential transformations:
1. Horizontal shift left by 4 units: replace x with (x + 4).
2. Vertical stretch by factor 2: multiply by 2.
3. Reflection across x-axis: multiply output by -1.
4. Vertical shift upward by 3 units: add 3 to output.

Stage 2 (Algebraic Preparation):
Assemble formula step by step:
Step 1: y_1 = sqrt(x + 4)
Step 2: y_2 = 2 * sqrt(x + 4)
Step 3: y_3 = -2 * sqrt(x + 4)
Step 4: g(x) = -2 * sqrt(x + 4) + 3 = 3 - 2 * sqrt(x + 4)

Stage 3 (Core Operation):
Determine domain and range of transformed function:
Domain condition: radicand must be non-negative:
x + 4 >= 0  ==>  x >= -4  ==>  [-4, inf).
Range analysis:
For all x >= -4, sqrt(x + 4) >= 0.
Multiplying by -2 reverses inequality: -2 * sqrt(x + 4) <= 0.
Adding 3 shifts maximum: 3 - 2 * sqrt(x + 4) <= 3.
Range is (-inf, 3].

Stage 4 (Interpretation & Boundary Check):
Anchor check:
Evaluate at start of domain x = -4:
g(-4) = 3 - 2 * sqrt(0) = 3 (peak coordinate (-4, 3)).
As x -> inf, -2*sqrt(x + 4) -> -inf, so g(x) -> -inf.
Final formula: g(x) = 3 - 2*sqrt(x + 4); Domain: [-4, inf); Range: (-inf, 3].
```

### Example 3: One-sided limits and discontinuity analysis on a piecewise curve

Consider the piecewise function:

$$f(x) = \begin{cases} \frac{x^2 - 4}{x - 2} & \text{if } x < 2 \\ 1 & \text{if } x = 2 \\ 2x - 1 & \text{if } x > 2 \end{cases}$$

Evaluate $\lim_{x \to 2^-} f(x)$, $\lim_{x \to 2^+} f(x)$, and determine whether $\lim_{x \to 2} f(x)$ exists. Classify any discontinuity at $x = 2$.

```text
Stage 1 (Classification & Domain):
Function is piecewise defined with transition boundary at x = 2.
For x < 2: f(x) = (x^2 - 4)/(x - 2).
At x = 2: f(2) = 1.
For x > 2: f(x) = 2x - 1.

Stage 2 (Algebraic Preparation):
Prepare expression for x < 2 (as x -> 2^-):
Direct substitution yields 0/0.
Factor numerator: x^2 - 4 = (x - 2)(x + 2).
For x < 2, x != 2, so (x - 2)/(x - 2) = 1.
Thus f(x) = x + 2 for x < 2.

Stage 3 (Core Operation):
Compute one-sided limits:
Left-hand limit:
lim_{x -> 2^-} f(x) = lim_{x -> 2^-} (x + 2) = 2 + 2 = 4.
Right-hand limit:
lim_{x -> 2^+} f(x) = lim_{x -> 2^+} (2x - 1) = 2(2) - 1 = 3.

Stage 4 (Interpretation & Boundary Check):
Compare one-sided limits:
lim_{x -> 2^-} f(x) = 4 != lim_{x -> 2^+} f(x) = 3.
Since the directional limits are unequal, the two-sided limit lim_{x -> 2} f(x) Does Not Exist (DNE).
Classification:
The function exhibits a jump discontinuity of magnitude |4 - 3| = 1 at x = 2.
Note: The isolated point f(2) = 1 does not alter the fact that the two-sided limit fails to exist.
```

### Example 4: Evaluating an indeterminate limit via conjugate rationalization

Evaluate the limit:

$$\lim_{x \to 0} \frac{\sqrt{x + 25} - 5}{x}$$

```text
Stage 1 (Classification & Domain):
Input function: f(x) = (sqrt(x + 25) - 5)/x.
Test direct substitution at x = 0:
f(0) = (sqrt(25) - 5)/0 = (5 - 5)/0 = 0/0 (indeterminate form).

Stage 2 (Algebraic Preparation):
Rationalize the radical numerator by multiplying numerator and denominator
by the conjugate expression (sqrt(x + 25) + 5):
(sqrt(x + 25) - 5) * (sqrt(x + 25) + 5)
---------------------------------------
      x * (sqrt(x + 25) + 5)
Expand numerator using difference of squares (u - v)(u + v) = u^2 - v^2:
(x + 25) - 25        x
-------------- = ----------------------
x * (sqrt...)    x * (sqrt(x + 25) + 5)

Stage 3 (Core Operation):
Cancel common non-zero factor x for x != 0:
1 / (sqrt(x + 25) + 5)
Apply Quotient and Root Limit Laws as x -> 0:
lim_{x -> 0} [ 1 / (sqrt(x + 25) + 5) ] = 1 / (sqrt(0 + 25) + 5)
                                        = 1 / (5 + 5) = 1/10.

Stage 4 (Interpretation & Boundary Check):
Verify value near boundary:
For small positive x = 0.01:
(sqrt(25.01) - 5)/0.01 approx (5.0009999 - 5)/0.01 = 0.09999 approx 0.10.
The limit exists and equals 1/10.
```

## Exercises

### Q1

**1.** Determine the natural domain of $f(x) = \frac{3x - 1}{x^2 - 4x - 12}$ and express the answer in interval notation.

**2.** Determine the natural domain of $g(t) = \sqrt{5 - t} - \sqrt{t + 3}$ and express the answer in interval notation.

**3.** Determine the natural domain of $h(x) = \frac{2x + 7}{\sqrt[4]{x^2 - 4x}}$ and express the answer in interval notation.

**4.** Determine the natural domain of $k(u) = \frac{u - 2}{2 - \frac{6}{u + 1}}$ and express the answer in interval notation.

### Q2

**1.** Consider the piecewise function $g(x)$ defined by:

$$g(x) = \begin{cases} x^2 - 2x + 3 & \text{if } x < 2 \\ 5 & \text{if } x = 2 \\ 7 - 2x & \text{if } x > 2 \end{cases}$$

Which of the following statements regarding the behavior of $g(x)$ at $x = 2$ is mathematically correct?

- A) The limit $\lim_{x \to 2} g(x)$ does not exist because $g(2) \neq 3$.
- B) The limit $\lim_{x \to 2} g(x) = 3$, and $g(x)$ has a removable discontinuity at $x = 2$ because $\lim_{x \to 2} g(x) \neq g(2)$.
- C) The function $g(x)$ is continuous at $x = 2$ because both one-sided limits are finite real numbers.
- D) The limit $\lim_{x \to 2} g(x) = 5$ because direct evaluation at $x = 2$ gives $g(2) = 5$.
- E) The one-sided limits $\lim_{x \to 2^-} g(x)$ and $\lim_{x \to 2^+} g(x)$ are unequal, creating a jump discontinuity at $x = 2$.

### Q3

**1.** Let prototype function $f(x) = \sqrt{x}$. Write the explicit formula for the transformed function $h(x)$ obtained by shifting the graph of $f(x)$ horizontally to the right by $3$ units, reflecting it across the $x$-axis, stretching it vertically by a factor of $2$, and shifting it vertically upward by $5$ units. State the domain and range of $h(x)$ in interval notation.

**2.** For $f(x) = \sqrt{x}$ and $g(x) = 9 - x^2$, determine the composite formula $(f \circ g)(x)$ and state its exact domain in interval notation.

**3.** For $f(x) = \sqrt{x}$ and $g(x) = 9 - x^2$, determine the composite formula $(g \circ f)(x)$ and state its exact domain and range in interval notation.

### Q4

**1.** Evaluate the algebraic limit:

$$\lim_{x \to 3} \frac{2x^2 - 5x - 3}{x^2 - 9}$$

**2.** Evaluate the algebraic limit:

$$\lim_{t \to 0} \frac{\sqrt{t + 16} - 4}{t}$$

**3.** Evaluate the algebraic limit:

$$\lim_{x \to -2} \frac{\frac{1}{x + 4} - \frac{1}{2}}{x + 2}$$

**4.** Evaluate the trigonometric limit:

$$\lim_{\theta \to 0} \frac{\sin(5\theta)}{3\theta}$$

### Q5

**1.** An industrial electric kiln operates according to a computer-controlled temperature profile $T(t)$ (measured in hundreds of degrees Celsius) as a function of elapsed heating time $t$ (in hours) on the domain $[0, 6]$:

$$T(t) = \begin{cases} 2 + 1.5t & \text{if } 0 \le t < 2 \\ 5 & \text{if } t = 2 \\ 8 - \frac{6}{t + 1} & \text{if } 2 < t \le 6 \end{cases}$$

Compute the one-sided limits $\lim_{t \to 2^-} T(t)$ and $\lim_{t \to 2^+} T(t)$.

**2.** State whether the two-sided limit $\lim_{t \to 2} T(t)$ exists, and classify the mathematical discontinuity of $T(t)$ at $t = 2$.

**3.** Determine the absolute minimum temperature and absolute maximum temperature attained by the kiln on $[0, 6]$, and state the complete range of $T(t)$ in interval notation.

### Q6

**1.** An autonomous transit shuttle navigates a dedicated transit corridor according to a programmed forward velocity profile $v(t)$ (in meters per second) over the mission window $[0, 30]$ seconds:

$$v(t) = \begin{cases} \frac{a t^2 + 12t}{t + 4} & \text{if } 0 \le t < 10 \\ b & \text{if } t = 10 \\ \frac{\sqrt{t - 1} - 3}{t - 10} + 15 & \text{if } 10 < t \le 30 \end{cases}$$

where $a$ and $b$ are design parameters. Evaluate the right-hand velocity limit $\lim_{t \to 10^+} v(t)$ algebraically using conjugate rationalization.

**2.** Determine the exact value of parameter $a$ required so that the left-hand limit $\lim_{t \to 10^-} v(t)$ equals the right-hand limit $\lim_{t \to 10^+} v(t)$, establishing the existence of $\lim_{t \to 10} v(t)$.

**3.** Determine the exact value of parameter $b$ such that the velocity profile $v(t)$ is continuous at $t = 10$.

**4.** Compute the average acceleration of the shuttle over the interval $[17, 26]$ seconds, defined by $\bar{a} = \frac{v(26) - v(17)}{26 - 17}$.
