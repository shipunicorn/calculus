# Prompt for Handout 002: Limit Laws, Squeeze Theorem, Continuity, and the IVT

Use the `/calculus-create-handout` skill to create a new handout package `002-limit-laws-squeeze-theorem-and-continuity` ("Limit Laws, Squeeze Theorem, Continuity, and the IVT"). Do not create or edit any other handout in this session.

```text
/calculus-create-handout
```

---

## 1. Package Specification

- **Package Number (Fixed):** `002`
- **Target Package Directory:** `C:\dev\calculus\handouts\002-limit-laws-squeeze-theorem-and-continuity\`
- **Action Required:** Create new package using `002` as the package ID.
- **Handout Title:** `Handout 002: Limit Laws, Squeeze Theorem, Continuity, and the IVT`
- **Page Budget:** 12–14 pages for `handout.print.pdf` (Strict limit: $\le 16$ pages). `answers.print.pdf` has no page limit.

---

## 2. Pedagogical Context & MATH 254 Critical Path Alignment

- **Role in Sequence:** Stage 1 (Foundations & Limits, Handout 2 of 7).
- **Prerequisites Assumed:** Handout 001 (`001-functions-transformations-and-limits`): natural domains, function transformations, reading piecewise graphs, and intuitive two-sided and one-sided limits.
- **Subsequent Handout Unlocked:** Handout 003: Tangent Lines, Differentiability, and Rates of Change.
- **MATH 254 (Multivariable Calculus) Critical Link:**
  - Essential foundation for evaluating multivariable limits $\lim_{(x,y) \to (a,b)} f(x,y)$ along distinct approach paths ($y = mx$, $y = kx^2$).
  - Mastering algebraic indeterminate forms ($0/0$) and Squeeze Theorem bounding allows students to establish multivariable limit existence or prove non-existence.
  - The 3-condition continuity definition directly generalizes to continuity of multivariable scalar and vector fields.

---

## 3. Source Documents & Grounding

- **Master Plan Authority:** [`C:\dev\calculus\topics_from_Stewart\handouts_plan.md`](file:///C:/dev/calculus/topics_from_Stewart/handouts_plan.md) (Sections 1–4).
- **Primary Source Notes:**
  - [`C:\dev\calculus\topics_from_Stewart\topics_2.md`](file:///C:/dev/calculus/topics_from_Stewart/topics_2.md) (Sections 1.1–1.7, 2.1–2.5: Limit Laws, algebraic evaluation, Squeeze Theorem, intuitive $\varepsilon$-$\delta$).
  - [`C:\dev\calculus\topics_from_Stewart\topics_3.md`](file:///C:/dev/calculus/topics_from_Stewart/topics_3.md) (Sections 1.1–1.5, 2: Continuity, classification of discontinuities, and the Intermediate Value Theorem).
- **Textbook Authority:** Stewart *Calculus: Early Transcendentals* (7th Edition), Sections 2.3, 2.4, 2.5, and Chapter 2 Review.

---

## 4. Standalone Modern SVG Figures

Copy the following verified SVG figures from `C:\dev\calculus\topics_from_Stewart\figures\` into `<package>/figures/` and embed them into `handout.md`:

1. `sec2_3_figure3_abs_x.svg`: Absolute value split and one-sided limit evaluation at $x = 0$.
2. `sec2_3_figure4_sign_step.svg`: Signum step function showing jump discontinuity at the origin.
3. `sec2_3_figure5_piecewise_corner.svg`: Piecewise continuous curve with sharp corner.
4. `sec2_3_figure7_squeeze_theorem.svg`: Geometric bounding of $g(x)$ between $f(x)$ and $h(x)$.
5. `sec2_3_figure8_squeeze_x2_sin.svg`: Bounding of oscillating $x^2 \sin(1/x)$ between $-x^2$ and $+x^2$.
6. `sec2_3_ex2_graphs_fg.svg`: Reading and combining limits of $f$ and $g$ from coordinate grids.
7. `sec2_4_figures4_5_6_eps_delta_strips.svg`: Intuitive $\varepsilon$-$\delta$ tolerance band challenge model.
8. `sec2_5_figure1_continuity_definition.svg`: Geometric definition of continuity at a number $a$.
9. `sec2_5_figure2_discontinuities_example1.svg`: Graph illustrating removable, jump, and infinite discontinuities.
10. `sec2_5_figure3_example2_discontinuity_types.svg`: Classification catalog of discontinuity types.
11. `sec2_5_figure_ivt.svg`: Intermediate Value Theorem showing guaranteed root crossing $f(c) = 0$ on $[a, b]$.

**Figure Generators:**
- [`C:\dev\calculus\topics_from_Stewart\generate_figures_topics2.py`](file:///C:/dev/calculus/topics_from_Stewart/generate_figures_topics2.py)
- [`C:\dev\calculus\topics_from_Stewart\generate_figures_topics3.py`](file:///C:/dev/calculus/topics_from_Stewart/generate_figures_topics3.py)

**Figure Rules:**
- Page fonts only: `Aptos` for text labels, `"Cascadia Mono"` for numbers, coordinates, and equations.
- Draw order: (1) grid and axes, (2) dashed guides, (3) curves and shaded regions, (4) open/closed markers, (5) label boxes.
- Open (excluded) markers must have white fill, colored stroke, and never be traversed by guides or curves.

---

## 5. Instructional Structure & Pedagogical Content

Interleave concise theoretical principles with 4-stage worked examples:

1. **Limit Laws Catalog:**
   - Sum, difference, constant multiple, product, quotient (with $\lim g(x) \ne 0$), power, and root laws.
   - Direct substitution property for polynomials and rational functions within their natural domains.
2. **Indeterminate Form $0/0$ Strategies:**
   - Algebraic factoring and cancellation of $(x - a)$ factors (with domain caveat $x \ne a$).
   - Conjugate rationalization for radical expressions ($\frac{\sqrt{t+9}-3}{t} \cdot \frac{\sqrt{t+9}+3}{\sqrt{t+9}+3}$).
   - Simplifying compound fractions.
3. **One-Sided Limits & Absolute Value Splits:**
   - Evaluating $\lim_{x \to a^-}$ and $\lim_{x \to a^+}$ for piecewise functions and $|x - a| / (x - a)$.
   - Theorem: $\lim_{x \to a} f(x) = L \iff \lim_{x \to a^-} f(x) = L = \lim_{x \to a^+} f(x)$.
4. **The Squeeze (Sandwich) Theorem:**
   - Theorem statement: If $f(x) \le g(x) \le h(x)$ near $a$ and $\lim f = \lim h = L$, then $\lim g = L$.
   - Bounding oscillating terms: $|\sin(1/x)| \le 1$ and $|\cos(1/x)| \le 1 \implies -x^2 \le x^2 \sin(1/x) \le x^2$.
5. **Precise Intuition ($\varepsilon$-$\delta$ Tolerance Bands):**
   - Geometric understanding of $\varepsilon$ output tolerance creating a $\delta$ input window around $a$.
   - Focus on graphical band estimation without tedious algebraic delta proofs.
6. **Continuity at a Number and on an Interval:**
   - 3-Condition Continuity Test at $x = a$:
     1. $f(a)$ is defined ($a \in \operatorname{dom}(f)$).
     2. $\lim_{x \to a} f(x)$ exists.
     3. $\lim_{x \to a} f(x) = f(a)$.
   - Continuity on intervals: French Bourbaki notation $[a, b]$, $[a, b\mathclose{[}$, $\mathopen{]}a, b\mathclose{[}$.
   - Classification of Discontinuities:
     - Removable (hole): limit exists but $f(a)$ is undefined or $\ne$ limit.
     - Jump: one-sided limits both exist but $\lim_{x \to a^-} f(x) \ne \lim_{x \to a^+} f(x)$.
     - Infinite: one or both one-sided limits blow up to $\pm\infty$ (vertical asymptote).
7. **The Intermediate Value Theorem (IVT):**
   - Theorem statement: If $f$ is continuous on $[a, b]$ and $u$ is between $f(a)$ and $f(b)$, there exists $c \in \mathopen{]}a, b\mathclose{[}$ such that $f(c) = u$.
   - Essential hypotheses: Must be continuous on a closed bounded interval $[a, b]$.
   - Practical application: Root finding ($f(c) = 0$) by detecting sign change $f(a) \cdot f(b) < 0$.
8. **Diagnostic Section (`## Mistakes, edge cases & strategies`):**
   Include an explicit Markdown table: `| Trap | Correct reasoning | Strategy |` covering:
   - Applying the Quotient Law when the denominator limit is $0$.
   - Forgetting that $\sqrt{x^2} = |x|$, causing sign errors in limits as $x \to -\infty$ or near zero.
   - Confusing non-existence of a limit with an indeterminate form $0/0$ that can be simplified.
   - Asserting that a function has a jump discontinuity when one side is unbounded (it is infinite).
   - Applying IVT on an interval containing a discontinuity (e.g. $1/x$ on $[-1, 1]$).
   - Concluding IVT guarantees uniqueness of the root (it guarantees existence, not uniqueness).

