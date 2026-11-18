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
    <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#d92672" />
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

# 1. Figure 3: y = |x|
def make_fig_sec2_3_fig3():
    w, h = 320, 220
    ox, oy = 160, 165
    u = 35

    axes = f'''
    <line x1="{ox - 130}" y1="{oy}" x2="{ox + 130}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 30}" x2="{ox}" y2="{oy - 145}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 135}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 12}" y="{oy - 140}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>
    '''

    curve = f'''
    <line x1="{ox - 3.2*u}" y1="{oy - 3.2*u}" x2="{ox}" y2="{oy}" stroke="#0284c7" stroke-width="2.2" />
    <line x1="{ox}" y1="{oy}" x2="{ox + 3.2*u}" y2="{oy - 3.2*u}" stroke="#0284c7" stroke-width="2.2" />
    <text x="{ox + 1.2*u}" y="{oy - 2.5*u}" {FONT} font-size="12" font-style="italic" fill="#0f172a">y = |x|</text>
    '''
    caption = f'<text x="25" y="205" {FONT} font-size="12" font-weight="bold">FIGURE 3</text>'
    return svg_wrapper(w, h, axes + curve + caption)

# 2. Figure 4: y = |x|/x
def make_fig_sec2_3_fig4():
    w, h = 340, 230
    ox, oy = 170, 120
    u = 35

    axes = f'''
    <line x1="{ox - 140}" y1="{oy}" x2="{ox + 140}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 85}" x2="{ox}" y2="{oy - 95}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 145}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 12}" y="{oy - 90}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>
    <line x1="{ox - 3}" y1="{oy - 1.2*u}" x2="{ox + 3}" y2="{oy - 1.2*u}" stroke="#1e293b" />
    <text x="{ox - 14}" y="{oy - 1.2*u + 4}" {FONT} font-size="11">1</text>
    <line x1="{ox - 3}" y1="{oy + 1.2*u}" x2="{ox + 3}" y2="{oy + 1.2*u}" stroke="#1e293b" />
    <text x="{ox - 18}" y="{oy + 1.2*u + 4}" {FONT} font-size="11">-1</text>
    '''

    curve = f'''
    <line x1="{ox - 130}" y1="{oy + 1.2*u}" x2="{ox}" y2="{oy + 1.2*u}" stroke="#0284c7" stroke-width="2.2" />
    <circle cx="{ox}" cy="{oy + 1.2*u}" r="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.8" />
    <line x1="{ox}" y1="{oy - 1.2*u}" x2="{ox + 130}" y2="{oy - 1.2*u}" stroke="#0284c7" stroke-width="2.2" />
    <circle cx="{ox}" cy="{oy - 1.2*u}" r="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.8" />
    <text x="{ox - 120}" y="{oy - 1.2*u - 8}" {FONT} font-size="13" font-style="italic" fill="#0f172a">y = |x| / x</text>
    '''
    caption = f'<text x="25" y="215" {FONT} font-size="12" font-weight="bold">FIGURE 4</text>'
    return svg_wrapper(w, h, axes + curve + caption)

# 3. Figure 5: Piecewise corner (Example 9)
def make_fig_sec2_3_fig5():
    w, h = 380, 230
    ox, oy = 80, 165
    u = 30

    axes = f'''
    <line x1="{ox - 50}" y1="{oy}" x2="{ox + 270}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 35}" x2="{ox}" y2="{oy - 145}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 275}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 12}" y="{oy - 140}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>
    <text x="{ox + 4*u - 4}" y="{oy + 16}" {FONT} font-size="11">4</text>
    <line x1="{ox + 4*u}" y1="{oy - 3}" x2="{ox + 4*u}" y2="{oy + 3}" stroke="#1e293b" />
    '''

    curve = f'''
    <line x1="{ox + 1.2*u}" y1="{oy - 3.8*u}" x2="{ox + 4*u}" y2="{oy}" stroke="#0284c7" stroke-width="2.2" />
    <path d="M {ox + 4*u} {oy} Q {ox + 5.5*u} {oy - 1.2*u}, {ox + 8*u} {oy - 1.6*u}" fill="none" stroke="#0284c7" stroke-width="2.2" />
    <circle cx="{ox + 4*u}" cy="{oy}" r="3.2" fill="#0284c7" />
    '''
    caption = f'<text x="25" y="215" {FONT} font-size="12" font-weight="bold">FIGURE 5</text>'
    return svg_wrapper(w, h, axes + curve + caption)

# 4. Figure 6: Greatest Integer Function
def make_fig_sec2_3_fig6():
    w, h = 340, 290
    ox, oy = 110, 185
    u = 26

    grid = []
    for x in range(-2, 6):
        px = ox + x * u
        grid.append(f'<line x1="{px}" y1="{oy - 4.5*u}" x2="{px}" y2="{oy + 2.5*u}" stroke="#cbd5e1" stroke-width="0.8" />')
    for y in range(-2, 5):
        py = oy - y * u
        grid.append(f'<line x1="{ox - 2*u}" y1="{py}" x2="{ox + 5.5*u}" y2="{py}" stroke="#cbd5e1" stroke-width="0.8" />')

    axes = f'''
    <line x1="{ox - 2.2*u}" y1="{oy}" x2="{ox + 6*u}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 2.5*u}" x2="{ox}" y2="{oy - 4.8*u}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <text x="{ox + 6*u + 4}" y="{oy + 14}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox - 10}" y="{oy - 4.8*u}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox - 10}" y="{oy + 14}" {FONT} font-size="10">0</text>
    '''
    ticks = []
    for x in range(1, 6):
        ticks.append(f'<text x="{ox + x*u - 3}" y="{oy + 14}" {FONT} font-size="10">{x}</text>')
    for y in range(1, 5):
        ticks.append(f'<text x="{ox - 12}" y="{oy - y*u + 4}" {FONT} font-size="10">{y}</text>')

    steps = []
    for n in range(-2, 5):
        x1 = ox + n * u
        x2 = ox + (n + 1) * u
        y = oy - n * u
        steps.append(f'''
        <line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#0284c7" stroke-width="2.2" />
        <circle cx="{x1}" cy="{y}" r="2.8" fill="#0284c7" />
        <circle cx="{x2}" cy="{y}" r="3.2" fill="#ffffff" stroke="#0284c7" stroke-width="1.6" />
        ''')

    label = f'<text x="{ox + 2.8*u}" y="{oy - 3.2*u}" {FONT} font-size="12" font-style="italic" fill="#0f172a">y = ⟦x⟧</text>'
    caption = f'<text x="25" y="275" {FONT} font-size="12" font-weight="bold">FIGURE 6</text>'
    content = "".join(grid) + axes + "".join(ticks) + "".join(steps) + label + caption
    return svg_wrapper(w, h, content)

