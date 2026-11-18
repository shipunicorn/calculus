# Minimal Prerequisites for MATH 254 (Multivariable Calculus)

## 1. Executive Summary & Objective

**MATH 254 (Multivariable Calculus)** is the accredited mathematical engine for Machine Learning, Deep Learning, and Computer Science. It covers partial differentiation, directional derivatives, gradient vectors ($\nabla f$), tangent hyperplanes, the multivariable chain rule (the algorithmic foundation of backpropagation), Lagrange multipliers, and iterated multiple integrals (double and triple integrals with Jacobian transformations).

A common misconception is that enrolling in MATH 254 requires completing all of Calculus I and Calculus II in full university sequence. In reality, **over 60% of classical Calculus II consists of 19th-century mechanical physics and manual series convergence tests that are completely absent from MATH 254**.

This document outlines the **exact minimal prerequisite toolkit** required to enter and excel in MATH 254 from day one. It details what to study, the optimal chronological order, recommended textbooks, curated YouTube lectures, and targeted exercise sets.

## 2. What You Can Safely Ignore vs. What You Must Master

### What You Can 100% Ignore for MATH 254

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       CALCULUS TOPICS TO BYPASS                             │
├───────────────────────────────────┬─────────────────────────────────────────┤
│ Topic from Traditional Calc I/II  │ Why It Can Be Ignored for MATH 254      │
├───────────────────────────────────┼─────────────────────────────────────────┤
│ 1. Infinite Series & Convergence  │ Ratio test, root test, integral test,   │
│    Tests (Stewart Ch. 11)         │ alternating series, and radius of       │
│    (Math 253 / Calc II)           │ convergence are not used in multivariable│
│                                   │ differentiation or iterated integrals.  │
├───────────────────────────────────┼─────────────────────────────────────────┤
│ 2. Physics Applications of        │ Work with leaking buckets, hydrostatic  │
│    Integration (Stewart Ch. 6 & 8)│ force on dams, centers of mass, and     │
│    (Washers, Shells, Springs)     │ solids of revolution have zero presence.│
├───────────────────────────────────┼─────────────────────────────────────────┤
│ 3. Arcane Trigonometric           │ Iterated integrals in MATH 254 use      │
│    Substitutions (Stewart §7.2–3) │ polynomials, exponentials, or basic     │
│    (e.g., secant-cube, trig integrals)│ single-step substitutions; brutal   │
│                                   │ trig manipulations are not required.    │
├───────────────────────────────────┼─────────────────────────────────────────┤
│ 4. Heavy Epsilon-Delta ($\epsilon$-$\delta$)│ MATH 254 evaluates multivariable limits│
│    Formal Limit Proofs            │ along paths ($y = mx$, $y = kx^2$); no  │
│    (Stewart §2.4)                 │ rigorous delta-epsilon proofs expected. │
└───────────────────────────────────┴─────────────────────────────────────────┘
```

---

### The Strict Non-Negotiable Core: What You Must Master

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          THE ESSENTIAL TOOLKIT                              │
├──────────────────────────────┬──────────────────┬───────────────────────────┤
│ Module                       │ Target Time      │ Primary Competencies      │
├──────────────────────────────┼──────────────────┼───────────────────────────┤
│ 1. 3D Coordinate Geometry &  │ ~10–12 Hours     │ Completing the square,    │
│    Algebraic Precalculus     │                  │ quadrics in R^3, unit trig│
├──────────────────────────────┼──────────────────┼───────────────────────────┤
│ 2. Single-Variable           │ ~15–18 Hours     │ Power, Product, Quotient, │
│    Differentiation Fluency   │                  │ Chain rules; implicit diff│
├──────────────────────────────┼──────────────────┼───────────────────────────┤
│ 3. Single-Variable           │ ~12–15 Hours     │ FTC, standard anti-derivs,│
│    Integration Fluency       │                  │ algebraic & exp u-sub     │
├──────────────────────────────┼──────────────────┼───────────────────────────┤
│ 4. Foundational Vector       │ ~8–10 Hours      │ Dot product, projections, │
│    Algebra in R^2 and R^3    │                  │ cross product, determinants│
└──────────────────────────────┴──────────────────┴───────────────────────────┘
```

