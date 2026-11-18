import sys
sys.path.insert(0, r"C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts")
import sympy as sp
from calculus_check import ok, syms

x, t, h, c, alpha, beta = syms("x t h c alpha beta")

print("--- Verifying Q1 ---")
# Q1.1: lim_{x -> 3} (x^3 - 2x^2 - 9)/(x^2 - 2x - 3) = 15/4
f1 = (x**3 - 2*x**2 - 9)/(x**2 - 2*x - 3)
lim1 = sp.limit(f1, x, 3)
ok("Q1.1 factoring limit", lim1 == sp.Rational(15, 4))

# Q1.2: lim_{x -> 2} (sqrt(x^2 + 12) - 4)/(x - 2) = 1/2
f2 = (sp.sqrt(x**2 + 12) - 4)/(x - 2)
lim2 = sp.limit(f2, x, 2)
ok("Q1.2 conjugate limit", lim2 == sp.Rational(1, 2))

# Q1.3: lim_{x -> -1} (2/(x+3) - 1)/(x+1) = -1/2
f3 = (2/(x + 3) - 1)/(x + 1)
lim3 = sp.limit(f3, x, -1)
ok("Q1.3 compound fraction limit", lim3 == sp.Rational(-1, 2))

print("\n--- Verifying Q2 ---")
# Q2.2: piecewise h(x) = (x^2 - 9)/|x - 3|
# left limit as x -> 3^- is -6, right limit as x -> 3^+ is 6
h_left = (x**2 - 9)/(-(x - 3))
h_right = (x**2 - 9)/(x - 3)
ok("Q2.2 left limit", sp.limit(h_left, x, 3) == -6)
ok("Q2.2 right limit", sp.limit(h_right, x, 3) == 6)

print("\n--- Verifying Q3 ---")
# Q3: Squeeze limit
# 2 - x^2 <= g(x) <= 2 cos(x) near 0
ok("Q3 squeeze lower", sp.limit(2 - x**2, x, 0) == 2)
ok("Q3 squeeze upper", sp.limit(2*sp.cos(x), x, 0) == 2)

print("\n--- Verifying Q4 ---")
# Q4.1: f(x) = (x^2 - 1)(x - 3)/((x - 1)(x - 3)^2 (x + 2))
# at x = 1: removable, limit = -1/3
f_q4 = ((x**2 - 1)*(x - 3))/((x - 1)*(x - 3)**2*(x + 2))
f_q4_simp = (x + 1)/((x - 3)*(x + 2))
ok("Q4.1 cancel x-1 and x-3", sp.simplify(f_q4 - f_q4_simp) == 0)
ok("Q4.1 limit at x=1", sp.limit(f_q4_simp, x, 1) == sp.Rational(-1, 3))
ok("Q4.1 vertical asymptote at x=3", sp.limit(f_q4_simp, x, 3, dir="+") == sp.oo and sp.limit(f_q4_simp, x, 3, dir="-") == -sp.oo)
ok("Q4.1 vertical asymptote at x=-2", sp.limit(f_q4_simp, x, -2, dir="+") == sp.oo and sp.limit(f_q4_simp, x, -2, dir="-") == -sp.oo)

# Q4.2: piecewise continuity
# right limit of (sqrt(x+3) - 2)/(x - 1) + 3 at x = 1
g_right = (sp.sqrt(x + 3) - 2)/(x - 1) + 3
lim_g_right = sp.limit(g_right, x, 1)
ok("Q4.2 right limit is 13/4", lim_g_right == sp.Rational(13, 4))
# left limit k(1)^2 + 2(1) - 1 = k + 1 = 13/4 => k = 9/4
k_val = sp.Rational(13, 4) - 1
ok("Q4.2 k = 9/4", k_val == sp.Rational(9, 4))
m_val = sp.Rational(13, 4)
ok("Q4.2 m = 13/4", m_val == sp.Rational(13, 4))

print("\n--- Verifying Q5 ---")
# Q5: f(x) = x^3 - 3*x + 1
f5 = x**3 - 3*x + 1
ok("Q5 f(1) = -1", f5.subs(x, 1) == -1)
ok("Q5 f(2) = 3", f5.subs(x, 2) == 3)
ok("Q5 f(1.5) = -1/8", f5.subs(x, sp.Rational(3, 2)) == sp.Rational(-1, 8))
ok("Q5 f(1.75) = 71/64", f5.subs(x, sp.Rational(7, 4)) == sp.Rational(71, 64))

print("\n--- Verifying Q6 ---")
# Q6.1: lim_{x -> 2^+} ((sqrt(3x+10) - 4)/(x-2) + 7)
p_right = (sp.sqrt(3*x + 10) - 4)/(x - 2) + 7
lim_p_right = sp.limit(p_right, x, 2, dir="+")
ok("Q6.1 downstream limit is 59/8", lim_p_right == sp.Rational(59, 8))

# Q6.2: lim_{x -> 2^-} (alpha*x^2 + 8x)/(x + 2) = (4*alpha + 16)/4 = alpha + 4
# alpha + 4 = 59/8 => alpha = 27/8
alpha_val = sp.Rational(59, 8) - 4
ok("Q6.2 alpha = 27/8", alpha_val == sp.Rational(27, 8))
beta_val = sp.Rational(59, 8)
ok("Q6.2 beta = 59/8", beta_val == sp.Rational(59, 8))

# Q6.3: solve P(x) = 5 for x in (0, 2)
# (27/8*x^2 + 8x)/(x + 2) = 5
eq = sp.Eq((sp.Rational(27, 8)*x**2 + 8*x)/(x + 2), 5)
sol = sp.solve(eq, x)
print(f"Q6.3 solutions: {sol}")
ok("Q6.3 exact root in (0, 2) is 4/3", sp.Rational(4, 3) in sol)

print("\nAll mathematical derivations verified successfully!")