# 5. Figure 7: Squeeze Theorem concept
def make_fig_sec2_3_fig7():
    w, h = 380, 240
    ox, oy = 80, 185
    u = 30

    axes = f'''
    <line x1="{ox - 40}" y1="{oy}" x2="{ox + 260}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 30}" x2="{ox}" y2="{oy - 160}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 265}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 12}" y="{oy - 155}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>
    '''

    ax = ox + 130
    ly = oy - 65

    dashed = f'''
    <line x1="{ox}" y1="{ly}" x2="{ax}" y2="{ly}" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4 3" />
    <line x1="{ax}" y1="{oy}" x2="{ax}" y2="{ly}" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4 3" />
    <text x="{ax - 3}" y="{oy + 16}" {FONT} font-size="12" font-style="italic">a</text>
    <text x="{ox - 16}" y="{ly + 4}" {FONT} font-size="12" font-style="italic">L</text>
    '''

    # Upper curve h(x) (green)
    h_d = f"M {ox - 30} {oy - 130} Q {ox + 30} {oy - 150}, {ax} {ly} Q {ox + 190} {oy - 110}, {ox + 240} {oy - 145}"
    curve_h = f'<path d="{h_d}" fill="none" stroke="#16a34a" stroke-width="2" />' \
              f'<text x="{ox + 245}" y="{oy - 140}" {FONT} font-size="12" font-style="italic" fill="#16a34a">h</text>'

    # Middle curve g(x) (pink)
    g_d = f"M {ox - 30} {oy - 70} Q {ox + 20} {oy - 60}, {ox + 60} {oy - 95} Q {ox + 95} {oy - 65}, {ax} {ly} Q {ox + 175} {oy - 75}, {ox + 240} {oy - 110}"
    curve_g = f'<path d="{g_d}" fill="none" stroke="#d92672" stroke-width="2.2" />' \
              f'<text x="{ox + 245}" y="{oy - 105}" {FONT} font-size="12" font-style="italic" fill="#d92672">g</text>'

    # Lower curve f(x) (sky)
    f_d = f"M {ox - 30} {oy - 50} Q {ox + 40} {oy - 40}, {ax} {ly} Q {ox + 190} {oy - 55}, {ox + 240} {oy - 30}"
    curve_f = f'<path d="{f_d}" fill="none" stroke="#0284c7" stroke-width="2" />' \
              f'<text x="{ox + 245}" y="{oy - 25}" {FONT} font-size="12" font-style="italic" fill="#0284c7">f</text>'

    caption = f'<text x="25" y="225" {FONT} font-size="12" font-weight="bold">FIGURE 7</text>'
    return svg_wrapper(w, h, axes + dashed + curve_h + curve_g + curve_f + caption)

# 6. Figure 8: Squeeze Theorem for x^2 sin(1/x)
def make_fig_sec2_3_fig8():
    w, h = 420, 270
    ox, oy = 210, 135
    u = 80

    axes = f'''
    <line x1="{ox - 170}" y1="{oy}" x2="{ox + 170}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 105}" x2="{ox}" y2="{oy - 115}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 175}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 12}" y="{oy - 110}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>
    '''

    # Parabola y = x^2 (green)
    pts_up = []
    pts_down = []
    for i in range(-160, 161, 4):
        x_val = i / 100.0
        px = ox + x_val * u
        py_up = oy - (x_val**2) * 45
        py_dn = oy + (x_val**2) * 45
        pts_up.append(f"{px:.1f},{py_up:.1f}")
        pts_down.append(f"{px:.1f},{py_dn:.1f}")

    parab_up = f'<polyline points="{" ".join(pts_up)}" fill="none" stroke="#16a34a" stroke-width="1.8" />' \
               f'<text x="{ox + 65}" y="{oy - 85}" {FONT} font-size="12" font-style="italic" fill="#16a34a">y = x²</text>'
    parab_dn = f'<polyline points="{" ".join(pts_down)}" fill="none" stroke="#0284c7" stroke-width="1.8" />' \
               f'<text x="{ox + 65}" y="{oy + 95}" {FONT} font-size="12" font-style="italic" fill="#0284c7">y = -x²</text>'

    # Oscillating function x^2 sin(1/x)
    pts_osc = []
    for i in range(-150, 151):
        if i == 0:
            pts_osc.append(f"{ox},{oy}")
            continue
        x_val = i / 100.0
        # Smooth damping wave
        y_val = (x_val**2) * math.sin(12.0 / x_val) * 45
        px = ox + x_val * u
        py = oy - y_val
        pts_osc.append(f"{px:.1f},{py:.1f}")

    curve_osc = f'<polyline points="{" ".join(pts_osc)}" fill="none" stroke="#d92672" stroke-width="1.6" />'

    caption = f'<text x="25" y="245" {FONT} font-size="12" font-weight="bold">FIGURE 8: <tspan font-weight="normal" font-style="italic">y = x² sin(1/x)</tspan></text>'
    return svg_wrapper(w, h, axes + parab_up + parab_dn + curve_osc + caption)

