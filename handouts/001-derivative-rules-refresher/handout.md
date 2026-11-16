---
title: "Handout 001: Derivative Rules Refresher"
---

# 001: Derivative Rules Refresher

Calculus studies continuous change. The derivative of a function $f(x)$ measures its instantaneous rate of change with respect to the input variable $x$. Geometrically, the derivative $f'(x_0)$ evaluates the exact slope of the tangent line to the graph $y = f(x)$ at the coordinate $(x_0, f(x_0))$.

Rather than repeatedly evaluating the limit definition $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$, standard calculus workflows rely on established derivative formulas for elementary functions paired with algebraic combination rules. This handout provides a foundational refresher of the fundamental formulas and differentiation rules, accompanied by real-world software engineering and business decision examples, using prime notation throughout.

## Common derivative formulas

The derivative formulas below apply to standard elementary functions. In each formula, $x$ is the independent variable, $c$ is a real constant, and trigonometric angles are measured strictly in radians.

| Function category | Function $f(x)$ | Derivative $f'(x)$ | Domain / Conditions |
| :--- | :--- | :--- | :--- |
| **Constant** | $c$ | $0$ | $c \in \mathbb{R}$ |
| **Linear** | $x$ | $1$ | $x \in \mathbb{R}$ |
| **Constant Multiple of $x$** | $ax$ | $a$ | $a \in \mathbb{R}$ |
| **Square** | $x^2$ | $2x$ | $x \in \mathbb{R}$ |
| **General Power** | $x^n$ | $n x^{n-1}$ | $n \neq 0$; $x > 0$ if $n$ is fractional |
| **Square Root** | $\sqrt{x} = x^{1/2}$ | $\frac{1}{2\sqrt{x}} = \frac{1}{2}x^{-1/2}$ | $x > 0$ |
| **Natural Exponential** | $e^x$ | $e^x$ | $x \in \mathbb{R}$ |
| **General Exponential** | $a^x$ | $a^x \ln(a)$ | $a > 0, a \neq 1$ |
| **Natural Logarithm** | $\ln(x)$ | $\frac{1}{x}$ | $x > 0$ |
| **General Logarithm** | $\log_a(x)$ | $\frac{1}{x \ln(a)}$ | $x > 0, a > 0, a \neq 1$ |
| **Sine** | $\sin(x)$ | $\cos(x)$ | $x \in \mathbb{R}$ |
| **Cosine** | $\cos(x)$ | $-\sin(x)$ | $x \in \mathbb{R}$ |
| **Tangent** | $\tan(x)$ | $\sec^2(x)$ | $x \neq \frac{\pi}{2} + k\pi$ |
| **Secant** | $\sec(x)$ | $\sec(x)\tan(x)$ | $x \neq \frac{\pi}{2} + k\pi$ |
| **Cosecant** | $\csc(x)$ | $-\csc(x)\cot(x)$ | $x \neq k\pi$ |
| **Cotangent** | $\cot(x)$ | $-\csc^2(x)$ | $x \neq k\pi$ |
| **Inverse Sine** | $\arcsin(x) = \sin^{-1}(x)$ | $\frac{1}{\sqrt{1-x^2}}$ | $-1 < x < 1$ |
| **Inverse Cosine** | $\arccos(x) = \cos^{-1}(x)$ | $-\frac{1}{\sqrt{1-x^2}}$ | $-1 < x < 1$ |
| **Inverse Tangent** | $\arctan(x) = \tan^{-1}(x)$ | $\frac{1}{1+x^2}$ | $x \in \mathbb{R}$ |

## General differentiation rules

When functions are scaled, added, multiplied, divided, or composed, the derivative is determined by structural combination rules.

