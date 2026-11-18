# Prompt for Handout 003: Tangent Lines, Differentiability, and Rates of Change

Use the `/calculus-create-handout` skill to create a new handout package `003-tangent-lines-differentiability-and-rates` ("Tangent Lines, Differentiability, and Rates of Change"). Do not create or edit any other handout in this session.

```text
/calculus-create-handout
```

---

## 1. Package Specification

- **Package Number (Fixed):** `003`
- **Target Package Directory:** `C:\dev\calculus\handouts\003-tangent-lines-differentiability-and-rates\`
- **Action Required:** Create new package using `003` as the package ID.
- **Handout Title:** `Handout 003: Tangent Lines, Differentiability, and Rates of Change`
- **Page Budget:** 11–13 pages for `handout.print.pdf` (Strict limit: $\le 16$ pages). `answers.print.pdf` has no page limit.

---

## 2. Pedagogical Context & MATH 254 Critical Path Alignment

- **Role in Sequence:** Stage 2 (The Derivative & Differentiation Fluency, Handout 3 of 7).
- **Prerequisites Assumed:**
  - Handout 001: Functions, coordinate graphs, domain restrictions.
  - Handout 002: Limit laws, indeterminate form evaluation ($0/0$), one-sided limits, continuity definitions.
- **Subsequent Handout Unlocked:** Handout 004: Differentiation Rules, Higher Derivatives, and Graphical Analysis.
- **MATH 254 (Multivariable Calculus) Critical Link:**
  - The limit definition of the derivative via difference quotients provides the precise geometric template for partial derivatives:
    $$f_x(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h}$$
  - The tangent line equation $y - y_0 = f'(x_0)(x - x_0)$ directly extends to the tangent plane equation in 3D:
    $$z - z_0 = f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$$
  - Linear approximation $L(x) \approx f(a) + f'(a)(x - a)$ generalizes to the total differential $df = f_x dx + f_y dy$ and linear approximations $L(x, y)$ in multivariable calculus.

---

## 3. Source Documents & Grounding

- **Master Plan Authority:** [`C:\dev\calculus\topics_from_Stewart\handouts_plan.md`](file:///C:/dev/calculus/topics_from_Stewart/handouts_plan.md) (Sections 1–4).
- **Primary Source Notes:** [`C:\dev\calculus\topics_from_Stewart\topics_4.md`](file:///C:/dev/calculus/topics_from_Stewart/topics_4.md) (Sections 1.1–1.3, 2.1–2.3, 3.1–3.2: Tangent Lines, The Derivative at a Point, Differentiability, Failure Modes, Kinematics).
- **Textbook Authority:** Stewart *Calculus: Early Transcendentals* (7th Edition), Sections 2.7 and 2.8.

---

## 4. Standalone Modern SVG Figures

Copy the following verified SVG figures from `C:\dev\calculus\topics_from_Stewart\figures\` into `<package>/figures/` and embed them into `handout.md`:

1. `sec2_7_figure_parabola_tangent.svg`: Secant chord converging to the tangent line at $P(1, 1)$ on $y = x^2$ as $Q \to P$.
2. `sec2_7_figure4_hyperbola_tangent.svg`: Tangent line slope calculation on the reciprocal curve $y = 3/x$.
3. `sec2_7_exercise12_runners.svg`: Position vs time graph comparing two runners (average vs instantaneous rates of change).
4. `sec2_8_figure5_abs_derivative.svg`: Non-differentiability at the sharp corner of $f(x) = |x|$ at $x = 0$ (one-sided slopes $-1$ vs $+1$).
5. `sec2_8_figure7_non_differentiable.svg`: Complete geometric taxonomy of differentiability failure modes: (a) corner, (b) cusp, (c) vertical tangent, (d) jump discontinuity.

**Respective Figure Generator:** [`C:\dev\calculus\topics_from_Stewart\generate_figures_topics4.py`](file:///C:/dev/calculus/topics_from_Stewart/generate_figures_topics4.py).

**Figure Quality Rules:**
- Page fonts: `Aptos` for text labels, `"Cascadia Mono"` for equations and numerical coordinates.
- Correct draw order: grid/axes $\to$ dashed drop lines $\to$ function curves and tangents $\to$ open/closed points $\to$ text labels.
- Never use ASCII or text-block diagrams.

---

## 5. Instructional Structure & Pedagogical Content

Interleave concise foundational theory with 4-stage worked examples:

1. **The Tangent Line and Secant Slopes:**
   - The secant slope between $P(a, f(a))$ and nearby $Q(x, f(x))$: $m_{PQ} = \frac{f(x) - f(a)}{x - a}$.
   - The tangent line slope as the limiting value: $m = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$.
   - Alternative increment formulation ($x = a + h$ with $h \to 0$):
     $$m = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$
2. **The Derivative at a Point and Linear Approximation:**
   - Definition of $f'(a)$.
   - Point-slope form of the tangent line: $y - f(a) = f'(a)(x - a)$.
   - The linearization / linear approximation function: $L(x) = f(a) + f'(a)(x - a)$.
3. **The Derivative as a Function:**
   - Defining $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$.
   - Domain of the derivative: $\operatorname{dom}(f') \subseteq \operatorname{dom}(f)$.
4. **Differentiability vs Continuity:**
   - **Theorem:** If $f$ is differentiable at $a$, then $f$ is continuous at $a$.
   - Proof intuition via $\lim_{x \to a} [f(x) - f(a)] = \lim_{x \to a} \left[\frac{f(x)-f(a)}{x-a} \cdot (x-a)\right] = f'(a) \cdot 0 = 0$.
   - **Crucial Warning (Converse is FALSE):** Continuity does not imply differentiability. Canonical counterexample: $f(x) = |x|$ at $x = 0$ is continuous everywhere but not differentiable at $x = 0$.
5. **Taxonomy of Differentiability Failure Modes:**
   - **Sharp Corner:** Left-hand and right-hand difference quotients approach different finite limits ($\lim_{h \to 0^-} \ne \lim_{h \to 0^+}$).
   - **Cusp:** Slopes blow up to infinite values with opposite signs ($\to -\infty$ on one side, $\to +\infty$ on the other).
   - **Vertical Tangent:** Slopes blow up to $+\infty$ or $-\infty$ on both sides ($f'(x) \to \pm\infty$, e.g. $\sqrt[3]{x}$ at $0$). The curve is continuous and has a vertical tangent line $x = 0$, but is NOT differentiable.
   - **Discontinuity:** Fails continuity, hence automatically fails differentiability.
6. **Physical & Kinematic Rates of Change:**
   - Position function $s(t)$.
   - Average velocity on $[t_1, t_2]$: $v_{\text{avg}} = \frac{s(t_2) - s(t_1)}{t_2 - t_1}$.
   - Instantaneous velocity: $v(t) = s'(t) = \lim_{\Delta t \to 0} \frac{s(t+\Delta t) - s(t)}{\Delta t}$.
   - Speed vs velocity: Speed is the scalar magnitude $|v(t)|$.
   - Acceleration: $a(t) = v'(t) = s''(t)$.
7. **Diagnostic Section (`## Mistakes, edge cases & strategies`):**
   Table `| Trap | Correct reasoning | Strategy |` covering:
   - Confusing average rate of change $\frac{\Delta y}{\Delta x}$ with instantaneous rate $\frac{dy}{dx}$.
   - Assuming that because a function is continuous at $a$, it must be differentiable at $a$.
   - Confusing a vertical tangent line (which exists geometrically: $x = a$) with differentiability (which does not exist analytically: $m = \pm\infty$).
   - Dropping the limit notation $\lim_{h \to 0}$ during intermediate difference quotient algebra before evaluating $h = 0$.
   - Failing to test one-sided difference quotients when checking differentiability of piecewise functions at boundary transitions.

