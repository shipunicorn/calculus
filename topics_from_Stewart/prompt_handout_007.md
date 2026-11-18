# Prompt for Handout 007: Antiderivatives, Riemann Sums, and the Definite Integral

Use the `/calculus-create-handout` skill to create a new handout package `007-antiderivatives-riemann-sums-and-integrals` ("Antiderivatives, Riemann Sums, and the Definite Integral"). Do not create or edit any other handout in this session.

```text
/calculus-create-handout
```

---

## 1. Package Specification

- **Package Number (Fixed):** `007`
- **Target Package Directory:** `C:\dev\calculus\handouts\007-antiderivatives-riemann-sums-and-integrals\`
- **Action Required:** Create new package using `007` as the package ID.
- **Handout Title:** `Handout 007: Antiderivatives, Riemann Sums, and the Definite Integral`
- **Page Budget:** 13–15 pages for `handout.print.pdf` (Strict limit: $\le 16$ pages). `answers.print.pdf` has no page limit.

---

## 2. Pedagogical Context & MATH 254 Critical Path Alignment

- **Role in Sequence:** Stage 3 (Applied Optimization & Integration Foundations, Handout 7 of 7 — Capstone Synthesis of Single-Variable Calculus).
- **Prerequisites Assumed:** Handouts 001 through 006 (Functions, Limits, Difference Quotients, Operational Differentiation, Extrema Theory, and Optimization Modeling).
- **MATH 254 (Multivariable Calculus) Critical Link:**
  - The definition of the definite integral as a limit of Riemann sums is the indispensable theoretical foundation for:
    - **Double Integrals** over 2D planar regions: $\iint_D f(x, y)\,dA = \lim_{m,n \to \infty} \sum_{i=1}^m \sum_{j=1}^n f(x_{ij}^*, y_{ij}^*)\Delta A$.
    - **Triple Integrals** over 3D solid volumes: $\iiint_E f(x, y, z)\,dV$.
    - **Vector Line Integrals:** $\int_C \mathbf{F} \cdot d\mathbf{r}$ (work and circulation).
    - **Surface Flux Integrals:** $\iint_S \mathbf{F} \cdot d\mathbf{S}$ (flow and flux).
  - Understanding **net signed area** versus **total geometric area** is critical for applying Green's Theorem, Stokes' Theorem, and the Divergence Theorem without sign errors.
  - Solving Initial Value Problems (IVPs) establishes the core mechanism for reconstructing potential functions from conservative vector fields ($\nabla f = \mathbf{F}$).

---

## 3. Source Documents & Grounding

- **Master Plan Authority:** [`C:\dev\calculus\topics_from_Stewart\handouts_plan.md`](file:///C:/dev/calculus/topics_from_Stewart/handouts_plan.md) (Sections 1–4).
- **Primary Source Notes:**
  - [`C:\dev\calculus\topics_from_Stewart\topics_6.md`](file:///C:/dev/calculus/topics_from_Stewart/topics_6.md) (Sections 4.1–4.3, 5.1–5.5: Antiderivatives, Families $+ C$, Kinematic IVPs, Graphical Antiderivative Reconstruction).
  - [`C:\dev\calculus\topics_from_Stewart\topics_7.md`](file:///C:/dev/calculus/topics_from_Stewart/topics_7.md) (Sections 1, 2.1–2.4, 3.1–3.2: True-False Quiz, The Area Problem, Approximating Sums $L_n, R_n, M_n$, Limit of Riemann Sums, The Definite Integral, Net Signed Area, Integral Properties).
- **Textbook Authority:** Stewart *Calculus: Early Transcendentals* (7th Edition), Sections 3.9, 4.1, 4.2, and Chapter 4 Review.

---

## 4. Standalone Modern SVG Figures

Copy the following verified SVG figures from `C:\dev\calculus\topics_from_Stewart\figures\` into `<package>/figures/` and embed them into `handout.md`:

1. `sec3_9_fig1_antiderivatives_family.svg`: Family of antiderivatives $F(x) + C$ illustrating vertical translation by the constant of integration.
2. `sec3_9_fig2_sketch_antiderivative.svg`: Reconstructing the shape of $F(x)$ from the graph of $f(x)$ using intervals of increase/decrease and inflection points.
3. `sec3_9_ex45_antiderivative_sketch.svg`: Graphical antiderivative reconstruction with prescribed initial condition $F(0) = 0$.
4. `sec3_9_ex43_antiderivative_matching.svg` & `sec3_9_ex44_antiderivative_matching.svg`: Matching rate graphs $f(x)$ with their corresponding antiderivatives $F(x)$.
5. `sec3_9_ex46_velocity_position.svg`: Kinematic position recovery $s(t)$ from a piecewise linear velocity curve $v(t)$.
6. `sec3_9_ex47_step_derivative.svg`: Antiderivative of a step-like piecewise rate curve.
7. `sec4_1_figure1_area_under_curve.svg`: The Area Problem: region $S$ bounded by $y = f(x)$, $y = 0$, $x = a$, and $x = b$.
8. `sec4_1_figure2_straight_sided_areas.svg`: Comparing elementary straight-sided geometric regions with curves requiring calculus limits.
9. `sec4_1_figure3_parabola_region.svg` through `sec4_1_figure7_parabola_n_rectangles.svg`: The historical Archimedean parabola area problem, showing the convergence of Riemann partitions ($R_4, L_4, R_8 \dots$ as $n \to \infty$).
10. `sec4_1_figure13_sample_points.svg`: Arbitrary sample points $x_i^*$ within each subinterval $[x_{i-1}, x_i]$.
11. `sec4_1_figure14_lower_upper_sums.svg`: Darboux lower and upper sums sandwiching the true area under a curve.

**Respective Figure Generators:**
- [`C:\dev\calculus\topics_from_Stewart\generate_figures_topics6.py`](file:///C:/dev/calculus/topics_from_Stewart/generate_figures_topics6.py)
- [`C:\dev\calculus\topics_from_Stewart\generate_figures_topics7.py`](file:///C:/dev/calculus/topics_from_Stewart/generate_figures_topics7.py)

---

## 5. Instructional Structure & Pedagogical Content

Interleave concise theoretical principles with 4-stage worked examples:

1. **Antiderivatives and the General Antiderivative:**
   - Definition: A function $F$ is an antiderivative of $f$ on an interval $I$ if $F'(x) = f(x)$ for all $x \in I$.
   - **Theorem:** If $F$ is an antiderivative of $f$, the most general antiderivative is $F(x) + C$, where $C$ is an arbitrary constant.
   - Catalog of standard antiderivatives:
     - Power rule: $\int x^n dx = \frac{x^{n+1}}{n+1} + C$ for $n \ne -1$.
     - Logarithmic rule: $\int \frac{1}{x} dx = \ln|x| + C$.
     - Exponential rule: $\int e^{k x} dx = \frac{1}{k} e^{k x} + C$.
     - Trigonometric rules: $\cos x \to \sin x$, $\sin x \to -\cos x$, $\sec^2 x \to \tan x$, $\sec x \tan x \to \sec x$.
2. **Initial Value Problems (IVPs) & Kinematics:**
   - Solving first-order differential equations $\frac{dy}{dx} = f(x)$ with initial condition $y(x_0) = y_0$ to uniquely determine $C$.
   - Second-order kinematic recovery: acceleration $a(t) \to$ velocity $v(t) = \int a(t)dt + C_1 \to$ position $s(t) = \int v(t)dt + C_2$.
3. **Graphical Antiderivative Reconstruction:**
   - Where $f(x) > 0$, $F(x)$ is increasing; where $f(x) < 0$, $F(x)$ is decreasing.
   - Zero-crossings of $f(x)$ correspond to horizontal tangents and local extrema of $F(x)$.
   - Where $f(x)$ is increasing ($f'(x) > 0$), $F(x)$ is concave upward; where $f(x)$ is decreasing, $F(x)$ is concave downward.
4. **The Area Problem & Approximating Riemann Sums:**
   - Subdividing $[a, b]$ into $n$ equal subintervals of width $\Delta x = \frac{b - a}{n}$.
   - Grid points: $x_i = a + i \Delta x$.
   - **Left Endpoint Sum:** $L_n = \sum_{i=1}^n f(x_{i-1})\Delta x$.
   - **Right Endpoint Sum:** $R_n = \sum_{i=1}^n f(x_i)\Delta x$.
   - **Midpoint Sum:** $M_n = \sum_{i=1}^n f(\bar{x}_i)\Delta x$, where $\bar{x}_i = \frac{x_{i-1} + x_i}{2}$.
   - Sigma algebra formulas: $\sum_{i=1}^n 1 = n$, $\sum_{i=1}^n i = \frac{n(n+1)}{2}$, $\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$.
5. **The Definite Integral Definition:**
   - Formal definition:
     $$\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*)\,\Delta x$$
   - Interpretation as **Net Signed Area**:
     $$\int_a^b f(x)\,dx = A_{\text{above}} - A_{\text{below}}$$
   - Contrast with Total Geometric Area: $A_{\text{total}} = \int_a^b |f(x)|\,dx$.
6. **Properties of the Definite Integral:**
   - Order of integration: $\int_b^a f(x)\,dx = -\int_a^b f(x)\,dx$, and $\int_a^a f(x)\,dx = 0$.
   - Linearity: $\int_a^b [c f(x) + g(x)]\,dx = c \int_a^b f(x)\,dx + \int_a^b g(x)\,dx$.
   - Interval Additivity: $\int_a^c f(x)\,dx = \int_a^b f(x)\,dx + \int_b^c f(x)\,dx$.
   - Comparison Properties: If $f(x) \ge 0$, then $\int_a^b f(x)\,dx \ge 0$; if $f(x) \le g(x)$, then $\int_a^b f \le \int_a^b g$.
   - Bounding Property: If $m \le f(x) \le M$ on $[a, b]$, then $m(b - a) \le \int_a^b f(x)\,dx \le M(b - a)$.
7. **Diagnostic Section (`## Mistakes, edge cases & strategies`):**
   Table `| Trap | Correct reasoning | Strategy |` covering:
   - Forgetting the arbitrary constant $+ C$ on general indefinite antiderivatives.
   - Forgetting the absolute value: $\int \frac{1}{x} dx = \ln|x| + C$, not $\ln(x) + C$.
   - Confusing net signed area with total area (e.g. evaluating $\int_0^{2\pi} \sin x\,dx = 0$ while total area is $4$).
   - Reversing limits of integration without changing sign: $\int_b^a f \ne \int_a^b f$.
   - Algebraic index errors when setting up Riemann sum limits: miscounting $\Delta x$ or evaluating $\sum i^2$.
   - Assuming a definite integral must be positive even when the function lies entirely beneath the $x$-axis.