| Rule name | Function expression | Derivative formula | Description / Notes |
| :--- | :--- | :--- | :--- |
| **Constant Multiple** | $c \cdot f(x)$ | $c \cdot f'(x)$ | Constants factor out of differentiation. |
| **Sum Rule** | $f(x) + g(x)$ | $f'(x) + g'(x)$ | Differentiate term by term. |
| **Difference Rule** | $f(x) - g(x)$ | $f'(x) - g'(x)$ | Differentiate term by term preserving sign. |
| **Product Rule** | $f(x) \cdot g(x)$ | $f'(x)g(x) + f(x)g'(x)$ | Rate of change when both factors vary simultaneously. |
| **Quotient Rule** | $\frac{f(x)}{g(x)}$ | $\frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$ | Numerator is $(f'g - fg')$; denominator is squared ($g(x) \neq 0$). |
| **Reciprocal Rule** | $\frac{1}{f(x)}$ | $-\frac{f'(x)}{[f(x)]^2}$ | Special case of Quotient Rule with constant numerator 1. |
| **Chain Rule** | $f(g(x))$ | $f'(g(x)) \cdot g'(x)$ | Derivative of outer at inner, times derivative of inner. |

## Strategy routines

Apply these five strategic habits to navigate differentiation problems reliably:

- **S1 Classify:** Inspect the overall algebraic structure of the function before calculating. Determine whether the outermost operation is a sum, difference, constant multiple, product, quotient, or composite layer.
- **S2 Rewrite:** Convert radical expressions to rational exponents ($\sqrt{x} = x^{1/2}$, $\sqrt[3]{x} = x^{1/3}$) and reciprocal terms to negative powers ($\frac{1}{x^k} = x^{-k}$). Algebraic preparation eliminates unnecessary use of the Quotient Rule on simple power terms.
- **S3 Anchor:** Apply the primary outer rule first. Keep bracketed placeholders for individual derivative components, writing out $f'(x)g(x) + f(x)g'(x)$ before evaluating.
- **S4 Inner sweep:** In composite functions $f(g(x))$, evaluate the outer derivative $f'$ evaluated at the undisturbed inner argument $g(x)$, then multiply immediately by the inner derivative $g'(x)$.
- **S5 Check:** Confirm that constants without variables differentiated to zero, trigonometric "co-" functions received negative signs, and units/dimensions match expectation.

## Mistakes, edge cases & strategies

The table below outlines common pitfalls encountered when differentiating elementary functions and combinations.

| Trap | Correct reasoning | Strategy |
| :--- | :--- | :--- |
| **Differentiating constants as powers** | Constants such as $\pi$, $e$, and $\pi^3$ contain no variable $x$. Their derivative is $0$, not $3\pi^2$ or $e$. | Scan every term for the presence of the differentiation variable $x$. If no variable appears, the derivative is $0$. |
| **Confusing Power and Exponential rules** | The Power Rule applies to $\text{variable}^\text{constant}$ ($x^n$). The Exponential Rule applies to $\text{constant}^\text{variable}$ ($a^x$). | Identify the base and exponent: base $x$ requires $n x^{n-1}$; base $a$ requires $a^x \ln(a)$. |
| **Omitting the Product Rule** | The derivative of a product is not the product of the derivatives: $(fg)' \neq f'g'$. Both factors vary simultaneously. | When two variable factors multiply, use the explicit Product Rule template $f'g + fg'$. |
| **Quotient Rule subtraction order flip** | Subtraction is not commutative: $(f/g)' \neq \frac{fg' - f'g}{g^2}$. The numerator must begin with $f'g$. | Memorize the cadence "low d-high minus high d-low over low squared". |
| **Dropping the inner derivative in Chain Rule** | $(f(g(x)))' \neq f'(g(x))$. The outer rate of change must be scaled by the inner rate of change $g'(x)$. | Circle the inner function $u = g(x)$, compute $u'$, and multiply the outer derivative by $u'$. |
| **Trigonometric sign errors** | Derivatives of cosine, cosecant, and cotangent are negative, whereas sine, secant, and tangent are positive. | Associate the "co-" prefix with negative signs: $(\cos(x))' = -\sin(x)$, $(\cot(x))' = -\csc^2(x)$, $(\csc(x))' = -\csc(x)\cot(x)$. |

## Worked examples

### Example 1: Constant Rule ($c \to 0$) in cloud architecture

An enterprise maintains a dedicated AWS Direct Connect gateway with a fixed contractual monthly line fee of \$500, regardless of monthly query traffic $q$: $C(q) = 500$. Determine the marginal infrastructure line cost $C'(q)$ with respect to query traffic $q$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the function type. $C(q) = 500$ is a constant function independent of the query volume variable $q$.

**Step 2.** Differentiate using the Constant Rule:
$$C'(q) = 0$$

*Why it works:* Sunk fixed overhead incurs zero incremental cost per additional transaction.

### Example 2: Linear Rule ($x \to 1$) in telemetry pipelines

A backend telemetry service forwards exactly one health-check ping per incoming client connection $x$: $T(x) = x$. Determine the marginal telemetry emission rate $T'(x)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the linear function $T(x) = x^1$. Applying the Power Rule with $n = 1$ yields:
$$T'(x) = 1(x^0) = 1$$

*Why it works:* The rate of change is strictly 1-to-1: each additional connection produces exactly one additional ping.

### Example 3: Constant Multiple of $x$ ($ax \to a$) in SaaS bandwidth billing

A cloud storage provider bills data egress at a constant tier rate of \$0.08 per gigabyte $g$: $B(g) = 0.08g$. Determine the marginal billing cost $B'(g)$ per additional gigabyte downloaded.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the constant multiple $a = 0.08$ scaling variable $g$. Differentiating yields:
$$B'(g) = 0.08(1) = 0.08$$

*Why it works:* Every additional gigabyte transferred increases costs at the constant marginal rate of \$0.08/GB.

### Example 4: Square Rule ($x^2 \to 2x$) in algorithmic complexity

In an unoptimized quadratic comparison algorithm (such as bubble sort), the number of pairwise key comparisons for an array of size $n$ scales as $K(n) = n^2$. Determine the marginal comparison growth rate $K'(n)$ when the array expands.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the square function $K(n) = n^2$.

**Step 2.** Apply the Power Rule with $n = 2$:
$$K'(n) = 2n$$

*Why it works:* The computational burden of inserting the next item into an existing set of size $n$ requires $2n$ additional comparisons, showing why quadratic algorithms degrade rapidly as dataset size grows.

### Example 5: General Power Rule ($x^n \to n x^{n-1}$) in graphics rendering

A 3D spatial voxel rendering engine evaluates volumetric shader workloads scaling cubically with grid resolution $k$: $W(k) = k^3$. Determine the marginal workload growth rate $W'(k)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the power function $W(k) = k^3$ where exponent $n = 3$.

**Step 2.** Apply the Power Rule $W'(k) = 3k^{3-1}$:
$$W'(k) = 3k^2$$

*Why it works:* Increasing voxel resolution by 1 unit along all three axes creates an incremental workload proportional to the surface area $3k^2$ of the bounding grid.

### Example 6: Square Root Rule ($\sqrt{x} \to \frac{1}{2\sqrt{x}}$) in cache latency

The average lookup latency $L(s)$ (in milliseconds) of a compressed search tree varies with index cache allocation $s$ (in MB) as $L(s) = \sqrt{s}$. Determine the marginal latency sensitivity $L'(s)$ with respect to cache memory.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Apply strategy S2 to rewrite the radical into a fractional power: $L(s) = s^{1/2}$.

**Step 2.** Differentiate using the Power Rule with $n = \frac{1}{2}$:
$$L'(s) = \frac{1}{2}s^{-1/2} = \frac{1}{2\sqrt{s}}$$

*Why it works:* As cache allocation $s$ becomes large, the denominator $2\sqrt{s}$ grows, driving $L'(s)$ toward 0. This mathematically captures diminishing returns: adding 1 MB to a small cache yields large benefits, while adding 1 MB to a large cache produces negligible returns.

### Example 7: Natural Exponential ($e^x \to e^x$) in viral product adoption

A high-virality social platform experiences early compounding user growth modeled by $U(t) = e^t$, where $t$ is measured in months. Determine the instantaneous user growth velocity $U'(t)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the natural exponential function with base $e$.

**Step 2.** Differentiate using the exponential rule:
$$U'(t) = e^t$$

*Why it works:* For base $e$, the instantaneous rate of new user signups $U'(t)$ is equal to the current user population $U(t)$ at every instant.

### Example 8: General Exponential ($a^x \to a^x \ln(a)$) in binary branching

A distributed consensus network creates a binary partition tree where server node count doubles at each hierarchy depth $d$: $N(d) = 2^d$. Determine the marginal node generation rate $N'(d)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the general exponential function $a^d$ with constant base $a = 2$.

**Step 2.** Differentiate using the general exponential rule:
$$N'(d) = 2^d \ln(2)$$

*Why it works:* Unlike base $e$ where $\ln(e) = 1$, base-2 doubling scales the instantaneous growth rate by the conversion factor $\ln(2) \approx 0.6931$.

### Example 9: Natural Logarithm ($\ln(x) \to \frac{1}{x}$) in customer utility

In product economics, the perceived cumulative utility $U(f)$ of adding features $f$ to a software suite exhibits logarithmic returns: $U(f) = \ln(f)$ for $f \ge 1$. Determine the marginal utility yield $U'(f)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the natural logarithm function.

**Step 2.** Differentiate:
$$U'(f) = \frac{1}{f}$$

*Why it works:* Shipping the second feature yields marginal utility $U'(2) = 0.5$, whereas shipping feature 100 yields marginal utility $U'(100) = 0.01$, guiding executive decisions on feature bloat versus product simplification.

### Example 10: General Logarithm ($\log_a(x) \to \frac{1}{x \ln(a)}$) in binary tree search

The search depth $D(n)$ of a balanced binary search tree containing $n$ records is $D(n) = \log_2(n)$. Determine the marginal search depth increase $D'(n)$ as records accumulate.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the base-2 logarithm function.

**Step 2.** Differentiate using the general logarithm rule:
$$D'(n) = \frac{1}{n \ln(2)}$$

*Why it works:* In a database with $n = 1{,}000{,}000$ records, the marginal search depth cost of inserting an additional record is $D'(10^6) \approx \frac{1}{693{,}147}$ steps, demonstrating the logarithmic scalability of indexed systems.

### Example 11: Sine Function ($\sin(x) \to \cos(x)$) in diurnal server traffic

Daily server CPU utilization fluctuates sinusoidally over a normalized 24-hour business cycle according to $C(t) = \sin(t)$, where $t \in [0, 2\pi]$. Find the rate of change of CPU utilization $C'(t)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the trigonometric sine function.

**Step 2.** Differentiate:
$$C'(t) = \cos(t)$$

*Why it works:* CPU utilization accelerates fastest at the start of the morning shift ($t = 0$, where $C'(0) = \cos(0) = 1$), while rate of change stalls at peak midday utilization ($t = \frac{\pi}{2}$, where $C'(\frac{\pi}{2}) = 0$).

### Example 12: Cosine Function ($\cos(x) \to -\sin(x)$) in automated ad bidding

An automated programmatic advertising engine modulates spend multipliers cyclically around peak shopping hours using $B(t) = \cos(t)$. Find the bid adjustment velocity $B'(t)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the trigonometric cosine function.

**Step 2.** Differentiate:
$$B'(t) = -\sin(t)$$

*Why it works:* The negative sign reflects that immediately past peak midday spend ($t > 0$), bids must decrease to preserve budget efficiency.

### Example 13: Tangent Function ($\tan(x) \to \sec^2(x)$) in automated camera tracking

In an automated warehouse, an optical camera tracks an automated guided vehicle moving along a linear rail at unit distance. The lateral position of the vehicle is $y(\theta) = \tan(\theta)$ for $-\frac{\pi}{2} < \theta < \frac{\pi}{2}$. Determine the lateral tracking velocity $y'(\theta)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the tangent function.

**Step 2.** Differentiate:
$$y'(\theta) = \sec^2(\theta)$$

*Why it works:* As the vehicle approaches the camera's peripheral boundary ($\theta \to \frac{\pi}{2}$), $\sec^2(\theta) \to \infty$, showing that tracking speed must accelerate dramatically to keep the vehicle centered.

### Example 14: Secant Function ($\sec(x) \to \sec(x)\tan(x)$) in sensor rangefinder tracking

The direct line-of-sight distance $D(\theta)$ from a fixed LiDAR tower to a delivery drone navigating a lateral offset path is $D(\theta) = \sec(\theta)$ for $-\frac{\pi}{2} < \theta < \frac{\pi}{2}$. Determine the rate of change of distance $D'(\theta)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the secant function.

**Step 2.** Differentiate:
$$D'(\theta) = \sec(\theta)\tan(\theta)$$

*Why it works:* Directly perpendicular to the tower ($\theta = 0$), $D'(0) = \sec(0)\tan(0) = (1)(0) = 0$, indicating a momentary stationary minimum distance.

### Example 15: Cosecant Function ($\csc(x) \to -\csc(x)\cot(x)$) in RF gain calibration

A ground-station radio antenna adjusts signal gain $G(\phi) = \csc(\phi)$ to compensate for atmospheric path attenuation as elevation angle $\phi$ changes ($0 < \phi < \pi$). Find the gain tuning sensitivity $G'(\phi)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the cosecant function.

**Step 2.** Differentiate:
$$G'(\phi) = -\csc(\phi)\cot(\phi)$$

*Why it works:* The negative derivative confirms that as the satellite rises higher into the sky ($\phi$ increasing), required signal gain drops smoothly.

### Example 16: Cotangent Function ($\cot(x) \to -\csc^2(x)$) in audio DSP filter phase

An audio digital signal processing filter exhibits a phase response curve $P(\omega) = \cot(\omega)$ across operating frequency band $\omega \in (0, \pi)$. Compute the rate of phase delay change $P'(\omega)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the cotangent function.

**Step 2.** Differentiate:
$$P'(\omega) = -\csc^2(\omega)$$

*Why it works:* Because $\csc^2(\omega) > 0$ for all valid $\omega$, $P'(\omega) = -\csc^2(\omega) < 0$ is strictly negative, ensuring monotonic phase response across the entire passband.

### Example 17: Inverse Sine ($\arcsin(x) \to \frac{1}{\sqrt{1-x^2}}$) in robotic arm kinematics

A robotic pick-and-place arm controls its shoulder joint angle $\theta(x) = \arcsin(x)$ to position a tool head at normalized horizontal offset $x \in (-1, 1)$. Compute the angular velocity sensitivity $\theta'(x)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the inverse sine function.

**Step 2.** Differentiate:
$$\theta'(x) = \frac{1}{\sqrt{1-x^2}}$$

*Why it works:* Near the center ($x \approx 0$), sensitivity is close to $1$. Near the physical boundary ($|x| \to 1$), the denominator approaches zero, requiring extremely rapid joint motor adjustments to maintain steady lateral velocity.

### Example 18: Inverse Cosine ($\arccos(x) \to -\frac{1}{\sqrt{1-x^2}}$) in solar panel tilt control

A solar tracking array adjusts panel inclination angle $\psi(s) = \arccos(s)$ based on normalized solar zenith ratio $s \in (-1, 1)$. Determine the adjustment rate $\psi'(s)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the inverse cosine function.

**Step 2.** Differentiate:
$$\psi'(s) = -\frac{1}{\sqrt{1-s^2}}$$

*Why it works:* The negative sign directs the automated actuator to decrease the tilt angle as the sun rises higher in the sky.

### Example 19: Inverse Tangent ($\arctan(x) \to \frac{1}{1+x^2}$) in neural network activation

A machine learning model uses the inverse tangent activation function $A(z) = \arctan(z)$ to map unbounded feature scores $z \in \mathbb{R}$ into bounded activation outputs. Determine the gradient sensitivity $A'(z)$ for backpropagation.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify the inverse tangent function.

**Step 2.** Differentiate:
$$A'(z) = \frac{1}{1+z^2}$$

*Why it works:* The gradient is maximum at $z = 0$ ($A'(0) = 1$) and smoothly damps toward $0$ for large outlier inputs ($|z| \gg 0$), preventing gradient explosion during training.

### Example 20: Constant Multiple Rule ($c \cdot f(x) \to c \cdot f'(x)$) in server cluster scaling

A cloud compute cluster consists of $c = 40$ identical virtual worker machines. Each machine draws energy $p(u) = u^2$ watts at CPU load $u$. The total cluster power is $E(u) = 40 u^2$. Find the marginal cluster power draw $E'(u)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Factor out the constant multiplier and differentiate $u^2$:
$$E'(u) = 40 \cdot (u^2)' = 40(2u) = 80u$$

*Why it works:* The entire cluster's marginal power increase is exactly 40 times that of an individual machine.

### Example 21: Sum Rule ($f(x) + g(x) \to f'(x) + g'(x)$) in operational expenditure

A fintech startup's total monthly operational cost $C(q)$ comprises transaction processing fees $F(q) = 0.04q$ and fraud dispute management costs $D(q) = 0.02q^2$ for monthly payment volume $q$: $C(q) = 0.04q + 0.02q^2$. Determine the marginal processing cost $C'(q)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Differentiate term by term using the Sum Rule:
$$C'(q) = F'(q) + D'(q) = 0.04(1) + 0.02(2q) = 0.04 + 0.04q$$

*Why it works:* The total marginal cost is the direct sum of each component's individual marginal rate.

### Example 22: Difference Rule ($f(x) - g(x) \to f'(x) - g'(x)$) in SaaS profit optimization

A B2B SaaS platform generates annual subscription revenue $R(x) = 150x$ and incurs onboarding and customer success costs $C(x) = 3x^2$ for $x$ enterprise clients. Net profit is $P(x) = 150x - 3x^2$. Determine the marginal profit rate $P'(x)$ and identify the client capacity where marginal profit is zero.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Apply the Difference Rule $P'(x) = R'(x) - C'(x)$.

**Step 2.** Differentiate each term:
$$P'(x) = 150 - 3(2x) = 150 - 6x$$

**Step 3.** Set $P'(x) = 0$ to find optimal client capacity:
$$150 - 6x = 0 \implies x = 25$$

*Why it works:* Beyond 25 clients, customization and support overhead grow faster than revenue ($P'(x) < 0$), showing executive leadership where to enforce self-serve onboarding.

### Example 23: Product Rule ($fg \to f'g + fg'$) in subscription revenue growth

A SaaS business model models monthly recurring revenue as $R(t) = S(t) \cdot A(t)$, where total subscriber count $S(t) = 500 + 40t$ grows over months $t$, while average revenue per user (ARPU) shifts due to tier discounts as $A(t) = 60 - t$. Determine the instantaneous revenue growth rate $R'(t)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify factor functions $S(t) = 500 + 40t$ and $A(t) = 60 - t$. Compute their derivatives: $S'(t) = 40$ and $A'(t) = -1$.

**Step 2.** Apply the Product Rule formula $R'(t) = S'(t)A(t) + S(t)A'(t)$:
$$R'(t) = (40)(60 - t) + (500 + 40t)(-1)$$

**Step 3.** Expand and collect like terms:
$$R'(t) = 2400 - 40t - 500 - 40t = 1900 - 80t$$

*Why it works:* Total revenue change decomposes into two distinct business drivers: revenue gained from acquiring new subscribers ($S'A$) and revenue lost due to promotional discounting on existing volume ($SA'$).

### Example 24: Quotient Rule in microservice energy efficiency

A microservice cluster's computational efficiency $E(t)$ is defined as requests processed $T(t) = 80t$ divided by electrical wattage consumed $P(t) = t^2 + 16$: $E(t) = \frac{80t}{t^2 + 16}$. Compute the rate of efficiency change $E'(t)$ over operating clock frequency $t$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify numerator $T(t) = 80t \implies T'(t) = 80$ and denominator $P(t) = t^2 + 16 \implies P'(t) = 2t$.

**Step 2.** Apply the Quotient Rule formula $E'(t) = \frac{T'(t)P(t) - T(t)P'(t)}{[P(t)]^2}$:
$$E'(t) = \frac{80(t^2 + 16) - (80t)(2t)}{(t^2 + 16)^2}$$

**Step 3.** Expand and simplify the numerator:
$$E'(t) = \frac{80t^2 + 1280 - 160t^2}{(t^2 + 16)^2} = \frac{1280 - 80t^2}{(t^2 + 16)^2}$$

*Why it works:* Efficiency improves while $1280 - 80t^2 > 0$ ($t < 4$) and peaks when $E'(t) = 0$ at $t = 4$, providing infrastructure engineers the exact optimal clock speed for green computing.

### Example 25: Reciprocal Rule in database connection pool latency

In a high-throughput relational database, average query wait latency $L(c)$ (in seconds) depends on dedicated connection pool capacity $c$ as $L(c) = \frac{1}{c}$ for $c > 0$. Compute the latency sensitivity $L'(c)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Apply the Reciprocal Rule $(1/f)' = -\frac{f'}{f^2}$ with $f(c) = c$ and $f'(c) = 1$:
$$L'(c) = -\frac{1}{c^2}$$

*Why it works:* When capacity is small ($c = 2$), adding a connection reduces latency rapidly ($L'(2) = -0.25$ s). When capacity is large ($c = 50$), adding another connection has virtually no impact ($L'(50) = -0.0004$ s).

### Example 26: Chain Rule in marketing-driven infrastructure costs

A cloud platform's monthly hosting cost $C(u)$ scales with active users $u$ as $C(u) = 200\sqrt{u}$. Marketing ad spend $m$ expands active users according to $u(m) = 5m + 100$. Determine the marginal infrastructure cost with respect to marketing spend: $C'(m)$.

*Try it first before reading the solution.*

**Solution.**

**Step 1.** Identify inner function $u(m) = 5m + 100$ and outer function $C(u) = 200u^{1/2}$.

**Step 2.** Compute the inner derivative: $u'(m) = 5$. Compute the outer derivative: $C'(u) = 200\left(\frac{1}{2}u^{-1/2}\right) = \frac{100}{\sqrt{u}}$.

**Step 3.** Apply the Chain Rule $C'(m) = C'(u(m)) \cdot u'(m)$:
$$C'(m) = \frac{100}{\sqrt{5m + 100}} \cdot 5 = \frac{500}{\sqrt{5m + 100}}$$

*Why it works:* The Chain Rule chains the marketing conversion velocity ($u'$) to the technical infrastructure cost curve ($C'$), allowing financial teams to budget infrastructure growth directly from marketing spend.

## Exercises

### Q1

**1.** Differentiate $f(x) = 5x^4 - 2x + \frac{3}{x^2}$. Express the derivative $f'(x)$ in simplified form.

**2.** Differentiate $g(x) = 6\sqrt{x} - e^3 + \ln(x)$ for $x > 0$. Express the derivative $g'(x)$ in simplified form.

**3.** Differentiate $h(x) = 4\cos(x) - 2\sin(x) + 3e^x$. Express the derivative $h'(x)$ in simplified form.

### Q2

**1.** Determine the derivative of the function $f(x) = 2^x + x^2 + \pi^4$ with respect to $x$.

- A) $2^x + 2x$
- B) $2^x \ln(2) + 2x + 4\pi^3$
- C) $x \cdot 2^{x-1} + 2x + 4\pi^3$
- D) $\frac{2^x}{\ln(2)} + 2x$
- E) $2^x \ln(2) + 2x$

