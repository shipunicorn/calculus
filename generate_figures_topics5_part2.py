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

# -------------------------------------------------------------------
# 1. Exercise 5: Curves a, b, c (f, f', f'')
# -------------------------------------------------------------------
def make_sec2_rev_ex5_curves():
    w, h = 520, 360
    ox, oy = 260, 220
    ux = 70
    
    # We model curve a as a bell-like curve: a(x) = 140 / (1 + 0.8*x^2)
    # c(x) is derivative of a(x) * scale: c(x) = -224 * x / (1 + 0.8*x^2)^2
    # b(x) is derivative of c(x) * scale: b(x) = -110 * (1 - 2.4*x^2) / (1 + 0.8*x^2)^3
    # Wait, in image:
    # a (pink): peak at x=0, value ~130 above oy (y=90)
    # c (green): passes through (0,0) going down! At x < 0, c > 0 (peak around x=-1); at x > 0, c < 0 (valley around x=1)
    # b (sky): valley at x=0 (value ~120 below oy, y=340), rises to peaks around x = +-1.2 (above oy), then decays
    
    pts_a = []
    pts_c = []
    pts_b = []
    for i in range(-200, 201):
        x = i / 60.0
        px = ox + x * ux
        # a(x)
        ya = 140.0 / (1.0 + 0.65 * x**2)
        py_a = oy - ya
        pts_a.append(f"{px:.1f},{py_a:.1f}")
        
        # c(x) = a'(x) * scale factor
        # d/dx [ 140 / (1 + 0.65 x^2) ] = -182 x / (1 + 0.65 x^2)^2
        yc = -130.0 * x / ((1.0 + 0.55 * x**2)**2)
        py_c = oy - yc
        pts_c.append(f"{px:.1f},{py_c:.1f}")
        
        # b(x) = c'(x) * scale factor
        yb = -135.0 * (1.0 - 1.4 * x**2) / ((1.0 + 0.5 * x**2)**3)
        py_b = oy - yb
        pts_b.append(f"{px:.1f},{py_b:.1f}")

    content = [
        # Axes
        f'<line x1="40" y1="{oy}" x2="480" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="345" x2="{ox}" y2="35" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="475" y="{oy + 18}" {FONT} font-size="13" font-style="italic">x</text>',
        f'<text x="{ox - 18}" y="42" {FONT} font-size="13" font-style="italic">y</text>',
        f'<text x="{ox - 16}" y="{oy + 16}" {FONT} font-size="12">0</text>',
        
        # Curves
        f'<path d="M ' + ' L '.join(pts_a) + '" fill="none" stroke="#db2777" stroke-width="2.2" />',
        f'<path d="M ' + ' L '.join(pts_c) + '" fill="none" stroke="#16a34a" stroke-width="2.0" />',
        f'<path d="M ' + ' L '.join(pts_b) + '" fill="none" stroke="#0284c7" stroke-width="2.0" />',
        
        # Labels for curves
        f'<text x="{ox + 50}" y="95" {FONT} font-size="15" font-style="italic" font-weight="bold" fill="#db2777">a</text>',
        f'<text x="{ox + 42}" y="195" {FONT} font-size="15" font-style="italic" font-weight="bold" fill="#0284c7">b</text>',
        f'<text x="{ox + 75}" y="270" {FONT} font-size="15" font-style="italic" font-weight="bold" fill="#16a34a">c</text>',
    ]
    return svg_wrapper(w, h, '\n'.join(content))

# -------------------------------------------------------------------
# 2. Figure 11: y = x^3 with horizontal tangent at 0
# -------------------------------------------------------------------
def make_sec4_1_fig11_cubic_inflection():
    w, h = 340, 260
    ox, oy = 170, 150
    ux, uy = 55, 30
    
    pts = []
    for i in range(-120, 121):
        x = i / 70.0
        px = ox + x * ux
        py = oy - (x**3) * uy
        pts.append(f"{px:.1f},{py:.1f}")
        
    content = [
        # Axes
        f'<line x1="30" y1="{oy}" x2="310" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="240" x2="{ox}" y2="30" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="305" y="{oy + 16}" {FONT} font-size="12" font-style="italic">x</text>',
        f'<text x="{ox - 16}" y="36" {FONT} font-size="12" font-style="italic">y</text>',
        f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>',
        
        # Horizontal tangent line at origin
        f'<line x1="{ox - 50}" y1="{oy}" x2="{ox + 50}" y2="{oy}" stroke="#db2777" stroke-width="2.4" stroke-dasharray="4 3" />',
        
        # Curve
        f'<path d="M ' + ' L '.join(pts) + '" fill="none" stroke="#db2777" stroke-width="2.2" />',
        
        # Origin point
        f'<circle cx="{ox}" cy="{oy}" r="3.2" fill="#db2777" />',
        
        # Curve label
        f'<text x="{ox + 15}" y="70" {FONT} font-size="13" font-style="italic">y = x³</text>',
    ]
    return svg_wrapper(w, h, '\n'.join(content))

