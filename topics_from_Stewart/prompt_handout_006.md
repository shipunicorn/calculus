# Prompt for Handout 006: Applied Optimization and Economic Models

Use the `/calculus-create-handout` skill to create a new handout package `006-applied-optimization-and-economic-models` ("Applied Optimization and Economic Models"). Do not create or edit any other handout in this session.

```text
/calculus-create-handout
```

---

## 1. Package Specification

- **Package Number (Fixed):** `006`
- **Target Package Directory:** `C:\dev\calculus\handouts\006-applied-optimization-and-economic-models\`
- **Action Required:** Create new package using `006` as the package ID.
- **Handout Title:** `Handout 006: Applied Optimization and Economic Models`
- **Page Budget:** 12–14 pages for `handout.print.pdf` (Strict limit: $\le 16$ pages). `answers.print.pdf` has no page limit.

---

## 2. Pedagogical Context & MATH 254 Critical Path Alignment

- **Role in Sequence:** Stage 3 (Applied Optimization & Integration Foundations, Handout 6 of 7).
- **Prerequisites Assumed:**
  - Handout 004: Differentiation rules and operational fluency.
  - Handout 005: Critical points, Fermat's Theorem, Extreme Value Theorem, and the Closed Interval Method.
- **Subsequent Handout Unlocked:** Handout 007: Antiderivatives, Riemann Sums, and the Definite Integral.
- **MATH 254 (Multivariable Calculus) Critical Link:**
  - Establishes the modeling discipline of identifying primary objective functions subject to geometric and physical constraints, which directly sets up **Constrained Optimization via Lagrange Multipliers** ($\nabla f = \lambda \nabla g$ or $\nabla f = \lambda \nabla g + \mu \nabla h$).
  - Analyzing feasible physical boundaries $[a, b]$ provides the prerequisite mindset for evaluating extreme values on closed, bounded boundary curves $\partial D$ in multivariable calculus.

---

## 3. Source Documents & Grounding

- **Master Plan Authority:** [`C:\dev\calculus\topics_from_Stewart\handouts_plan.md`](file:///C:/dev/calculus/topics_from_Stewart/handouts_plan.md) (Sections 1–4).
- **Primary Source Notes:** [`C:\dev\calculus\topics_from_Stewart\topics_6.md`](file:///C:/dev/calculus/topics_from_Stewart/topics_6.md) (Sections 1.1–1.2, 2.1–2.3, 3.1–3.7: Optimization Problems, Six-Step Strategy, Classic Configurations, Business/Economics Applications, Marginal Analysis).
- **Textbook Authority:** Stewart *Calculus: Early Transcendentals* (7th Edition), Section 3.7 and Chapter 4 Review.

---

## 4. Standalone Modern SVG Figures

Copy the following verified SVG figures from `C:\dev\calculus\topics_from_Stewart\figures\` into `<package>/figures/` and embed them into `handout.md`:

1. `sec3_7_fig1_fencing_cases.svg`: Rectangular river enclosure showing why distinct aspect ratios yield different enclosed areas for a fixed fencing perimeter.
2. `sec3_7_fig2_fencing_general.svg`: General rectangular pasture along a riverbank with variable dimensions $x$ and $y$.
3. `sec3_7_ex11_four_pens.svg`: Multi-compartment agricultural fencing configuration with internal dividing walls.
4. `sec3_7_ex35_wire_shapes.svg`: Wire-cutting optimization problem: cutting a wire of length $L$ into a circle and a square (demonstrating boundary vs interior extrema).
5. `sec3_7_ex56_tangent_triangle.svg`: Geometric optimization: minimizing the area of a right triangle formed by coordinate axes and a tangent line to a curve.

**Respective Figure Generator:** [`C:\dev\calculus\topics_from_Stewart\generate_figures_topics6.py`](file:///C:/dev/calculus/topics_from_Stewart/generate_figures_topics6.py).

**Figure Quality Standards:**
- Page fonts: `Aptos` for text labels, `"Cascadia Mono"` for numbers, equations, and coordinates.
- Draw order: grid/axes $\to$ dashed guides $\to$ bounding curves $\to$ shaded geometric regions $\to$ markers $\to$ labels.
- Standalone SVGs only; no ASCII or Unicode text graphs.

---

## 5. Instructional Structure & Pedagogical Content

Interleave concise theoretical principles with 4-stage worked examples:

1. **The Six-Step Applied Optimization Procedure:**
   - **Step 1 (Understand the Scenario):** Identify the unknown target, given quantities, and restrictive conditions.
   - **Step 2 (Draw and Label a Diagram):** Sketch the geometric/physical arrangement and label all fixed constants and variable dimensions.
   - **Step 3 (Introduce Notation):** Assign a primary symbol to the objective quantity to maximize/minimize ($Q, A, V, C, P$). Assign symbols to auxiliary variables ($x, y, r, h, \theta$).
   - **Step 4 (Formulate the Objective Function):** Write an equation expressing $Q$ in terms of the variables: $Q = f(x, y)$.
   - **Step 5 (Eliminate Auxiliary Variables and Establish the Feasible Domain):** Use constraint equations (e.g. perimeter, surface area, volume, Pythagoras) to express $Q$ as a single-variable function $Q = f(x)$. Explicitly define the closed feasible domain $[a, b]$ based on non-negativity and physical limits.
   - **Step 6 (Locate the Absolute Extremum):** Apply the Closed Interval Method or the First/Second Derivative Test. Conclude with an interpretation checking units and feasible boundary points.
2. **Classic Geometric & Physical Paradigms:**
   - **Enclosure Problems:** Multi-pen pastures, differing cost per linear foot for exterior vs interior fencing, utilizing existing natural boundaries (rivers, walls).
   - **Open-Top and Closed Containers:** Maximizing volume for a given sheet metal area; minimizing surface area for a specified capacity.
   - **Distance Minimization & The Squared-Distance Trick:** Finding the point on a curve $y = f(x)$ closest to a point $(x_0, y_0)$. Minimizing $D = \sqrt{(x-x_0)^2 + (y-y_0)^2}$ is equivalent to minimizing $S = D^2$, eliminating messy square root derivatives.
   - **The Wire-Cutting Paradox (Interior vs Boundary Extrema):** Cutting a wire into a circle and a square to maximize or minimize total area. Show that the interior critical point yields the *minimum* area, while the *maximum* area occurs at the boundary (bending the entire wire into a circle)!
3. **Business & Economic Optimization:**
   - Total Cost function $C(x)$, Marginal Cost $C'(x)$, Average Cost $c(x) = \frac{C(x)}{x}$.
   - Demand (price) function $p(x)$, Total Revenue function $R(x) = x \cdot p(x)$, Marginal Revenue $R'(x) = p(x) + x p'(x)$.
   - Total Profit function $P(x) = R(x) - C(x)$, Marginal Profit $P'(x) = R'(x) - C'(x)$.
   - **Golden Rule of Profit Maximization:** $P'(x) = 0 \iff R'(x) = C'(x)$ ($MR = MC$).
   - **Minimizing Average Cost:** $\frac{d}{dx}[c(x)] = 0 \iff C'(x) = c(x)$ (Marginal Cost equals Average Cost at the minimum efficient scale).
4. **Diagnostic Section (`## Mistakes, edge cases & strategies`):**
   Table `| Trap | Correct reasoning | Strategy |` covering:
   - Forgetting to eliminate auxiliary variables before differentiating the objective function.
   - Failing to define the feasible physical domain (e.g. allowing lengths or dimensions to be negative).
   - Omitting boundary endpoints (failing to recognize when an absolute extremum occurs at the edge of the feasible domain, as in wire-cutting).
   - Confusing a local minimum with an absolute maximum by neglecting the Second Derivative Test or endpoint comparison.
   - Forgetting to multiply unit price by quantity $x$ when setting up total revenue $R(x) = x \cdot p(x)$.
   - Misapplying the squared-distance trick by forgetting that the resulting optimal $x$ must still be plugged into the original distance formula if the minimal distance itself is requested.

