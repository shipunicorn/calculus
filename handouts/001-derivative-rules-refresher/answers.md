---
title: "001: Derivative Rules Refresher — Answer Key"
---

# 001: Derivative Rules Refresher — Answer Key

## Exercises

### Q1

**1.** Apply strategy S2 to rewrite the reciprocal power as $f(x) = 5x^4 - 2x + 3x^{-2}$. Differentiating each term with the Power Rule yields:
$$f'(x) = 5(4x^3) - 2(1) + 3(-2x^{-3}) = 20x^3 - 2 - \frac{6}{x^3}$$

**2.** Rewrite the radical term as $g(x) = 6x^{1/2} - e^3 + \ln(x)$. Note that $e^3$ is a constant whose derivative is $0$. Differentiating term by term gives:
$$g'(x) = 6\left(\frac{1}{2}x^{-1/2}\right) - 0 + \frac{1}{x} = \frac{3}{\sqrt{x}} + \frac{1}{x}$$

**3.** Differentiate each term using trigonometric and exponential derivative formulas ($\frac{d}{dx}[\cos(x)] = -\sin(x)$, $\frac{d}{dx}[\sin(x)] = \cos(x)$, $\frac{d}{dx}[e^x] = e^x$):
$$h'(x) = 4(-\sin(x)) - 2(\cos(x)) + 3(e^x) = -4\sin(x) - 2\cos(x) + 3e^x$$

### Q2

**1. Correct answer: E.**

- **A (Incorrect):** Omits the factor of $\ln(2)$ required when differentiating a general exponential function $a^x$.
- **B (Incorrect):** Correctly differentiates $2^x$ and $x^2$ but differentiates the constant term $\pi^4$ as $4\pi^3$ instead of $0$.
- **C (Incorrect):** Treats the exponential $2^x$ with the Power Rule as $x \cdot 2^{x-1}$ and treats the constant $\pi^4$ as a power function yielding $4\pi^3$.
- **D (Incorrect):** Divides by $\ln(2)$ instead of multiplying, confusing differentiation of exponential functions with integration.
- **E (Correct):** Evaluates the base-2 exponential derivative as $2^x \ln(2)$, differentiates $x^2$ to $2x$, and evaluates the derivative of constant $\pi^4$ as $0$.

### Q3

**1. Correct answer: D.**

- **A (Incorrect):** Differentiates each factor and adds the results rather than applying the Product Rule.
- **B (Incorrect):** Differentiates both factors directly without applying the Product Rule, multiplying $(x^3)'$ by $(\cos(x))'$.
- **C (Incorrect):** Inverts which factor receives the negative sign, attaching the negative sign to the derivative of $x^3$.
- **D (Correct):** Applies the Product Rule $(fg)' = f'g + fg'$ with $f'=3x^2$ and $g'=-\sin(x)$ to obtain $3x^2 \cos(x) - x^3 \sin(x)$.
- **E (Incorrect):** Applies the Product Rule but drops the negative sign required when differentiating cosine, writing $(\cos(x))' = \sin(x)$.

### Q4

**1.** With factor functions $u(x) = x^2$ and $v(x) = e^x$, the derivatives are $u'(x) = 2x$ and $v'(x) = e^x$. Applying the Product Rule $f'(x) = u'v + uv'$:
$$f'(x) = (2x)e^x + x^2(e^x) = (x^2 + 2x)e^x = x(x+2)e^x$$

**2.** With numerator $u(x) = \sin(x)$ and denominator $v(x) = x^2 + 1$, the derivatives are $u' = \cos(x)$ and $v' = 2x$. Applying the Quotient Rule:
$$g'(x) = \frac{\cos(x)(x^2 + 1) - \sin(x)(2x)}{(x^2 + 1)^2} = \frac{(x^2 + 1)\cos(x) - 2x\sin(x)}{(x^2 + 1)^2}$$

**3.** Apply the Reciprocal Rule $\frac{d}{dx}\left[\frac{1}{f(x)}\right] = -\frac{f'(x)}{[f(x)]^2}$ with $f(x) = \cos(x)$ and $f'(x) = -\sin(x)$:
$$k'(x) = -\frac{-\sin(x)}{\cos^2(x)} = \frac{1}{\cos(x)} \cdot \frac{\sin(x)}{\cos(x)} = \sec(x)\tan(x)$$
This directly confirms the standard differentiation formula $\frac{d}{dx}[\sec(x)] = \sec(x)\tan(x)$.

### Q5

**1.** Differentiate each composite function using the Chain Rule:
- (a) For $u(x) = \cos(5x)$, the inner derivative is $\frac{d}{dx}[5x] = 5$, giving $u'(x) = -\sin(5x) \cdot 5 = -5\sin(5x)$.
- (b) For $v(x) = e^{-3x}$, the inner derivative is $\frac{d}{dx}[-3x] = -3$, giving $v'(x) = e^{-3x} \cdot (-3) = -3e^{-3x}$.

**2.** Apply the General Power Rule $\frac{d}{dx}[u^n] = n u^{n-1} \cdot u'$ with $u = 2x^3 - 1$, $n = 4$, and inner derivative $u' = 6x^2$:
$$p'(x) = 4(2x^3 - 1)^3 \cdot (6x^2) = 24x^2(2x^3 - 1)^3$$

**3.** Apply the logarithmic Chain Rule $\frac{d}{dx}[\ln(u)] = \frac{u'}{u}$ with $u = x^2 + 4$ (noting $x^2 + 4 > 0$ for all $x \in \mathbb{R}$) and $u' = 2x$:
$$q'(x) = \frac{2x}{x^2 + 4}$$

### Q6

**1.** Differentiating $f(x) = x e^x$ with the Product Rule gives $f'(x) = (1)e^x + x(e^x) = (x+1)e^x$. At $x = 0$, the slope is $m = f'(0) = (0+1)e^0 = 1$, and the tangency coordinate is $(0, f(0)) = (0, 0)$. Point-slope form gives $y - 0 = 1(x - 0)$, so the tangent line equation is $y = x$.

**2.** Differentiating $g(x) = \frac{2x}{x+1}$ with the Quotient Rule gives:
$$g'(x) = \frac{2(x+1) - 2x(1)}{(x+1)^2} = \frac{2}{(x+1)^2}$$
At $x = 1$, the tangent line slope is $g'(1) = \frac{2}{(1+1)^2} = \frac{2}{4} = \frac{1}{2}$. Because $g'(1) = \frac{1}{2} > 0$, the function $g(x)$ is strictly increasing at $x = 1$.