---

## 6. Exercise Progression & MECE Requirements

Author 6 fresh, non-bank exercises under `## Exercises`, ordered strictly from easiest to hardest:

- **Universal Formatting Rules:**
  - Bare sequential headings: `### Q1` through `### Q6`.
  - Every question begins with bold subpart `**1.**`.
  - Never use Markdown ordered lists (`1.`, `2.`).
  - Strict answer-free objectivity.
- **Exercise Breakdown:**
  - **Q1 (Foundational Difference Quotients):**
    - Subpart **1.** Compute $f'(a)$ from the limit definition using $\lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$ for a rational function $f(x) = \frac{2}{x+3}$ at $a = 1$.
    - Subpart **2.** Compute $f'(x)$ as a function from the limit definition for a radical function $f(x) = \sqrt{3x + 1}$.
  - **Q2 (Tangent Lines & Linear Approximation):**
    - Subpart **1.** Determine the exact equation of the tangent line to $y = x^3 - 4x + 1$ at $(2, 1)$.
    - Subpart **2.** Construct the linear approximation $L(x)$ at $a = 2$ and use it to estimate $f(2.03)$ and $f(1.97)$, comparing against the true function values.
  - **Q3 (Diagnostic Multiple Choice):** 5-option conceptual item (`A)` through `E)`):
    - Subpart **1.** Identifying the exact geometric failure mode (corner, cusp, vertical tangent, or jump discontinuity) for a given curve at $x = 0$, explicitly testing misconceptions from the diagnostic table.
  - **Q4 (Kinematic Motion & Rate Interpretation):**
    - A particle moves along a coordinate axis with position $s(t) = 2t^3 - 9t^2 + 12t$ ($t \ge 0$, meters and seconds).
    - Subpart **1.** Find the velocity $v(t)$ and acceleration $a(t)$.
    - Subpart **2.** Determine all time intervals when the particle is moving in the positive direction, moving in the negative direction, and temporarily at rest.
    - Subpart **3.** Calculate the total distance traveled during the time interval $[0, 3]$ (distinguishing net displacement from total distance).
  - **Q5 (Piecewise Differentiability & Parameter Tuning):**
    - Let $f(x)$ be defined by:
      $$f(x) = \begin{cases} x^2 + 2x, & x \le 1 \\ m x + b, & x > 1 \end{cases}$$
    - Subpart **1.** Determine the unique values of constants $m$ and $b$ that make $f(x)$ differentiable everywhere on $\mathbb{R}$.
    - Subpart **2.** Formulate both one-sided difference quotients at $x = 1$ to prove differentiability rigorously.
  - **Capstone Q6 (Very Hard Applied Transfer Task):**
    - A multi-stage aerospace launch ascent where altitude $y(t)$ transitions between an initial rocket burn phase $y_1(t) = c t^2$ and a sustained aerodynamic flight phase $y_2(t) = k \sqrt{t - t_0} + h_0$.
    - Requires matching position and velocity across the staging boundary to ensure smooth physical acceleration, establishing tangent lines, and calculating maximum speed and deceleration points.

