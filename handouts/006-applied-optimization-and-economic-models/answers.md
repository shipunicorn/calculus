---
title: "Handout 006: Optimization & Economics — Key"
---

# 006: Applied Optimization and Economic Models — Answer Key

## Exercises

### Q1

**1.**

> **Stage 1 (Classification & Domain).** The geometric shape is an open-top right circular cylinder of radius $r > 0$ and height $h > 0$. The volume is fixed at $V_0 = 500\pi\,\text{m}^3$. Objective: express exterior surface area $A$ in terms of $r$. Feasible domain: because radius must be strictly positive and height decreases to zero as radius grows arbitrarily large, the physical domain is the open interval $\mathopen{]}0, +\infty\mathclose{[}$.
>
> **Stage 2 (Algebraic Preparation).** The cylinder volume formula provides the constraint:
>
> $\displaystyle V = \pi r^2 h = 500\pi \;\Longrightarrow\; h = \frac{500}{r^2}$
>
> The exterior surface area consists of one circular bottom base of area $\pi r^2$ plus the vertical lateral wall of area $2\pi r h$:
>
> $\displaystyle A = \pi r^2 + 2\pi r h$
>
> Substitute $h = \frac{500}{r^2}$ into the area equation:
>
> $\displaystyle A(r) = \pi r^2 + 2\pi r \left(\frac{500}{r^2}\right) = \pi r^2 + \frac{1000\pi}{r}, \quad r \in \mathopen{]}0, +\infty\mathclose{[}$
>
> **Stage 3 (Core Operation).** Rewrite powers in readiness for differentiation: $A(r) = \pi r^2 + 1000\pi r^{-1}$. Differentiate with respect to $r$:
>
> $\displaystyle A'(r) = 2\pi r - 1000\pi r^{-2} = 2\pi r - \frac{1000\pi}{r^2} = \frac{2\pi(r^3 - 500)}{r^2}$
>
> Set $A'(r) = 0 \;\Longrightarrow\; 2\pi(r^3 - 500) = 0 \;\Longrightarrow\; r^3 = 500 \;\Longrightarrow\; r = \sqrt[3]{500} = 5\sqrt[3]{4}\,\text{m}$.
>
> **Stage 4 (Interpretation & Boundary Check).** As $r \to 0^+$, $\frac{1000\pi}{r} \to +\infty$ (infinitely tall, narrow cylinder). As $r \to +\infty$, $\pi r^2 \to +\infty$ (infinitely wide, shallow disc). The single critical number $r = \sqrt[3]{500} \approx 7.937\,\text{m}$ must therefore produce the absolute minimum.

**2.**

> **Stage 1 (Classification & Domain).** Candidate critical point: $r = \sqrt[3]{500}\,\text{m}$ on $\mathopen{]}0, +\infty\mathclose{[}$.
>
> **Stage 2 (Algebraic Preparation).** Compute the corresponding height $h$ from the volume constraint $h = \frac{500}{r^2}$:
>
> $\displaystyle h = \frac{500}{(\sqrt[3]{500})^2} = \frac{500}{500^{2/3}} = 500^{1/3} = \sqrt[3]{500}\,\text{m}$
>
> This demonstrates directly that $h = r = \sqrt[3]{500}\,\text{m}$.
>
> **Stage 3 (Core Operation).** Verify concavity using the second derivative:
>
> $\displaystyle A''(r) = \frac{d}{dr}\left(2\pi r - 1000\pi r^{-2}\right) = 2\pi + 2000\pi r^{-3} = 2\pi + \frac{2000\pi}{r^3}$
>
> For all $r > 0$, $A''(r) > 0$. Because $A(r)$ is strictly concave upward throughout its entire domain, $r = \sqrt[3]{500}$ provides the unique global minimum.
>
> **Stage 4 (Interpretation & Boundary Check).** Evaluate the exact minimum surface area:
>
> $\displaystyle A(\sqrt[3]{500}) = \pi (\sqrt[3]{500})^2 + \frac{1000\pi}{\sqrt[3]{500}} = \pi (500)^{2/3} + 2\pi (500)^{2/3} = 3\pi (500)^{2/3}$
>
> Noting that $500 = 125 \times 4 = 5^3 \times 4$:
>
> $\displaystyle A_{\text{min}} = 3\pi \cdot 25 \cdot 4^{2/3} = 75\pi \cdot 2^{4/3} = 150\pi \sqrt[3]{2} \approx 593.72\,\text{m}^2$
>
> Dimensions: radius $r = 5\sqrt[3]{4} \approx 7.94\,\text{m}$, height $h = 5\sqrt[3]{4} \approx 7.94\,\text{m}$, enclosing minimum surface area $150\pi \sqrt[3]{2}\,\text{m}^2$.

### Q2

**1.**

> **Stage 1 (Classification & Domain).** The corral has 2 horizontal outer boundaries of length $y$ and 4 vertical fence segments of length $x$ (2 outer borders and 2 interior dividing fences). Exterior fencing costs \$12/ft and interior dividing fencing costs \$8/ft. Total budget is \$7,200. Objective: maximize total enclosed area $A = xy$.
>
> **Stage 2 (Algebraic Preparation).** Calculate total construction cost in terms of dimensions:
>
> $\displaystyle \text{Cost} = 2(\$12 \cdot y) + 2(\$12 \cdot x) + 2(\$8 \cdot x) = 24y + 24x + 16x = 40x + 24y$
>
> Equate total cost to the allocated budget:
>
> $\displaystyle 40x + 24y = 7200$
>
> Divide both sides by 8:
>
> $\displaystyle 5x + 3y = 900 \;\Longrightarrow\; 3y = 900 - 5x \;\Longrightarrow\; y = 300 - \frac{5}{3}x$
>
> Determine the feasible physical domain from non-negativity: $x \ge 0$, and $y \ge 0 \;\Rightarrow\; 300 - \frac{5}{3}x \ge 0 \;\Rightarrow\; x \le 180$. The domain is $[0, 180]$.
>
> **Stage 3 (Core Operation).** Substitute $y$ into the area equation:
>
> $\displaystyle A(x) = x\left(300 - \frac{5}{3}x\right) = 300x - \frac{5}{3}x^2, \quad x \in [0, 180]$
>
> **Stage 4 (Interpretation & Boundary Check).** At $x = 0$, $A(0) = 0$. At $x = 180$, $y = 0 \;\Rightarrow\; A(180) = 0$. The quadratic function is bounded and non-negative on $[0, 180]$.

**2.**

> **Stage 1 (Classification & Domain).** Objective function: $A(x) = 300x - \frac{5}{3}x^2$ on the closed interval $[0, 180]$.
>
> **Stage 2 (Algebraic Preparation).** Function is polynomial and everywhere differentiable.
>
> **Stage 3 (Core Operation).** Differentiate with respect to $x$:
>
> $\displaystyle A'(x) = 300 - \frac{10}{3}x$
>
> Set $A'(x) = 0$:
>
> $\displaystyle \frac{10}{3}x = 300 \;\Longrightarrow\; 10x = 900 \;\Longrightarrow\; x = 90\,\text{ft}$
>
> **Stage 4 (Interpretation & Boundary Check).** Evaluate $A(x)$ at the critical number and endpoints:
>
> $\displaystyle A(0) = 0\,\text{ft}^2, \quad A(180) = 0\,\text{ft}^2$
>
> $\displaystyle A(90) = 300(90) - \frac{5}{3}(90)^2 = 27{,}000 - \frac{5}{3}(8100) = 27{,}000 - 13{,}500 = 13{,}500\,\text{ft}^2$
>
> Second derivative check confirms concavity: $A''(x) = -\frac{10}{3} < 0$ for all $x$. Optimal dimensions: depth $x = 90\,\text{ft}$, width $y = 300 - \frac{5}{3}(90) = 150\,\text{ft}$. The maximum total area is $13{,}500\,\text{ft}^2$. Each of the three pens has dimensions $90\,\text{ft} \times 50\,\text{ft}$ and area $4{,}500\,\text{ft}^2$.

### Q3

**1. Correct answer: D.**

- **A (Incorrect):** Employs an invalid domain $[0, 12]$ that produces negative base dimensions for $x > 6$, and misinterprets the endpoint $x = 6$ (where volume is 0) as a maximum.
- **B (Incorrect):** Subtracts only a single cutout $x$ along each dimension instead of two corners, resulting in an erroneous base $(12 - x)^2$ and an invalid domain $[0, 12]$.
- **C (Incorrect):** Erroneously factors $(12 - 2x)^2$ as $144 - 4x^2$, dropping the middle cross term $-48x$ and leading to a false critical point $x = 2\sqrt{3}$.
- **D (Correct):** Two squares of side $x$ are removed from each $12\,\text{in}$ edge, producing base dimensions $(12 - 2x) \times (12 - 2x)$ and height $x$. Non-negativity requires $x \ge 0$ and $12 - 2x \ge 0 \;\Rightarrow\; x \in [0, 6]$. Setting $V'(x) = 12(x - 2)(x - 6) = 0$ yields interior critical point $x = 2$, where $V(2) = 2(8)^2 = 128\,\text{in}^3$.
- **E (Incorrect):** Confuses a local minimum with a maximum; while $V'(6) = 0$, evaluating $V(6) = 6(0)^2 = 0\,\text{in}^3$ confirms that folding completely in half destroys all internal storage volume.

### Q4

**1.**

> **Stage 1 (Classification & Domain).** Total wire length is $20\,\text{m}$. Wire length $x$ forms an equilateral triangle, and remaining wire $20 - x$ forms a regular hexagon. Feasible domain is $[0, 20]$.
>
> **Stage 2 (Algebraic Preparation).** Triangle side length is $s = \frac{x}{3}$. Area of an equilateral triangle of side $s$:
>
> $\displaystyle A_{\text{tri}} = \frac{\sqrt{3}}{4} s^2 = \frac{\sqrt{3}}{4} \left(\frac{x}{3}\right)^2 = \frac{\sqrt{3}}{36}x^2$
>
> Hexagon perimeter is $20 - x$, so each of the 6 sides has length $h = \frac{20 - x}{6}$. A regular hexagon consists of 6 equilateral triangles of side $h$:
>
> $\displaystyle A_{\text{hex}} = 6 \left(\frac{\sqrt{3}}{4} h^2\right) = \frac{3\sqrt{3}}{2} \left(\frac{20 - x}{6}\right)^2 = \frac{3\sqrt{3}}{2 \times 36} (20 - x)^2 = \frac{\sqrt{3}}{24}(20 - x)^2$
>
> Objective function for total combined area:
>
> $\displaystyle A(x) = \frac{\sqrt{3}}{36}x^2 + \frac{\sqrt{3}}{24}(20 - x)^2, \quad x \in [0, 20]$
>
> **Stage 3 (Core Operation).** Express over the common denominator 72:
>
> $\displaystyle A(x) = \frac{\sqrt{3}}{72}\left[2x^2 + 3(20 - x)^2\right] = \frac{\sqrt{3}}{72}\left[2x^2 + 3(400 - 40x + x^2)\right] = \frac{\sqrt{3}}{72}\left(5x^2 - 120x + 1200\right)$
>
> **Stage 4 (Interpretation & Boundary Check).** Feasible interval is the closed set $[0, 20]$. The function is quadratic with leading coefficient $\frac{5\sqrt{3}}{72} > 0$, forming an upward-opening parabola.

**2.**

> **Stage 1 (Classification & Domain).** Objective function: $A(x) = \frac{\sqrt{3}}{72}(5x^2 - 120x + 1200)$ on $[0, 20]$.
>
> **Stage 2 (Algebraic Preparation).** Differentiate $A(x)$ with respect to $x$:
>
> $\displaystyle A'(x) = \frac{\sqrt{3}}{72}(10x - 120) = \frac{10\sqrt{3}}{72}(x - 12) = \frac{5\sqrt{3}}{36}(x - 12)$
>
> **Stage 3 (Core Operation).** Set $A'(x) = 0 \;\Longrightarrow\; x - 12 = 0 \;\Longrightarrow\; x = 12\,\text{m}$.
>
> Second derivative check: $A''(x) = \frac{5\sqrt{3}}{36} > 0$ everywhere, confirming that $x = 12\,\text{m}$ is the unique interior local and absolute minimum.
>
> **Stage 4 (Interpretation & Boundary Check).** Evaluate minimal area at $x = 12\,\text{m}$:
>
> $\displaystyle A(12) = \frac{\sqrt{3}}{72}\left[5(144) - 120(12) + 1200\right] = \frac{\sqrt{3}}{72}(720 - 1440 + 1200) = \frac{\sqrt{3}}{72}(480) = \frac{20\sqrt{3}}{3} \approx 11.55\,\text{m}^2$
>
> Minimal area occurs when $12\,\text{m}$ of wire is allocated to the triangle and $8\,\text{m}$ is allocated to the hexagon, enclosing a minimum area of $\frac{20\sqrt{3}}{3} \approx 11.55\,\text{m}^2$.

**3.**

> **Stage 1 (Classification & Domain).** To maximize the convex quadratic function $A(x)$ on the closed interval $[0, 20]$, we apply the Closed Interval Method and evaluate the boundary endpoints.
>
> **Stage 2 (Algebraic Preparation).** Compare the boundary values:
>
> At $x = 0$ (all $20\,\text{m}$ allocated to the hexagon):
>
> $\displaystyle A(0) = \frac{\sqrt{3}}{72}(1200) = \frac{50\sqrt{3}}{3} \approx 28.87\,\text{m}^2$
>
> At $x = 20$ (all $20\,\text{m}$ allocated to the triangle):
>
> $\displaystyle A(20) = \frac{\sqrt{3}}{72}\left[5(400) - 120(20) + 1200\right] = \frac{\sqrt{3}}{72}(2000 - 2400 + 1200) = \frac{\sqrt{3}}{72}(800) = \frac{100\sqrt{3}}{9} \approx 19.25\,\text{m}^2$
>
> **Stage 3 (Core Operation).** Compare the values across the entire domain:
>
> $\displaystyle A(12) = \frac{20\sqrt{3}}{3} \approx 11.55\,\text{m}^2 \quad (\text{absolute minimum})$
>
> $\displaystyle A(20) = \frac{100\sqrt{3}}{9} = \frac{33.33\sqrt{3}}{3} \approx 19.25\,\text{m}^2$
>
> $\displaystyle A(0) = \frac{50\sqrt{3}}{3} = \frac{150\sqrt{3}}{9} \approx 28.87\,\text{m}^2 \quad (\text{absolute maximum})$
>
> **Stage 4 (Interpretation & Boundary Check).** Because $\frac{50\sqrt{3}}{3} > \frac{100\sqrt{3}}{9} > \frac{20\sqrt{3}}{3}$, the absolute maximum combined area is achieved at $x = 0$. The wire should not be cut; the entire $20\,\text{m}$ length should be bent into the regular hexagon, yielding an absolute maximum area of $\frac{50\sqrt{3}}{3} \approx 28.87\,\text{m}^2$.

### Q5

**1.**

> **Stage 1 (Classification & Domain).** Production quantity $x \ge 0$ is measured in thousands of units. Total cost is $C(x) = 2x^3 - 12x^2 + 30x + 100$ and unit demand price is $p(x) = 150 - 6x$. Non-negativity of price requires $150 - 6x \ge 0 \;\Rightarrow\; x \le 25$. Feasible domain is $[0, 25]$.
>
> **Stage 2 (Algebraic Preparation).** Gross revenue is quantity times unit price:
>
> $\displaystyle R(x) = x \cdot p(x) = x(150 - 6x) = 150x - 6x^2$
>
> Total profit function $P(x) = R(x) - C(x)$:
>
> $\displaystyle P(x) = (150x - 6x^2) - (2x^3 - 12x^2 + 30x + 100) = -2x^3 + 6x^2 + 120x - 100$
>
> **Stage 3 (Core Operation).** Differentiate $P(x)$ to find critical production levels:
>
> $\displaystyle P'(x) = -6x^2 + 12x + 120 = -6(x^2 - 2x - 20)$
>
> Set $P'(x) = 0 \;\Rightarrow\; x^2 - 2x - 20 = 0$. Solve using the quadratic formula:
>
> $\displaystyle x = \frac{2 \pm \sqrt{(-2)^2 - 4(1)(-20)}}{2} = \frac{2 \pm \sqrt{4 + 80}}{2} = \frac{2 \pm \sqrt{84}}{2} = 1 \pm \sqrt{21}$
>
> Since $x \ge 0$, reject $1 - \sqrt{21} < 0$. The interior critical point is $x = 1 + \sqrt{21} \approx 5.583$ thousand units ($5{,}583$ units).
>
> **Stage 4 (Interpretation & Boundary Check).** Second derivative check:
>
> $\displaystyle P''(x) = -12x + 12 = -12(x - 1)$
>
> At $x = 1 + \sqrt{21}$:
>
> $\displaystyle P''(1 + \sqrt{21}) = -12(1 + \sqrt{21} - 1) = -12\sqrt{21} < 0$
>
> Because $P''(x) < 0$ at the critical point and $P'(x)$ changes sign from positive to negative, $x = 1 + \sqrt{21} \approx 5.583$ produces the unique absolute maximum profit.

**2.**

> **Stage 1 (Classification & Domain).** Average cost is $c(x) = \frac{C(x)}{x}$ for $x \in \mathopen{]}0, 25]$.
>
> **Stage 2 (Algebraic Preparation).** Formulate average cost:
>
> $\displaystyle c(x) = \frac{2x^3 - 12x^2 + 30x + 100}{x} = 2x^2 - 12x + 30 + \frac{100}{x}$
>
> **Stage 3 (Core Operation).** Differentiate average cost with respect to $x$:
>
> $\displaystyle c'(x) = 4x - 12 - \frac{100}{x^2} = \frac{4x^3 - 12x^2 - 100}{x^2} = \frac{4(x^3 - 3x^2 - 25)}{x^2}$
>
> Set $c'(x) = 0 \;\Rightarrow\; x^3 - 3x^2 - 25 = 0 \;\Rightarrow\; x^2(x - 3) = 25$. Solving numerically yields the unique real root $x \approx 4.332$ thousand units ($4{,}332$ units).
>
> **Stage 4 (Interpretation & Boundary Check).** Verify that marginal cost equals average cost at $x \approx 4.332$:
>
> $\displaystyle C'(x) = 6x^2 - 24x + 30$
>
> At $x \approx 4.332$:
>
> $\displaystyle C'(4.332) = 6(4.332)^2 - 24(4.332) + 30 \approx 112.597 - 103.968 + 30 \approx \$38.63\text{ per unit}$
>
> $\displaystyle c(4.332) = 2(4.332)^2 - 12(4.332) + 30 + \frac{100}{4.332} \approx 37.532 - 51.984 + 30 + 23.084 \approx \$38.63\text{ per unit}$
>
> This numerically and analytically verifies that $C'(x) = c(x)$ at the production level minimizing average cost.