# 7. Section 2.3 Exercise 2: Graphs of f and g
def make_fig_sec2_3_ex2():
    w, h = 580, 260
    # Left grid: f(x)
    ox1, oy1 = 120, 140
    # Right grid: g(x)
    ox2, oy2 = 390, 140
    u = 24

    def draw_grid_axes(ox, oy, x_min, x_max, y_min, y_max, fn_name):
        lines = []
        for x in range(x_min, x_max + 1):
            px = ox + x * u
            lines.append(f'<line x1="{px}" y1="{oy - y_max*u}" x2="{px}" y2="{oy - y_min*u}" stroke="#cbd5e1" stroke-width="0.8" />')
        for y in range(y_min, y_max + 1):
            py = oy - y * u
            lines.append(f'<line x1="{ox + x_min*u}" y1="{py}" x2="{ox + x_max*u}" y2="{py}" stroke="#cbd5e1" stroke-width="0.8" />')

        ax = f'''
        <line x1="{ox + x_min*u - 10}" y1="{oy}" x2="{ox + x_max*u + 15}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
        <line x1="{ox}" y1="{oy - y_min*u + 10}" x2="{ox}" y2="{oy - y_max*u - 15}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
        <text x="{ox + x_max*u + 18}" y="{oy + 14}" {FONT} font-size="11" font-style="italic">x</text>
        <text x="{ox - 10}" y="{oy - y_max*u - 12}" {FONT} font-size="11" font-style="italic">y</text>
        <text x="{ox - 10}" y="{oy + 14}" {FONT} font-size="10">0</text>
        <text x="{ox + u - 3}" y="{oy + 14}" {FONT} font-size="10">1</text>
        <text x="{ox - 10}" y="{oy - u + 4}" {FONT} font-size="10">1</text>
        <text x="{ox - 30}" y="{oy - y_max*u - 2}" {FONT} font-size="12" font-style="italic" fill="#0f172a">{fn_name}</text>
        '''
        return "".join(lines) + ax

    grid1 = draw_grid_axes(ox1, oy1, -2, 3, -1, 3, "y = f(x)")
    grid2 = draw_grid_axes(ox2, oy2, -2, 3, -1, 3, "y = g(x)")

    # Curve for f(x):
    # Passes (-2, 1), drops to (-1, 0), through (0, 0), (1, 1), up to open circle at (2, 2).
    # Isolated solid dot at (2, 1). After x=2, goes to (3, 1).
    curve_f = f'''
    <path d="M {ox1 - 2*u} {oy1 - 1*u} C {ox1 - 1.5*u} {oy1 + 0.5*u}, {ox1 - 0.8*u} {oy1 + 0.4*u}, {ox1} {oy1} C {ox1 + 0.6*u} {oy1 - 0.4*u}, {ox1 + 1.2*u} {oy1 - 1.2*u}, {ox1 + 2*u} {oy1 - 2*u}" fill="none" stroke="#d92672" stroke-width="2" />
    <circle cx="{ox1 + 2*u}" cy="{oy1 - 2*u}" r="3.2" fill="#ffffff" stroke="#d92672" stroke-width="1.6" />
    <circle cx="{ox1 + 2*u}" cy="{oy1 - 1*u}" r="3" fill="#d92672" />
    <path d="M {ox1 + 2*u} {oy1 - 2*u} L {ox1 + 3*u} {oy1 - 1*u}" fill="none" stroke="#d92672" stroke-width="2" />
    '''

    # Curve for g(x):
    # From (-2, -1) curving up through (-1, 0.5) to open circle at (1, 2).
    # Solid dot at (1, 1). After x=1, drops through (2, 0) to (2.5, -1).
    curve_g = f'''
    <path d="M {ox2 - 2*u} {oy2 + 1*u} Q {ox2 - 0.5*u} {oy2 - 1.8*u}, {ox2 + 1*u} {oy2 - 2*u}" fill="none" stroke="#0284c7" stroke-width="2" />
    <circle cx="{ox2 + 1*u}" cy="{oy2 - 2*u}" r="3.2" fill="#ffffff" stroke="#0284c7" stroke-width="1.6" />
    <circle cx="{ox2 + 1*u}" cy="{oy2 - 1*u}" r="3" fill="#0284c7" />
    <path d="M {ox2 + 1*u} {oy2 - 1*u} Q {ox2 + 1.8*u} {oy2 - 0.8*u}, {ox2 + 2.4*u} {oy2 + 1*u}" fill="none" stroke="#0284c7" stroke-width="2" />
    '''

    caption = f'<text x="25" y="245" {FONT} font-size="12" font-weight="bold">Exercise 2: Graphs of f and g</text>'
    return svg_wrapper(w, h, grid1 + grid2 + curve_f + curve_g + caption)

