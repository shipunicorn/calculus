import os
import math

OUTPUT_DIR = r"C:\dev\calculus\figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT = 'font-family="Aptos, \'Segoe UI\', sans-serif"'

def svg_wrapper(width, height, content):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #ffffff; display: block; margin: 0 auto;">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b" />
  </marker>
  <marker id="arrow-pink" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#db2777" />
  </marker>
  <marker id="arrow-sky" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0284c7" />
  </marker>
  <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#16a34a" />
  </marker>
</defs>
{content}
</svg>'''

# -------------------------------------------------------------
# 1. Figure 10: Cubic, First Derivative, and Second Derivative
# f(x) = x^3 - x, f'(x) = 3x^2 - 1, f''(x) = 6x
# -------------------------------------------------------------
def make_fig10_cubic_derivatives():
    w, h = 480, 340
    ox, oy = 240, 170
    ux, uy = 100, 45

    # Axes
    content = [
        f'<line x1="{ox - 180}" y1="{oy}" x2="{ox + 190}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="{oy + 140}" x2="{ox}" y2="{oy - 150}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="{ox + 195}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>',
        f'<text x="{ox - 16}" y="{oy - 145}" {FONT} font-size="12" font-style="italic">y</text>',
        f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>',
    ]

    # Ticks
    for tx in [-1, 1]:
        px = ox + tx * ux
        content.append(f'<line x1="{px}" y1="{oy - 3}" x2="{px}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />')
        content.append(f'<text x="{px - 4}" y="{oy + 16}" {FONT} font-size="11">{tx}</text>')
    for ty in [-2, -1, 1, 2]:
        py = oy - ty * uy
        content.append(f'<line x1="{ox - 3}" y1="{py}" x2="{ox + 3}" y2="{py}" stroke="#1e293b" stroke-width="1.2" />')
        content.append(f'<text x="{ox - 18}" y="{py + 4}" {FONT} font-size="11">{ty}</text>')

    # 1. f(x) = x^3 - x
    pts_f = []
    for s in range(-160, 161):
        x = s * 0.01
        y = x**3 - x
        px = ox + x * ux
        py = oy - y * uy
        if 20 <= py <= h - 30:
            pts_f.append(f"{px:.1f},{py:.1f}")
    content.append(f'<path d="M {" L ".join(pts_f)}" fill="none" stroke="#0284c7" stroke-width="2.2" />')
    content.append(f'<text x="{ox + 1.25*ux}" y="{oy - 1.2*uy}" {FONT} font-size="12" font-weight="bold" fill="#0284c7">f(x) = x³ - x</text>')

    # 2. f'(x) = 3x^2 - 1
    pts_df = []
    for s in range(-120, 121):
        x = s * 0.01
        y = 3 * x**2 - 1
        px = ox + x * ux
        py = oy - y * uy
        if 20 <= py <= h - 30:
            pts_df.append(f"{px:.1f},{py:.1f}")
    content.append(f'<path d="M {" L ".join(pts_df)}" fill="none" stroke="#db2777" stroke-width="2.2" />')
    content.append(f'<text x="{ox - 1.4*ux}" y="{oy - 2.1*uy}" {FONT} font-size="12" font-weight="bold" fill="#db2777">f\'(x) = 3x² - 1</text>')

    # 3. f''(x) = 6x
    lx1 = ox - 0.45 * ux
    ly1 = oy - (6 * -0.45) * uy
    lx2 = ox + 0.45 * ux
    ly2 = oy - (6 * 0.45) * uy
    content.append(f'<line x1="{lx1:.1f}" y1="{ly1:.1f}" x2="{lx2:.1f}" y2="{ly2:.1f}" stroke="#16a34a" stroke-width="2.0" />')
    content.append(f'<text x="{lx2 + 8}" y="{ly2 + 4}" {FONT} font-size="12" font-weight="bold" fill="#16a34a">f\'\'(x) = 6x</text>')

    # Caption
    content.append(f'<text x="25" y="325" {FONT} font-size="12" font-weight="bold" fill="#1e293b">FIGURE 10: Graphs of f, f\', and f\'\' for f(x) = x³ - x</text>')
    return svg_wrapper(w, h, "\n".join(content))


# -------------------------------------------------------------
# 2. Section 2.2 Exercise 1 Grid
# -------------------------------------------------------------
def make_sec2_2_ex1_grid():
    w, h = 420, 320
    ox, oy = 210, 160
    u = 24  # grid unit size (pixels)

    content = []
    # Grid lines (-5 to 5 horizontally, -4 to 4 vertically)
    for i in range(-5, 6):
        gx = ox + i * u
        content.append(f'<line x1="{gx}" y1="{oy - 4*u}" x2="{gx}" y2="{oy + 4*u}" stroke="#cbd5e1" stroke-width="1.0" />')
    for j in range(-4, 5):
        gy = oy + j * u
        content.append(f'<line x1="{ox - 5*u}" y1="{gy}" x2="{ox + 5*u}" y2="{gy}" stroke="#cbd5e1" stroke-width="1.0" />')

    # Axes
    content.append(f'<line x1="{ox - 5*u - 15}" y1="{oy}" x2="{ox + 5*u + 20}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />')
    content.append(f'<line x1="{ox}" y1="{oy + 4*u + 15}" x2="{ox}" y2="{oy - 4*u - 20}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />')
    content.append(f'<text x="{ox + 5*u + 25}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>')
    content.append(f'<text x="{ox - 15}" y="{oy - 4*u - 15}" {FONT} font-size="12" font-style="italic">y</text>')

    # Labels
    content.append(f'<text x="{ox + u - 3}" y="{oy + 16}" {FONT} font-size="11">1</text>')
    content.append(f'<text x="{ox - 14}" y="{oy - u + 4}" {FONT} font-size="11">1</text>')

    # Curve y = f(x):
    # From book drawing: Bézier path
    # ox=153.1, oy=460.2, step=12
    # In grid units:
    # (-4, -1.6) -> (-2, -2.0) [min, m=0] -> (0, 0) [inflection, m~2] -> (2, 2.0) [max, m=0] -> (4, 1.6)
    pts = []
    # Spline through key points: (-4, -1.7), (-3, -1.9), (-2, -2.0), (-1, -1.4), (0, 0), (1, 1.4), (2, 2.0), (3, 1.9), (4, 1.6)
    d_path = f"M {ox - 4*u} {oy + 1.65*u} C {ox - 3.2*u} {oy + 1.85*u}, {ox - 2.5*u} {oy + 2.0*u}, {ox - 2.0*u} {oy + 2.0*u} C {ox - 1.2*u} {oy + 2.0*u}, {ox - 0.6*u} {oy + 1.2*u}, {ox} {oy} C {ox + 0.6*u} {oy - 1.2*u}, {ox + 1.2*u} {oy - 2.0*u}, {ox + 2.0*u} {oy - 2.0*u} C {ox + 2.5*u} {oy - 2.0*u}, {ox + 3.2*u} {oy - 1.85*u}, {ox + 4*u} {oy - 1.65*u}"
    content.append(f'<path d="{d_path}" fill="none" stroke="#0284c7" stroke-width="2.2" />')

    # Dots at key integer x values
    key_x = [-3, -2, -1, 0, 1, 2, 3]
    for kx in key_x:
        # approximate y
        if kx == -3: ky = -1.9
        elif kx == -2: ky = -2.0
        elif kx == -1: ky = -1.4
        elif kx == 0: ky = 0.0
        elif kx == 1: ky = 1.4
        elif kx == 2: ky = 2.0
        elif kx == 3: ky = 1.9
        px = ox + kx * u
        py = oy - ky * u
        content.append(f'<circle cx="{px}" cy="{py}" r="3" fill="#0284c7" />')

    content.append(f'<text x="25" y="305" {FONT} font-size="12" font-weight="bold" fill="#1e293b">EXERCISE 1: Graph of y = f(x) on a Square Grid</text>')
    return svg_wrapper(w, h, "\n".join(content))


# -------------------------------------------------------------
# 3. Section 2.2 Exercise 2 Grid
# -------------------------------------------------------------
def make_sec2_2_ex2_grid():
    w, h = 460, 320
    ox, oy = 75, 175
    u = 24

    content = []
    # Grid lines (-1 to 8 horizontally, -3 to 3 vertically)
    for i in range(-1, 9):
        gx = ox + i * u
        content.append(f'<line x1="{gx}" y1="{oy - 3*u}" x2="{gx}" y2="{oy + 3*u}" stroke="#cbd5e1" stroke-width="1.0" />')
    for j in range(-3, 4):
        gy = oy + j * u
        content.append(f'<line x1="{ox - u}" y1="{gy}" x2="{ox + 8*u}" y2="{gy}" stroke="#cbd5e1" stroke-width="1.0" />')

    # Axes
    content.append(f'<line x1="{ox - u - 15}" y1="{oy}" x2="{ox + 8*u + 20}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />')
    content.append(f'<line x1="{ox}" y1="{oy + 3*u + 15}" x2="{ox}" y2="{oy - 3*u - 20}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />')
    content.append(f'<text x="{ox + 8*u + 25}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>')
    content.append(f'<text x="{ox - 15}" y="{oy - 3*u - 15}" {FONT} font-size="12" font-style="italic">y</text>')

    content.append(f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>')
    content.append(f'<text x="{ox + u - 3}" y="{oy + 16}" {FONT} font-size="11">1</text>')
    content.append(f'<text x="{ox - 14}" y="{oy - u + 4}" {FONT} font-size="11">1</text>')

    # Curve passes through: (0,0) [slope ~3], peak at (1, 2) [slope 0], root at (2.5, 0), valley at (5, -2) [slope 0], rises to (7, -1.6)
    d_path = f"M {ox} {oy} C {ox + 0.4*u} {oy - 1.4*u}, {ox + 0.6*u} {oy - 2.0*u}, {ox + 1.0*u} {oy - 2.0*u} C {ox + 1.6*u} {oy - 2.0*u}, {ox + 2.0*u} {oy - 0.8*u}, {ox + 2.5*u} {oy} C {ox + 3.2*u} {oy + 1.3*u}, {ox + 4.0*u} {oy + 2.0*u}, {ox + 5.0*u} {oy + 2.0*u} C {ox + 5.8*u} {oy + 2.0*u}, {ox + 6.6*u} {oy + 1.8*u}, {ox + 7.5*u} {oy + 1.5*u}"
    content.append(f'<path d="{d_path}" fill="none" stroke="#0284c7" stroke-width="2.2" />')

    # Points at 0, 1, 2, 3, 4, 5, 6, 7
    coords = [(0, 0), (1, 2.0), (2, 0.8), (3, -0.7), (4, -1.7), (5, -2.0), (6, -1.8), (7, -1.5)]
    for kx, ky in coords:
        px = ox + kx * u
        py = oy - ky * u
        content.append(f'<circle cx="{px}" cy="{py}" r="3" fill="#0284c7" />')

    content.append(f'<text x="25" y="305" {FONT} font-size="12" font-weight="bold" fill="#1e293b">EXERCISE 2: Graph of y = f(x) on a Square Grid</text>')
    return svg_wrapper(w, h, "\n".join(content))


# -------------------------------------------------------------
# 4. Section 2.2 Exercise 3 Matching (8 Subplots)
# -------------------------------------------------------------
def make_sec2_2_ex3_matching():
    w, h = 640, 320
    content = []

    # 4 columns, 2 rows
    # Col widths: ~150px each, gap 10px
    # Row 1: functions (a), (b), (c), (d)
    # Row 2: derivatives I, II, III, IV

    xs = [75, 230, 385, 540]
    y_row1 = 75
    y_row2 = 230

    def draw_mini_axes(cx, cy, label):
        return f'''
        <line x1="{cx - 65}" y1="{cy}" x2="{cx + 65}" y2="{cy}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
        <line x1="{cx}" y1="{cy + 55}" x2="{cx}" y2="{cy - 55}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
        <text x="{cx + 68}" y="{cy + 12}" {FONT} font-size="11" font-style="italic">x</text>
        <text x="{cx - 12}" y="{cy - 55}" {FONT} font-size="11" font-style="italic">y</text>
        <text x="{cx - 10}" y="{cy + 13}" {FONT} font-size="10">0</text>
        <text x="{cx - 65}" y="{cy - 50}" {FONT} font-size="12" font-weight="bold" fill="#1e293b">{label}</text>
        '''

    # --- Row 1: Functions ---
    # (a) Cubic-like: high on left, valley, peak, low on right
    content.append(draw_mini_axes(xs[0], y_row1, "(a)"))
    # path: starts (-50, -40), drops to min at (-25, 25), rises to max at (25, -25), drops to (50, 40)
    p_a = f"M {xs[0]-45} {y_row1-35} C {xs[0]-35} {y_row1+15}, {xs[0]-25} {y_row1+25}, {xs[0]-15} {y_row1+25} C {xs[0]} {y_row1+25}, {xs[0]+15} {y_row1-35}, {xs[0]+28} {y_row1-35} C {xs[0]+38} {y_row1-35}, {xs[0]+42} {y_row1+10}, {xs[0]+50} {y_row1+40}"
    content.append(f'<path d="{p_a}" fill="none" stroke="#0284c7" stroke-width="2.0" />')

    # (b) Piecewise linear: rises to peak, drops to corner, rises
    content.append(draw_mini_axes(xs[1], y_row1, "(b)"))
    p_b = f"M {xs[1]-50} {y_row1+5} L {xs[1]-20} {y_row1-35} L {xs[1]+25} {y_row1+30} L {xs[1]+55} {y_row1-5}"
    content.append(f'<path d="{p_b}" fill="none" stroke="#0284c7" stroke-width="2.0" />')

    # (c) Dip at origin: horizontal asymptotes y=0, smooth valley at x=0
    content.append(draw_mini_axes(xs[2], y_row1, "(c)"))
    p_c = f"M {xs[2]-55} {y_row1-3} C {xs[2]-25} {y_row1-3}, {xs[2]-15} {y_row1+22}, {xs[2]} {y_row1+22} C {xs[2]+15} {y_row1+22}, {xs[2]+25} {y_row1-3}, {xs[2]+55} {y_row1-3}"
    content.append(f'<path d="{p_c}" fill="none" stroke="#0284c7" stroke-width="2.0" />')

    # (d) Double peak (quartic-like): drops left, peaks left, valley at 0, peaks right, drops right
    content.append(draw_mini_axes(xs[3], y_row1, "(d)"))
    p_d = f"M {xs[3]-45} {y_row1+45} C {xs[3]-35} {y_row1-40}, {xs[3]-20} {y_row1-40}, {xs[3]} {y_row1-5} C {xs[3]+20} {y_row1-40}, {xs[3]+35} {y_row1-40}, {xs[3]+45} {y_row1+45}"
    content.append(f'<path d="{p_d}" fill="none" stroke="#0284c7" stroke-width="2.0" />')

    # --- Row 2: Derivatives ---
    # I: Derivative of (c) - negative left, rises to positive peak, drops to 0
    content.append(draw_mini_axes(xs[0], y_row2, "I"))
    p_I = f"M {xs[0]-55} {y_row2+3} C {xs[0]-35} {y_row2+5}, {xs[0]-15} {y_row2+20}, {xs[0]} {y_row2} C {xs[0]+15} {y_row2-20}, {xs[0]+35} {y_row2-5}, {xs[0]+55} {y_row2-3}"
    content.append(f'<path d="{p_I}" fill="none" stroke="#db2777" stroke-width="2.0" />')

    # II: Derivative of (a) - downward parabola: negative, positive, negative
    content.append(draw_mini_axes(xs[1], y_row2, "II"))
    p_II = f"M {xs[1]-40} {y_row2+45} C {xs[1]-20} {y_row2-40}, {xs[1]} {y_row2-40}, {xs[1]+40} {y_row2+45}"
    content.append(f'<path d="{p_II}" fill="none" stroke="#db2777" stroke-width="2.0" />')

    # III: Derivative of (d) - odd polynomial with 3 zeros
    content.append(draw_mini_axes(xs[2], y_row2, "III"))
    p_III = f"M {xs[2]-35} {y_row2-40} C {xs[2]-25} {y_row2+35}, {xs[2]-10} {y_row2+35}, {xs[2]} {y_row2} C {xs[2]+10} {y_row2-35}, {xs[2]+25} {y_row2-35}, {xs[2]+38} {y_row2+45}"
    content.append(f'<path d="{p_III}" fill="none" stroke="#db2777" stroke-width="2.0" />')

    # IV: Derivative of (b) - step function with jump discontinuities
    content.append(draw_mini_axes(xs[3], y_row2, "IV"))
    # segment 1: positive const
    content.append(f'<line x1="{xs[3]-50}" y1="{y_row2-20}" x2="{xs[3]-20}" y2="{y_row2-20}" stroke="#db2777" stroke-width="2.0" />')
    content.append(f'<circle cx="{xs[3]-20}" cy="{y_row2-20}" r="2.8" fill="#ffffff" stroke="#db2777" stroke-width="1.4" />')
    # segment 2: negative const
    content.append(f'<line x1="{xs[3]-20}" y1="{y_row2+20}" x2="{xs[3]+25}" y2="{y_row2+20}" stroke="#db2777" stroke-width="2.0" />')
    content.append(f'<circle cx="{xs[3]-20}" cy="{y_row2+20}" r="2.8" fill="#ffffff" stroke="#db2777" stroke-width="1.4" />')
    content.append(f'<circle cx="{xs[3]+25}" cy="{y_row2+20}" r="2.8" fill="#ffffff" stroke="#db2777" stroke-width="1.4" />')
    # segment 3: positive const
    content.append(f'<line x1="{xs[3]+25}" y1="{y_row2-20}" x2="{xs[3]+55}" y2="{y_row2-20}" stroke="#db2777" stroke-width="2.0" />')
    content.append(f'<circle cx="{xs[3]+25}" cy="{y_row2-20}" r="2.8" fill="#ffffff" stroke="#db2777" stroke-width="1.4" />')

    content.append(f'<text x="25" y="310" {FONT} font-size="12" font-weight="bold" fill="#1e293b">EXERCISE 3: Functions (a)–(d) and their Derivatives I–IV</text>')
    return svg_wrapper(w, h, "\n".join(content))


# -------------------------------------------------------------
# 5. Section 2.4 Exercise 72 Grid (P(x)=F(x)G(x), Q(x)=F(x)/G(x))
# -------------------------------------------------------------
def make_sec2_4_ex72_grid():
    w, h = 460, 320
    ox, oy = 60, 230
    u = 36  # 36 px per grid unit

    content = []
    # Grid lines (x from 0 to 9, y from 0 to 6)
    for i in range(0, 10):
        gx = ox + i * u
        content.append(f'<line x1="{gx}" y1="{oy - 6*u}" x2="{gx}" y2="{oy}" stroke="#cbd5e1" stroke-width="1.0" />')
    for j in range(0, 7):
        gy = oy - j * u
        content.append(f'<line x1="{ox}" y1="{gy}" x2="{ox + 9*u}" y2="{gy}" stroke="#cbd5e1" stroke-width="1.0" />')

    # Axes
    content.append(f'<line x1="{ox - 15}" y1="{oy}" x2="{ox + 9*u + 20}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />')
    content.append(f'<line x1="{ox}" y1="{oy + 15}" x2="{ox}" y2="{oy - 6*u - 20}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />')
    content.append(f'<text x="{ox + 9*u + 25}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>')
    content.append(f'<text x="{ox - 15}" y="{oy - 6*u - 15}" {FONT} font-size="12" font-style="italic">y</text>')

    content.append(f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>')
    content.append(f'<text x="{ox + u - 3}" y="{oy + 16}" {FONT} font-size="11">1</text>')
    content.append(f'<text x="{ox - 14}" y="{oy - u + 4}" {FONT} font-size="11">1</text>')

    # Function G(x) (blue): (0, 1) -> (4, 3) -> (8, 1/3)
    # At x=7, G(7) = 1!
    gx1, gy1 = ox, oy - 1 * u
    gx2, gy2 = ox + 4 * u, oy - 3 * u
    gx3, gy3 = ox + 8 * u, oy - (1.0/3.0) * u
    content.append(f'<line x1="{gx1}" y1="{gy1}" x2="{gx2}" y2="{gy2}" stroke="#0284c7" stroke-width="2.2" />')
    content.append(f'<line x1="{gx2}" y1="{gy2}" x2="{gx3}" y2="{gy3}" stroke="#0284c7" stroke-width="2.2" />')
    content.append(f'<text x="{ox + 5.5*u}" y="{oy - 2.0*u}" {FONT} font-size="12" font-weight="bold" fill="#0284c7">G</text>')

    # Function F(x) (pink):
    # Parabola from (0.5, 6) through (1, 4), min at (2, 3), up to (3, 4).
    # Then line from (3, 4) through (7, 5) to (8.5, 5.375).
    d_f_curve = f"M {ox + 0.5*u} {oy - 5.25*u} Q {ox + 2.0*u} {oy - 1.5*u}, {ox + 3.0*u} {oy - 4.0*u}"
    content.append(f'<path d="{d_f_curve}" fill="none" stroke="#db2777" stroke-width="2.2" />')
    fx1, fy1 = ox + 3 * u, oy - 4 * u
    fx2, fy2 = ox + 8.5 * u, oy - 5.375 * u
    content.append(f'<line x1="{fx1}" y1="{fy1}" x2="{fx2}" y2="{fy2}" stroke="#db2777" stroke-width="2.2" />')
    content.append(f'<text x="{ox + 3.6*u}" y="{oy - 4.3*u}" {FONT} font-size="12" font-weight="bold" fill="#db2777">F</text>')

    # Points of interest:
    # At x=2: F(2)=3, G(2)=2
    p_f2 = (ox + 2*u, oy - 3*u)
    p_g2 = (ox + 2*u, oy - 2*u)
    content.append(f'<circle cx="{p_f2[0]}" cy="{p_f2[1]}" r="3.5" fill="#db2777" />')
    content.append(f'<circle cx="{p_g2[0]}" cy="{p_g2[1]}" r="3.5" fill="#0284c7" />')
    content.append(f'<line x1="{ox + 2*u}" y1="{oy}" x2="{ox + 2*u}" y2="{oy - 3*u}" stroke="#64748b" stroke-width="1.0" stroke-dasharray="3 3" />')

    # At x=7: F(7)=5, G(7)=1
    p_f7 = (ox + 7*u, oy - 5*u)
    p_g7 = (ox + 7*u, oy - 1*u)
    content.append(f'<circle cx="{p_f7[0]}" cy="{p_f7[1]}" r="3.5" fill="#db2777" />')
    content.append(f'<circle cx="{p_g7[0]}" cy="{p_g7[1]}" r="3.5" fill="#0284c7" />')
    content.append(f'<line x1="{ox + 7*u}" y1="{oy}" x2="{ox + 7*u}" y2="{oy - 5*u}" stroke="#64748b" stroke-width="1.0" stroke-dasharray="3 3" />')

    content.append(f'<text x="25" y="305" {FONT} font-size="12" font-weight="bold" fill="#1e293b">EXERCISE 72: Functions F and G for Product and Quotient Rules</text>')
    return svg_wrapper(w, h, "\n".join(content))


# -------------------------------------------------------------
# 6. Section 2.5 Exercise 65 Grid (u=f(g), v=g(f), w=g(g))
# -------------------------------------------------------------
def make_sec2_5_ex65_grid():
    w, h = 440, 320
    ox, oy = 60, 235
    u = 36

    content = []
    # Grid lines (-1 to 7 horizontally, -1 to 6 vertically)
    for i in range(-1, 8):
        gx = ox + i * u
        content.append(f'<line x1="{gx}" y1="{oy - 6*u}" x2="{gx}" y2="{oy + u}" stroke="#cbd5e1" stroke-width="1.0" />')
    for j in range(-1, 7):
        gy = oy - j * u
        content.append(f'<line x1="{ox - u}" y1="{gy}" x2="{ox + 7*u}" y2="{gy}" stroke="#cbd5e1" stroke-width="1.0" />')

    # Axes
    content.append(f'<line x1="{ox - u - 15}" y1="{oy}" x2="{ox + 7*u + 20}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />')
    content.append(f'<line x1="{ox}" y1="{oy + u + 15}" x2="{ox}" y2="{oy - 6*u - 20}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />')
    content.append(f'<text x="{ox + 7*u + 25}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>')
    content.append(f'<text x="{ox - 15}" y="{oy - 6*u - 15}" {FONT} font-size="12" font-style="italic">y</text>')

    content.append(f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>')
    content.append(f'<text x="{ox + u - 3}" y="{oy + 16}" {FONT} font-size="11">1</text>')
    content.append(f'<text x="{ox - 14}" y="{oy - u + 4}" {FONT} font-size="11">1</text>')

    # Function f (pink): (-1, 1) -> (0, 0) -> (2, 4) -> (7, 2.75)
    f_pts = [(ox - u, oy - u), (ox, oy), (ox + 2*u, oy - 4*u), (ox + 7*u, oy - 2.75*u)]
    d_f = f"M {f_pts[0][0]} {f_pts[0][1]} L {f_pts[1][0]} {f_pts[1][1]} L {f_pts[2][0]} {f_pts[2][1]} L {f_pts[3][0]} {f_pts[3][1]}"
    content.append(f'<path d="{d_f}" fill="none" stroke="#db2777" stroke-width="2.2" />')
    content.append(f'<text x="{ox + 3.5*u}" y="{oy - 4.2*u}" {FONT} font-size="12" font-weight="bold" fill="#db2777">f</text>')

    # Function g (blue): (0, 6) -> (2, 0) -> (7, 3.33)
    g_pts = [(ox, oy - 6*u), (ox + 2*u, oy), (ox + 7*u, oy - (10.0/3.0)*u)]
    d_g = f"M {g_pts[0][0]} {g_pts[0][1]} L {g_pts[1][0]} {g_pts[1][1]} L {g_pts[2][0]} {g_pts[2][1]}"
    content.append(f'<path d="{d_g}" fill="none" stroke="#0284c7" stroke-width="2.2" />')
    content.append(f'<text x="{ox + 4.5*u}" y="{oy - 1.5*u}" {FONT} font-size="12" font-weight="bold" fill="#0284c7">g</text>')

    # Marked corner on g at (2, 0)
    content.append(f'<circle cx="{ox + 2*u}" cy="{oy}" r="3.5" fill="#0284c7" />')
    # Marked point at x=1 for f (1, 2) and g (1, 3)
    content.append(f'<circle cx="{ox + u}" cy="{oy - 2*u}" r="3.0" fill="#db2777" />')
    content.append(f'<circle cx="{ox + u}" cy="{oy - 3*u}" r="3.0" fill="#0284c7" />')
    content.append(f'<line x1="{ox + u}" y1="{oy}" x2="{ox + u}" y2="{oy - 3*u}" stroke="#64748b" stroke-width="1.0" stroke-dasharray="3 3" />')

    content.append(f'<text x="25" y="305" {FONT} font-size="12" font-weight="bold" fill="#1e293b">EXERCISE 65: Functions f and g for Composite Derivatives</text>')
    return svg_wrapper(w, h, "\n".join(content))


# -------------------------------------------------------------
# 7. Section 2.5 Exercise 66 Grid (h(x)=f(f(x)), g(x)=f(x^2))
# -------------------------------------------------------------
def make_sec2_5_ex66_grid():
    w, h = 420, 320
    ox, oy = 80, 220
    u = 36

    content = []
    # Grid lines (-1 to 5 horizontally, -1 to 5 vertically)
    for i in range(-1, 6):
        gx = ox + i * u
        content.append(f'<line x1="{gx}" y1="{oy - 5*u}" x2="{gx}" y2="{oy + u}" stroke="#cbd5e1" stroke-width="1.0" />')
    for j in range(-1, 6):
        gy = oy - j * u
        content.append(f'<line x1="{ox - u}" y1="{gy}" x2="{ox + 5*u}" y2="{gy}" stroke="#cbd5e1" stroke-width="1.0" />')

    # Axes
    content.append(f'<line x1="{ox - u - 15}" y1="{oy}" x2="{ox + 5*u + 20}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />')
    content.append(f'<line x1="{ox}" y1="{oy + u + 15}" x2="{ox}" y2="{oy - 5*u - 20}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />')
    content.append(f'<text x="{ox + 5*u + 25}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>')
    content.append(f'<text x="{ox - 15}" y="{oy - 5*u - 15}" {FONT} font-size="12" font-style="italic">y</text>')

    content.append(f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>')
    content.append(f'<text x="{ox + u - 3}" y="{oy + 16}" {FONT} font-size="11">1</text>')
    content.append(f'<text x="{ox - 14}" y="{oy - u + 4}" {FONT} font-size="11">1</text>')

    # Curve y = f(x):
    # Starts (-1, 2.5), peaks near (0, 3.0), drops through (1, 2.5), (2, 1.0) with slope -1,
    # reaches min around (2.3, 0.8), rises steeply through (3, 1.0) and (4, 3.0) with slope ~2, ends (4.5, 5.0).
    d_f = f"M {ox - u} {oy - 2.5*u} C {ox - 0.5*u} {oy - 2.9*u}, {ox - 0.2*u} {oy - 3.0*u}, {ox} {oy - 3.0*u} C {ox + 0.6*u} {oy - 3.0*u}, {ox + 1.2*u} {oy - 2.3*u}, {ox + 2.0*u} {oy - 1.0*u} C {ox + 2.3*u} {oy - 0.5*u}, {ox + 2.8*u} {oy - 0.5*u}, {ox + 3.2*u} {oy - 1.2*u} C {ox + 3.7*u} {oy - 2.2*u}, {ox + 4.0*u} {oy - 3.0*u}, {ox + 4.5*u} {oy - 5.0*u}"
    content.append(f'<path d="{d_f}" fill="none" stroke="#db2777" stroke-width="2.2" />')
    content.append(f'<text x="{ox + 1.6*u}" y="{oy - 3.2*u}" {FONT} font-size="12" font-weight="bold" fill="#db2777">y = f(x)</text>')

    # Key points: (2, 1) and (4, 3)
    content.append(f'<circle cx="{ox + 2*u}" cy="{oy - u}" r="3.5" fill="#db2777" />')
    content.append(f'<circle cx="{ox + 4*u}" cy="{oy - 3*u}" r="3.5" fill="#db2777" />')
    content.append(f'<line x1="{ox + 2*u}" y1="{oy}" x2="{ox + 2*u}" y2="{oy - u}" stroke="#64748b" stroke-width="1.0" stroke-dasharray="3 3" />')
    content.append(f'<line x1="{ox + 4*u}" y1="{oy}" x2="{ox + 4*u}" y2="{oy - 3*u}" stroke="#64748b" stroke-width="1.0" stroke-dasharray="3 3" />')

    content.append(f'<text x="25" y="305" {FONT} font-size="12" font-weight="bold" fill="#1e293b">EXERCISE 66: Graph of y = f(x) for Self-Composition</text>')
    return svg_wrapper(w, h, "\n".join(content))


# -------------------------------------------------------------
# 8. Section 2.5 Exercise 67 Grid (g(x)=sqrt(f(x)) at x=3)
# -------------------------------------------------------------
def make_sec2_5_ex67_grid():
    w, h = 440, 320
    ox, oy = 60, 235
    u = 36

    content = []
    # Grid lines (-1 to 7 horizontally, -1 to 5 vertically)
    for i in range(-1, 8):
        gx = ox + i * u
        content.append(f'<line x1="{gx}" y1="{oy - 5*u}" x2="{gx}" y2="{oy + u}" stroke="#cbd5e1" stroke-width="1.0" />')
    for j in range(-1, 6):
        gy = oy - j * u
        content.append(f'<line x1="{ox - u}" y1="{gy}" x2="{ox + 7*u}" y2="{gy}" stroke="#cbd5e1" stroke-width="1.0" />')

    # Axes
    content.append(f'<line x1="{ox - u - 15}" y1="{oy}" x2="{ox + 7*u + 20}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />')
    content.append(f'<line x1="{ox}" y1="{oy + u + 15}" x2="{ox}" y2="{oy - 5*u - 20}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />')
    content.append(f'<text x="{ox + 7*u + 25}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>')
    content.append(f'<text x="{ox - 15}" y="{oy - 5*u - 15}" {FONT} font-size="12" font-style="italic">y</text>')

    content.append(f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>')
    content.append(f'<text x="{ox + u - 3}" y="{oy + 16}" {FONT} font-size="11">1</text>')
    content.append(f'<text x="{ox - 14}" y="{oy - u + 4}" {FONT} font-size="11">1</text>')

    # Tangent line (cyan/blue): passes through (0, 4), (3, 2), (6, 0)
    tx1, ty1 = ox - 0.5 * u, oy - (4 - (-2.0/3.0)*(-0.5)) * u
    tx2, ty2 = ox + 6.8 * u, oy - (4 - (2.0/3.0)*6.8) * u
    content.append(f'<line x1="{tx1}" y1="{ty1}" x2="{tx2}" y2="{ty2}" stroke="#0284c7" stroke-width="2.0" />')

    # Function f(x) (pink): concave down, passes through (-1, 0.5), peak around (1.8, 2.3), touches line at (3, 2), valley/rises around x=6
    d_f = f"M {ox - u} {oy - 0.5*u} C {ox} {oy - 2.2*u}, {ox + 1.2*u} {oy - 2.4*u}, {ox + 2.0*u} {oy - 2.3*u} C {ox + 2.6*u} {oy - 2.2*u}, {ox + 3.0*u} {oy - 2.0*u}, {ox + 3.5*u} {oy - 1.5*u} C {ox + 4.2*u} {oy - 0.7*u}, {ox + 5.5*u} {oy + 0.8*u}, {ox + 6.2*u} {oy + 1.0*u} C {ox + 6.6*u} {oy + 0.8*u}, {ox + 6.8*u} {oy}, {ox + 7.0*u} {oy - 0.6*u}"
    content.append(f'<path d="{d_f}" fill="none" stroke="#db2777" stroke-width="2.2" />')
    content.append(f'<text x="{ox + 6.2*u}" y="{oy - 1.2*u}" {FONT} font-size="12" font-weight="bold" fill="#db2777">f</text>')

    # Point of tangency at (3, 2)
    px, py = ox + 3 * u, oy - 2 * u
    content.append(f'<circle cx="{px}" cy="{py}" r="3.5" fill="#1e293b" />')
    content.append(f'<line x1="{px}" y1="{oy}" x2="{px}" y2="{py}" stroke="#64748b" stroke-width="1.0" stroke-dasharray="3 3" />')
    content.append(f'<text x="{px + 8}" y="{py - 6}" {FONT} font-size="11" font-weight="bold" fill="#1e293b">(3, 2)</text>')

    content.append(f'<text x="25" y="305" {FONT} font-size="12" font-weight="bold" fill="#1e293b">EXERCISE 67: Curve y = f(x) and its Tangent Line at (3, 2)</text>')
    return svg_wrapper(w, h, "\n".join(content))


# -------------------------------------------------------------
# 9. Section 2.6 Figure 1: Circle and Semicircles (3 Subplots)
# -------------------------------------------------------------
def make_sec2_6_fig1_circle_semicircles():
    w, h = 640, 240
    content = []

    xs = [110, 320, 530]
    cy = 115
    r = 65  # represents 5 units

    def draw_circle_axes(cx, title):
        return f'''
        <line x1="{cx - 85}" y1="{cy}" x2="{cx + 85}" y2="{cy}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
        <line x1="{cx}" y1="{cy + 85}" x2="{cx}" y2="{cy - 85}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
        <text x="{cx + 88}" y="{cy + 12}" {FONT} font-size="11" font-style="italic">x</text>
        <text x="{cx - 12}" y="{cy - 85}" {FONT} font-size="11" font-style="italic">y</text>
        <text x="{cx - 10}" y="{cy + 13}" {FONT} font-size="10">0</text>
        <text x="{cx}" y="{cy + 105}" {FONT} font-size="12" text-anchor="middle" font-weight="bold" fill="#1e293b">{title}</text>
        '''

    # (a) x^2 + y^2 = 25 (Full circle, pink)
    content.append(draw_circle_axes(xs[0], "(a) x² + y² = 25"))
    content.append(f'<circle cx="{xs[0]}" cy="{cy}" r="{r}" fill="none" stroke="#db2777" stroke-width="2.2" />')

    # (b) f(x) = sqrt(25 - x^2) (Upper semicircle, sky blue)
    content.append(draw_circle_axes(xs[1], "(b) f(x) = √(25 - x²)"))
    d_semi_top = f"M {xs[1] - r} {cy} A {r} {r} 0 0 1 {xs[1] + r} {cy}"
    content.append(f'<path d="{d_semi_top}" fill="none" stroke="#0284c7" stroke-width="2.2" />')

    # (c) g(x) = -sqrt(25 - x^2) (Lower semicircle, green)
    content.append(draw_circle_axes(xs[2], "(c) g(x) = -√(25 - x²)"))
    d_semi_bot = f"M {xs[2] - r} {cy} A {r} {r} 0 0 0 {xs[2] + r} {cy}"
    content.append(f'<path d="{d_semi_bot}" fill="none" stroke="#16a34a" stroke-width="2.2" />')

    content.append(f'<text x="25" y="232" {FONT} font-size="12" font-weight="bold" fill="#1e293b">FIGURE 1: Implicit Curve x² + y² = 25 and its Explicit Semicircular Branches</text>')
    return svg_wrapper(w, h, "\n".join(content))


# -------------------------------------------------------------
# 10. Section 2.6 Figure 2: The Folium of Descartes
# x^3 + y^3 = 6xy
# -------------------------------------------------------------
def make_sec2_6_fig2_folium():
    w, h = 440, 360
    ox, oy = 180, 220
    u = 35  # pixels per unit

    content = []
    # Axes
    content.append(f'<line x1="{ox - 130}" y1="{oy}" x2="{ox + 220}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />')
    content.append(f'<line x1="{ox}" y1="{oy + 110}" x2="{ox}" y2="{oy - 190}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />')
    content.append(f'<text x="{ox + 225}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>')
    content.append(f'<text x="{ox - 15}" y="{oy - 185}" {FONT} font-size="12" font-style="italic">y</text>')
    content.append(f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>')

    # Ticks for 1, 2, 3
    for k in [1, 2, 3, 4]:
        px = ox + k * u
        content.append(f'<line x1="{px}" y1="{oy - 3}" x2="{px}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.0" />')
        content.append(f'<text x="{px - 3}" y="{oy + 16}" {FONT} font-size="10">{k}</text>')
        py = oy - k * u
        content.append(f'<line x1="{ox - 3}" y1="{py}" x2="{ox + 3}" y2="{py}" stroke="#1e293b" stroke-width="1.0" />')
        content.append(f'<text x="{ox - 14}" y="{py + 4}" {FONT} font-size="10">{k}</text>')

    # Parametric equations of folium:
    # x(t) = 3 a t / (1 + t^3), y(t) = 3 a t^2 / (1 + t^3), where 3a = 6 => a = 2.
    # So x(t) = 6t / (1 + t^3), y(t) = 6t^2 / (1 + t^3).
    # t in (-inf, -1) -> bottom right asymptote branch (x > 0, y < 0)
    # t in (-1, 0) -> upper left asymptote branch (x < 0, y > 0)
    # t in (0, inf) -> loop in quadrant 1!
    # Tip of loop at t = 1: x = 3, y = 3!

    # 1. Loop: t from 0 to 40 (covers the entire loop)
    loop_pts = []
    # denser near 0 and inf
    ts = [0.0]
    for step in range(1, 150):
        ts.append(step * 0.05)
    for step in range(150, 400):
        ts.append(7.5 + (step - 150) * 0.25)
    for t in ts:
        x = (6 * t) / (1 + t**3)
        y = (6 * t**2) / (1 + t**3)
        px = ox + x * u
        py = oy - y * u
        loop_pts.append(f"{px:.1f},{py:.1f}")
    content.append(f'<path d="M {" L ".join(loop_pts)}" fill="none" stroke="#db2777" stroke-width="2.2" />')

    # 2. Branch 1: t in (-0.95, 0.0) -> x < 0, y > 0
    b1_pts = []
    t_vals1 = [-0.01 * k for k in range(0, 85)]
    for t in t_vals1:
        x = (6 * t) / (1 + t**3)
        y = (6 * t**2) / (1 + t**3)
        px = ox + x * u
        py = oy - y * u
        if py >= 25 and px >= ox - 120:
            b1_pts.append(f"{px:.1f},{py:.1f}")
    if b1_pts:
        content.append(f'<path d="M {" L ".join(b1_pts)}" fill="none" stroke="#db2777" stroke-width="2.2" />')

    # 3. Branch 2: t in (-30.0, -1.05) -> x > 0, y < 0
    b2_pts = []
    t_vals2 = [-1.08 - 0.05 * k for k in range(0, 150)] + [-8.5 - 0.5 * k for k in range(0, 50)]
    for t in t_vals2:
        x = (6 * t) / (1 + t**3)
        y = (6 * t**2) / (1 + t**3)
        px = ox + x * u
        py = oy - y * u
        if py <= oy + 100 and px <= ox + 200:
            b2_pts.append(f"{px:.1f},{py:.1f}")
    if b2_pts:
        content.append(f'<path d="M {" L ".join(b2_pts)}" fill="none" stroke="#db2777" stroke-width="2.2" />')

    # Asymptote: x + y + 2 = 0 => y = -x - 2
    # For x = -4 => y = 2
    # For x = 2 => y = -4
    ax1, ay1 = ox - 3.5 * u, oy - (1.5) * u
    ax2, ay2 = ox + 2.5 * u, oy - (-4.5) * u
    content.append(f'<line x1="{ax1:.1f}" y1="{ay1:.1f}" x2="{ax2:.1f}" y2="{ay2:.1f}" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3" />')
    content.append(f'<text x="{ax1 + 10}" y="{ay1 - 6}" {FONT} font-size="11" fill="#64748b">Asymptote: x + y + 2 = 0</text>')

    # Point (3, 3)
    p3x = ox + 3 * u
    p3y = oy - 3 * u
    content.append(f'<circle cx="{p3x}" cy="{p3y}" r="3.5" fill="#1e293b" />')
    content.append(f'<text x="{p3x + 8}" y="{p3y + 4}" {FONT} font-size="11" font-weight="bold" fill="#1e293b">(3, 3)</text>')
    content.append(f'<text x="{ox + 1.2*u}" y="{oy - 3.5*u}" {FONT} font-size="12" font-weight="bold" fill="#db2777">x³ + y³ = 6xy</text>')

    content.append(f'<text x="25" y="345" {FONT} font-size="12" font-weight="bold" fill="#1e293b">FIGURE 2: The Folium of Descartes (x³ + y³ = 6xy)</text>')
    return svg_wrapper(w, h, "\n".join(content))


# -------------------------------------------------------------
# 11. Section 2.6 Figure 3: Three Functions Defined by the Folium
# -------------------------------------------------------------
def make_sec2_6_fig3_folium_branches():
    w, h = 640, 220
    content = []

    xs = [110, 320, 530]
    cy = 120
    u = 22

    def draw_mini_folium_axes(cx, title):
        return f'''
        <line x1="{cx - 75}" y1="{cy}" x2="{cx + 75}" y2="{cy}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
        <line x1="{cx}" y1="{cy + 75}" x2="{cx}" y2="{cy - 75}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
        <text x="{cx + 78}" y="{cy + 12}" {FONT} font-size="10" font-style="italic">x</text>
        <text x="{cx - 10}" y="{cy - 72}" {FONT} font-size="10" font-style="italic">y</text>
        <text x="{cx - 10}" y="{cy + 12}" {FONT} font-size="9">0</text>
        <text x="{cx}" y="{cy + 85}" {FONT} font-size="11" text-anchor="middle" font-weight="bold" fill="#1e293b">{title}</text>
        '''

    # Branch 1: Upper loop + upper-left branch (sky blue)
    content.append(draw_mini_folium_axes(xs[0], "Function 1: Upper Branch"))
    pts1 = []
    # from t = -0.85 to 1.0 (reaches max y)
    t_vals = [-0.85 + 0.02 * k for k in range(93)]
    for t in t_vals:
        x = (6 * t) / (1 + t**3)
        y = (6 * t**2) / (1 + t**3)
        px = xs[0] + x * u
        py = cy - y * u
        if -70 <= px - xs[0] <= 70 and -70 <= cy - py <= 70:
            pts1.append(f"{px:.1f},{py:.1f}")
    content.append(f'<path d="M {" L ".join(pts1)}" fill="none" stroke="#0284c7" stroke-width="2.0" />')

    # Branch 2: Lower loop (green)
    content.append(draw_mini_folium_axes(xs[1], "Function 2: Lower Loop"))
    pts2 = []
    # from t = 1.0 to 15.0
    t_vals = [1.0 + 0.05 * k for k in range(120)] + [7.0 + 0.5 * k for k in range(20)]
    for t in t_vals:
        x = (6 * t) / (1 + t**3)
        y = (6 * t**2) / (1 + t**3)
        px = xs[1] + x * u
        py = cy - y * u
        if -70 <= px - xs[1] <= 70 and -70 <= cy - py <= 70:
            pts2.append(f"{px:.1f},{py:.1f}")
    content.append(f'<path d="M {" L ".join(pts2)}" fill="none" stroke="#16a34a" stroke-width="2.0" />')

    # Branch 3: Lower right asymptote branch (orange)
    content.append(draw_mini_folium_axes(xs[2], "Function 3: Bottom Branch"))
    pts3 = []
    t_vals = [-1.15 - 0.05 * k for k in range(100)]
    for t in t_vals:
        x = (6 * t) / (1 + t**3)
        y = (6 * t**2) / (1 + t**3)
        px = xs[2] + x * u
        py = cy - y * u
        if -70 <= px - xs[2] <= 70 and -70 <= cy - py <= 70:
            pts3.append(f"{px:.1f},{py:.1f}")
    content.append(f'<path d="M {" L ".join(pts3)}" fill="none" stroke="#ea580c" stroke-width="2.0" />')

    content.append(f'<text x="25" y="212" {FONT} font-size="12" font-weight="bold" fill="#1e293b">FIGURE 3: Graphs of Three Functions Defined Implicitly by the Folium of Descartes</text>')
    return svg_wrapper(w, h, "\n".join(content))


# -------------------------------------------------------------
# 12. Section 2.6 Figure 4 & 5: Tangent Lines to the Folium
# Tangent at (3, 3) and horizontal tangent at (2^(4/3), 2^(5/3))
# -------------------------------------------------------------
def make_sec2_6_fig4_folium_tangents():
    w, h = 480, 360
    ox, oy = 180, 240
    u = 36

    content = []
    # Axes
    content.append(f'<line x1="{ox - 100}" y1="{oy}" x2="{ox + 250}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />')
    content.append(f'<line x1="{ox}" y1="{oy + 80}" x2="{ox}" y2="{oy - 210}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />')
    content.append(f'<text x="{ox + 255}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>')
    content.append(f'<text x="{ox - 15}" y="{oy - 205}" {FONT} font-size="12" font-style="italic">y</text>')
    content.append(f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>')

    # Ticks
    for k in [1, 2, 3, 4, 5]:
        px = ox + k * u
        content.append(f'<line x1="{px}" y1="{oy - 3}" x2="{px}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.0" />')
        content.append(f'<text x="{px - 3}" y="{oy + 16}" {FONT} font-size="10">{k}</text>')
        py = oy - k * u
        content.append(f'<line x1="{ox - 3}" y1="{py}" x2="{ox + 3}" y2="{py}" stroke="#1e293b" stroke-width="1.0" />')
        content.append(f'<text x="{ox - 14}" y="{py + 4}" {FONT} font-size="10">{k}</text>')

    # Folium loop and branches
    loop_pts = []
    ts = [0.0]
    for step in range(1, 150): ts.append(step * 0.05)
    for step in range(150, 400): ts.append(7.5 + (step - 150) * 0.25)
    for t in ts:
        x = (6 * t) / (1 + t**3)
        y = (6 * t**2) / (1 + t**3)
        px = ox + x * u
        py = oy - y * u
        loop_pts.append(f"{px:.1f},{py:.1f}")
    content.append(f'<path d="M {" L ".join(loop_pts)}" fill="none" stroke="#db2777" stroke-width="2.2" />')

    # Tangent 1 at (3, 3): line x + y = 6 (slope -1)
    lx1 = ox + 1.2 * u
    ly1 = oy - (6 - 1.2) * u
    lx2 = ox + 4.8 * u
    ly2 = oy - (6 - 4.8) * u
    content.append(f'<line x1="{lx1}" y1="{ly1}" x2="{lx2}" y2="{ly2}" stroke="#0284c7" stroke-width="2.0" />')
    p3x = ox + 3 * u
    p3y = oy - 3 * u
    content.append(f'<circle cx="{p3x}" cy="{p3y}" r="3.5" fill="#1e293b" />')
    content.append(f'<text x="{p3x + 8}" y="{p3y + 4}" {FONT} font-size="11" font-weight="bold" fill="#1e293b">(3, 3)</text>')
    content.append(f'<text x="{lx2 - 30}" y="{ly2 - 8}" {FONT} font-size="11" font-weight="bold" fill="#0284c7">x + y = 6 (m = -1)</text>')

    # Tangent 2 (Horizontal) at (2^(4/3), 2^(5/3)) ~ (2.5198, 3.1748)
    hx = 2**(4.0/3.0)
    hy = 2**(5.0/3.0)
    phx = ox + hx * u
    phy = oy - hy * u
    content.append(f'<line x1="{ox + 0.5*u}" y1="{phy}" x2="{ox + 4.5*u}" y2="{phy}" stroke="#16a34a" stroke-width="2.0" stroke-dasharray="4 3" />')
    content.append(f'<circle cx="{phx}" cy="{phy}" r="3.5" fill="#1e293b" />')
    content.append(f'<text x="{phx - 10}" y="{phy - 8}" {FONT} font-size="11" font-weight="bold" fill="#1e293b">(2⁴ᐟ³, 2⁵ᐟ³)</text>')
    content.append(f'<text x="{ox + 4.6*u}" y="{phy + 4}" {FONT} font-size="11" font-weight="bold" fill="#16a34a">y = 2⁵ᐟ³ (m = 0)</text>')

    content.append(f'<text x="25" y="345" {FONT} font-size="12" font-weight="bold" fill="#1e293b">FIGURE 4 &amp; 5: Tangent Lines to the Folium of Descartes</text>')
    return svg_wrapper(w, h, "\n".join(content))


def main():
    figs = {
        "sec2_2_figure10_cubic_derivatives.svg": make_fig10_cubic_derivatives(),
        "sec2_2_ex1_grid.svg": make_sec2_2_ex1_grid(),
        "sec2_2_ex2_grid.svg": make_sec2_2_ex2_grid(),
        "sec2_2_ex3_matching.svg": make_sec2_2_ex3_matching(),
        "sec2_4_ex72_grid.svg": make_sec2_4_ex72_grid(),
        "sec2_5_ex65_grid.svg": make_sec2_5_ex65_grid(),
        "sec2_5_ex66_grid.svg": make_sec2_5_ex66_grid(),
        "sec2_5_ex67_grid.svg": make_sec2_5_ex67_grid(),
        "sec2_6_figure1_circle_semicircles.svg": make_sec2_6_fig1_circle_semicircles(),
        "sec2_6_figure2_folium.svg": make_sec2_6_fig2_folium(),
        "sec2_6_figure3_folium_branches.svg": make_sec2_6_fig3_folium_branches(),
        "sec2_6_figure4_folium_tangents.svg": make_sec2_6_fig4_folium_tangents(),
    }

    for fname, svg_data in figs.items():
        fpath = os.path.join(OUTPUT_DIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(svg_data)
        print(f"Generated {fname} ({len(svg_data)} bytes)")

if __name__ == "__main__":
    main()