### Q6

**1.**

> **Stage 1 (Classification & Domain).** Platform $P$ is $8\,\text{km}$ out to sea from $A$. Refinery $B$ is $20\,\text{km}$ along the coast from $A$. The pipeline lands at point $D$ at distance $x$ from $A$ along the straight coast. Unit construction costs: underwater pipe costs $c_{\text{sea}} = 5$ million dollars/km; overland pipe costs $c_{\text{land}} = 3$ million dollars/km. Feasible domain: landing point $D$ lies between $A$ and $B$, so $x \in [0, 20]$.
>
> **Stage 2 (Algebraic Preparation).** Triangle $PAD$ is a right triangle with legs $8\,\text{km}$ and $x\,\text{km}$. The underwater distance from $P$ to $D$ is the hypotenuse:
>
> $\displaystyle d_{\text{sea}} = \sqrt{x^2 + 8^2} = \sqrt{x^2 + 64}$
>
> The remaining overland distance along the coastline from $D$ to refinery $B$ is:
>
> $\displaystyle d_{\text{land}} = 20 - x$
>
> Total pipeline construction cost function $C(x)$ (in millions of dollars):
>
> $\displaystyle C(x) = 5\sqrt{x^2 + 64} + 3(20 - x), \quad x \in [0, 20]$
>
> **Stage 3 (Core Operation).** Rewrite the radical using fractional powers: $C(x) = 5(x^2 + 64)^{1/2} + 60 - 3x$.
>
> **Stage 4 (Interpretation & Boundary Check).** Non-negativity of geometric distances confirms $0 \le x \le 20$. The function is continuous on the closed, bounded interval $[0, 20]$.