## 3. Ordered Learning Sequence (Syllabus)

Follow this structured, sequential pathway to build fluency without backtracking.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ Phase 1: Algebra & 3D Geometry (Completing Square & Quadric Surfaces)       │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ Phase 2: Differentiation Fluency (Multi-Rule Drilling & Chain Rule)         │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ Phase 3: Integration Fluency (Antiderivatives, FTC & u-Substitution)        │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ Phase 4: Vector Algebra & Spatial Geometry (Dot/Cross Products & Planes)    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### Phase 1: Algebraic Foundations & 3D Coordinate Geometry (10–12 Hours)

#### Core Concepts to Master:
1. **Completing the Square in Multiple Variables:**
   * In MATH 254, quadric surfaces (spheres, ellipsoids, paraboloids, hyperboloids) are introduced in expanded quadratic forms. You must instantly convert them into standard center-radius forms:
     $$x^2 + y^2 + z^2 - 6x + 4y - 10z + 13 = 0 \implies (x-3)^2 + (y+2)^2 + (z-5)^2 = 25$$
2. **Unit Circle Trigonometry:**
   * Instant recall of exact values of $\sin(\theta), \cos(\theta), \tan(\theta)$ at key angles: $0, \frac{\pi}{6}, \frac{\pi}{4}, \frac{\pi}{3}, \frac{\pi}{2}, \pi, \frac{3\pi}{2}, 2\pi$.
   * Polar coordinate conversions: $x = r\cos\theta, y = r\sin\theta, r^2 = x^2 + y^2, \tan\theta = y/x$.
   * Cylindrical coordinates $(r, \theta, z)$ and spherical coordinates $(\rho, \theta, \phi)$ angle boundaries.
3. **2D and 3D Basic Surfaces:**
   * Equations and geometric profiles of planes ($Ax + By + Cz = D$), paraboloids ($z = x^2 + y^2$), cones ($z^2 = x^2 + y^2$), and cylinders ($x^2 + y^2 = a^2$).

---

### Phase 2: Single-Variable Differentiation Fluency (15–18 Hours)

#### Core Concepts to Master:
1. **Primary Operational Rules:**
   * **Power Rule:** $\frac{d}{dx}[x^n] = n x^{n-1}$.
   * **Product Rule:** $\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)$.
   * **Quotient Rule:** $\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$.
   * **Chain Rule:** $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$.
2. **Transcendental & Composite Functions:**
   * Exponential: $\frac{d}{dx}[e^{kx}] = k e^{kx}$; $\frac{d}{dx}[e^{u(x)}] = e^{u(x)} u'(x)$.
   * Logarithmic: $\frac{d}{dx}[\ln(x)] = \frac{1}{x}$; $\frac{d}{dx}[\ln(u(x))] = \frac{u'(x)}{u(x)}$.
   * Trigonometric: $\frac{d}{dx}[\sin(x)] = \cos(x)$; $\frac{d}{dx}[\cos(x)] = -\sin(x)$.
3. **Implicit Differentiation:**
   * Differentiating equations relating $x$ and $y$ treating $y$ as an implicit function $y(x)$:
     $$x^2 + y^2 = 25 \implies 2x + 2y \frac{dy}{dx} = 0 \implies \frac{dy}{dx} = -\frac{x}{y}$$
   * *Why this is critical:* This trains the exact mental abstraction used in partial differentiation ($\frac{\partial f}{\partial x}$ holds all other variables constant).

---

### Phase 3: Single-Variable Integration & $u$-Substitution (12–15 Hours)

#### Core Concepts to Master:
1. **Fundamental Theorem of Calculus (FTC):**
   * Evaluating definite integrals: $\int_a^b f'(x)\,dx = f(b) - f(a)$.
2. **Standard Anti-derivatives:**
   * Power rule: $\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \ne -1)$.
   * Reciprocal: $\int \frac{1}{x} \, dx = \ln|x| + C$.
   * Exponential: $\int e^{kx} \, dx = \frac{1}{k}e^{kx} + C$.
   * Trigonometric: $\int \cos(kx) \, dx = \frac{1}{k}\sin(kx) + C$; $\int \sin(kx) \, dx = -\frac{1}{k}\cos(kx) + C$.
