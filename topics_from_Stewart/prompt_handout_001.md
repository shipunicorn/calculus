# Prompt for Handout 001: Functions, Transformations, and Limits

Use the `/calculus-create-handout` skill to update and renumber the existing handout package into `001-functions-transformations-and-limits` ("Functions, Transformations, and Limits"). Do not create or edit any other handout in this session.

```text
/calculus-create-handout
```

---

## 1. Package Specification & Directory Migration

- **Package Number (Fixed):** `001`
- **Target Package Directory:** `C:\dev\calculus\handouts\001-functions-transformations-and-limits\`
- **Source Existing Package:** `C:\dev\calculus\handouts\002-functions-transformations-and-limits\`
- **Action Required:**
  1. Inspect the existing directory `C:\dev\calculus\handouts\002-functions-transformations-and-limits\` using `ls` / `Get-ChildItem`.
  2. Following project file-safety rules (`mv` only, verify first, zero `rm -rf`), rename the existing folder from `002-functions-transformations-and-limits` to `001-functions-transformations-and-limits`.
  3. Update `handout.md` YAML front matter:
     ```markdown
     ---
     title: "Handout 001: Functions, Transformations, and Limits"
     ---
     ```
  4. Update top-level heading: `# 001: Functions, Transformations, and Limits`.
  5. Update `answers.md` YAML front matter and top heading:
     ```markdown
     ---
     title: "Handout 001: Functions, Transformations, and Limits — Answer Key"
     ---

     # 001: Functions, Transformations, and Limits — Answer Key
     ```
  6. Update forward cross-references in the opening lines and closing notes to reference **Handout 002: Limit Laws, Squeeze Theorem, Continuity, and the IVT**.
- **Page Budget:** 10 pages (Handout) / 7 pages (Key). Must remain $\le 16$ pages for `handout.print.pdf`.

---

## 2. Pedagogical Context & MATH 254 Critical Path Alignment

- **Role in Sequence:** Foundational entry point (Stage 1: Foundations & Limits).
- **Prerequisites Assumed:** High school algebra, basic coordinate geometry, domain/range concepts, function notation.
- **Subsequent Handout Unlocked:** Handout 002: Limit Laws, Squeeze Theorem, Continuity, and the IVT.
- **MATH 254 (Multivariable Calculus) Critical Link:**
  - Establishes natural domain and range determination, which directly extends to multivariable scalar fields $f(x, y)$ and domain regions in $\mathbb{R}^2$.
  - Grounds reading coordinate graphs, level curves, and rigid/non-rigid function transformations.
  - Introduces intuitive two-sided and one-sided limits ($\lim_{x \to a^-} f(x)$ and $\lim_{x \to a^+} f(x)$), which are essential for testing multivariable path limits ($y = mx$, $y = kx^2$) and detecting non-existence.

---

## 3. Source Documents & Assets

- **Master Plan Authority:** [`C:\dev\calculus\topics_from_Stewart\handouts_plan.md`](file:///C:/dev/calculus/topics_from_Stewart/handouts_plan.md) (Sections 1–4).
- **Primary Source Document:** [`C:\dev\calculus\topics_from_Stewart\topics.md`](file:///C:/dev/calculus/topics_from_Stewart/topics.md) (Functions, Transformations, and Intuitive Limits).
- **Figure Directory:** `C:\dev\calculus\handouts\001-functions-transformations-and-limits\figures\` (retained from existing package).
- **Respective Image Generator:** [`C:\dev\calculus\topics_from_Stewart\generate_figures.py`](file:///C:/dev/calculus/topics_from_Stewart/generate_figures.py).

---

## 4. Required Structural & Formatting Rules

- **Derivation Box Format:**
  Every worked example and answer key derivation must use a Markdown blockquote derivation box (`>`) structured across the Four-Stage Continuous Problem Framework:
  - **Stage 1 (Classification & Domain):** Function class, domain restrictions ($g(x) \ne 0$, radicands $\ge 0$).
  - **Stage 2 (Algebraic Preparation):** Factoring, power conversion, piecewise partition.
  - **Stage 3 (Core Operation):** Limit substitution, graph inspection, transformation calculation.
  - **Stage 4 (Interpretation & Boundary Check):** Interval boundary checks, open vs closed endpoints, one-sided agreement.
- **Prohibited Phrases:** Never write "solution", "Solution.", "**Solution.**", or "try first".
- **Interval Notation:** French Bourbaki notation only: $\mathopen{]}a, b\mathclose{[}$, $[a, b\mathclose{[}$, $\mathopen{]}-\infty, +\infty\mathclose{[}$. Never use parentheses $(a, b)$ for intervals.
- **Exercise Numbering:**
  - Level-three headings: `### Q1`, `### Q2`, etc.
  - Bold subparts: `**1.**`, `**2.**`. Never use Markdown ordered lists (`1.`, `2.`) anywhere.
  - Bare sequential question headings; do not include difficulty labels ("capstone", "stretch", "bonus").
  - Strictly answer-free exercises with bounded prompts (no "Explain in your own words").

---

## 5. Verification & Finalization Pipeline

After completing updates and renumbering:
1. Re-verify all mathematical derivations with SymPy.
2. Run the package validator:
   ```powershell
   python -X utf8 -I C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/validate_handout.py C:/dev/calculus/handouts/001-functions-transformations-and-limits
   ```
3. Balance and shuffle multiple-choice option letters:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/shuffle_mc_options.py --package C:/dev/calculus/handouts/001-functions-transformations-and-limits --apply
   ```
4. Render print PDFs and verify visual layout:
   - `handout.print.pdf` ($\le 16$ pages)
   - `answers.print.pdf`
5. Verify page count limits:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/check_page_limit.py C:/dev/calculus/handouts/001-functions-transformations-and-limits
   ```
6. Clean up scratch files:
   ```powershell
   python C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts/finalize_package.py C:/dev/calculus/handouts/001-functions-transformations-and-limits
   ```