# 8. Section 2.3 Exercise 47: Signum Function
def make_fig_sec2_3_ex47():
    w, h = 340, 220
    ox, oy = 170, 115
    u = 35

    axes = f'''
    <line x1="{ox - 130}" y1="{oy}" x2="{ox + 130}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 80}" x2="{ox}" y2="{oy - 85}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 135}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 12}" y="{oy - 80}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>
    <text x="{ox - 16}" y="{oy - u + 4}" {FONT} font-size="11">1</text>
    <text x="{ox - 18}" y="{oy + u + 4}" {FONT} font-size="11">-1</text>
    '''

    curve = f'''
    <line x1="{ox - 120}" y1="{oy + u}" x2="{ox}" y2="{oy + u}" stroke="#0284c7" stroke-width="2.2" />
    <circle cx="{ox}" cy="{oy + u}" r="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.8" />
    <circle cx="{ox}" cy="{oy}" r="3.2" fill="#0284c7" />
    <line x1="{ox}" y1="{oy - u}" x2="{ox + 120}" y2="{oy - u}" stroke="#0284c7" stroke-width="2.2" />
    <circle cx="{ox}" cy="{oy - u}" r="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.8" />
    <text x="{ox + 50}" y="{oy - u - 8}" {FONT} font-size="12" font-style="italic" fill="#0f172a">y = sgn(x)</text>
    '''
    caption = f'<text x="25" y="205" {FONT} font-size="12" font-weight="bold">Exercise 47: Signum Function</text>'
    return svg_wrapper(w, h, axes + curve + caption)

# 9. Section 2.3 Exercise 48: Piecewise function graph
def make_fig_sec2_3_ex48():
    w, h = 360, 240
    ox, oy = 110, 170
    u = 32

    axes = f'''
    <line x1="{ox - 70}" y1="{oy}" x2="{ox + 210}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 40}" x2="{ox}" y2="{oy - 145}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 215}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 12}" y="{oy - 140}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>
    <text x="{ox + u - 3}" y="{oy + 14}" {FONT} font-size="11">1</text>
    <text x="{ox + 2*u - 3}" y="{oy + 14}" {FONT} font-size="11">2</text>
    <text x="{ox - 12}" y="{oy - u + 4}" {FONT} font-size="11">1</text>
    <text x="{ox - 12}" y="{oy - 2*u + 4}" {FONT} font-size="11">2</text>
    '''

    # Branch 1: x < 1: y = x^2 + 1 (parabola)
    pts1 = []
    for i in range(-12, 10):
        xv = i / 10.0
        yv = xv**2 + 1
        px = ox + xv * u
        py = oy - yv * u
        pts1.append(f"{px:.1f},{py:.1f}")
    poly1 = f'<polyline points="{" ".join(pts1)}" fill="none" stroke="#0284c7" stroke-width="2.2" />' \
            f'<circle cx="{ox + u}" cy="{oy - 2*u}" r="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.8" />'

    # Branch 2: x >= 1: y = (x - 2)^2
    pts2 = []
    for i in range(10, 35):
        xv = i / 10.0
        yv = (xv - 2)**2
        px = ox + xv * u
        py = oy - yv * u
        pts2.append(f"{px:.1f},{py:.1f}")
    poly2 = f'<polyline points="{" ".join(pts2)}" fill="none" stroke="#0284c7" stroke-width="2.2" />' \
            f'<circle cx="{ox + u}" cy="{oy - u}" r="3" fill="#0284c7" />'

    caption = f'<text x="25" y="225" {FONT} font-size="12" font-weight="bold">Exercise 48: Piecewise Quadratic</text>'
    return svg_wrapper(w, h, axes + poly1 + poly2 + caption)

# 10. Section 2.4 Figure 1: Linear Epsilon-Delta Model
def make_fig_sec2_4_fig1():
    w, h = 440, 310
    ox, oy = 100, 240
    u = 30

    axes = f'''
    <line x1="{ox - 40}" y1="{oy}" x2="{ox + 290}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 30}" x2="{ox}" y2="{oy - 215}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 295}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 12}" y="{oy - 210}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>
    '''

    # Function line passing through (0, -1), (1, 1), (2, 3), (3, 5), (4, 7)
    a_x = ox + 90
    l_y = oy - 150
    delta = 26
    eps = 52

    # Shaded band
    shade = f'<rect x="{a_x - delta}" y="{l_y - eps}" width="{2*delta}" height="{2*eps}" fill="#f0f9ff" stroke="none" />'

    # Guidelines
    dashed = f'''
    <line x1="{a_x - delta}" y1="{oy}" x2="{a_x - delta}" y2="{l_y + eps}" stroke="#0284c7" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="{a_x + delta}" y1="{oy}" x2="{a_x + delta}" y2="{l_y - eps}" stroke="#0284c7" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="{a_x}" y1="{oy}" x2="{a_x}" y2="{l_y}" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 3" />
    <line x1="{ox}" y1="{l_y - eps}" x2="{a_x + delta}" y2="{l_y - eps}" stroke="#0284c7" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="{ox}" y1="{l_y}" x2="{a_x}" y2="{l_y}" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 3" />
    <line x1="{ox}" y1="{l_y + eps}" x2="{a_x - delta}" y2="{l_y + eps}" stroke="#0284c7" stroke-width="1" stroke-dasharray="3 3" />
    '''

    ticks_labels = f'''
    <text x="{a_x - 3}" y="{oy + 15}" {FONT} font-size="11">3</text>
    <text x="{a_x - delta - 12}" y="{oy + 30}" {FONT} font-size="10">3 − δ</text>
    <text x="{a_x + delta - 10}" y="{oy + 30}" {FONT} font-size="10">3 + δ</text>
    <text x="{ox - 20}" y="{l_y + 4}" {FONT} font-size="11">5</text>
    <text x="{ox - 42}" y="{l_y - eps + 4}" {FONT} font-size="10">5 + ε</text>
    <text x="{ox - 42}" y="{l_y + eps + 4}" {FONT} font-size="10">5 − ε</text>
    <text x="{a_x - 45}" y="{oy + 48}" {FONT} font-size="10" fill="#0284c7">when x is in here (x ≠ 3)</text>
    <text x="{ox - 52}" y="{l_y - 8}" {FONT} font-size="10" fill="#0284c7">f(x) is</text>
    <text x="{ox - 52}" y="{l_y + 8}" {FONT} font-size="10" fill="#0284c7">in here</text>
    '''

    # Linear curve
    curve = f'''
    <line x1="{ox + 20}" y1="{oy - 20}" x2="{ox + 130}" y2="{oy - 200}" stroke="#0284c7" stroke-width="2.2" />
    <circle cx="{a_x}" cy="{l_y}" r="3.8" fill="#ffffff" stroke="#0284c7" stroke-width="2" />
    <circle cx="{a_x}" cy="{l_y - 25}" r="3.2" fill="#0284c7" />
    '''

    caption = f'<text x="25" y="295" {FONT} font-size="12" font-weight="bold">FIGURE 1</text>'
    return svg_wrapper(w, h, shade + axes + dashed + ticks_labels + curve + caption)