**2.**

> **Stage 1 (Classification & Domain).** Objective function: $C(x) = 5(x^2 + 64)^{1/2} + 60 - 3x$ on $[0, 20]$.
>
> **Stage 2 (Algebraic Preparation).** Differentiate with respect to $x$ using the Chain Rule:
>
> $\displaystyle C'(x) = 5 \cdot \frac{1}{2}(x^2 + 64)^{-1/2}(2x) - 3 = \frac{5x}{\sqrt{x^2 + 64}} - 3$
>
> **Stage 3 (Core Operation).** Locate critical numbers by setting $C'(x) = 0$:
>
> $\displaystyle \frac{5x}{\sqrt{x^2 + 64}} = 3 \;\Longrightarrow\; 5x = 3\sqrt{x^2 + 64}$
>
> Since $x \ge 0$, both sides are non-negative. Square both sides:
>
> $\displaystyle 25x^2 = 9(x^2 + 64) = 9x^2 + 576 \;\Longrightarrow\; 16x^2 = 576 \;\Longrightarrow\; x^2 = \frac{576}{16} = 36$
>
> $\displaystyle x = 6\,\text{km} \quad (\text{since } x \ge 0)$
>
> The critical number $x = 6\,\text{km}$ lies strictly inside the feasible interval $[0, 20]$.
>
> **Stage 4 (Interpretation & Boundary Check).** Evaluate $C(x)$ at the critical number and at both endpoints using the Closed Interval Method:
>
> At $x = 0$ (pipeline runs perpendicular to coast, then entirely overland):
>
> $\displaystyle C(0) = 5\sqrt{0 + 64} + 3(20 - 0) = 5(8) + 60 = 40 + 60 = 100\text{ million dollars}$
>
> At $x = 20$ (pipeline laid entirely underwater directly to the refinery):
>
> $\displaystyle C(20) = 5\sqrt{20^2 + 64} + 3(0) = 5\sqrt{464} = 5(4\sqrt{29}) = 20\sqrt{29} \approx 107.70\text{ million dollars}$
>
> At interior critical number $x = 6\,\text{km}$:
>
> $\displaystyle C(6) = 5\sqrt{6^2 + 64} + 3(20 - 6) = 5\sqrt{100} + 3(14) = 5(10) + 42 = 50 + 42 = 92\text{ million dollars}$
>
> Comparing values: $C(6) = 92 < C(0) = 100 < C(20) \approx 107.70$.