---

## 7. Answer Key Specifications (`answers.md`)

- Title: `Handout 003: Tangent Lines, Differentiability, and Rates of Change — Answer Key`
- Matching `### Q1` through `### Q6` headings under `## Exercises`.
- Every subpart answered with a full Four-Stage derivation box (`>`).
- For Q3 (Multiple Choice):
  - Bold declaration: `**1. Correct answer: X.**`
  - Explanations for all 5 options (`- **A (Incorrect):** ...`), explaining why the correct choice is valid and the specific misconception behind each incorrect distractor.
  - No option letters repeated inside the explanation prose.

---

## 8. Verification & Finalization Pipeline

1. Independently verify all derivations using a SymPy script.
2. Validate handout structure:
   ```powershell
   python -X utf8 -I C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/validate_handout.py C:/dev/calculus/handouts/003-tangent-lines-differentiability-and-rates
   ```
3. Balance and shuffle multiple-choice letters:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/shuffle_mc_options.py --package C:/dev/calculus/handouts/003-tangent-lines-differentiability-and-rates --apply
   ```
4. Render print PDFs and visually inspect pages:
   - `handout.print.pdf` ($\le 16$ pages)
   - `answers.print.pdf`
5. Verify page count limits:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/check_page_limit.py C:/dev/calculus/handouts/003-tangent-lines-differentiability-and-rates
   ```
6. Package finalization:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/finalize_package.py C:/dev/calculus/handouts/003-tangent-lines-differentiability-and-rates
   ```