# 11. Section 2.4 Figures 2 & 3: Arrow diagrams
def make_fig_sec2_4_figs2_3():
    w, h = 580, 260
    
    # Figure 2: Top
    f2_y = 50
    fig2 = f'''
    <line x1="60" y1="{f2_y}" x2="280" y2="{f2_y}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="330" y1="{f2_y}" x2="540" y2="{f2_y}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <circle cx="120" cy="{f2_y}" r="3" fill="#1e293b" />
    <circle cx="180" cy="{f2_y}" r="3" fill="#1e293b" />
    <text x="117" y="{f2_y + 16}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="177" y="{f2_y + 16}" {FONT} font-size="11" font-style="italic">a</text>
    <circle cx="400" cy="{f2_y}" r="3" fill="#1e293b" />
    <circle cx="460" cy="{f2_y}" r="3" fill="#1e293b" />
    <text x="390" y="{f2_y + 16}" {FONT} font-size="11" font-style="italic">f(a)</text>
    <text x="450" y="{f2_y + 16}" {FONT} font-size="11" font-style="italic">f(x)</text>
    <path d="M 120 {f2_y - 6} Q 280 {f2_y - 45}, 460 {f2_y - 6}" fill="none" stroke="#d92672" stroke-width="1.8" marker-end="url(#arrow-pink)" />
    <path d="M 180 {f2_y - 6} Q 290 {f2_y - 30}, 400 {f2_y - 6}" fill="none" stroke="#d92672" stroke-width="1.8" marker-end="url(#arrow-pink)" />
    <text x="300" y="{f2_y - 25}" {FONT} font-size="12" font-style="italic" fill="#0f172a">f</text>
    <text x="25" y="{f2_y + 5}" {FONT} font-size="11" font-weight="bold">FIGURE 2</text>
    '''

    # Figure 3: Bottom
    f3_y = 170
    fig3 = f'''
    <line x1="60" y1="{f3_y}" x2="280" y2="{f3_y}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="330" y1="{f3_y}" x2="540" y2="{f3_y}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <!-- Interval (a - delta, a + delta) -->
    <line x1="120" y1="{f3_y}" x2="200" y2="{f3_y}" stroke="#0284c7" stroke-width="3" />
    <circle cx="160" cy="{f3_y}" r="3" fill="#1e293b" />
    <circle cx="140" cy="{f3_y}" r="2.5" fill="#d92672" />
    <text x="105" y="{f3_y + 18}" {FONT} font-size="10">a − δ</text>
    <text x="157" y="{f3_y + 18}" {FONT} font-size="11" font-style="italic">a</text>
    <text x="195" y="{f3_y + 18}" {FONT} font-size="10">a + δ</text>
    <text x="137" y="{f3_y + 18}" {FONT} font-size="10" font-style="italic">x</text>

    <!-- Interval (L - eps, L + eps) -->
    <line x1="380" y1="{f3_y}" x2="480" y2="{f3_y}" stroke="#ea580c" stroke-width="3" />
    <circle cx="430" cy="{f3_y}" r="3" fill="#1e293b" />
    <circle cx="460" cy="{f3_y}" r="2.5" fill="#d92672" />
    <text x="365" y="{f3_y + 18}" {FONT} font-size="10">L − ε</text>
    <text x="427" y="{f3_y + 18}" {FONT} font-size="11" font-style="italic">L</text>
    <text x="475" y="{f3_y + 18}" {FONT} font-size="10">L + ε</text>
    <text x="455" y="{f3_y - 8}" {FONT} font-size="10" font-style="italic">f(x)</text>

    <path d="M 140 {f3_y - 6} Q 290 {f3_y - 45}, 460 {f3_y - 6}" fill="none" stroke="#d92672" stroke-width="1.8" marker-end="url(#arrow-pink)" />
    <text x="300" y="{f3_y - 25}" {FONT} font-size="12" font-style="italic" fill="#0f172a">f</text>
    <text x="25" y="{f3_y + 5}" {FONT} font-size="11" font-weight="bold">FIGURE 3</text>
    '''

    return svg_wrapper(w, h, fig2 + fig3)