### Q3

**1.** Determine the derivative of the function $g(x) = x^3 \cos(x)$ with respect to $x$.

- A) $3x^2 - \sin(x)$
- B) $-3x^2 \sin(x)$
- C) $x^3 \cos(x) - 3x^2 \sin(x)$
- D) $3x^2 \cos(x) - x^3 \sin(x)$
- E) $3x^2 \cos(x) + x^3 \sin(x)$

### Q4

**1.** Compute the derivative of $f(x) = x^2 e^x$ using the Product Rule. Show the two product terms explicitly and write the factored final expression.

**2.** Compute the derivative of $g(x) = \frac{\sin(x)}{x^2 + 1}$ using the Quotient Rule. Express the derivative in simplified rational form.

**3.** Compute the derivative of $k(x) = \frac{1}{\cos(x)}$ for $x \neq \frac{\pi}{2} + k\pi$ using the Reciprocal Rule, and express the result in terms of $\sec(x)$ and $\tan(x)$.

### Q5

**1.** Differentiate the composite functions (a) $u(x) = \cos(5x)$ and (b) $v(x) = e^{-3x}$ showing the inner and outer derivative steps.

**2.** Differentiate $p(x) = (2x^3 - 1)^4$ using the Chain Rule (General Power Rule). Express the final derivative $p'(x)$ with factors factored completely.

**3.** Differentiate $q(x) = \ln(x^2 + 4)$ for all $x \in \mathbb{R}$ using the Chain Rule. Express the derivative as a single rational expression.

### Q6

**1.** Let $f(x) = x e^x$. Compute the derivative $f'(x)$, evaluate the slope $f'(0)$, and determine the standard slope-intercept equation of the tangent line to $y = f(x)$ at $x = 0$.

**2.** Let $g(x) = \frac{2x}{x+1}$ for $x \neq -1$. Compute the derivative $g'(x)$, evaluate the slope of the tangent line at $x = 1$, and state whether the function is increasing or decreasing at $x = 1$ based on the sign of $g'(1)$.