3. **$u$-Substitution (The Cornerstone of Multivariable Iterated Integrals):**
   * Identifying $u = g(x)$ such that $du = g'(x)\,dx$.
   * Algebraic substitutions: $\int 2x \sqrt{x^2 + 4} \, dx$.
   * Exponential substitutions: $\int x e^{-x^2} \, dx$.
   * Updating limits of integration in definite integrals:
     $$\int_0^1 x e^{x^2} \, dx = \frac{1}{2} \int_0^1 e^u \, du = \frac{1}{2}(e - 1)$$
   * *Why this is critical:* In MATH 254, double integrals such as $\int_0^1 \int_0^{\sqrt{1-x^2}} x y \, dy \, dx$ simply require executing two single-variable integrals sequentially. If your $u$-substitution is rock solid, 90% of multiple integrals are trivial.
4. **Basic Single-Step Integration by Parts:**
   * $\int u \, dv = u v - \int v \, du$ on standard forms like $\int x e^x \, dx$ or $\int x \cos(x) \, dx$.

---

### Phase 4: Foundational Vector Algebra in $\mathbb{R}^2$ and $\mathbb{R}^3$ (8–10 Hours)

#### Core Concepts to Master:
1. **Vectors, Magnitude, and Direction:**
   * Vector components: $\mathbf{v} = \langle v_1, v_2, v_3 \rangle = v_1 \mathbf{i} + v_2 \mathbf{j} + v_3 \mathbf{k}$.
   * Magnitude (Euclidean norm): $\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + v_3^2}$.
   * Unit vectors: $\mathbf{u} = \frac{\mathbf{v}}{\|\mathbf{v}\|}$.
2. **Dot Product (Scalar Product) & Projections:**
   * Algebraic definition: $\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + u_3 v_3$.
   * Geometric definition: $\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos(\theta)$.
   * Orthogonality criterion: $\mathbf{u} \cdot \mathbf{v} = 0 \iff \mathbf{u} \perp \mathbf{v}$.
   * Scalar projection: $\text{comp}_{\mathbf{a}} \mathbf{b} = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|}$.
   * Vector projection: $\text{proj}_{\mathbf{a}} \mathbf{b} = \left(\frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|^2}\right) \mathbf{a}$.
3. **Cross Product in $\mathbb{R}^3$:**
   * Determinant computation:
     $$\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix}$$
   * Geometric property: $\mathbf{u} \times \mathbf{v}$ is orthogonal to both $\mathbf{u}$ and $\mathbf{v}$, with magnitude equal to the area of the spanned parallelogram.
4. **Equations of Lines and Planes in 3D:**
   * Line through $\mathbf{r}_0$ parallel to $\mathbf{v}$: $\mathbf{r}(t) = \mathbf{r}_0 + t\mathbf{v}$.
   * Plane through $P_0(x_0, y_0, z_0)$ with normal vector $\mathbf{n} = \langle a, b, c \rangle$:
     $$a(x - x_0) + b(y - y_0) + c(z - z_0) = 0$$

## 4. Primary Textbooks & Specific Problem Sets

### 1. James Stewart — *Calculus: Early Transcendentals* (7th / 8th / 9th Ed.)

