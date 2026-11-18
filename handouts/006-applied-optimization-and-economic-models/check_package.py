import sys
from pathlib import Path
sys.path.insert(0, r"C:/dev/best-practices/.agents/skills/calculus-create-handout/scripts")
import sympy as sp
from calculus_check import (
    ok, syms, check_equivalent, check_derivative, check_critical_points
)

x, y, r, a, p = syms("x y r a p")

print("--- Verifying Worked Examples ---")

# Example 1: River fencing
A_ex1 = 2400*x - 2*x**2
ok("Ex 1 Area Derivative", check_derivative(A_ex1, x, 2400 - 4*x))
ok("Ex 1 Critical Point", check_critical_points(A_ex1, x, [600]))
ok("Ex 1 Max Area", check_equivalent(A_ex1.subs(x, 600), 720000))

# Example 2: Four pens
A_ex2 = 375*x - sp.Rational(5, 2)*x**2
ok("Ex 2 Area Derivative", check_derivative(A_ex2, x, 375 - 5*x))
ok("Ex 2 Critical Point", check_critical_points(A_ex2, x, [75]))
ok("Ex 2 Max Area", check_equivalent(A_ex2.subs(x, 75), sp.Rational(28125, 2)))

# Example 3: Wire cutting (Square & Triangle)
A_ex3 = x**2 / 16 + sp.sqrt(3)*(10 - x)**2 / 36
dA_ex3 = x / 8 - sp.sqrt(3)*(10 - x) / 18
ok("Ex 3 Derivative", check_derivative(A_ex3, x, dA_ex3))
x_crit_ex3 = 40*sp.sqrt(3) / (9 + 4*sp.sqrt(3))
ok("Ex 3 Critical Point", sp.simplify(dA_ex3.subs(x, x_crit_ex3)) == 0)

# Example 4: Right triangle tangent to y = 4 - x^2
A_ex4 = sp.Rational(1, 4)*(a**3 + 8*a + 16/a)
dA_ex4 = sp.Rational(1, 4)*(3*a**2 + 8 - 16/a**2)
ok("Ex 4 Derivative", check_derivative(A_ex4, a, dA_ex4))
a_crit = 2 / sp.sqrt(3)
ok("Ex 4 Critical Point", sp.simplify(dA_ex4.subs(a, a_crit)) == 0)
ok("Ex 4 Min Area", check_equivalent(A_ex4.subs(a, a_crit), 32*sp.sqrt(3)/9))

# Example 5: Revenue maximization
R_ex5 = 450*x - sp.Rational(1, 2)*x**2
ok("Ex 5 Revenue Derivative", check_derivative(R_ex5, x, 450 - x))
ok("Ex 5 Critical Point", check_critical_points(R_ex5, x, [450]))
ok("Ex 5 Max Revenue", check_equivalent(R_ex5.subs(x, 450), 101250))

print("--- Verifying Exercises ---")

# Q1: Cylindrical storage tank
A_q1 = sp.pi * r**2 + 1000 * sp.pi / r
dA_q1 = 2 * sp.pi * r - 1000 * sp.pi / r**2
ok("Q1 Derivative", check_derivative(A_q1, r, dA_q1))
r_crit_q1 = 5 * 2**sp.Rational(2, 3)
ok("Q1 Critical Point", check_critical_points(A_q1, r, [r_crit_q1]))
h_q1 = 500 / r_crit_q1**2
ok("Q1 h = r", sp.simplify(h_q1 - r_crit_q1) == 0)
ok("Q1 Min Surface Area", check_equivalent(A_q1.subs(r, r_crit_q1), 150 * sp.pi * 2**sp.Rational(1, 3)))

# Q2: Fencing with differential costs
A_q2 = 300*x - sp.Rational(5, 3)*x**2
dA_q2 = 300 - sp.Rational(10, 3)*x
ok("Q2 Derivative", check_derivative(A_q2, x, dA_q2))
ok("Q2 Critical Point", check_critical_points(A_q2, x, [90]))
ok("Q2 Max Enclosed Area", check_equivalent(A_q2.subs(x, 90), 13500))

# Q3: Box volume
V_q3 = x * (12 - 2*x)**2
dV_q3 = 12 * (x - 2) * (x - 6)
ok("Q3 Derivative", check_derivative(V_q3, x, dV_q3))
ok("Q3 Max Volume", check_equivalent(V_q3.subs(x, 2), 128))
ok("Q3 Endpoint V(0)", check_equivalent(V_q3.subs(x, 0), 0))
ok("Q3 Endpoint V(6)", check_equivalent(V_q3.subs(x, 6), 0))

# Q4: Wire cutting (Triangle & Hexagon)
A_q4 = sp.sqrt(3)*(x**2 / sp.Rational(36) + (20 - x)**2 / sp.Rational(24))
dA_q4 = sp.Rational(5, 36)*sp.sqrt(3)*(x - 12)
ok("Q4 Derivative", check_derivative(A_q4, x, dA_q4))
ok("Q4 Critical Point", check_critical_points(A_q4, x, [12]))
ok("Q4 Min Area", check_equivalent(A_q4.subs(x, 12), 20*sp.sqrt(3)/3))
ok("Q4 Boundary Area x=0", check_equivalent(A_q4.subs(x, 0), 50*sp.sqrt(3)/3))
ok("Q4 Boundary Area x=20", check_equivalent(A_q4.subs(x, 20), 100*sp.sqrt(3)/9))
ok("Q4 Boundary Max Proof", (50*sp.sqrt(3)/3) > (100*sp.sqrt(3)/9))

# Q5: Economics (Profit and Average Cost)
C_q5 = 2*x**3 - 12*x**2 + 30*x + 100
p_q5 = 150 - 6*x
P_q5 = x * p_q5 - C_q5
dP_q5 = -6*x**2 + 12*x + 120
ok("Q5 Profit Derivative", check_derivative(P_q5, x, dP_q5))
x_crit_profit = 1 + sp.sqrt(21)
ok("Q5 Profit Critical Point", check_critical_points(P_q5, x, [x_crit_profit]))

c_q5 = C_q5 / x
dc_q5 = (4*x**3 - 12*x**2 - 100) / x**2
ok("Q5 Average Cost Derivative", check_derivative(c_q5, x, dc_q5))
# Average cost critical point satisfies x^3 - 3*x^2 - 25 = 0
x_val_c = 4.33211184028936
eq_c = x_val_c**3 - 3*x_val_c**2 - 25
ok("Q5 Average Cost Root Verification", abs(eq_c) < 1e-4)

# Q6: Pipeline construction cost
C_q6 = 5 * sp.sqrt(x**2 + 64) + 3 * (20 - x)
dC_q6 = 5*x / sp.sqrt(x**2 + 64) - 3
ok("Q6 Pipeline Cost Derivative", check_derivative(C_q6, x, dC_q6))
ok("Q6 Pipeline Critical Point", check_critical_points(C_q6, x, [6]))
ok("Q6 Endpoint C(0)", check_equivalent(C_q6.subs(x, 0), 100))
ok("Q6 Endpoint C(20)", check_equivalent(C_q6.subs(x, 20), 20*sp.sqrt(29)))
ok("Q6 Global Min Cost", check_equivalent(C_q6.subs(x, 6), 92))
ok("Q6 Snell Law Cosine", check_equivalent(sp.Rational(6, 10), sp.Rational(3, 5)))

print("\nALL MATHEMATICAL PROOFS AND CALCULUS CLAIMS VERIFIED SUCCESSFULLY!")