# -------------------------------------------------------------------
# 3. Figure 12: y = |x| with corner at 0
# -------------------------------------------------------------------
def make_sec4_1_fig12_abs_value_corner():
    w, h = 340, 260
    ox, oy = 170, 180
    ux, uy = 55, 55
    
    content = [
        # Axes
        f'<line x1="30" y1="{oy}" x2="310" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="230" x2="{ox}" y2="30" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="305" y="{oy + 16}" {FONT} font-size="12" font-style="italic">x</text>',
        f'<text x="{ox - 16}" y="36" {FONT} font-size="12" font-style="italic">y</text>',
        f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>',
        
        # Curve: V shape
        f'<line x1="{ox - 120}" y1="{oy - 120}" x2="{ox}" y2="{oy}" stroke="#db2777" stroke-width="2.2" />',
        f'<line x1="{ox}" y1="{oy}" x2="{ox + 120}" y2="{oy - 120}" stroke="#db2777" stroke-width="2.2" />',
        
        # Origin point (sharp minimum)
        f'<circle cx="{ox}" cy="{oy}" r="3.2" fill="#db2777" />',
        
        # Curve label
        f'<text x="{ox + 50}" y="125" {FONT} font-size="13" font-style="italic">y = |x|</text>',
    ]
    return svg_wrapper(w, h, '\n'.join(content))

# -------------------------------------------------------------------
# 4. Figure 13: f(x) = x^(3/5)(4 - x)
# -------------------------------------------------------------------
def make_sec4_1_fig13_critical_numbers():
    w, h = 480, 280
    ox, oy = 110, 190
    ux = 55
    uy = 38
    
    # Range x from -0.8 to 4.8
    pts = []
    for i in range(-45, 270):
        x = i / 55.0
        if x < 0:
            # (-x)^(3/5) with negative sign: -(-x)^(3/5)
            val = -((-x)**(3.0/5.0)) * (4.0 - x)
        else:
            val = (x**(3.0/5.0)) * (4.0 - x)
        px = ox + x * ux
        py = oy - val * uy
        pts.append(f"{px:.1f},{py:.1f}")
        
    content = [
        # Box frame like in textbook figure
        f'<rect x="25" y="20" width="430" height="235" rx="12" fill="none" stroke="#0284c7" stroke-width="1.4" />',
        
        # Axes
        f'<line x1="35" y1="{oy}" x2="445" y2="{oy}" stroke="#1e293b" stroke-width="1.2" />',
        f'<line x1="{ox}" y1="245" x2="{ox}" y2="30" stroke="#1e293b" stroke-width="1.2" />',
        
        # Ticks on x-axis: 0, 1.5, 4, 5
        f'<line x1="{ox + 1.5*ux}" y1="{oy - 3}" x2="{ox + 1.5*ux}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.0" />',
        f'<line x1="{ox + 4*ux}" y1="{oy - 3}" x2="{ox + 4*ux}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.0" />',
        f'<line x1="{ox + 5*ux}" y1="{oy - 3}" x2="{ox + 5*ux}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.0" />',
        
        f'<text x="{ox + 5*ux + 4}" y="{oy + 4}" {FONT} font-size="11">5</text>',
        f'<text x="{ox - 30}" y="{oy + 4}" {FONT} font-size="11">-0.5</text>',
        f'<text x="{ox - 10}" y="32" {FONT} font-size="11">3.5</text>',
        f'<text x="{ox - 8}" y="248" {FONT} font-size="11">-2</text>',
        
        # Curve
        f'<path d="M ' + ' L '.join(pts) + '" fill="none" stroke="#db2777" stroke-width="2.2" />',
        
        # Horizontal tangent line at x = 1.5
        # peak value is (1.5)^0.6 * 2.5 = 1.2754 * 2.5 = 3.188
        f'<line x1="{ox + 1.5*ux - 35}" y1="{oy - 3.188*uy}" x2="{ox + 1.5*ux + 35}" y2="{oy - 3.188*uy}" stroke="#0284c7" stroke-width="1.6" stroke-dasharray="3 2" />',
        f'<circle cx="{ox + 1.5*ux}" cy="{oy - 3.188*uy}" r="2.8" fill="#db2777" />',
        
        # Vertical tangent indicator at x = 0
        f'<line x1="{ox}" y1="{oy - 30}" x2="{ox}" y2="{oy + 30}" stroke="#0284c7" stroke-width="1.6" stroke-dasharray="3 2" />',
        f'<circle cx="{ox}" cy="{oy}" r="2.8" fill="#db2777" />',
    ]
    return svg_wrapper(w, h, '\n'.join(content))