The industry-standard reference for MATH 254. Use Stewart to drill the prerequisite mechanics.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     STEWART PREREQUISITE ASSIGNMENTS                        │
├─────────┬──────────────────────────────────────┬────────────────────────────┤
│ Section │ Topic Title                          │ Recommended Exercises      │
├─────────┼──────────────────────────────────────┼────────────────────────────┤
│ §2.5    │ Continuity & Piecewise Functions     │ 15, 17, 21, 35, 37         │
│ §3.1    │ Derivatives of Polynomials & Exp     │ 3–23 (odd), 31, 35         │
│ §3.2    │ Product and Quotient Rules           │ 3–25 (odd), 31, 43         │
│ §3.4    │ The Chain Rule (Crucial)             │ 7–37 (odd), 45, 51, 61     │
│ §3.5    │ Implicit Differentiation             │ 5–19 (odd), 25, 29         │
│ §3.6    │ Derivatives of Logarithmic Functions │ 2–24 (even), 33, 39        │
│ §4.9    │ Antiderivatives                      │ 1–25 (odd), 31, 41         │
│ §5.3    │ Fundamental Theorem of Calculus      │ 7–29 (odd), 39, 43         │
│ §5.5    │ The Substitution Rule (u-sub)        │ 7–45 (odd), 53, 57, 67     │
│ §7.1    │ Integration by Parts (Single Step)   │ 3–15 (odd), 23             │
│ §12.1   │ 3D Coordinate Systems & Quadrics     │ 5–17 (odd), 23, 29, 31, 37 │
│ §12.2   │ Vectors & Norms                      │ 3–25 (odd), 29             │
│ §12.3   │ The Dot Product & Projections        │ 1–27 (odd), 39, 41, 43     │
│ §12.4   │ The Cross Product                    │ 1–19 (odd), 27, 29, 33     │
│ §12.5   │ Lines and Planes in Space            │ 1–27 (odd), 31, 35, 45     │
│ §12.6   │ Cylinders and Quadric Surfaces       │ 1–21 (odd), 29, 31–36 (all)│
└─────────┴──────────────────────────────────────┴────────────────────────────┘
```

---

### 2. Michael Corral — *Vector Calculus* (Open-Access Text)

Michael Corral’s open-access text provides an exceptionally clean, geometric, and computationally concise introduction to multivariable geometry.

* **Free Legal PDF:** Available via [mecmath.net/calculus](https://mecmath.net/calculus/)
* **Relevant Sections for Prerequisites & Stage 1:**
  * **Section 1.1 (Vectors in Euclidean Space):** Definition of vectors, scalar multiplication, vector addition.
    * *Exercises:* Section 1.1, Exercises 1–10.
  * **Section 1.2 (Dot Product):** Law of cosines derivation, dot product properties, component projections.
    * *Exercises:* Section 1.2, Exercises 1, 3, 5, 7, 9, 13, 15.
  * **Section 1.3 (Cross Product):** 3D vector products, perpendicularity, area calculations.
    * *Exercises:* Section 1.3, Exercises 1, 3, 5, 8, 11, 14.
  * **Section 1.4 (Lines and Planes in Space):** Parametric lines, normal vectors, symmetric equations.
    * *Exercises:* Section 1.4, Exercises 1–15 (odd), 18, 20.
  * **Section 1.5 (Surfaces in Space):** Ellipsoids, paraboloids, hyperboloids of one/two sheets.
    * *Exercises:* Section 1.5, Exercises 1–12 (matching and sketches).

---

### 3. Steven J. Leon — *Linear Algebra with Applications* (Global Edition)

Leon’s classic linear algebra textbook anchors the spatial intuition of vectors and projections in higher dimensions.

* **Relevant Sections for MATH 254 Preparation:**
  * **Section 1.2 (Matrices & Row Operations):** Solving systems of linear equations (used for plane intersections).
    * *Exercises:* Section 1.2, Exercises 1–5, 9.
  * **Section 3.1 & 3.2 (Vector Spaces & Subspaces):** Visualizing lines and planes through the origin as subspaces of $\mathbb{R}^3$.
    * *Exercises:* Section 3.2, Exercises 1–6.
  * **Section 5.1 (The Scalar Product in $\mathbb{R}^n$):** Vector lengths, Cauchy-Schwarz inequality, angle between vectors in high-dimensional space ($\mathbb{R}^n$).
    * *Exercises:* Section 5.1, Exercises 1, 3, 5, 7, 9, 13, 17.
  * **Section 5.2 & 5.5 (Orthogonality & Projections):** Orthogonal projections onto lines and planes ($P = \frac{\mathbf{u} \mathbf{u}^T}{\mathbf{u}^T \mathbf{u}}$).
    * *Exercises:* Section 5.2, Exercises 1–8; Section 5.5, Exercises 1–5.

---

### 4. C. Henry Edwards, David E. Penney, David T. Calvis — *Differential Equations and Linear Algebra*

Edwards & Penney bridges linear algebra with dynamical equations, offering unmatched clarity on vector operations, determinants, and coordinate transformations.

* **Relevant Sections for Prerequisites:**
  * **Section 3.1 & 3.2 (Matrices & Vector Operations):** Algebraic manipulation of column vectors and linear combinations.
    * *Exercises:* Section 3.2, Exercises 1–15 (odd).
  * **Section 3.5 (Determinants of $2 \times 2$ and $3 \times 3$ Matrices):** Cofactor expansion and computational mechanics used for cross products and 3D Jacobians.
    * *Exercises:* Section 3.5, Exercises 1–19 (odd), 25.
  * **Section 4.1 (Vectors in $\mathbb{R}^n$):** Dot products, angles, Cauchy-Schwarz, and hyperplanes.
    * *Exercises:* Section 4.1, Exercises 1–17 (odd), 21.

## 5. Curated YouTube Lectures & Video Playlists

### Top Video Recommendations by Topic

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       CURATED VIDEO GUIDE                                   │
├──────────────────────┬──────────────────────────────┬───────────────────────┤
│ Topic                │ Channel / Creator            │ Key Videos / Playlist │
├──────────────────────┼──────────────────────────────┼───────────────────────┤
│ Geometric Intuition  │ 3Blue1Brown                  │ "Essence of Calculus" │
│ of Derivatives       │ (Grant Sanderson)            │ Videos 1, 2, 3, 4     │
├──────────────────────┼──────────────────────────────┼───────────────────────┤
│ Geometric Intuition  │ 3Blue1Brown                  │ "Essence of Calculus" │
│ of Integrals & FTC   │ (Grant Sanderson)            │ Videos 7, 8           │
├──────────────────────┼──────────────────────────────┼───────────────────────┤
│ Spatial Vector       │ 3Blue1Brown                  │ "Essence of Linear    │
│ Foundations          │ (Grant Sanderson)            │ Algebra" Videos 1–4   │
├──────────────────────┼──────────────────────────────┼───────────────────────┤
│ Step-by-Step Chain   │ Khan Academy                 │ Differential Calculus │
│ Rule Drilling        │ (Sal Khan)                   │ Chain Rule Playlist   │
├──────────────────────┼──────────────────────────────┼───────────────────────┤
│ Step-by-Step u-Sub   │ Khan Academy                 │ Integral Calculus     │
│ Practice Drills      │ (Sal Khan)                   │ u-Substitution Unit   │
├──────────────────────┼──────────────────────────────┼───────────────────────┤
│ Complete Lecture on  │ Professor Leonard            │ Calculus 1: Ch 3      │
│ Derivative Rules     │                              │ Derivative Lectures   │
├──────────────────────┼──────────────────────────────┼───────────────────────┤
│ Completing Square for│ Brian McLogan                │ "Completing Square to │
│ Conics and 3D Quadric│                              │ Graph Conic Sections" │
├──────────────────────┼──────────────────────────────┼───────────────────────┤
│ Multivariable Intro  │ MIT OpenCourseWare (18.02)   │ Lecture 1: Vectors,   │
│ Vectors & Geometry   │ (Prof. Denis Auroux)         │ Dot Product, Planes   │
└──────────────────────┴──────────────────────────────┴───────────────────────┘
```

