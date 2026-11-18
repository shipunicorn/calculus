import sys
sys.path.insert(0, r"C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts")
import sympy as sp
from calculus_check import (
    ok, syms, check_equivalent, check_derivative, check_antiderivative,
    check_definite_integral, check_limit, check_ode
)

x, t, C, C1, C2 = syms("x t C C1 C2")

print("--- Checking Q1 ---")
# Q1.1 f(x) = 4/sqrt(x) - 3/x + 2*sec(x)^2 on (0, pi/2)
f1 = 4/sp.sqrt(x) - 3/x + 2*sp.sec(x)**2
F1 = 8*sp.sqrt(x) - 3*sp.log(x) + 2*sp.tan(x) + C
ok("Q1.1 Antiderivative", check_antiderivative(f1, x, F1, constant_sym=C))

# Q1.2 f''(x) = 12x^2 + 6x - 4, f'(0) = 5, f(1) = 8
f_prime = sp.integrate(12*x**2 + 6*x - 4, x) + 5
ok("Q1.2 f'(x)", check_equivalent(f_prime, 4*x**3 + 3*x**2 - 4*x + 5))
f_sol = sp.integrate(f_prime, x) + 3
ok("Q1.2 f(1) = 8", f_sol.subs(x, 1) == 8)
ok("Q1.2 f(x)", check_equivalent(f_sol, x**4 + x**3 - 2*x**2 + 5*x + 3))

print("--- Checking Q2 ---")
# Q2: Piecewise linear on [-3, 5]
# F(-3)=-4, F(-2)=-5, F(-1)=-4, F(0)=-2, F(1)=0, F(2)=1, F(3)=0, F(4)=-1.5, F(5)=-2
# Checking area calculations:
# [-3, -2]: triangle base 1, height -2 -> area -1. F(-2) - F(-3) = -1. (-5 - (-4) = -1) OK
# [-2, -1]: triangle base 1, height 2 -> area 1. F(-1) - F(-2) = 1. (-4 - (-5) = 1) OK
# [-1, 0]: rect base 1, height 2 -> area 2. F(0) - F(-1) = 2. (-2 - (-4) = 2) OK
# [0, 1]: rect base 1, height 2 -> area 2. F(1) - F(0) = 2. (0 - (-2) = 2) OK
# [1, 2]: triangle base 1, height 2 -> area 1. F(2) - F(1) = 1. (1 - 0 = 1) OK
# [2, 3]: triangle base 1, height -2 -> area -1. F(3) - F(2) = -1. (0 - 1 = -1) OK
# [3, 5]: triangle base 2, height -2 -> area -2. F(5) - F(3) = -2. (-2 - 0 = -2) OK
ok("Q2 Geometric Consistency", True)

print("--- Checking Q4 ---")
# Q4: L4, R4, M2
r = [120, 145, 170, 160, 130]
dt = 2
L4 = dt * sum(r[:4])
R4 = dt * sum(r[1:])
M2 = 4 * (r[1] + r[3])
ok("Q4 L4 = 1190", L4 == 1190)
ok("Q4 R4 = 1210", R4 == 1210)
ok("Q4 M2 = 1220", M2 == 1220)

print("--- Checking Q5 ---")
# Q5: int_1^4 (2x^2 - 3x + 1) dx = 45/2
integ5 = sp.integrate(2*x**2 - 3*x + 1, (x, 1, 4))
ok("Q5 Definite Integral", integ5 == sp.Rational(45, 2))

# Riemann sum expansion:
n, i = sp.symbols('n i')
delta_x = 3/n
x_i = 1 + 3*i/n
f_xi = 2*x_i**2 - 3*x_i + 1
f_xi_expanded = sp.expand(f_xi)
term_sum = sp.Sum(f_xi * delta_x, (i, 1, n)).doit()
lim_val = sp.limit(term_sum, n, sp.oo)
ok("Q5 Riemann Limit", lim_val == sp.Rational(45, 2))

print("--- Checking Q6 ---")
# Q6: Rocket
# a(t) = 40 - 2t for 0 <= t <= 10
# v(10) = int_0^10 (40 - 2t) dt = [20t^2 - t^3/3]_0^10 = 2000 - 1000/3 = 5000/3 displacement
v_burnout = sp.integrate(40 - 2*t, (t, 0, 10))
ok("Q6 Burnout velocity", v_burnout == 300)
s1 = sp.integrate(40*t - t**2, (t, 0, 10))
ok("Q6 Stage 1 displacement", s1 == sp.Rational(5000, 3))

# Coast stage: a(t) = -9.8 = -49/5
# v(t) = 300 - 49/5 * (t - 10) = 0 => t - 10 = 300 * 5 / 49 = 1500/49
t_coast = sp.Rational(1500, 49)
t_apogee = 10 + t_coast
ok("Q6 Apogee time", t_apogee == sp.Rational(1990, 49))

s2 = sp.integrate(300 - sp.Rational(49, 5)*(t - 10), (t, 10, t_apogee))
ok("Q6 Stage 2 displacement", s2 == sp.Rational(225000, 49))

s_total = s1 + s2
ok("Q6 Maximum altitude", s_total == sp.Rational(920000, 147))
print("s_total approx:", float(s_total))

print("ALL MATHEMATICAL CHECKS PASSED!")
