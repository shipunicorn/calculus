# Prompt for Handout 004: Differentiation Rules, Higher Derivatives, and Graphical Analysis

Use the `/calculus-create-handout` skill to update, renumber, and expand the existing handout package into `004-differentiation-rules-and-graphical-analysis` ("Differentiation Rules, Higher Derivatives, and Graphical Analysis"). Do not create or edit any other handout in this session.

```text
/calculus-create-handout
```

---

## 1. Package Specification & Directory Migration

- **Package Number (Fixed):** `004`
- **Target Package Directory:** `C:\dev\calculus\handouts\004-differentiation-rules-and-graphical-analysis\`
- **Source Existing Package:** `C:\dev\calculus\handouts\001-derivative-rules-refresher\`
- **Action Required:**
  1. Inspect existing directory `C:\dev\calculus\handouts\001-derivative-rules-refresher\` using `ls` / `Get-ChildItem`.
  2. Following project file-safety rules (`mv` only, verify first, zero `rm -rf`), rename the existing directory to `004-differentiation-rules-and-graphical-analysis`.
  3. Update `handout.md` YAML front matter:
     ```markdown
     ---
     title: "Handout 004: Differentiation Rules, Higher Derivatives, and Graphical Analysis"
     ---
     ```
  4. Update top-level heading: `# 004: Differentiation Rules, Higher Derivatives, and Graphical Analysis`.
  5. Update `answers.md` YAML front matter and top heading:
     ```markdown
     ---
     title: "Handout 004: Differentiation Rules, Higher Derivatives, and Graphical Analysis — Answer Key"
     ---

     # 004: Differentiation Rules, Higher Derivatives, and Graphical Analysis — Answer Key
     ```
  6. Expand the existing text by integrating **Graphical Derivative Analysis, Curve Matching ($f, f', f''$), and Evaluating Derivatives of Compositions and Products directly from Graphs** as specified below.
- **Page Budget:** 13–15 pages for `handout.print.pdf` (Strict limit: $\le 16$ pages). `answers.print.pdf` has no page limit.

---

## 2. Pedagogical Context & MATH 254 Critical Path Alignment

- **Role in Sequence:** Stage 2 (The Derivative & Differentiation Fluency, Handout 4 of 7).
- **Prerequisites Assumed:**
  - Handout 001: Functions, transformations, domain restrictions.
  - Handout 002: Limits and continuity.
  - Handout 003: Tangent line definitions, difference quotients, differentiability failure modes.
- **Subsequent Handout Unlocked:** Handout 005: Implicit Differentiation, Critical Points, and the Mean Value Theorem.
- **MATH 254 (Multivariable Calculus) Critical Link:**
  - Fast, error-free single-variable differentiation fluency is non-negotiable for computing partial derivatives ($\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}$) and directional derivatives ($\nabla f \cdot \mathbf{u}$).
  - Mastering the Chain Rule with nested structures is the direct conceptual prerequisite for the Multivariable Chain Rule (the backpropagation engine across neural networks and gradient optimization).
  - Graphical slope matching ($f, f', f''$) builds spatial intuition for identifying local extrema and saddle points on multivariable surfaces $z = f(x, y)$ using the Hessian determinant $D = f_{xx}f_{yy} - (f_{xy})^2$.

---

## 3. Source Documents & Grounding

- **Master Plan Authority:** [`C:\dev\calculus\topics_from_Stewart\handouts_plan.md`](file:///C:/dev/calculus/topics_from_Stewart/handouts_plan.md) (Sections 1–4).
- **Existing Handout Text:** `C:\dev\calculus\handouts\001-derivative-rules-refresher\handout.md`.
- **Primary Source Notes:** [`C:\dev\calculus\topics_from_Stewart\topics_5.md`](file:///C:/dev/calculus/topics_from_Stewart/topics_5.md) (Sections 1.1–1.3, 2.1–2.3, 3.1–3.2, 4.1–4.5, 7, 8.1–8.3: Higher Derivatives, Graphical Slope Estimation, Derivative Matching, Product/Quotient/Chain Rule from Graphs).
- **Textbook Authority:** Stewart *Calculus: Early Transcendentals* (7th Edition), Sections 2.2, 2.4, 2.5, and Chapter 2 Review.

---

## 4. Standalone Modern SVG Figures

Create `<package>/figures/` if missing, copy the following verified SVG figures from `C:\dev\calculus\topics_from_Stewart\figures\` into `<package>/figures/`, and embed them into `handout.md`:

1. `sec2_2_figure10_cubic_derivatives.svg`: Interplay between $f(x)$, $f'(x)$, and $f''(x)$ on a cubic polynomial curve.
2. `sec2_2_ex1_grid.svg`: Reading coordinate points and estimating tangent slopes on a grid.
3. `sec2_2_ex2_grid.svg`: Estimating instantaneous rates of change on an asymmetric curve.
4. `sec2_2_ex3_matching.svg`: Matching 4 curves ($a, b, c, d$) with their respective first derivatives.
5. `sec2_4_ex72_grid.svg`: Evaluating product and quotient derivatives $[f \cdot g]'(x)$ and $[f / g]'(x)$ from graphs.
6. `sec2_5_ex65_grid.svg`: Evaluating composite derivatives $[f \circ g]'(x) = f'(g(x))g'(x)$ from piecewise linear graphs.
7. `sec2_5_ex66_grid.svg`: Evaluating nested chain rule derivatives from graphical coordinate curves.

**Respective Figure Generator:** [`C:\dev\calculus\topics_from_Stewart\generate_figures_topics5.py`](file:///C:/dev/calculus/topics_from_Stewart/generate_figures_topics5.py).

---

## 5. Instructional Structure & Pedagogical Content

Interleave concise computational catalogs with graphical analysis and 4-stage worked examples:

1. **Fundamental Operational Rules:**
   - Power Rule: $\frac{d}{dx} x^n = n x^{n-1}$ for any real $n$.
   - Constant Multiple and Sum/Difference Rules.
   - Product Rule: $[f \cdot g]' = f' g + f g'$.
   - Quotient Rule: $[\frac{f}{g}]' = \frac{g f' - f g'}{g^2}$ (mnemonic: $\frac{\text{Lo}\,d\text{Hi} - \text{Hi}\,d\text{Lo}}{\text{Lo}^2}$).
   - Reciprocal Rule: $[\frac{1}{g}]' = -\frac{g'}{g^2}$.
2. **The Chain Rule & Transcendental Derivatives:**
   - Chain Rule: $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$.
   - Exponential derivatives: $\frac{d}{dx} e^x = e^x$, $\frac{d}{dx} a^x = a^x \ln a$.
   - Logarithmic derivatives: $\frac{d}{dx} \ln|x| = \frac{1}{x}$, $\frac{d}{dx} \log_a x = \frac{1}{x \ln a}$.
   - Trigonometric derivatives: $\sin \to \cos$, $\cos \to -\sin$, $\tan \to \sec^2$, $\sec \to \sec\tan$, $\csc \to -\csc\cot$, $\cot \to -\csc^2$.
   - Inverse trigonometric derivatives: $\arcsin x \to \frac{1}{\sqrt{1-x^2}}$, $\arctan x \to \frac{1}{1+x^2}$.
3. **Higher-Order Derivatives & Physical Interpretations:**
   - Second and third derivatives: $f''(x), f'''(x)$, Leibniz notation $\frac{d^2y}{dx^2}, \frac{d^3y}{dx^3}$.
   - Concavity: $f'' > 0$ concave upward (slopes increasing), $f'' < 0$ concave downward (slopes decreasing).
   - Physical hierarchy: position $s(t) \to$ velocity $v(t) = s'(t) \to$ acceleration $a(t) = s''(t) \to$ jerk $j(t) = s'''(t)$.
4. **Graphical Derivative Analysis & Slope Reading:**
   - Estimating derivative values $f'(x_0)$ from grid curves by reading rise over run on tangent segments.
   - Identifying where $f'(x) = 0$ (horizontal tangents / peaks / valleys).
   - Identifying where $f'(x) > 0$ (rising) and $f'(x) < 0$ (falling).
   - Matching a set of curves with their derivative curves: tracking zero-crossings of $f'$ matching peaks/troughs of $f$.
5. **Evaluating Product, Quotient, and Composite Derivatives from Graphs:**
   - Computing $u'(x)$ when $u(x) = f(x)g(x)$ or $v(x) = f(g(x))$ using values and slopes read directly from piecewise linear or curved graphs without closed-form formulas.
6. **Diagnostic Section (`## Mistakes, edge cases & strategies`):**
   Table `| Trap | Correct reasoning | Strategy |` covering:
   - Applying product rule as $(fg)' = f'g'$ (missing cross terms).
   - Reversing the numerator order in the quotient rule: $(f/g)' \ne (fg' - f'g)/g^2$.
   - Forgetting the inner chain factor $g'(x)$ in composite functions like $\sin(x^3) \to \cos(x^3) \cdot 3x^2$.
   - Confusing power rules with exponential rules: $\frac{d}{dx} 2^x \ne x 2^{x-1}$; it is $2^x \ln 2$.
   - Confusing $(\sin x)^{-1} = \csc x$ with $\arcsin x = \sin^{-1} x$.
   - Misreading graphical slope zero-crossings when matching $f$ and $f'$.

---

## 6. Exercise Progression & MECE Requirements

Author 6 fresh, non-bank exercises under `## Exercises`, ordered strictly from easiest to hardest:

- **Universal Formatting Rules:**
  - Bare sequential headings: `### Q1` through `### Q6`.
  - Every question begins with bold subpart `**1.**`.
  - Never use Markdown ordered lists (`1.`, `2.`).
  - Answer-free, objective, and neutral.
- **Exercise Breakdown:**
  - **Q1 (Operational Differentiation Fluency):**
    - Subpart **1.** Compute $f'(x)$ for a combination of power, exponential, and trig terms requiring algebraic preparation first: $f(x) = \frac{x^3 - 4\sqrt{x}}{x} + 3e^{2x}$.
    - Subpart **2.** Compute $\frac{dy}{dx}$ for a quotient with embedded chain rule: $y = \frac{\cos(3x)}{1 + \sin^2(x)}$.
  - **Q2 (Graphical Derivative Estimation & Curve Matching):**
    - Subpart **1.** Given a grid-based plot of $y = f(x)$, estimate $f'(-2), f'(0), f'(3)$ by constructing tangent chords.
    - Subpart **2.** Given four curves labeled $a, b, c, d$ on a single axis, identify which curve is the position $s(t)$, velocity $v(t)$, acceleration $a(t)$, and jerk $j(t)$, with rigorous justification based on zero-crossings and extrema.
  - **Q3 (Diagnostic Multiple Choice):** 5-option conceptual item (`A)` through `E)`):
    - Subpart **1.** Identifying the correct derivative of a deeply nested transcendental composition (e.g. $\ln(\arctan(\sqrt{x^2 + 1}))$), with distractors capturing dropped inner derivatives, power-rule confusions, and quotient sign inversions.
  - **Q4 (Evaluating Derivatives from Piecewise Graphs):**
    - Using embedded SVG graphs of functions $f$ and $g$:
      - Subpart **1.** Evaluate $h'(2)$ where $h(x) = f(x)g(x)$.
      - Subpart **2.** Evaluate $k'(1)$ where $k(x) = \frac{f(x)}{g(x)}$.
      - Subpart **3.** Evaluate $w'(3)$ where $w(x) = f(g(x))$.
  - **Q5 (Higher-Order Derivatives & Kinematics):**
    - A damped mechanical oscillator has position function $s(t) = e^{-t/2} \cos(2t)$ ($t \ge 0$).
    - Subpart **1.** Find the velocity $v(t)$ and acceleration $a(t)$ in exact factored form.
    - Subpart **2.** Determine the exact values of $t$ in $[0, \pi]$ where the acceleration is zero.
  - **Capstone Q6 (Very Hard Applied Transfer Task):**
    - Pharmacokinetic drug absorption model: plasma concentration is governed by the surge function $C(t) = A t e^{-k t}$ with clearance rate adjustment.
    - Calculate first and second derivatives, determine the time of maximum concentration ($t_{\max}$), find the inflection point of most rapid clearance decline, and verify that $C(t)$ satisfies the second-order differential equation $C''(t) + 2k C'(t) + k^2 C(t) = 0$.

---

## 7. Answer Key Specifications (`answers.md`)

- Title: `Handout 004: Differentiation Rules, Higher Derivatives, and Graphical Analysis — Answer Key`
- Matching `### Q1` through `### Q6` headings under `## Exercises`.
- Every subpart answered with a full Four-Stage derivation box (`>`).
- For Q3 (Multiple Choice):
  - Bold declaration: `**1. Correct answer: X.**`
  - Explanations for all 5 options (`- **A (Incorrect):** ...`), explaining why the correct choice is valid and detailing the exact error in each distractor.
  - No option letters repeated in the explanation prose.

---

## 8. Verification & Finalization Pipeline

1. Mathematical derivation re-check with SymPy.
2. Validate handout structure:
   ```powershell
   python -X utf8 -I C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/validate_handout.py C:/dev/calculus/handouts/004-differentiation-rules-and-graphical-analysis
   ```
3. Multiple-choice letter balancing and shuffling:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/shuffle_mc_options.py --package C:/dev/calculus/handouts/004-differentiation-rules-and-graphical-analysis --apply
   ```
4. Render print PDFs (`handout.print.pdf`, `answers.print.pdf`) and visually inspect pages.
5. Check 16-page limit:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/check_page_limit.py C:/dev/calculus/handouts/004-differentiation-rules-and-graphical-analysis
   ```
6. Package finalization:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/finalize_package.py C:/dev/calculus/handouts/004-differentiation-rules-and-graphical-analysis
   ```