---

## 6. Exercise Progression & MECE Requirements

Author 6 fresh, non-bank exercises under `## Exercises`, ordered strictly from easiest to hardest:

- **Universal Formatting Rules:**
  - Bare sequential headings: `### Q1` through `### Q6`.
  - Every question begins with bold subpart `**1.**`.
  - Never use Markdown ordered lists (`1.`, `2.`).
  - Strict answer-free objectivity.
- **Exercise Breakdown:**
  - **Q1 (Container Surface Area Minimization):**
    - An open-top cylindrical storage tank must hold a fixed volume $V_0 = 500\pi\,\text{m}^3$.
    - Subpart **1.** Express the total exterior surface area $A$ as a function of the radius $r$ only, stating the feasible domain.
    - Subpart **2.** Find the radius $r$ and height $h$ that minimize the surface area, and show that the optimal height equals the radius ($h = r$).
  - **Q2 (Multi-Compartment Agricultural Fencing with Differential Costs):**
    - A rancher builds a rectangular corral divided into three equal pens by two interior fences parallel to one side. The exterior fencing costs \$12 per linear foot, while the interior dividing fences cost \$8 per linear foot. The rancher has a total budget of \$7,200.
    - Subpart **1.** Set up the objective function for total enclosed area in terms of one dimension.
    - Subpart **2.** Find the optimal dimensions that maximize the total enclosed area.
  - **Q3 (Diagnostic Multiple Choice):** 5-option conceptual item (`A)` through `E)`):
    - Subpart **1.** Identifying the correct mathematical formulation and domain boundary behavior for a classic optimization scenario (e.g. folding an open-top box from a cardboard sheet or wire cutting), with distractors capturing lost constraints, missed endpoint extrema, and algebraic elimination slips.
  - **Q4 (Wire-Cutting Problem — Boundary vs Interior Extremum):**
    - A wire of length $L = 20\,\text{m}$ is cut into two pieces. One piece of length $x$ is bent into an equilateral triangle, and the remaining piece of length $20 - x$ is bent into a regular hexagon.
    - Subpart **1.** Express the total combined area $A(x)$ as a function of $x$, stating the feasible interval $[0, 20]$.
    - Subpart **2.** Determine how the wire should be cut to *minimize* the total combined area.
    - Subpart **3.** Determine how the wire should be cut to *maximize* the total combined area, explicitly evaluating boundary endpoints.
  - **Q5 (Economic Production & Average Cost Minimization):**
    - A manufacturing company has total cost function $C(x) = 2x^3 - 12x^2 + 30x + 100$ and price-demand function $p(x) = 150 - 6x$ (where $x \ge 0$ is thousands of units).
    - Subpart **1.** Find the production level $x$ that maximizes total profit $P(x)$, verifying the Second Derivative condition.
    - Subpart **2.** Calculate the production level where average cost $c(x)$ is minimized, and verify that marginal cost equals average cost ($C'(x) = c(x)$) at that point.
  - **Capstone Q6 (Very Hard Applied Transfer Task):**
    - Routing an offshore oil pipeline: An offshore drilling platform is located $8\,\text{km}$ out to sea from a straight coastline. A refinery is located $20\,\text{km}$ down the coast from the nearest shore point. Pipeline construction costs \$5 million per km underwater and \$3 million per km over land.
    - Formulate the total pipeline cost function, determine the feasible landing interval, locate the critical point minimizing total cost, and verify whether a direct overland, direct sea, or hybrid path is globally optimal.

---

## 7. Answer Key Specifications (`answers.md`)

- Title: `Handout 006: Applied Optimization and Economic Models — Answer Key`
- Matching `### Q1` through `### Q6` headings under `## Exercises`.
- Every subpart answered with a full Four-Stage derivation box (`>`).
- For Q3 (Multiple Choice):
  - Bold declaration: `**1. Correct answer: X.**`
  - Explanations for all 5 options (`- **A (Incorrect):** ...`), explaining why the correct choice holds and describing the specific modeling error in each distractor.
  - No option letters repeated in explanation prose.

---

## 8. Verification & Finalization Pipeline

1. Independently verify all derivations using a SymPy script.
2. Validate handout structure:
   ```powershell
   python -X utf8 -I C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/validate_handout.py C:/dev/calculus/handouts/006-applied-optimization-and-economic-models
   ```
3. Balance and shuffle multiple-choice letters:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/shuffle_mc_options.py --package C:/dev/calculus/handouts/006-applied-optimization-and-economic-models --apply
   ```
4. Render print PDFs (`handout.print.pdf`, `answers.print.pdf`) and visually inspect pages.
5. Check 16-page limit:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/check_page_limit.py C:/dev/calculus/handouts/006-applied-optimization-and-economic-models
   ```
6. Package finalization:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/finalize_package.py C:/dev/calculus/handouts/006-applied-optimization-and-economic-models
   ```