# 12. Section 2.4 Figures 4, 5, 6: Geometric strip interpretation
def make_fig_sec2_4_figs4_5_6():
    w, h = 640, 240
    u = 18

    def make_strip_panel(ox, oy, fig_num, show_vert=False, tighter=False):
        eps_px = 24 if not tighter else 14
        delta_px = 30 if not tighter else 16
        ax = ox + 65
        ly = oy - 65

        ax_svg = f'''
        <line x1="{ox - 20}" y1="{oy}" x2="{ox + 130}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
        <line x1="{ox}" y1="{oy + 20}" x2="{ox}" y2="{oy - 125}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
        <text x="{ox + 132}" y="{oy + 12}" {FONT} font-size="10" font-style="italic">x</text>
        <text x="{ox - 10}" y="{oy - 120}" {FONT} font-size="10" font-style="italic">y</text>
        <text x="{ox - 8}" y="{oy + 12}" {FONT} font-size="9">0</text>
        '''

        # Horizontal band
        h_band = f'<rect x="{ox - 10}" y="{ly - eps_px}" width="140" height="{2*eps_px}" fill="#e0f2fe" opacity="0.85" />'
        h_lines = f'''
        <line x1="{ox - 10}" y1="{ly - eps_px}" x2="{ox + 130}" y2="{ly - eps_px}" stroke="#0284c7" stroke-width="1" />
        <line x1="{ox - 10}" y1="{ly + eps_px}" x2="{ox + 130}" y2="{ly + eps_px}" stroke="#0284c7" stroke-width="1" />
        <line x1="{ox}" y1="{ly}" x2="{ox + 130}" y2="{ly}" stroke="#64748b" stroke-width="1" stroke-dasharray="3 2" />
        <text x="{ox + 75}" y="{ly - eps_px - 4}" {FONT} font-size="9">y = L + ε</text>
        <text x="{ox + 75}" y="{ly + eps_px + 12}" {FONT} font-size="9">y = L − ε</text>
        <text x="{ox - 16}" y="{ly + 3}" {FONT} font-size="10" font-style="italic">L</text>
        '''

        # Vertical strip (if enabled)
        v_band = ""
        v_lines = ""
        if show_vert:
            v_band = f'<rect x="{ax - delta_px}" y="{ly - eps_px}" width="{2*delta_px}" height="{2*eps_px}" fill="#fed7aa" opacity="0.85" />'
            v_lines = f'''
            <line x1="{ax - delta_px}" y1="{oy}" x2="{ax - delta_px}" y2="{ly - eps_px}" stroke="#ea580c" stroke-width="1" />
            <line x1="{ax + delta_px}" y1="{oy}" x2="{ax + delta_px}" y2="{ly - eps_px}" stroke="#ea580c" stroke-width="1" />
            <line x1="{ax}" y1="{oy}" x2="{ax}" y2="{ly}" stroke="#64748b" stroke-width="1" stroke-dasharray="3 2" />
            <text x="{ax - 2}" y="{oy + 12}" {FONT} font-size="10" font-style="italic">a</text>
            <text x="{ax - delta_px - 8}" y="{oy + 22}" {FONT} font-size="8">a − δ</text>
            <text x="{ax + delta_px - 6}" y="{oy + 22}" {FONT} font-size="8">a + δ</text>
            '''

        # Curve
        curve_d = f"M {ox - 10} {oy - 100} C {ox + 35} {oy - 100}, {ax} {ly}, {ox + 85} {oy - 30} S {ox + 120} {oy - 75}, {ox + 130} {oy - 85}"
        curve = f'<path d="{curve_d}" fill="none" stroke="#d92672" stroke-width="1.8" />'

        caption = f'<text x="{ox + 20}" y="225" {FONT} font-size="11" font-weight="bold">FIGURE {fig_num}</text>'
        return h_band + v_band + ax_svg + h_lines + v_lines + curve + caption

    p1 = make_strip_panel(30, 180, 4)
    p2 = make_strip_panel(240, 180, 5, show_vert=True)
    p3 = make_strip_panel(450, 180, 6, show_vert=True, tighter=True)

    return svg_wrapper(w, h, p1 + p2 + p3)