---

## 6. Exercise Progression & MECE Requirements

Author 6 fresh, non-bank exercises under `## Exercises`, ordered strictly from easiest to hardest:

- **Universal Formatting Rules:**
  - Bare sequential headings: `### Q1`, `### Q2`, `### Q3`, `### Q4`, `### Q5`, `### Q6`.
  - Every question begins with bold subpart `**1.**`.
  - Never use Markdown ordered lists (`1.`, `2.`).
  - Answer-free, objective, and neutral (no meta-commentary).
- **Exercise Breakdown:**
  - **Q1 (Foundational Calculation):** Algebraic limit evaluation of indeterminate forms $0/0$:
    - Subpart **1.** Factoring quadratic/cubic rational expressions.
    - Subpart **2.** Conjugate rationalization of radical differences.
  - **Q2 (Graphical & One-Sided Limits):** Reading limits from piecewise curves:
    - Subpart **1.** Evaluating left-hand and right-hand limits at partition boundaries.
    - Subpart **2.** Evaluating limits of combinations $[2f(x) - g(x)^2]$ using Limit Laws from graphs.
  - **Q3 (Diagnostic Multiple Choice):** 5-option conceptual item (`A)` through `E)`):
    - Subpart **1.** Distinguishing valid vs invalid applications of the Squeeze Theorem and continuity hypotheses. Distractors must target named traps from the diagnostic table.
  - **Q4 (Discontinuity Classification & Parameter Tuning):**
    - Subpart **1.** Classifying all points of discontinuity of a given rational/piecewise function as removable, jump, or infinite.
    - Subpart **2.** Determining constants $k, m$ so that a piecewise-defined function is continuous everywhere on $\mathbb{R}$.
  - **Q5 (Intermediate Value Theorem Application):**
    - Subpart **1.** Verifying IVT hypotheses and proving that a transcendental polynomial equation has at least one real root in a specified interval.
    - Subpart **2.** Using interval bisection to narrow the root to a subinterval of width $< 0.25$.
  - **Capstone Q6 (Very Hard Applied Transfer Task):**
    - Modeling an engineering/physics phenomenon with a threshold transition (e.g. electrostatic potential or fluid flow across a semi-permeable membrane with piecewise resistance).
    - Requires one-sided limit evaluation, tuning a barrier parameter to remove an energy discontinuity, and applying the IVT to prove the existence of an equilibrium operating point.