# -------------------------------------------------------------------
# 5. Example 8: y = x^3 - 3x^2 + 1 on [-1/2, 4]
# -------------------------------------------------------------------
def make_sec4_1_fig_ex8_closed_interval():
    w, h = 440, 360
    ox, oy = 110, 270
    ux = 55
    uy = 10.5
    
    # f(x) = x^3 - 3x^2 + 1
    # f(-0.5) = -0.125 - 0.75 + 1 = 0.125
    # f(0) = 1
    # f(1) = -1
    # f(2) = 8 - 12 + 1 = -3
    # f(3) = 27 - 27 + 1 = 1
    # f(4) = 64 - 48 + 1 = 17
    
    pts = []
    for i in range(-30, 225):
        x = i / 55.0
        if x < -0.5 or x > 4.0:
            continue
        val = x**3 - 3*x**2 + 1
        px = ox + x * ux
        py = oy - val * uy
        pts.append(f"{px:.1f},{py:.1f}")
        
    content = [
        # Axes
        f'<line x1="30" y1="{oy}" x2="410" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="330" x2="{ox}" y2="40" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="405" y="{oy + 16}" {FONT} font-size="12" font-style="italic">x</text>',
        f'<text x="{ox - 16}" y="46" {FONT} font-size="12" font-style="italic">y</text>',
        f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>',
        
        # x-axis ticks
        f'<line x1="{ox - ux}" y1="{oy - 3}" x2="{ox - ux}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.0" />',
        f'<text x="{ox - ux - 8}" y="{oy + 16}" {FONT} font-size="11">-1</text>',
        for_ticks := '',
    ]
    for tx in [1, 2, 3, 4]:
        content.append(f'<line x1="{ox + tx*ux}" y1="{oy - 3}" x2="{ox + tx*ux}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.0" />')
        content.append(f'<text x="{ox + tx*ux - 3}" y="{oy + 16}" {FONT} font-size="11">{tx}</text>')
        
    # y-axis ticks: -5, 5, 10, 15, 20
    for ty in [-5, 5, 10, 15, 20]:
        py = oy - ty * uy
        content.append(f'<line x1="{ox - 3}" y1="{py}" x2="{ox + 3}" y2="{py}" stroke="#1e293b" stroke-width="1.0" />')
        content.append(f'<text x="{ox - 24}" y="{py + 4}" {FONT} font-size="11">{ty}</text>')
        
    # Curve
    content.append(f'<path d="M ' + ' L '.join(pts) + '" fill="none" stroke="#db2777" stroke-width="2.2" />')
    
    # Marked points
    # (-0.5, 0.125)
    p_start_x = ox - 0.5 * ux
    p_start_y = oy - 0.125 * uy
    content.append(f'<circle cx="{p_start_x}" cy="{p_start_y}" r="3.2" fill="#db2777" />')
    
    # (2, -3) local & absolute min
    p_min_x = ox + 2 * ux
    p_min_y = oy - (-3) * uy
    content.append(f'<circle cx="{p_min_x}" cy="{p_min_y}" r="3.5" fill="#db2777" />')
    content.append(f'<text x="{p_min_x - 18}" y="{p_min_y + 16}" {FONT} font-size="11" fill="#1e293b">(2, -3)</text>')
    
    # (4, 17) absolute max
    p_max_x = ox + 4 * ux
    p_max_y = oy - 17 * uy
    content.append(f'<circle cx="{p_max_x}" cy="{p_max_y}" r="3.5" fill="#db2777" />')
    content.append(f'<text x="{p_max_x + 6}" y="{p_max_y + 2}" {FONT} font-size="11" fill="#1e293b">(4, 17)</text>')
    
    # Label for equation
    content.append(f'<text x="{ox + 30}" y="100" {FONT} font-size="13" font-style="italic">y = x³ - 3x² + 1</text>')
    
    return svg_wrapper(w, h, '\n'.join(content))