---

## 6. Exercise Progression & MECE Requirements

Author 6 fresh, non-bank exercises under `## Exercises`, ordered strictly from easiest to hardest:

- **Universal Formatting Rules:**
  - Bare sequential headings: `### Q1` through `### Q6`.
  - Every question begins with bold subpart `**1.**`.
  - Never use Markdown ordered lists (`1.`, `2.`).
  - Strict answer-free objectivity.
- **Exercise Breakdown:**
  - **Q1 (Antiderivatives & Initial Value Problems):**
    - Subpart **1.** Find the general antiderivative $F(x)$ of $f(x) = \frac{4}{\sqrt{x}} - \frac{3}{x} + 2\sec^2(x)$ on the interval $\mathopen{]}0, \pi/2\mathclose{[}$.
    - Subpart **2.** Solve the initial value problem $f''(x) = 12x^2 + 6x - 4$ with $f'(0) = 5$ and $f(1) = 8$.
  - **Q2 (Graphical Antiderivative Reconstruction & Matching):**
    - Given a piecewise linear rate graph $y = f(x)$ on $[-3, 5]$:
      - Subpart **1.** Identify all local extrema and inflection points of $F(x) = \int_0^x f(t)\,dt$.
      - Subpart **2.** Sketch the graph of $F(x)$ given the initial condition $F(0) = -2$, computing exact values at integer grid points using geometric areas.
  - **Q3 (Diagnostic Multiple Choice):** 5-option conceptual item (`A)` through `E)`):
    - Subpart **1.** Diagnosing true vs false statements regarding Riemann sums, net signed area, and definite integral properties, with distractors catching dropped signs, absolute value omissions, and reversed integration bounds.
  - **Q4 (Finite Riemann Sum Approximations from Tabular Data):**
    - A water purification facility monitors effluent flow rate $r(t)$ (liters/min) over an 8-hour shift, recorded every 2 hours:
      $$t \in \{0, 2, 4, 6, 8\}, \quad r(t) \in \{120, 145, 170, 160, 130\}$$
    - Subpart **1.** Compute the Left Endpoint approximation $L_4$ for total effluent.
    - Subpart **2.** Compute the Right Endpoint approximation $R_4$.
    - Subpart **3.** Compute the Midpoint approximation $M_2$ grouping into two 4-hour subintervals.
  - **Q5 (Evaluating Definite Integrals via the Limit of Riemann Sums):**
    - Evaluate the definite integral directly from the formal definition:
      $$\int_1^4 (2x^2 - 3x + 1)\,dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i)\,\Delta x$$
    - Subpart **1.** Express $\Delta x$ and $x_i$ in terms of $n$ and $i$.
    - Subpart **2.** Set up the Riemann sum and expand using sigma summation formulas.
    - Subpart **3.** Evaluate the limit as $n \to \infty$ to obtain the exact rational value.
  - **Capstone Q6 (Very Hard Applied Transfer Task):**
    - Multi-stage variable-thrust sounding rocket trajectory:
      Acceleration is piecewise defined by:
      $$a(t) = \begin{cases} 40 - 2t, & 0 \le t \le 10 \\ -9.8, & t > 10 \end{cases}$$
    - Subpart **1.** Find the velocity $v(t)$ for all $t \ge 0$, assuming launch from rest ($v(0) = 0$).
    - Subpart **2.** Determine the exact burnout velocity at $t = 10$ and the time $t_{\text{apogee}}$ when the rocket reaches maximum altitude.
    - Subpart **3.** Set up and evaluate the definite integrals for total distance traveled during ascent versus net displacement, establishing the connection between Riemann area limits and physical work/motion.

