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
</defs>
{content}
</svg>'''

# 1. Parabola Tangent: Example 1 (y = x^2 at (1,1))
def make_fig_example1_parabola():
    w, h = 420, 300
    ox, oy = 150, 220
    ux, uy = 70, 70

    axes = f'''
    <!-- Axes -->
    <line x1="{ox - 100}" y1="{oy}" x2="{ox + 210}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 40}" x2="{ox}" y2="{oy - 190}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 215}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 15}" y="{oy - 185}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>
    '''

    ticks = f'''
    <!-- Ticks -->
    <line x1="{ox + ux}" y1="{oy - 3}" x2="{ox + ux}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{ox + ux - 3}" y="{oy + 16}" {FONT} font-size="11">1</text>
    <line x1="{ox + 2*ux}" y1="{oy - 3}" x2="{ox + 2*ux}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{ox + 2*ux - 3}" y="{oy + 16}" {FONT} font-size="11">2</text>
    <line x1="{ox - ux}" y1="{oy - 3}" x2="{ox - ux}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{ox - ux - 7}" y="{oy + 16}" {FONT} font-size="11">-1</text>

    <line x1="{ox - 3}" y1="{oy - uy}" x2="{ox + 3}" y2="{oy - uy}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{ox - 16}" y="{oy - uy + 4}" {FONT} font-size="11">1</text>
    <line x1="{ox - 3}" y1="{oy - 2*uy}" x2="{ox + 3}" y2="{oy - 2*uy}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{ox - 16}" y="{oy - 2*uy + 4}" {FONT} font-size="11">2</text>
    '''

    # Parabola y = x^2 from x = -1.3 to x = 1.6
    # Let's generate points
    pts = []
    for step in range(-26, 33):
        x_val = step * 0.05
        y_val = x_val**2
        px = ox + x_val * ux
        py = oy - y_val * uy
        pts.append(f"{px:.1f},{py:.1f}")
    path_d = "M " + " L ".join(pts)

    curve = f'''
    <path d="{path_d}" fill="none" stroke="#0284c7" stroke-width="2.2" />
    <text x="{ox + 1.4*ux}" y="{oy - 2.2*uy}" {FONT} font-size="12" font-style="italic" fill="#0284c7">y = x²</text>
    '''

    # Tangent line at (1,1): y - 1 = 2(x - 1) => y = 2x - 1
    # For x = -0.2 => y = -1.4 (py = oy + 1.4*uy)
    # For x = 1.8 => y = 2.6 (py = oy - 2.6*uy)
    lx1 = ox - 0.2 * ux
    ly1 = oy - (-1.4) * uy
    lx2 = ox + 1.8 * ux
    ly2 = oy - 2.6 * uy

    # Dashed guidelines for (1, 1)
    p1x = ox + 1.0 * ux
    p1y = oy - 1.0 * uy
    guide = f'''
    <line x1="{p1x}" y1="{oy}" x2="{p1x}" y2="{p1y}" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3" />
    <line x1="{ox}" y1="{p1y}" x2="{p1x}" y2="{p1y}" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3" />
    <circle cx="{p1x}" cy="{p1y}" r="3.5" fill="#1e293b" />
    <text x="{p1x + 8}" y="{p1y + 4}" {FONT} font-size="11" fill="#1e293b">P(1, 1)</text>
    '''

    tangent = f'''
    <line x1="{lx1}" y1="{ly1}" x2="{lx2}" y2="{ly2}" stroke="#db2777" stroke-width="2" />
    <text x="{lx2 - 40}" y="{ly2 - 6}" {FONT} font-size="11" fill="#db2777">Tangent line: y = 2x - 1 (m = 2)</text>
    '''

    caption = f'<text x="25" y="285" {FONT} font-size="12" font-weight="bold" fill="#1e293b">FIGURE: Tangent Line to the Parabola y = x² at P(1, 1)</text>'
    return svg_wrapper(w, h, axes + ticks + curve + guide + tangent + caption)


# 2. Figure 4: Tangent to Hyperbola y = 3/x at (3, 1)
def make_fig_sec2_7_fig4():
    w, h = 460, 310
    ox, oy = 55, 235
    ux, uy = 60, 60

    axes = f'''
    <!-- Axes -->
    <line x1="{ox - 20}" y1="{oy}" x2="{ox + 6.3*ux}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 25}" x2="{ox}" y2="{oy - 3.4*uy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 6.4*ux}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 14}" y="{oy - 3.4*uy}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>
    '''

    ticks = ''
    for i in range(1, 7):
        tx = ox + i * ux
        ticks += f'<line x1="{tx}" y1="{oy - 3}" x2="{tx}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />'
        ticks += f'<text x="{tx - 3}" y="{oy + 16}" {FONT} font-size="11">{i}</text>'
    for j in range(1, 4):
        ty = oy - j * uy
        ticks += f'<line x1="{ox - 3}" y1="{ty}" x2="{ox + 3}" y2="{ty}" stroke="#1e293b" stroke-width="1.2" />'
        ticks += f'<text x="{ox - 14}" y="{ty + 4}" {FONT} font-size="11">{j}</text>'

    # Curve y = 3/x from x = 0.85 to 6.0
    pts = []
    for step in range(17, 121):
        x_val = step * 0.05
        y_val = 3.0 / x_val
        px = ox + x_val * ux
        py = oy - y_val * uy
        pts.append(f"{px:.1f},{py:.1f}")
    path_d = "M " + " L ".join(pts)

    curve = f'''
    <path d="{path_d}" fill="none" stroke="#0284c7" stroke-width="2.2" />
    <text x="{ox + 4.8*ux}" y="{oy - 0.75*uy}" {FONT} font-size="12" font-style="italic" fill="#0284c7">y = 3/x</text>
    '''

    # Tangent line at (3, 1): x + 3y - 6 = 0 => y = -1/3 x + 2
    # At x = 0 => y = 2
    # At x = 6 => y = 0
    tx1 = ox + 0 * ux
    ty1 = oy - 2 * uy
    tx2 = ox + 6.1 * ux
    ty2 = oy - (-0.033) * uy

    # Point (3, 1)
    px = ox + 3 * ux
    py = oy - 1 * uy
    point = f'''
    <!-- Dashed projection guidelines -->
    <line x1="{px}" y1="{oy}" x2="{px}" y2="{py}" stroke="#0d9488" stroke-width="1.2" stroke-dasharray="4 3" />
    <line x1="{ox}" y1="{py}" x2="{px}" y2="{py}" stroke="#0d9488" stroke-width="1.2" stroke-dasharray="4 3" />
    <circle cx="{px}" cy="{py}" r="3.5" fill="#1e293b" />
    <text x="{px + 6}" y="{py - 8}" {FONT} font-size="11" font-weight="bold" fill="#1e293b">(3, 1)</text>
    '''

    tangent = f'''
    <line x1="{tx1}" y1="{ty1}" x2="{tx2}" y2="{ty2}" stroke="#db2777" stroke-width="2" />
    <text x="{ox + 2.8*ux}" y="{oy - 1.6*uy}" {FONT} font-size="11" fill="#db2777">Tangent line: x + 3y - 6 = 0</text>
    <text x="{ox + 3.2*ux}" y="{oy - 1.35*uy}" {FONT} font-size="10" fill="#64748b">(slope m = -1/3)</text>
    '''

    caption = f'<text x="25" y="295" {FONT} font-size="12" font-weight="bold" fill="#1e293b">FIGURE 4: Tangent Line to the Hyperbola y = 3/x at (3, 1)</text>'
    return svg_wrapper(w, h, axes + ticks + curve + point + tangent + caption)


# 3. Exercise 12: Runners A and B
def make_fig_sec2_7_exercise12():
    w, h = 430, 215
    ox, oy = 50, 170
    # ux: 19 px per 1 sec => 14 * 19 = 266 px
    # uy: 1.3 px per 1 m => 100 * 1.3 = 130 px
    ux = 19.0
    uy = 1.3

    # Grid lines
    grid = '<!-- Grid -->'
    for t in range(0, 15, 2):
        gx = ox + t * ux
        grid += f'<line x1="{gx}" y1="{oy}" x2="{gx}" y2="{oy - 100*uy}" stroke="#e2e8f0" stroke-width="1" />'
    for s in range(0, 101, 20):
        gy = oy - s * uy
        grid += f'<line x1="{ox}" y1="{gy}" x2="{ox + 14*ux}" y2="{gy}" stroke="#e2e8f0" stroke-width="1" />'

    axes = f'''
    <!-- Axes -->
    <line x1="{ox - 10}" y1="{oy}" x2="{ox + 15*ux}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 12}" x2="{ox}" y2="{oy - 108*uy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 15*ux + 4}" y="{oy + 13}" {FONT} font-size="11" font-style="italic">t <tspan font-style="normal">(s)</tspan></text>
    <text x="{ox - 15}" y="{oy - 108*uy - 3}" {FONT} font-size="11" font-style="italic">s <tspan font-style="normal">(m)</tspan></text>
    <text x="{ox - 12}" y="{oy + 13}" {FONT} font-size="10">0</text>
    '''

    ticks = ''
    for t in [4, 8, 12]:
        tx = ox + t * ux
        ticks += f'<line x1="{tx}" y1="{oy - 3}" x2="{tx}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />'
        ticks += f'<text x="{tx - 3}" y="{oy + 14}" {FONT} font-size="10">{t}</text>'
    for s in [40, 80]:
        ty = oy - s * uy
        ticks += f'<line x1="{ox - 3}" y1="{ty}" x2="{ox + 3}" y2="{ty}" stroke="#1e293b" stroke-width="1.2" />'
        ticks += f'<text x="{ox - 18}" y="{ty + 4}" {FONT} font-size="10">{s}</text>'

    # Paths
    pathA = f"M {ox} {oy} C {ox + 2.5*ux} {oy - 25*uy}, {ox + 5.5*ux} {oy - 46*uy}, {ox + 8*ux} {oy - 56*uy} C {ox + 10.5*ux} {oy - 66*uy}, {ox + 12.5*ux} {oy - 82*uy}, {ox + 14*ux} {oy - 100*uy}"
    pathB = f"M {ox} {oy} C {ox + 3*ux} {oy - 8*uy}, {ox + 6*ux} {oy - 16*uy}, {ox + 8*ux} {oy - 24*uy} C {ox + 10*ux} {oy - 33*uy}, {ox + 12*ux} {oy - 56*uy}, {ox + 14*ux} {oy - 100*uy}"

    curves = f'''
    <!-- Runner A (pink/magenta) -->
    <path d="{pathA}" fill="none" stroke="#db2777" stroke-width="2.2" />
    <text x="{ox + 7.6*ux}" y="{oy - 61*uy}" {FONT} font-size="12" font-weight="bold" fill="#db2777">A</text>

    <!-- Runner B (cyan/blue) -->
    <path d="{pathB}" fill="none" stroke="#0284c7" stroke-width="2.2" />
    <text x="{ox + 8.1*ux}" y="{oy - 17*uy}" {FONT} font-size="12" font-weight="bold" fill="#0284c7">B</text>

    <!-- Tie endpoint -->
    <circle cx="{ox + 14*ux}" cy="{oy - 100*uy}" r="3" fill="#1e293b" />
    <text x="{ox + 14*ux - 46}" y="{oy - 102*uy}" {FONT} font-size="9.5" font-weight="bold" fill="#1e293b">Tie (14 s, 100 m)</text>
    '''

    caption = f'<text x="25" y="202" {FONT} font-size="11" font-weight="bold" fill="#1e293b">EXERCISE 12: Position Graphs of Runners A and B</text>'
    return svg_wrapper(w, h, grid + axes + ticks + curves + caption)


# 4. Figure 5: Graph of y = |x| and its derivative y = f'(x)
def make_fig_sec2_8_fig5():
    w, h = 520, 270
    
    # Subfigure (a): y = |x|
    # Centered around ox1 = 130, oy1 = 190
    ox1, oy1 = 130, 185
    u1 = 45

    sub_a = f'''
    <!-- Subfigure (a) -->
    <line x1="{ox1 - 100}" y1="{oy1}" x2="{ox1 + 105}" y2="{oy1}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox1}" y1="{oy1 + 25}" x2="{ox1}" y2="{oy1 - 145}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox1 + 108}" y="{oy1 + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox1 - 14}" y="{oy1 - 140}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox1 - 12}" y="{oy1 + 14}" {FONT} font-size="11">0</text>

    <!-- Function curve y = |x| -->
    <line x1="{ox1 - 85}" y1="{oy1 - 85}" x2="{ox1}" y2="{oy1}" stroke="#0284c7" stroke-width="2.2" />
    <line x1="{ox1}" y1="{oy1}" x2="{ox1 + 85}" y2="{oy1 - 85}" stroke="#0284c7" stroke-width="2.2" />
    <circle cx="{ox1}" cy="{oy1}" r="3" fill="#0284c7" />

    <text x="{ox1 - 65}" y="{oy1 + 45}" {FONT} font-size="12" font-weight="bold" fill="#1e293b">(a) <tspan font-style="italic" font-weight="normal">y = f(x) = |x|</tspan></text>
    '''

    # Subfigure (b): y = f'(x)
    # Centered around ox2 = 380, oy2 = 140
    ox2, oy2 = 380, 140
    u2 = 45

    sub_b = f'''
    <!-- Subfigure (b) -->
    <line x1="{ox2 - 100}" y1="{oy2}" x2="{ox2 + 105}" y2="{oy2}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox2}" y1="{oy2 + 70}" x2="{ox2}" y2="{oy2 - 100}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox2 + 108}" y="{oy2 + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox2 - 14}" y="{oy2 - 95}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox2 - 12}" y="{oy2 + 14}" {FONT} font-size="11">0</text>

    <!-- Tick marks for 1 and -1 -->
    <line x1="{ox2 - 3}" y1="{oy2 - u2}" x2="{ox2 + 3}" y2="{oy2 - u2}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{ox2 - 14}" y="{oy2 - u2 + 4}" {FONT} font-size="11">1</text>
    <line x1="{ox2 - 3}" y1="{oy2 + u2}" x2="{ox2 + 3}" y2="{oy2 + u2}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{ox2 + 8}" y="{oy2 + u2 + 4}" {FONT} font-size="11">-1</text>

    <!-- Derivative rays: y = 1 for x > 0, y = -1 for x < 0 -->
    <line x1="{ox2 + 4}" y1="{oy2 - u2}" x2="{ox2 + 85}" y2="{oy2 - u2}" stroke="#db2777" stroke-width="2.2" />
    <circle cx="{ox2}" cy="{oy2 - u2}" r="3.5" fill="#ffffff" stroke="#db2777" stroke-width="1.8" />

    <line x1="{ox2 - 85}" y1="{oy2 + u2}" x2="{ox2 - 4}" y2="{oy2 + u2}" stroke="#db2777" stroke-width="2.2" />
    <circle cx="{ox2}" cy="{oy2 + u2}" r="3.5" fill="#ffffff" stroke="#db2777" stroke-width="1.8" />

    <text x="{ox2 - 50}" y="{oy2 + 90}" {FONT} font-size="12" font-weight="bold" fill="#1e293b">(b) <tspan font-style="italic" font-weight="normal">y = f\'(x)</tspan></text>
    '''

    caption = f'<text x="25" y="255" {FONT} font-size="12" font-weight="bold" fill="#1e293b">FIGURE 5: Graph of f(x) = |x| and its Derivative f\'(x)</text>'
    return svg_wrapper(w, h, sub_a + sub_b + caption)


# 5. Figure 7: Three ways for a function to fail to be differentiable at a
def make_fig_sec2_8_fig7():
    w, h = 640, 260
    
    # 3 sub-panels: (a) Corner, (b) Discontinuity, (c) Vertical tangent
    # oxA = 90, oxB = 300, oxC = 510, oy = 180
    oy = 175

    # Panel A: A corner
    oxA = 90
    panel_a = f'''
    <!-- Panel A: Corner -->
    <line x1="{oxA - 65}" y1="{oy}" x2="{oxA + 95}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <line x1="{oxA - 40}" y1="{oy + 25}" x2="{oxA - 40}" y2="{oy - 120}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <text x="{oxA + 98}" y="{oy + 14}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{oxA - 52}" y="{oy - 115}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{oxA - 48}" y="{oy + 14}" {FONT} font-size="10">0</text>

    <!-- Tick mark at a -->
    <line x1="{oxA + 20}" y1="{oy - 3}" x2="{oxA + 20}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{oxA + 17}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">a</text>

    <!-- Corner curve -->
    <!-- Left branch curving up sharply to (oxA+20, oy-75) -->
    <path d="M {oxA - 35} {oy - 30} Q {oxA - 10} {oy - 35}, {oxA + 20} {oy - 75}" fill="none" stroke="#0284c7" stroke-width="2" />
    <!-- Right branch curving down sharply from peak -->
    <path d="M {oxA + 20} {oy - 75} Q {oxA + 45} {oy - 35}, {oxA + 75} {oy - 35}" fill="none" stroke="#0284c7" stroke-width="2" />

    <text x="{oxA - 15}" y="{oy + 40}" {FONT} font-size="12" fill="#1e293b">(a) A corner</text>
    '''

    # Panel B: A discontinuity
    oxB = 300
    panel_b = f'''
    <!-- Panel B: Discontinuity -->
    <line x1="{oxB - 65}" y1="{oy}" x2="{oxB + 95}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <line x1="{oxB - 40}" y1="{oy + 25}" x2="{oxB - 40}" y2="{oy - 120}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <text x="{oxB + 98}" y="{oy + 14}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{oxB - 52}" y="{oy - 115}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{oxB - 48}" y="{oy + 14}" {FONT} font-size="10">0</text>

    <!-- Tick mark at a -->
    <line x1="{oxB + 20}" y1="{oy - 3}" x2="{oxB + 20}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{oxB + 17}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">a</text>

    <!-- Left curve ending at open circle -->
    <path d="M {oxB - 35} {oy - 15} Q {oxB - 10} {oy - 55}, {oxB + 16} {oy - 65}" fill="none" stroke="#0284c7" stroke-width="2" />
    <circle cx="{oxB + 20}" cy="{oy - 65}" r="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.8" />

    <!-- Right curve starting at solid dot -->
    <circle cx="{oxB + 20}" cy="{oy - 25}" r="3.2" fill="#0284c7" />
    <path d="M {oxB + 20} {oy - 25} Q {oxB + 45} {oy - 20}, {oxB + 75} {oy - 45}" fill="none" stroke="#0284c7" stroke-width="2" />

    <text x="{oxB - 25}" y="{oy + 40}" {FONT} font-size="12" fill="#1e293b">(b) A discontinuity</text>
    '''

    # Panel C: A vertical tangent
    oxC = 510
    panel_c = f'''
    <!-- Panel C: Vertical tangent -->
    <line x1="{oxC - 65}" y1="{oy}" x2="{oxC + 95}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <line x1="{oxC - 40}" y1="{oy + 25}" x2="{oxC - 40}" y2="{oy - 120}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <text x="{oxC + 98}" y="{oy + 14}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{oxC - 52}" y="{oy - 115}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{oxC - 48}" y="{oy + 14}" {FONT} font-size="10">0</text>

    <!-- Tick mark at a -->
    <line x1="{oxC + 20}" y1="{oy - 3}" x2="{oxC + 20}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{oxC + 17}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">a</text>

    <!-- Vertical tangent line in pink/magenta -->
    <line x1="{oxC + 20}" y1="{oy - 95}" x2="{oxC + 20}" y2="{oy}" stroke="#db2777" stroke-width="2" />

    <!-- Curve with vertical inflection at x = a -->
    <!-- Left half: rises to local crest, plunges vertically at x=a -->
    <path d="M {oxC - 35} {oy - 25} C {oxC - 15} {oy - 75}, {oxC + 15} {oy - 70}, {oxC + 20} {oy - 48}" fill="none" stroke="#0284c7" stroke-width="2" />
    <!-- Right half: continues from vertical slope down to trough and rises -->
    <path d="M {oxC + 20} {oy - 48} C {oxC + 25} {oy - 25}, {oxC + 55} {oy - 20}, {oxC + 75} {oy - 50}" fill="none" stroke="#0284c7" stroke-width="2" />

    <text x="{oxC - 25}" y="{oy + 40}" {FONT} font-size="12" fill="#1e293b">(c) A vertical tangent</text>
    '''

    caption = f'<text x="25" y="245" {FONT} font-size="12" font-weight="bold" fill="#1e293b">FIGURE 7: Three Ways for a Function to Fail to Be Differentiable</text>'
    return svg_wrapper(w, h, panel_a + panel_b + panel_c + caption)


def main():
    figs = {
        "sec2_7_figure_parabola_tangent.svg": make_fig_example1_parabola(),
        "sec2_7_figure4_hyperbola_tangent.svg": make_fig_sec2_7_fig4(),
        "sec2_7_exercise12_runners.svg": make_fig_sec2_7_exercise12(),
        "sec2_8_figure5_abs_derivative.svg": make_fig_sec2_8_fig5(),
        "sec2_8_figure7_non_differentiable.svg": make_fig_sec2_8_fig7(),
    }

    for filename, content in figs.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filepath}")

if __name__ == "__main__":
    main()
