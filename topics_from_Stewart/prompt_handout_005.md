# Prompt for Handout 005: Implicit Differentiation, Critical Points, and the Mean Value Theorem

Use the `/calculus-create-handout` skill to create a new handout package `005-implicit-differentiation-extrema-and-mvt` ("Implicit Differentiation, Critical Points, and the Mean Value Theorem"). Do not create or edit any other handout in this session.

```text
/calculus-create-handout
```

---

## 1. Package Specification

- **Package Number (Fixed):** `005`
- **Target Package Directory:** `C:\dev\calculus\handouts\005-implicit-differentiation-extrema-and-mvt\`
- **Action Required:** Create new package using `005` as the package ID.
- **Handout Title:** `Handout 005: Implicit Differentiation, Critical Points, and the Mean Value Theorem`
- **Page Budget:** 13–15 pages for `handout.print.pdf` (Strict limit: $\le 16$ pages). `answers.print.pdf` has no page limit.

---

## 2. Pedagogical Context & MATH 254 Critical Path Alignment

- **Role in Sequence:** Stage 2 (The Derivative & Differentiation Fluency, Handout 5 of 7).
- **Prerequisites Assumed:**
  - Handout 003: Tangent line definitions, difference quotients, differentiability failure modes.
  - Handout 004: Operational differentiation rules (Power, Product, Quotient, Chain) and transcendental derivatives.
- **Subsequent Handouts Unlocked:**
  - Handout 006: Applied Optimization and Economic Models.
  - Handout 007: Antiderivatives, Riemann Sums, and the Definite Integral.
- **MATH 254 (Multivariable Calculus) Critical Link:**
  - Implicit differentiation is the direct conceptual precursor to multivariable level sets $F(x, y) = c$ and $F(x, y, z) = c$, the Implicit Function Theorem, and constraint gradient equations in Lagrange Multipliers ($\nabla f = \lambda \nabla g$).
  - Locating interior critical points and testing them against closed boundaries via the Closed Interval Method provides the exact algorithmic structure used in MATH 254 for finding absolute extrema of functions $f(x, y)$ on compact regions $D \subset \mathbb{R}^2$.
  - Rolle's Theorem and the Mean Value Theorem establish the theoretical guarantees for conservative vector fields and gradient line integrals ($\int_C \nabla f \cdot d\mathbf{r}$).

---

## 3. Source Documents & Grounding

- **Master Plan Authority:** [`C:\dev\calculus\topics_from_Stewart\handouts_plan.md`](file:///C:/dev/calculus/topics_from_Stewart/handouts_plan.md) (Sections 1–4).
- **Primary Source Notes:** [`C:\dev\calculus\topics_from_Stewart\topics_5.md`](file:///C:/dev/calculus/topics_from_Stewart/topics_5.md) (Sections 5.1–5.5, 6.1–6.3, 9.1–9.6, 10.1–10.4: Implicit Differentiation, Folium of Descartes, Extrema Definitions, Fermat's Theorem, Closed Interval Method, Rolle's Theorem, Mean Value Theorem).
- **Textbook Authority:** Stewart *Calculus: Early Transcendentals* (7th Edition), Sections 2.6, 4.1, 4.2, and Chapter 2/4 Review Quizzes.

---

## 4. Standalone Modern SVG Figures

Copy the following verified SVG figures from `C:\dev\calculus\topics_from_Stewart\figures\` into `<package>/figures/` and embed them into `handout.md`:

1. `sec2_6_figure1_circle_semicircles.svg`: Implicit circle $x^2 + y^2 = 25$ decomposed into explicit top and bottom semicircles $y = \pm\sqrt{25 - x^2}$.
2. `sec2_6_figure2_folium.svg`: Folium of Descartes $x^3 + y^3 = 6xy$ with asymptote $x + y + 2 = 0$.
3. `sec2_6_figure3_folium_branches.svg`: Decomposing the folium into distinct differentiable functional branches.
4. `sec2_6_figure4_folium_tangents.svg`: Tangent lines to the folium, showing horizontal tangent and vertical tangent at the origin.
5. `sec4_1_fig11_cubic_inflection.svg`: Stationary inflection point $f'(c) = 0$ on $y = x^3$ demonstrating that $f'(c) = 0$ is not sufficient for an extremum.
6. `sec4_1_fig12_abs_value_corner.svg`: Absolute minimum at $x = 0$ on $f(x) = |x|$, demonstrating an extremum where the derivative does not exist.
7. `sec4_1_fig13_critical_numbers.svg`: Comprehensive catalog of critical points: local maxima, local minima, stationary inflections, and cusps/corners.
8. `sec4_1_fig_ex8_closed_interval.svg`: Closed Interval Method on $[a, b]$, comparing interior local extrema with boundary endpoint values.
9. `sec4_2_fig1_rolles_theorem_cases.svg`: Rolle's Theorem geometric cases: constant function, interior maximum, and interior minimum.
10. `sec4_2_fig3_mvt_single_tangent.svg`: Mean Value Theorem showing secant chord parallel to tangent line at $c \in \mathopen{]}a, b\mathclose{[}$.
11. `sec4_2_fig4_mvt_multiple_tangents.svg`: Mean Value Theorem showing multiple parallel tangent points $c_1, c_2$.

**Respective Figure Generators:**
- [`C:\dev\calculus\topics_from_Stewart\generate_figures_topics5.py`](file:///C:/dev/calculus/topics_from_Stewart/generate_figures_topics5.py)
- [`C:\dev\calculus\topics_from_Stewart\generate_figures_topics5_part2.py`](file:///C:/dev/calculus/topics_from_Stewart/generate_figures_topics5_part2.py)

---

## 5. Instructional Structure & Pedagogical Content

Interleave concise theoretical principles with 4-stage worked examples:

1. **Implicit Functions and the Chain Rule:**
   - Explicit functions $y = f(x)$ vs implicit relationships $F(x, y) = 0$.
   - Differentiating terms involving $y$: treating $y$ as an unknown differentiable function of $x$ and applying the chain rule:
     $$\frac{d}{dx}[y^n] = n y^{n-1} \frac{dy}{dx}, \quad \frac{d}{dx}[x y] = y + x \frac{dy}{dx}, \quad \frac{d}{dx}[\sin(y)] = \cos(y) \frac{dy}{dx}$$
   - Systematic algebraic procedure: collect all terms containing $\frac{dy}{dx}$ on one side, factor out $\frac{dy}{dx}$, and divide.
2. **Second Implicit Derivatives:**
   - Computing $\frac{d^2 y}{dx^2}$ by differentiating the expression for $\frac{dy}{dx}$ with respect to $x$ via quotient/product rules.
   - Crucial final step: substituting the first-derivative expression for $\frac{dy}{dx}$ to yield $\frac{d^2y}{dx^2}$ in terms of $x$ and $y$ only.
3. **Horizontal and Vertical Tangents on Implicit Curves:**
   - Horizontal tangent lines: $\frac{dy}{dx} = 0$ (numerator equals $0$ with denominator $\ne 0$).
   - Vertical tangent lines: $\frac{dx}{dy} = 0$ or denominator of $\frac{dy}{dx}$ equals $0$ (with numerator $\ne 0$).
   - Singular points / self-intersections where numerator and denominator simultaneously vanish (e.g. at origin of the folium).
4. **Extrema Definitions and the Extreme Value Theorem (EVT):**
   - Absolute (global) maximum and minimum values on a domain $D$.
   - Local (relative) maximum and minimum values.
   - **Extreme Value Theorem (EVT):** If $f$ is continuous on a closed, bounded interval $[a, b]$, then $f$ attains an absolute maximum value $f(c)$ and an absolute minimum value $f(d)$ at some numbers $c, d \in [a, b]$.
   - Counterexamples when hypotheses fail: open interval $(0, 1)$ or discontinuous functions.
5. **Critical Points and Fermat's Theorem:**
   - **Fermat's Theorem:** If $f$ has a local extremum at $c$, and if $f'(c)$ exists, then $f'(c) = 0$.
   - Definition of a **critical number**: A number $c$ in the domain of $f$ such that either $f'(c) = 0$ or $f'(c)$ does not exist.
   - The converse is false: $f'(c) = 0$ does not guarantee an extremum (e.g. $f(x) = x^3$ at $0$).
6. **The Closed Interval Method:**
   - 3-Step Routine to find absolute extrema of a continuous function on $[a, b]$:
     1. Find values of $f$ at all critical numbers of $f$ in the open interval $\mathopen{]}a, b\mathclose{[}$.
     2. Find values of $f$ at the boundary endpoints $a$ and $b$.
     3. The largest value from Steps 1 and 2 is the absolute maximum; the smallest is the absolute minimum.
7. **Rolle's Theorem and the Mean Value Theorem (MVT):**
   - **Rolle's Theorem:** If $f$ is continuous on $[a, b]$, differentiable on $\mathopen{]}a, b\mathclose{[}$, and $f(a) = f(b)$, then there exists $c \in \mathopen{]}a, b\mathclose{[}$ such that $f'(c) = 0$.
   - **Mean Value Theorem:** If $f$ is continuous on $[a, b]$ and differentiable on $\mathopen{]}a, b\mathclose{[}$, then there exists $c \in \mathopen{]}a, b\mathclose{[}$ such that:
     $$f'(c) = \frac{f(b) - f(a)}{b - a} \quad\iff\quad f(b) - f(a) = f'(c)(b - a)$$
   - Applications: proving an equation has exactly one real root, police speed calculation, bounding growth.
8. **Diagnostic Section (`## Mistakes, edge cases & strategies`):**
   Table `| Trap | Correct reasoning | Strategy |` covering:
   - Forgetting the chain factor $\frac{dy}{dx}$ when differentiating $y$-terms implicitly.
   - Forgetting to substitute $\frac{dy}{dx}$ back into the second derivative $\frac{d^2y}{dx^2}$.
   - Assuming that $f'(c) = 0$ guarantees an extremum (omitting the first/second derivative test or inflection check).
   - Omitting boundary endpoints $a$ and $b$ during closed-interval optimization.
   - Applying the Closed Interval Method to a function that has an interior discontinuity (e.g. $1/x$ on $[-1, 2]$).
   - Applying MVT when the function is not differentiable on the entire open interval (e.g. $|x|$ on $[-1, 1]$).