---

## 7. Answer Key Specifications (`answers.md`)

- Title: `Handout 007: Antiderivatives, Riemann Sums, and the Definite Integral — Answer Key`
- Matching `### Q1` through `### Q6` headings under `## Exercises`.
- Every subpart answered with a full Four-Stage derivation box (`>`).
- For Q3 (Multiple Choice):
  - Bold declaration: `**1. Correct answer: X.**`
  - Explanations for all 5 options (`- **A (Incorrect):** ...`), explaining why the correct choice holds and describing the specific conceptual error in each distractor.
  - No option letters repeated in explanation prose.

---

## 8. Verification & Finalization Pipeline

1. Independently verify all derivations using a SymPy script.
2. Validate handout structure:
   ```powershell
   python -X utf8 -I C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/validate_handout.py C:/dev/calculus/handouts/007-antiderivatives-riemann-sums-and-integrals
   ```
3. Balance and shuffle multiple-choice letters:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/shuffle_mc_options.py --package C:/dev/calculus/handouts/007-antiderivatives-riemann-sums-and-integrals --apply
   ```
4. Render print PDFs (`handout.print.pdf`, `answers.print.pdf`) and visually inspect pages.
5. Check 16-page limit:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/check_page_limit.py C:/dev/calculus/handouts/007-antiderivatives-riemann-sums-and-integrals
   ```
6. Package finalization:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/finalize_package.py C:/dev/calculus/handouts/007-antiderivatives-riemann-sums-and-integrals
   ```