1. **3Blue1Brown — *Essence of Calculus*:**
   * *Chapter 2:* [The Paradox of the Derivative](https://www.youtube.com/watch?v=9vKqVkMQHKk)
   * *Chapter 3:* [Derivative Formulas Through Geometry](https://www.youtube.com/watch?v=S0_qX4VJhMQ)
   * *Chapter 4:* [Visualizing the Chain Rule and Product Rule](https://www.youtube.com/watch?v=YG15m2VwSjA)
   * *Chapter 8:* [Integration and the Fundamental Theorem of Calculus](https://www.youtube.com/watch?v=rfG8ce4nNh0)
2. **Professor Leonard — *Calculus 1 & Calculus 3*:**
   * [The Chain Rule for Derivatives](https://www.youtube.com/watch?v=6k3ReR_A60I) — The most detailed, clear procedural walkthrough on YouTube.
   * [Integration by U-Substitution](https://www.youtube.com/watch?v=1A2b_wV3v8o) — Crystal-clear patterns for algebraic substitutions.
   * [Calculus 3: 3D Coordinate Systems & Vectors](https://www.youtube.com/watch?v=1xN5V_G5G5o) — Perfect orientation for the first week of MATH 254.
3. **MIT OpenCourseWare 18.02 (Multivariable Calculus — Denis Auroux):**
   * [Lecture 1: Dot Product](https://www.youtube.com/watch?v=k7RM-ot2NWY)
   * [Lecture 2: Determinants and Cross Product](https://www.youtube.com/watch?v=8y_V8Y4Zp9U)
   * [Lecture 3: Matrices and Planes](https://www.youtube.com/watch?v=CqYQ4v6mC8c)

## 6. Self-Diagnostic Readiness Assessment

Before beginning MATH 254, attempt the following 8 diagnostic problems closed-book. Complete solutions are provided below to verify your mechanics.

### Diagnostic Problems

1. **(Differentiation — Product & Chain Rule):**
   Compute $f'(x)$ where $f(x) = x^3 e^{-2x^2}$.
2. **(Differentiation — Quotient & Chain Rule):**
   Compute $g'(t)$ where $g(t) = \frac{\ln(3t^2 + 1)}{t^2 + 1}$.
3. **(Implicit Differentiation):**
   Given $x^3 + y^3 = 6xy$, compute $\frac{dy}{dx}$ in terms of $x$ and $y$.
4. **(Indefinite Integration — $u$-Substitution):**
   Evaluate $\int \frac{x}{\sqrt{2x^2 + 5}} \, dx$.
5. **(Definite Integration — $u$-Substitution):**
   Evaluate $\int_0^{\sqrt{\pi}} x \sin(x^2) \, dx$.
6. **(3D Geometry — Completing the Square):**
   Identify the center and radius of the sphere:
   $$x^2 + y^2 + z^2 - 4x + 6y - 8z - 7 = 0$$
7. **(Vector Algebra — Dot Product & Orthogonal Projection):**
   Let $\mathbf{a} = \langle 1, 2, -2 \rangle$ and $\mathbf{b} = \langle 3, 0, 4 \rangle$.
   Compute $\mathbf{a} \cdot \mathbf{b}$, the angle $\theta$ between them, and the vector projection $\text{proj}_{\mathbf{a}} \mathbf{b}$.
8. **(Vector Cross Product & Plane Equation):**
   Find an equation of the plane passing through points $P(1, 0, 0)$, $Q(0, 2, 0)$, and $R(0, 0, 3)$.

---

### Solutions & Answer Key

1. **Solution (Problem 1):**
   Using product rule and chain rule:
   $$f'(x) = \frac{d}{dx}[x^3] e^{-2x^2} + x^3 \frac{d}{dx}[e^{-2x^2}] = 3x^2 e^{-2x^2} + x^3 \left(e^{-2x^2} \cdot (-4x)\right) = x^2 e^{-2x^2} (3 - 4x^2)$$

2. **Solution (Problem 2):**
   Using quotient rule:
   $$g'(t) = \frac{\left(\frac{6t}{3t^2 + 1}\right)(t^2 + 1) - \ln(3t^2 + 1)(2t)}{(t^2 + 1)^2} = \frac{6t(t^2 + 1) - 2t(3t^2 + 1)\ln(3t^2 + 1)}{(3t^2 + 1)(t^2 + 1)^2}$$

3. **Solution (Problem 3):**
   Differentiate both sides with respect to $x$:
   $$3x^2 + 3y^2 \frac{dy}{dx} = 6y + 6x \frac{dy}{dx} \implies (3y^2 - 6x)\frac{dy}{dx} = 6y - 3x^2 \implies \frac{dy}{dx} = \frac{2y - x^2}{y^2 - 2x}$$

4. **Solution (Problem 4):**
   Let $u = 2x^2 + 5$, then $du = 4x \, dx \implies x \, dx = \frac{1}{4}du$:
   $$\int \frac{1}{4} u^{-1/2} \, du = \frac{1}{4} \cdot 2 u^{1/2} + C = \frac{1}{2}\sqrt{2x^2 + 5} + C$$

5. **Solution (Problem 5):**
   Let $u = x^2$, then $du = 2x \, dx \implies x \, dx = \frac{1}{2}du$.
   When $x = 0$, $u = 0$; when $x = \sqrt{\pi}$, $u = \pi$:
   $$\int_0^\pi \frac{1}{2}\sin(u)\,du = \left[ -\frac{1}{2}\cos(u) \right]_0^\pi = -\frac{1}{2}(\cos\pi - \cos 0) = -\frac{1}{2}(-1 - 1) = 1$$

6. **Solution (Problem 6):**
   Group variables and complete the square:
   $$(x^2 - 4x + 4) + (y^2 + 6y + 9) + (z^2 - 8z + 16) = 7 + 4 + 9 + 16$$
   $$(x - 2)^2 + (y + 3)^2 + (z - 4)^2 = 36$$
   *Center:* $(2, -3, 4)$; *Radius:* $R = \sqrt{36} = 6$.

7. **Solution (Problem 7):**
   * $\mathbf{a} \cdot \mathbf{b} = (1)(3) + (2)(0) + (-2)(4) = 3 + 0 - 8 = -5$.
   * Norms: $\|\mathbf{a}\| = \sqrt{1^2 + 2^2 + (-2)^2} = \sqrt{9} = 3$; $\|\mathbf{b}\| = \sqrt{3^2 + 0^2 + 4^2} = \sqrt{25} = 5$.
   * Angle $\theta$: $\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|\|\mathbf{b}\|} = \frac{-5}{3 \cdot 5} = -\frac{1}{3} \implies \theta = \arccos\left(-\frac{1}{3}\right) \approx 1.91 \text{ rad } (109.5^\circ)$.
   * Vector projection:
     $$\text{proj}_{\mathbf{a}} \mathbf{b} = \left(\frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|^2}\right)\mathbf{a} = \left(\frac{-5}{9}\right)\langle 1, 2, -2 \rangle = \left\langle -\frac{5}{9}, -\frac{10}{9}, \frac{10}{9} \right\rangle$$

8. **Solution (Problem 8):**
   Vectors in the plane:
   $\vec{PQ} = \langle -1, 2, 0 \rangle$, $\vec{PR} = \langle -1, 0, 3 \rangle$.
   Normal vector $\mathbf{n} = \vec{PQ} \times \vec{PR}$:
   $$\mathbf{n} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -1 & 2 & 0 \\ -1 & 0 & 3 \end{vmatrix} = \mathbf{i}(6 - 0) - \mathbf{j}(-3 - 0) + \mathbf{k}(0 - (-2)) = 6\mathbf{i} + 3\mathbf{j} + 2\mathbf{k} = \langle 6, 3, 2 \rangle$$
   Using point $P(1, 0, 0)$:
   $$6(x - 1) + 3(y - 0) + 2(z - 0) = 0 \implies 6x + 3y + 2z = 6$$

## 7. Recommended Weekly Sprint Schedule (3-Week Rapid Ramp-Up)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          3-WEEK SPRINT SCHEDULE                             │
├────────┬──────────────────────────┬─────────────────────────────────────────┤
│ Week   │ Core Target              │ Daily Breakdown                         │
├────────┼──────────────────────────┼─────────────────────────────────────────┤
│ Week 1 │ Differentiation Fluency  │ • Days 1–2: Power, Product, Quotient    │
│        │ & Multi-Rule Mechanics   │ • Days 3–4: Chain Rule & exp/ln         │
│        │                          │ • Days 5–6: Implicit diff & trig        │
│        │                          │ • Day 7: 40-problem drill               │
├────────┼──────────────────────────┼─────────────────────────────────────────┤
│ Week 2 │ Integration Competence   │ • Days 1–2: Anti-derivatives & FTC      │
│        │ & Substitution           │ • Days 3–4: Algebraic u-substitution    │
│        │                          │ • Days 5–6: Definite integral u-sub     │
│        │                          │ • Day 7: Mixed u-substitution drill     │
├────────┼──────────────────────────┼─────────────────────────────────────────┤
│ Week 3 │ 3D Geometry &            │ • Days 1–2: Completing square & quadrics│
│        │ Vector Operations        │ • Days 3–4: Dot product & projections   │
│        │                          │ • Days 5–6: Cross product & planes      │
│        │                          │ • Day 7: Diagnostic assessment          │
└────────┴──────────────────────────┴─────────────────────────────────────────┘
```

By completing this 35–40 hour targeted sequence, you enter MATH 254 fully equipped with the spatial intuition and calculus mechanics required to achieve top performance.