---

## 6. Exercise Progression & MECE Requirements

Author 6 fresh, non-bank exercises under `## Exercises`, ordered strictly from easiest to hardest:

- **Universal Formatting Rules:**
  - Bare sequential headings: `### Q1` through `### Q6`.
  - Every question begins with bold subpart `**1.**`.
  - Never use Markdown ordered lists (`1.`, `2.`).
  - Answer-free, objective, and neutral.
- **Exercise Breakdown:**
  - **Q1 (Implicit Tangent Lines):**
    - Consider the rotated ellipse $x^2 - xy + y^2 = 7$.
    - Subpart **1.** Compute $\frac{dy}{dx}$ by implicit differentiation.
    - Subpart **2.** Find the equation of the tangent line at the point $(2, 3)$.
  - **Q2 (Horizontal and Vertical Tangents & Second Derivative):**
    - Consider the cardiod-like algebraic curve $x^3 + y^3 = 3xy$.
    - Subpart **1.** Determine all coordinates where the curve has a horizontal tangent line.
    - Subpart **2.** Determine all coordinates where the curve has a vertical tangent line.
    - Subpart **3.** Calculate $\frac{d^2y}{dx^2}$ at the point where $x = y \ne 0$ and express the result in simplest terms.
  - **Q3 (Diagnostic Multiple Choice):** 5-option conceptual item (`A)` through `E)`):
    - Subpart **1.** Evaluating four mathematical claims about critical points, EVT, and MVT, identifying which claim is strictly true and diagnosing the exact hypothesis violation in each false option.
  - **Q4 (The Closed Interval Method):**
    - Subpart **1.** Find the absolute maximum and absolute minimum values of $f(x) = 2\cos(x) + \sin(2x)$ on the closed interval $[0, \pi/2]$.
    - Subpart **2.** Find the absolute extrema of $g(x) = x^{2/3}(5 - x)$ on the interval $[-1, 5]$, explicitly accounting for non-differentiable critical points.
  - **Q5 (Rolle's Theorem & MVT Applications):**
    - Subpart **1.** Prove that the cubic equation $2x^3 + 3x - 5 = 0$ has exactly one real root using the IVT for existence and Rolle's Theorem for uniqueness.
    - Subpart **2.** A vehicle passes two toll booths separated by 50 miles in 42 minutes. Use the Mean Value Theorem to prove the driver exceeded the 65 mph speed limit.
  - **Capstone Q6 (Very Hard Applied Transfer Task):**
    - Analyzing the Lemniscate of Bernoulli $(x^2 + y^2)^2 = 2a^2(x^2 - y^2)$ representing an electromagnetic dipole flux line.
    - Compute $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$, find all points of maximum vertical displacement, and apply the Mean Value Theorem along an explicit quadrant loop.

---

## 7. Answer Key Specifications (`answers.md`)

- Title: `Handout 005: Implicit Differentiation, Critical Points, and the Mean Value Theorem — Answer Key`
- Matching `### Q1` through `### Q6` headings under `## Exercises`.
- Every subpart answered with a full Four-Stage derivation box (`>`).
- For Q3 (Multiple Choice):
  - Bold declaration: `**1. Correct answer: X.**`
  - Explanations for all 5 options (`- **A (Incorrect):** ...`), explaining why the correct choice holds and describing the specific hypothesis failure in each incorrect option.
  - No option letters repeated in explanation prose.

---

## 8. Verification & Finalization Pipeline

1. Mathematical derivation re-check with SymPy script.
2. Validate handout structure:
   ```powershell
   python -X utf8 -I C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/validate_handout.py C:/dev/calculus/handouts/005-implicit-differentiation-extrema-and-mvt
   ```
3. Multiple-choice letter balancing and shuffling:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/shuffle_mc_options.py --package C:/dev/calculus/handouts/005-implicit-differentiation-extrema-and-mvt --apply
   ```
4. Render print PDFs (`handout.print.pdf`, `answers.print.pdf`) and visually inspect pages.
5. Check 16-page limit:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/check_page_limit.py C:/dev/calculus/handouts/005-implicit-differentiation-extrema-and-mvt
   ```
6. Package finalization:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/finalize_package.py C:/dev/calculus/handouts/005-implicit-differentiation-extrema-and-mvt
   ```