# 13. Section 2.4 Figures 7 & 8: Graphical Determination of Delta (Cubic)
def make_fig_sec2_4_figs7_8():
    w, h = 580, 260
    
    # Left: Figure 7 overview f(x) = x^3 - 5x + 6 on [-3, 3] x [-5, 15]
    ox1, oy1 = 110, 160
    box1 = f'''
    <rect x="25" y="20" width="170" height="180" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1" />
    <line x1="25" y1="{oy1}" x2="195" y2="{oy1}" stroke="#1e293b" stroke-width="1.2" />
    <line x1="{ox1}" y1="20" x2="{ox1}" y2="200" stroke="#1e293b" stroke-width="1.2" />
    <text x="30" y="{oy1 + 14}" {FONT} font-size="10">-3</text>
    <text x="180" y="{oy1 + 14}" {FONT} font-size="10">3</text>
    <text x="{ox1 - 10}" y="35" {FONT} font-size="10">15</text>
    <text x="{ox1 - 10}" y="195" {FONT} font-size="10">-5</text>
    '''
    # Plot cubic y = x^3 - 5x + 6
    pts1 = []
    for i in range(-25, 26):
        xv = i / 10.0
        yv = xv**3 - 5*xv + 6
        px = ox1 + xv * 26
        py = oy1 - (yv / 15.0) * 110
        if 20 <= py <= 200:
            pts1.append(f"{px:.1f},{py:.1f}")
    poly1 = f'<polyline points="{" ".join(pts1)}" fill="none" stroke="#d92672" stroke-width="1.8" />'
    cap1 = f'<text x="65" y="225" {FONT} font-size="11" font-weight="bold">FIGURE 7</text>'

    # Right: Figure 8 Zoom-in near (1, 2)
    # x in [0.8, 1.2], y in [1.7, 2.3]
    ox2, oy2 = 270, 20
    w2, h2 = 270, 180
    box2 = f'''
    <rect x="{ox2}" y="{oy2}" width="{w2}" height="{h2}" fill="#ffffff" stroke="#94a3b8" stroke-width="1" />
    <text x="{ox2 - 25}" y="{oy2 + 25}" {FONT} font-size="10">2.3</text>
    <text x="{ox2 - 25}" y="{oy2 + h2 - 15}" {FONT} font-size="10">1.7</text>
    <text x="{ox2 + 10}" y="{oy2 + h2 + 15}" {FONT} font-size="10">0.8</text>
    <text x="{ox2 + w2 - 25}" y="{oy2 + h2 + 15}" {FONT} font-size="10">1.2</text>
    '''
    # y = 2.2 line (top blue) and y = 1.8 line (bottom blue)
    # y in [1.7, 2.3] => range is 0.6.
    # 2.2 is (2.3 - 2.2)/0.6 = 1/6 down = 30px
    # 1.8 is (2.3 - 1.8)/0.6 = 5/6 down = 150px
    # 2.0 is 3/6 down = 90px
    y_22 = oy2 + 30
    y_18 = oy2 + 150
    y_20 = oy2 + 90
    
    # x in [0.8, 1.2] => range is 0.4.
    # x=1 is (1 - 0.8)/0.4 = 0.5 = 135px from left = ox2 + 135
    # x=0.911 is (0.911 - 0.8)/0.4 = 0.2775 => ox2 + 75
    # x=1.124 is (1.124 - 0.8)/0.4 = 0.81 => ox2 + 218.7
    x_10 = ox2 + 135
    x_left = ox2 + 75
    x_right = ox2 + 219

    lines2 = f'''
    <line x1="{ox2}" y1="{y_22}" x2="{ox2 + w2}" y2="{y_22}" stroke="#0284c7" stroke-width="1.2" />
    <text x="{ox2 + w2 - 60}" y="{y_22 - 6}" {FONT} font-size="10" fill="#0284c7">y = 2.2</text>
    <line x1="{ox2}" y1="{y_18}" x2="{ox2 + w2}" y2="{y_18}" stroke="#0284c7" stroke-width="1.2" />
    <text x="{ox2 + 15}" y="{y_18 - 6}" {FONT} font-size="10" fill="#0284c7">y = 1.8</text>
    <line x1="{x_left}" y1="{oy2}" x2="{x_left}" y2="{oy2 + h2}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2" />
    <line x1="{x_right}" y1="{oy2}" x2="{x_right}" y2="{oy2 + h2}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2" />
    <line x1="{x_10}" y1="{oy2}" x2="{x_10}" y2="{oy2 + h2}" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 2" />
    <circle cx="{x_10}" cy="{y_20}" r="3.2" fill="#d92672" />
    <circle cx="{x_left}" cy="{y_22}" r="3" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" />
    <circle cx="{x_right}" cy="{y_18}" r="3" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" />
    <text x="{x_10 - 24}" y="{y_20 + 16}" {FONT} font-size="10" fill="#0f172a">(1, 2)</text>
    <text x="{ox2 + 45}" y="{oy2 + 65}" {FONT} font-size="10" fill="#d92672">y = x³ − 5x + 6</text>
    '''

    # Curve through zoom box
    pts_zoom = [
        f"{ox2 + 20},{oy2 + 10}",
        f"{x_left},{y_22}",
        f"{x_10},{y_20}",
        f"{x_right},{y_18}",
        f"{ox2 + w2 - 15},{oy2 + h2 - 10}"
    ]
    poly_zoom = f'<path d="M {pts_zoom[0]} C {ox2 + 50} {oy2 + 22}, {x_left} {y_22}, {x_10} {y_20} C {x_10 + 40} {y_20 + 25}, {x_right} {y_18}, {pts_zoom[4]}" fill="none" stroke="#d92672" stroke-width="2" />'

    cap2 = f'<text x="360" y="225" {FONT} font-size="11" font-weight="bold">FIGURE 8</text>'

    return svg_wrapper(w, h, box1 + poly1 + cap1 + box2 + lines2 + poly_zoom + cap2)

# 14. Section 2.4 Figure 10: Infinite Limit (Positive Infinity)
def make_fig_sec2_4_fig10():
    w, h = 360, 180
    ox, oy = 180, 145
    u = 25

    axes = f'''
    <line x1="{ox - 140}" y1="{oy}" x2="{ox + 140}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox - 110}" y1="{oy + 20}" x2="{ox - 110}" y2="{oy - 125}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 145}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 122}" y="{oy - 120}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 122}" y="{oy + 14}" {FONT} font-size="11">0</text>
    '''

    ax = ox + 15
    m_y = oy - 70
    delta = 22

    # Vertical asymptote at ax
    asymptote = f'<line x1="{ax}" y1="{oy + 15}" x2="{ax}" y2="{oy - 120}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3" />'
    
    # Horizontal line y = M
    m_line = f'''
    <line x1="{ox - 130}" y1="{m_y}" x2="{ox + 130}" y2="{m_y}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{ox + 75}" y="{m_y - 6}" {FONT} font-size="11" font-style="italic">y = M</text>
    <text x="{ox - 125}" y="{m_y + 4}" {FONT} font-size="11" font-style="italic">M</text>
    '''

    # Vertical band (a - delta, a + delta)
    v_band = f'''
    <rect x="{ax - delta}" y="{oy - 120}" width="{2*delta}" height="120" fill="#fef3c7" opacity="0.6" />
    <line x1="{ax - delta}" y1="{oy}" x2="{ax - delta}" y2="{m_y}" stroke="#d97706" stroke-width="1.2" stroke-dasharray="3 2" />
    <line x1="{ax + delta}" y1="{oy}" x2="{ax + delta}" y2="{m_y}" stroke="#d97706" stroke-width="1.2" stroke-dasharray="3 2" />
    <text x="{ax - 2}" y="{oy + 14}" {FONT} font-size="11" font-style="italic">a</text>
    <text x="{ax - delta - 10}" y="{oy + 24}" {FONT} font-size="9">a − δ</text>
    <text x="{ax + delta - 8}" y="{oy + 24}" {FONT} font-size="9">a + δ</text>
    '''

    # Hyperbolic curve branches going to +inf
    curve_left = f'<path d="M {ax - 130} {oy - 12} Q {ax - 35} {oy - 20}, {ax - 6} {oy - 120}" fill="none" stroke="#0284c7" stroke-width="2.2" />'
    curve_right = f'<path d="M {ax + 6} {oy - 120} Q {ax + 35} {oy - 20}, {ax + 130} {oy - 12}" fill="none" stroke="#0284c7" stroke-width="2.2" />'

    caption = f'<text x="25" y="170" {FONT} font-size="11" font-weight="bold">FIGURE 10</text>'
    return svg_wrapper(w, h, v_band + axes + asymptote + m_line + curve_left + curve_right + caption)