**3.**

> **Stage 1 (Classification & Domain).** The global minimum cost is achieved at $x = 6\,\text{km}$, yielding a minimal cost of \$92 million.
>
> **Stage 2 (Algebraic Preparation).** In the right triangle $PAD$ formed by the platform, shore projection $A$, and landing point $D$:
>
> $\displaystyle \text{Adjacent leg along coast} = x = 6\,\text{km}$
>
> $\displaystyle \text{Opposite leg perpendicular to coast} = 8\,\text{km}$
>
> $\displaystyle \text{Underwater hypotenuse } PD = \sqrt{6^2 + 8^2} = 10\,\text{km}$
>
> **Stage 3 (Core Operation).** The angle $\theta$ between the underwater pipeline and the shoreline satisfies:
>
> $\displaystyle \cos \theta = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{x}{\sqrt{x^2 + 64}} = \frac{6}{10} = \frac{3}{5} = 0.6$
>
> **Stage 4 (Interpretation & Boundary Check).** Inspect the critical point equation from part 2:
>
> $\displaystyle C'(x) = 5\left(\frac{x}{\sqrt{x^2 + 64}}\right) - 3 = 0 \;\Longrightarrow\; \frac{x}{\sqrt{x^2 + 64}} = \frac{3}{5} \;\Longrightarrow\; \cos \theta = \frac{c_{\text{land}}}{c_{\text{sea}}}$
>
> This demonstrates that the optimal landing trajectory obeys the continuous principle of refraction (Snell's Law / Fermat's Principle of Least Time). The cosine of the incident shore angle equals the exact ratio of overland to underwater construction costs per unit distance ($\frac{3}{5}$). The pipeline lands $6\,\text{km}$ down the coast from $A$, saving \$8 million compared to the perpendicular path and \$15.7 million compared to direct underwater routing.