# -------------------------------------------------------------------
# 6. Rolle's Theorem 4 Cases: Figure 1 (a), (b), (c), (d)
# -------------------------------------------------------------------
def make_sec4_2_fig1_rolles_theorem_cases():
    w, h = 650, 200
    sub_w = 155
    
    content = []
    
    # Helper to draw a subfigure
    def draw_case(idx, title, curve_type):
        bx = idx * sub_w + 10
        ox = bx + 25
        oy = 150
        ux = 80
        
        # Subfigure label
        content.append(f'<text x="{bx + 68}" y="185" {FONT} font-size="12" font-weight="bold">({title})</text>')
        
        # Axes
        content.append(f'<line x1="{bx + 5}" y1="{oy}" x2="{bx + 145}" y2="{oy}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />')
        content.append(f'<line x1="{ox}" y1="{oy + 25}" x2="{ox}" y2="25" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />')
        content.append(f'<text x="{bx + 142}" y="{oy + 14}" {FONT} font-size="10" font-style="italic">x</text>')
        content.append(f'<text x="{ox - 10}" y="30" {FONT} font-size="10" font-style="italic">y</text>')
        content.append(f'<text x="{ox - 10}" y="{oy + 13}" {FONT} font-size="10">0</text>')
        
        ax = ox + 22
        bx_pt = ox + 95
        
        content.append(f'<line x1="{ax}" y1="{oy - 2}" x2="{ax}" y2="{oy + 2}" stroke="#1e293b" stroke-width="1.0" />')
        content.append(f'<text x="{ax - 3}" y="{oy + 13}" {FONT} font-size="10" font-style="italic">a</text>')
        content.append(f'<line x1="{bx_pt}" y1="{oy - 2}" x2="{bx_pt}" y2="{oy + 2}" stroke="#1e293b" stroke-width="1.0" />')
        content.append(f'<text x="{bx_pt - 3}" y="{oy + 13}" {FONT} font-size="10" font-style="italic">b</text>')
        
        if curve_type == 'a': # constant
            y_val = oy - 65
            content.append(f'<line x1="{ax}" y1="{y_val}" x2="{bx_pt}" y2="{y_val}" stroke="#0284c7" stroke-width="1.8" />')
            content.append(f'<line x1="{ax}" y1="{y_val}" x2="{ax}" y2="{oy}" stroke="#64748b" stroke-width="0.8" stroke-dasharray="2 2" />')
            content.append(f'<line x1="{bx_pt}" y1="{y_val}" x2="{bx_pt}" y2="{oy}" stroke="#64748b" stroke-width="0.8" stroke-dasharray="2 2" />')
            
            c1 = ax + 25
            c2 = ax + 50
            content.append(f'<line x1="{c1}" y1="{y_val}" x2="{c1}" y2="{oy}" stroke="#64748b" stroke-width="0.8" />')
            content.append(f'<text x="{c1 - 4}" y="{oy + 13}" {FONT} font-size="9" font-style="italic">c₁</text>')
            content.append(f'<line x1="{c2}" y1="{y_val}" x2="{c2}" y2="{oy}" stroke="#64748b" stroke-width="0.8" />')
            content.append(f'<text x="{c2 - 4}" y="{oy + 13}" {FONT} font-size="9" font-style="italic">c₂</text>')
            
        elif curve_type == 'b': # peak
            # parabolic arc: peak at c = (ax + bx_pt)/2
            c = (ax + bx_pt) / 2.0
            peak_y = oy - 80
            base_y = oy - 45
            content.append(f'<path d="M {ax} {base_y} Q {c} {peak_y - 35} {bx_pt} {base_y}" fill="none" stroke="#0284c7" stroke-width="1.8" />')
            content.append(f'<line x1="{c - 20}" y1="{peak_y}" x2="{c + 20}" y2="{peak_y}" stroke="#db2777" stroke-width="1.6" />')
            content.append(f'<line x1="{c}" y1="{peak_y}" x2="{c}" y2="{oy}" stroke="#64748b" stroke-width="0.8" />')
            content.append(f'<text x="{c - 3}" y="{oy + 13}" {FONT} font-size="10" font-style="italic">c</text>')
            
        elif curve_type == 'c': # oscillating (two extrema)
            base_y = oy - 50
            c1 = ax + 22
            c2 = ax + 52
            content.append(f'<path d="M {ax} {base_y} C {ax + 10} {base_y - 50}, {c1 + 10} {base_y - 50}, {(ax + bx_pt)/2} {base_y} C {c2 - 10} {base_y + 40}, {bx_pt - 10} {base_y + 40}, {bx_pt} {base_y}" fill="none" stroke="#0284c7" stroke-width="1.8" />')
            
            # tangents
            content.append(f'<line x1="{c1 - 15}" y1="{base_y - 25}" x2="{c1 + 15}" y2="{base_y - 25}" stroke="#db2777" stroke-width="1.6" />')
            content.append(f'<line x1="{c1}" y1="{base_y - 25}" x2="{c1}" y2="{oy}" stroke="#64748b" stroke-width="0.8" />')
            content.append(f'<text x="{c1 - 4}" y="{oy + 13}" {FONT} font-size="9" font-style="italic">c₁</text>')
            
            content.append(f'<line x1="{c2 - 15}" y1="{base_y + 20}" x2="{c2 + 15}" y2="{base_y + 20}" stroke="#db2777" stroke-width="1.6" />')
            content.append(f'<line x1="{c2}" y1="{base_y + 20}" x2="{c2}" y2="{oy}" stroke="#64748b" stroke-width="0.8" />')
            content.append(f'<text x="{c2 - 4}" y="{oy + 13}" {FONT} font-size="9" font-style="italic">c₂</text>')
            
        elif curve_type == 'd': # valley
            c = (ax + bx_pt) / 2.0
            valley_y = oy - 25
            base_y = oy - 65
            content.append(f'<path d="M {ax} {base_y} Q {c} {valley_y + 35} {bx_pt} {base_y}" fill="none" stroke="#0284c7" stroke-width="1.8" />')
            content.append(f'<line x1="{c - 20}" y1="{valley_y}" x2="{c + 20}" y2="{valley_y}" stroke="#db2777" stroke-width="1.6" />')
            content.append(f'<line x1="{c}" y1="{valley_y}" x2="{c}" y2="{oy}" stroke="#64748b" stroke-width="0.8" />')
            content.append(f'<text x="{c - 3}" y="{oy + 13}" {FONT} font-size="10" font-style="italic">c</text>')

    draw_case(0, 'a', 'a')
    draw_case(1, 'b', 'b')
    draw_case(2, 'c', 'c')
    draw_case(3, 'd', 'd')
    
    return svg_wrapper(w, h, '\n'.join(content))