# 15. Section 2.4 Figure 11: Infinite Limit (Negative Infinity)
def make_fig_sec2_4_fig11():
    w, h = 360, 180
    ox, oy = 180, 55
    u = 25

    axes = f'''
    <line x1="{ox - 140}" y1="{oy}" x2="{ox + 140}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox - 110}" y1="{oy + 115}" x2="{ox - 110}" y2="{oy - 35}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 145}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 122}" y="{oy - 30}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 122}" y="{oy + 14}" {FONT} font-size="11">0</text>
    '''

    ax = ox + 15
    n_y = oy + 65
    delta = 22

    # Vertical asymptote at ax
    asymptote = f'<line x1="{ax}" y1="{oy - 30}" x2="{ax}" y2="{oy + 110}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3" />'

    # Horizontal line y = N
    n_line = f'''
    <line x1="{ox - 130}" y1="{n_y}" x2="{ox + 130}" y2="{n_y}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{ox + 75}" y="{n_y + 16}" {FONT} font-size="11" font-style="italic">y = N</text>
    <text x="{ox - 125}" y="{n_y + 4}" {FONT} font-size="11" font-style="italic">N</text>
    '''

    # Vertical band (a - delta, a + delta)
    v_band = f'''
    <rect x="{ax - delta}" y="{oy}" width="{2*delta}" height="110" fill="#fef3c7" opacity="0.6" />
    <line x1="{ax - delta}" y1="{oy}" x2="{ax - delta}" y2="{n_y}" stroke="#d97706" stroke-width="1.2" stroke-dasharray="3 2" />
    <line x1="{ax + delta}" y1="{oy}" x2="{ax + delta}" y2="{n_y}" stroke="#d97706" stroke-width="1.2" stroke-dasharray="3 2" />
    <text x="{ax - 2}" y="{oy - 8}" {FONT} font-size="11" font-style="italic">a</text>
    <text x="{ax - delta - 10}" y="{oy - 8}" {FONT} font-size="9">a − δ</text>
    <text x="{ax + delta - 8}" y="{oy - 8}" {FONT} font-size="9">a + δ</text>
    '''

    # Hyperbolic curve branches plunging to -inf
    curve_left = f'<path d="M {ax - 130} {oy + 12} Q {ax - 35} {oy + 20}, {ax - 6} {oy + 110}" fill="none" stroke="#0284c7" stroke-width="2.2" />'
    curve_right = f'<path d="M {ax + 6} {oy + 110} Q {ax + 35} {oy + 20}, {ax + 130} {oy + 12}" fill="none" stroke="#0284c7" stroke-width="2.2" />'

    caption = f'<text x="25" y="170" {FONT} font-size="11" font-weight="bold">FIGURE 11</text>'
    return svg_wrapper(w, h, v_band + axes + asymptote + n_line + curve_left + curve_right + caption)

figures = {
    "sec2_3_figure3_abs_x.svg": make_fig_sec2_3_fig3(),
    "sec2_3_figure4_sign_step.svg": make_fig_sec2_3_fig4(),
    "sec2_3_figure5_piecewise_corner.svg": make_fig_sec2_3_fig5(),
    "sec2_3_figure6_greatest_integer.svg": make_fig_sec2_3_fig6(),
    "sec2_3_figure7_squeeze_theorem.svg": make_fig_sec2_3_fig7(),
    "sec2_3_figure8_squeeze_x2_sin.svg": make_fig_sec2_3_fig8(),
    "sec2_3_ex2_graphs_fg.svg": make_fig_sec2_3_ex2(),
    "sec2_3_ex47_sgn_graph.svg": make_fig_sec2_3_ex47(),
    "sec2_3_ex48_piecewise_graph.svg": make_fig_sec2_3_ex48(),
    "sec2_4_figure1_linear_eps_delta.svg": make_fig_sec2_4_fig1(),
    "sec2_4_figures2_3_arrow_diagrams.svg": make_fig_sec2_4_figs2_3(),
    "sec2_4_figures4_5_6_eps_delta_strips.svg": make_fig_sec2_4_figs4_5_6(),
    "sec2_4_figures7_8_cubic_graphical_delta.svg": make_fig_sec2_4_figs7_8(),
    "sec2_4_figure10_infinite_limit_pos.svg": make_fig_sec2_4_fig10(),
    "sec2_4_figure11_infinite_limit_neg.svg": make_fig_sec2_4_fig11(),
}

for name, svg in figures.items():
    filepath = os.path.join(OUTPUT_DIR, name)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {filepath}")