---

## 7. Answer Key Specifications (`answers.md`)

- Title: `Handout 002: Limit Laws, Squeeze Theorem, Continuity, and the IVT — Answer Key`
- Matching `### Q1` through `### Q6` headings under `## Exercises`.
- Every subpart answered with a full Four-Stage derivation box (`>`).
- For Q3 (Multiple Choice):
  - Bold declaration: `**1. Correct answer: X.**`
  - Individual explanations for all 5 options (`- **A (Incorrect):** ...`), explaining why the correct option holds and the exact mathematical error in each distractor.
  - Do not mention option letters inside the explanation prose.

---

## 8. Verification & Finalization Pipeline

1. Mathematical derivation check with SymPy script.
2. Package structure validation:
   ```powershell
   python -X utf8 -I C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/validate_handout.py C:/dev/calculus/handouts/002-limit-laws-squeeze-theorem-and-continuity
   ```
3. Multiple-choice letter balancing and shuffling:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/shuffle_mc_options.py --package C:/dev/calculus/handouts/002-limit-laws-squeeze-theorem-and-continuity --apply
   ```
4. Render print PDFs (`handout.print.pdf`, `answers.print.pdf`) and inspect every page.
5. Check 16-page limit:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/check_page_limit.py C:/dev/calculus/handouts/002-limit-laws-squeeze-theorem-and-continuity
   ```
6. Final cleanup:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/finalize_package.py C:/dev/calculus/handouts/002-limit-laws-squeeze-theorem-and-continuity
   ```