# -------------------------------------------------------------------
# 7. Figure 3: MVT Single Tangent Parallel to Secant
# -------------------------------------------------------------------
def make_sec4_2_fig3_mvt_single_tangent():
    w, h = 340, 260
    ox, oy = 50, 210
    
    ax, ay = ox + 30, oy - 60
    bx, by = ox + 220, oy - 20
    
    # Secant line slope = (by - ay) / (bx - ax) = (40) / 190 = 0.21 (downward in svg)
    # The curve arches above the secant line: peak around c = ox + 110, y = oy - 120
    cx = ox + 105
    cy = oy - 110
    
    content = [
        # Axes
        f'<line x1="20" y1="{oy}" x2="310" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="240" x2="{ox}" y2="30" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="305" y="{oy + 16}" {FONT} font-size="12" font-style="italic">x</text>',
        f'<text x="{ox - 16}" y="36" {FONT} font-size="12" font-style="italic">y</text>',
        f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>',
        
        # Secant line AB
        f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="#0284c7" stroke-width="1.8" />',
        f'<circle cx="{ax}" cy="{ay}" r="3.2" fill="#1e293b" />',
        f'<circle cx="{bx}" cy="{by}" r="3.2" fill="#1e293b" />',
        f'<text x="{ax - 20}" y="{ay + 18}" {FONT} font-size="11">A(a, f(a))</text>',
        f'<text x="{bx - 20}" y="{by + 20}" {FONT} font-size="11">B(b, f(b))</text>',
        
        # Curve y = f(x)
        f'<path d="M {ax} {ay} Q {cx} {cy - 40} {bx} {by}" fill="none" stroke="#1e293b" stroke-width="1.8" />',
        
        # Tangent line at P(c, f(c)) parallel to secant line
        # slope = (by - ay) / (bx - ax)
        f'<line x1="{cx - 65}" y1="{cy - 65 * (by - ay)/(bx - ax)}" x2="{cx + 65}" y2="{cy + 65 * (by - ay)/(bx - ax)}" stroke="#db2777" stroke-width="1.8" />',
        f'<circle cx="{cx}" cy="{cy}" r="3.2" fill="#db2777" />',
        f'<text x="{cx - 15}" y="{cy - 8}" {FONT} font-size="11">P(c, f(c))</text>',
        
        # Vertical drop lines to x-axis
        f'<line x1="{ax}" y1="{ay}" x2="{ax}" y2="{oy}" stroke="#64748b" stroke-width="0.8" stroke-dasharray="3 2" />',
        f'<text x="{ax - 3}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">a</text>',
        f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{oy}" stroke="#64748b" stroke-width="0.8" stroke-dasharray="3 2" />',
        f'<text x="{cx - 3}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">c</text>',
        f'<line x1="{bx}" y1="{by}" x2="{bx}" y2="{oy}" stroke="#64748b" stroke-width="0.8" stroke-dasharray="3 2" />',
        f'<text x="{bx - 3}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">b</text>',
    ]
    return svg_wrapper(w, h, '\n'.join(content))

# -------------------------------------------------------------------
# 8. Figure 4: MVT Multiple Tangents Parallel to Secant
# -------------------------------------------------------------------
def make_sec4_2_fig4_mvt_multiple_tangents():
    w, h = 340, 260
    ox, oy = 50, 210
    
    ax, ay = ox + 25, oy - 45
    bx, by = ox + 225, oy - 145
    
    # Secant line AB
    # slope = (by - ay) / (bx - ax) = (-100) / 200 = -0.5 (upward in math, upward in svg)
    slope = (by - ay) / (bx - ax)
    
    # S-curve with local peak P1 around c1 and valley P2 around c2
    c1 = ox + 80
    y1 = oy - 140
    c2 = ox + 155
    y2 = oy - 80
    
    content = [
        # Axes
        f'<line x1="20" y1="{oy}" x2="310" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="240" x2="{ox}" y2="30" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="305" y="{oy + 16}" {FONT} font-size="12" font-style="italic">x</text>',
        f'<text x="{ox - 16}" y="36" {FONT} font-size="12" font-style="italic">y</text>',
        f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>',
        
        # Secant line AB
        f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="#0284c7" stroke-width="1.8" />',
        f'<circle cx="{ax}" cy="{ay}" r="3.2" fill="#1e293b" />',
        f'<circle cx="{bx}" cy="{by}" r="3.2" fill="#1e293b" />',
        f'<text x="{ax - 15}" y="{ay + 4}" {FONT} font-size="11">A</text>',
        f'<text x="{bx + 8}" y="{by + 4}" {FONT} font-size="11">B</text>',
        
        # S-curve path
        f'<path d="M {ax} {ay} C {ax + 20} {ay - 120}, {c1 + 20} {y1 - 20}, {(c1 + c2)/2} {(y1 + y2)/2} C {c2 - 20} {y2 + 20}, {bx - 20} {by + 80}, {bx} {by}" fill="none" stroke="#1e293b" stroke-width="1.8" />',
        
        # Tangent line at P1
        f'<line x1="{c1 - 50}" y1="{y1 - 50*slope}" x2="{c1 + 50}" y2="{y1 + 50*slope}" stroke="#db2777" stroke-width="1.8" />',
        f'<circle cx="{c1}" cy="{y1}" r="3.2" fill="#db2777" />',
        f'<text x="{c1 - 5}" y="{y1 - 8}" {FONT} font-size="11">P₁</text>',
        
        # Tangent line at P2
        f'<line x1="{c2 - 50}" y1="{y2 - 50*slope}" x2="{c2 + 50}" y2="{y2 + 50*slope}" stroke="#db2777" stroke-width="1.8" />',
        f'<circle cx="{c2}" cy="{y2}" r="3.2" fill="#db2777" />',
        f'<text x="{c2 + 6}" y="{y2 + 12}" {FONT} font-size="11">P₂</text>',
        
        # Vertical drop lines to x-axis
        f'<line x1="{ax}" y1="{ay}" x2="{ax}" y2="{oy}" stroke="#64748b" stroke-width="0.8" stroke-dasharray="3 2" />',
        f'<text x="{ax - 3}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">a</text>',
        f'<line x1="{c1}" y1="{y1}" x2="{c1}" y2="{oy}" stroke="#64748b" stroke-width="0.8" stroke-dasharray="3 2" />',
        f'<text x="{c1 - 4}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">c₁</text>',
        f'<line x1="{c2}" y1="{y2}" x2="{c2}" y2="{oy}" stroke="#64748b" stroke-width="0.8" stroke-dasharray="3 2" />',
        f'<text x="{c2 - 4}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">c₂</text>',
        f'<line x1="{bx}" y1="{by}" x2="{bx}" y2="{oy}" stroke="#64748b" stroke-width="0.8" stroke-dasharray="3 2" />',
        f'<text x="{bx - 3}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">b</text>',
    ]
    return svg_wrapper(w, h, '\n'.join(content))

# -------------------------------------------------------------------
# 9. Figure 5: MVT Proof Auxiliary Function h(x)
# -------------------------------------------------------------------
def make_sec4_2_fig5_mvt_proof_hx():
    w, h = 420, 320
    ox, oy = 60, 240
    
    ax, ay = ox + 35, oy - 110
    bx, by = ox + 265, oy - 60
    
    # Secant line AB
    # Curve arches up
    cx = ox + 150
    cy = oy - 190
    
    # Generic x position
    gx = ox + 115
    # y on curve
    t = (gx - ax) / (bx - ax)
    # parabolic arch y = ay + t*(by - ay) - 4 * arch * t * (1 - t)
    sec_y = ay + t * (by - ay)
    curve_y = sec_y - 75.0 * math.sin(t * math.pi)
    
    content = [
        # Axes
        f'<line x1="20" y1="{oy}" x2="390" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="280" x2="{ox}" y2="35" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="385" y="{oy + 16}" {FONT} font-size="12" font-style="italic">x</text>',
        f'<text x="{ox - 16}" y="42" {FONT} font-size="12" font-style="italic">y</text>',
        f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>',
        
        # Secant line AB
        f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="#0284c7" stroke-width="1.8" />',
        f'<circle cx="{ax}" cy="{ay}" r="3.2" fill="#1e293b" />',
        f'<circle cx="{bx}" cy="{by}" r="3.2" fill="#1e293b" />',
        f'<text x="{ax - 18}" y="{ay + 4}" {FONT} font-size="12">A</text>',
        f'<text x="{bx + 6}" y="{by + 10}" {FONT} font-size="12">B</text>',
        
        # Curve y = f(x)
        f'<path d="M {ax} {ay} Q {cx} {cy - 20} {bx} {by}" fill="none" stroke="#1e293b" stroke-width="1.8" />',
        f'<text x="{cx + 70}" y="80" {FONT} font-size="13" font-style="italic">y = f(x)</text>',
        
        # Vertical column at x
        # Bracket / indicator for h(x)
        f'<line x1="{gx}" y1="{sec_y}" x2="{gx}" y2="{curve_y}" stroke="#db2777" stroke-width="3.0" />',
        f'<text x="{gx + 12}" y="{(sec_y + curve_y)/2 + 4}" {FONT} font-size="13" font-style="italic" fill="#db2777" font-weight="bold">h(x)</text>',
        
        # Bracket for secant line height
        f'<line x1="{gx - 1}" y1="{oy}" x2="{gx - 1}" y2="{sec_y}" stroke="#16a34a" stroke-width="1.6" />',
        
        # Left brace / bracket enclosing total f(x)
        f'<path d="M {gx - 10} {curve_y} C {gx - 16} {curve_y}, {gx - 16} {(curve_y + oy)/2}, {gx - 20} {(curve_y + oy)/2} C {gx - 16} {(curve_y + oy)/2}, {gx - 16} {oy}, {gx - 10} {oy}" fill="none" stroke="#64748b" stroke-width="1.2" />',
        f'<text x="{gx - 48}" y="{(curve_y + oy)/2 + 4}" {FONT} font-size="13" font-style="italic">f(x)</text>',
        
        # Pointer arrow to secant height
        f'<line x1="{gx + 55}" y1="{oy - 15}" x2="{gx + 8}" y2="{sec_y + 12}" stroke="#1e293b" stroke-width="1.0" marker-end="url(#arrow)" />',
        f'<text x="{gx + 20}" y="{oy + 30}" {FONT} font-size="11">f(a) + <tspan font-style="italic">m</tspan>(x - a)</text>',
        
        # Drops to x-axis
        f'<line x1="{ax}" y1="{ay}" x2="{ax}" y2="{oy}" stroke="#64748b" stroke-width="0.8" stroke-dasharray="3 2" />',
        f'<text x="{ax - 3}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">a</text>',
        f'<text x="{gx - 3}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">x</text>',
        f'<line x1="{bx}" y1="{by}" x2="{bx}" y2="{oy}" stroke="#64748b" stroke-width="0.8" stroke-dasharray="3 2" />',
        f'<text x="{bx - 3}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">b</text>',
    ]
    return svg_wrapper(w, h, '\n'.join(content))

# -------------------------------------------------------------------
# 10. Figure 6: Example 3 MVT on y = x^3 - x
# -------------------------------------------------------------------
def make_sec4_2_fig6_mvt_cubic_example():
    w, h = 380, 280
    ox, oy = 90, 210
    ux = 80
    uy = 24
    
    # f(x) = x^3 - x on [0, 2]
    # f(0) = 0, f(1) = 0, f(2) = 6
    # Secant line OB connects (0,0) to (2,6) with slope m = 3
    # c = 2 / sqrt(3) approx 1.1547
    # f(c) = 8 / (3*sqrt(3)) - 2 / sqrt(3) = 2 / (3*sqrt(3)) approx 0.3849
    # Tangent at c has slope 3
    
    pts = []
    for i in range(-50, 180):
        x = i / 80.0
        val = x**3 - x
        px = ox + x * ux
        py = oy - val * uy
        pts.append(f"{px:.1f},{py:.1f}")
        
    c = 2.0 / math.sqrt(3.0)
    fc = c**3 - c
    pcx = ox + c * ux
    pcy = oy - fc * uy
    
    content = [
        # Axes
        f'<line x1="30" y1="{oy}" x2="350" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="260" x2="{ox}" y2="30" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="345" y="{oy + 16}" {FONT} font-size="12" font-style="italic">x</text>',
        f'<text x="{ox - 16}" y="36" {FONT} font-size="12" font-style="italic">y</text>',
        f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">O</text>',
        
        # Secant line OB: (0, 0) to (2, 6)
        # In svg coords: (ox, oy) to (ox + 2*ux, oy - 6*uy)
        # Extend slightly past endpoints
        f'<line x1="{ox - 25}" y1="{oy + 25 * 3 * uy / ux}" x2="{ox + 2*ux + 25}" y2="{oy - (6 + 25 * 3 / ux) * uy}" stroke="#0284c7" stroke-width="1.8" />',
        f'<circle cx="{ox + 2*ux}" cy="{oy - 6*uy}" r="3.2" fill="#1e293b" />',
        f'<text x="{ox + 2*ux - 12}" y="{oy - 6*uy - 8}" {FONT} font-size="12">B</text>',
        
        # Tangent line at c parallel to OB (slope m = 3)
        # dy/dx in svg = -3 * uy / ux
        f'<line x1="{pcx - 55}" y1="{pcy + 55 * 3 * uy / ux}" x2="{pcx + 55}" y2="{pcy - 55 * 3 * uy / ux}" stroke="#db2777" stroke-width="1.8" />',
        f'<circle cx="{pcx}" cy="{pcy}" r="3.2" fill="#1e293b" />',
        
        # Curve y = x^3 - x
        f'<path d="M ' + ' L '.join(pts) + '" fill="none" stroke="#1e293b" stroke-width="1.8" />',
        f'<text x="{ox + 30}" y="55" {FONT} font-size="12" font-style="italic">y = x³ - x</text>',
        
        # Drops to x-axis
        f'<line x1="{pcx}" y1="{pcy}" x2="{pcx}" y2="{oy}" stroke="#64748b" stroke-width="0.8" stroke-dasharray="3 2" />',
        f'<text x="{pcx - 3}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">c</text>',
        f'<line x1="{ox + 2*ux}" y1="{oy - 6*uy}" x2="{ox + 2*ux}" y2="{oy}" stroke="#64748b" stroke-width="0.8" stroke-dasharray="3 2" />',
        f'<text x="{ox + 2*ux - 3}" y="{oy + 16}" {FONT} font-size="11">2</text>',
    ]
    return svg_wrapper(w, h, '\n'.join(content))


def main():
    figs = {
        "sec2_rev_ex5_curves.svg": make_sec2_rev_ex5_curves(),
        "sec4_1_fig11_cubic_inflection.svg": make_sec4_1_fig11_cubic_inflection(),
        "sec4_1_fig12_abs_value_corner.svg": make_sec4_1_fig12_abs_value_corner(),
        "sec4_1_fig13_critical_numbers.svg": make_sec4_1_fig13_critical_numbers(),
        "sec4_1_fig_ex8_closed_interval.svg": make_sec4_1_fig_ex8_closed_interval(),
        "sec4_2_fig1_rolles_theorem_cases.svg": make_sec4_2_fig1_rolles_theorem_cases(),
        "sec4_2_fig3_mvt_single_tangent.svg": make_sec4_2_fig3_mvt_single_tangent(),
        "sec4_2_fig4_mvt_multiple_tangents.svg": make_sec4_2_fig4_mvt_multiple_tangents(),
        "sec4_2_fig5_mvt_proof_hx.svg": make_sec4_2_fig5_mvt_proof_hx(),
        "sec4_2_fig6_mvt_cubic_example.svg": make_sec4_2_fig6_mvt_cubic_example(),
    }
    for filename, content in figs.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {filepath}")

if __name__ == "__main__":
    main()
