import math
import os

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
</defs>
{content}
</svg>'''

# 1. Figure 6: Section 1.1 Function on Grid
def make_fig_sec1_1_fig6():
    w, h = 420, 310
    ox, oy = 100, 175
    u = 26
    grid_lines = []
    for x in range(-2, 9):
        px = ox + x * u
        grid_lines.append(f'<line x1="{px}" y1="{oy - 4*u}" x2="{px}" y2="{oy + 3*u}" stroke="#94a3b8" stroke-width="0.9" />')
    for y in range(-3, 5):
        py = oy - y * u
        grid_lines.append(f'<line x1="{ox - 2*u}" y1="{py}" x2="{ox + 8*u}" y2="{py}" stroke="#94a3b8" stroke-width="0.9" />')
    
    axes = f'''
    <line x1="{ox - 2*u}" y1="{oy}" x2="{ox + 8.5*u}" y2="{oy}" stroke="#1e293b" stroke-width="1.6" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 3*u}" x2="{ox}" y2="{oy - 4.5*u}" stroke="#1e293b" stroke-width="1.6" marker-end="url(#arrow)" />
    <text x="{ox + 8.6*u}" y="{oy + 14}" {FONT} font-size="14" font-style="italic" fill="#1e293b">x</text>
    <text x="{ox - 14}" y="{oy - 4.4*u}" {FONT} font-size="14" font-style="italic" fill="#1e293b">y</text>
    <text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="13" fill="#1e293b">0</text>
    <text x="{ox + u - 4}" y="{oy + 18}" {FONT} font-size="13" fill="#1e293b">1</text>
    <text x="{ox - 16}" y="{oy - u + 4}" {FONT} font-size="13" fill="#1e293b">1</text>
    '''

    p0 = (ox, oy - 1*u)
    p_max = (ox + 1.8*u, oy - 3.8*u)
    p_mid = (ox + 4*u, oy - 1*u)
    p_min = (ox + 6.8*u, oy - (-2.2*u))
    p_end = (ox + 8*u, oy)

    curve_d = f"M {p0[0]} {p0[1]} C {ox + 0.4*u} {oy - 2.2*u}, {ox + 1.2*u} {oy - 3.8*u}, {p_max[0]} {p_max[1]} " \
              f"C {ox + 2.5*u} {oy - 3.8*u}, {ox + 3.2*u} {oy - 2.5*u}, {p_mid[0]} {p_mid[1]} " \
              f"C {ox + 4.2*u} {oy - 0.5*u}, {ox + 4.4*u} {oy + 0.5*u}, {ox + 5.0*u} {oy + 1.4*u} " \
              f"C {ox + 5.8*u} {oy + 2.3*u}, {ox + 6.3*u} {p_min[1]}, {p_min[0]} {p_min[1]} " \
              f"C {ox + 7.4*u} {p_min[1]}, {ox + 7.8*u} {oy - 0.5*u}, {p_end[0]} {p_end[1]}"

    curve = f'<path d="{curve_d}" fill="none" stroke="#d92672" stroke-width="2.2" stroke-linecap="round" />'
    caption = f'<text x="50" y="295" {FONT} font-size="13" font-weight="bold" fill="#0f172a" letter-spacing="0.5">FIGURE 6</text>'

    content = '\n'.join(grid_lines) + axes + curve + caption
    return svg_wrapper(w, h, content)

# 2. Figure 5: Section 1.1 Domain and Range
def make_fig_sec1_1_fig5():
    w, h = 420, 250
    ox, oy = 80, 185
    
    axes = f'''
    <line x1="{ox - 40}" y1="{oy}" x2="{ox + 290}" y2="{oy}" stroke="#1e293b" stroke-width="1.6" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 30}" x2="{ox}" y2="{oy - 160}" stroke="#1e293b" stroke-width="1.6" marker-end="url(#arrow)" />
    <text x="{ox + 295}" y="{oy + 14}" {FONT} font-size="14" font-style="italic" fill="#1e293b">x</text>
    <text x="{ox - 14}" y="{oy - 155}" {FONT} font-size="14" font-style="italic" fill="#1e293b">y</text>
    <text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="13" fill="#1e293b">0</text>
    '''

    x_start, y_start = ox + 40, oy - 45
    x_end, y_end = ox + 240, oy - 90
    x_peak, y_peak = ox + 180, oy - 125

    curve_d = f"M {x_start} {y_start} Q {ox + 120} {oy - 125}, {x_peak} {y_peak} T {x_end} {y_end}"
    curve = f'<path d="{curve_d}" fill="none" stroke="#0284c7" stroke-width="2.2" />'
    curve_label = f'<text x="{ox + 105}" y="{oy - 75}" {FONT} font-size="15" font-style="italic" fill="#0f172a">y = f(x)</text>'

    curve_dots = f'''
    <circle cx="{x_start}" cy="{y_start}" r="3.5" fill="#0284c7" />
    <circle cx="{x_end}" cy="{y_end}" r="3.5" fill="#0284c7" />
    '''

    dashed_domain = f'''
    <line x1="{x_start}" y1="{y_start}" x2="{x_start}" y2="{oy}" stroke="#1e293b" stroke-width="1.2" stroke-dasharray="4 3" />
    <line x1="{x_end}" y1="{y_end}" x2="{x_end}" y2="{oy}" stroke="#1e293b" stroke-width="1.2" stroke-dasharray="4 3" />
    '''

    domain_bar = f'''
    <line x1="{x_start}" y1="{oy}" x2="{x_end}" y2="{oy}" stroke="#d92672" stroke-width="3" />
    <circle cx="{x_start}" cy="{oy}" r="3.5" fill="#d92672" />
    <circle cx="{x_end}" cy="{oy}" r="3.5" fill="#d92672" />
    '''

    mid_x = (x_start + x_end) / 2
    domain_brace = f'''
    <path d="M {x_start} {oy + 6} Q {x_start + 10} {oy + 14}, {mid_x - 10} {oy + 14} Q {mid_x} {oy + 18}, {mid_x} {oy + 22} Q {mid_x} {oy + 18}, {mid_x + 10} {oy + 14} Q {x_end - 10} {oy + 14}, {x_end} {oy + 6}" fill="none" stroke="#334155" stroke-width="1" />
    <text x="{mid_x}" y="{oy + 38}" {FONT} font-size="14" fill="#0f172a" text-anchor="middle">domain</text>
    '''

    dashed_range = f'''
    <line x1="{x_start}" y1="{y_start}" x2="{ox}" y2="{y_start}" stroke="#1e293b" stroke-width="1.2" stroke-dasharray="4 3" />
    <line x1="{x_peak}" y1="{y_peak}" x2="{ox}" y2="{y_peak}" stroke="#1e293b" stroke-width="1.2" stroke-dasharray="4 3" />
    '''

    range_bar = f'''
    <line x1="{ox}" y1="{y_peak}" x2="{ox}" y2="{y_start}" stroke="#16a34a" stroke-width="3" />
    <circle cx="{ox}" cy="{y_peak}" r="3.5" fill="#16a34a" />
    <circle cx="{ox}" cy="{y_start}" r="3.5" fill="#16a34a" />
    '''

    mid_y = (y_peak + y_start) / 2
    range_brace = f'''
    <path d="M {ox - 6} {y_peak} Q {ox - 14} {y_peak + 10}, {ox - 14} {mid_y - 10} Q {ox - 18} {mid_y}, {ox - 22} {mid_y} Q {ox - 18} {mid_y}, {ox - 14} {mid_y + 10} Q {ox - 14} {y_start - 10}, {ox - 6} {y_start}" fill="none" stroke="#334155" stroke-width="1" />
    <text x="{ox - 28}" y="{mid_y + 4}" {FONT} font-size="14" fill="#0f172a" text-anchor="end">range</text>
    '''

    caption = f'<text x="40" y="240" {FONT} font-size="13" font-weight="bold" fill="#0f172a" letter-spacing="0.5">FIGURE 5</text>'
    content = axes + dashed_domain + domain_bar + domain_brace + dashed_range + range_bar + range_brace + curve + curve_dots + curve_label + caption
    return svg_wrapper(w, h, content)

# 3. Figure 1: Section 1.3 Translations
def make_fig_sec1_3_fig1():
    w, h = 540, 310
    ox, oy = 110, 205
    
    axes = f'''
    <line x1="{ox - 80}" y1="{oy}" x2="{ox + 380}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 70}" x2="{ox}" y2="{oy - 170}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 385}" y="{oy + 14}" {FONT} font-size="13" font-style="italic" fill="#1e293b">x</text>
    <text x="{ox - 12}" y="{oy - 165}" {FONT} font-size="13" font-style="italic" fill="#1e293b">y</text>
    <text x="{ox - 12}" y="{oy + 16}" {FONT} font-size="12" fill="#1e293b">0</text>
    '''

    c_px = 55
    def curve_path(bx, by):
        return f"M {bx} {by + 20} C {bx + 16} {by - 25}, {bx + 32} {by - 25}, {bx + 48} {by} C {bx + 62} {by + 22}, {bx + 75} {by + 10}, {bx + 85} {by + 16}"

    bx, by = ox + 75, oy - 45
    path_base = curve_path(bx, by)
    path_up = curve_path(bx, by - c_px)
    path_down = curve_path(bx, by + c_px)
    path_right = curve_path(bx + c_px, by)
    path_left = curve_path(bx - c_px, by)

    dashed = f'''
    <line x1="{bx}" y1="{by - c_px}" x2="{bx}" y2="{by + c_px + 20}" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4 3" />
    <line x1="{bx - c_px}" y1="{by + 20}" x2="{bx + c_px + 85}" y2="{by + 20}" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4 3" />
    <text x="{bx - 12}" y="{by - c_px/2 + 2}" {FONT} font-size="12" font-style="italic" fill="#475569">c</text>
    <text x="{bx + 26}" y="{by + 33}" {FONT} font-size="12" font-style="italic" fill="#475569">c</text>
    <text x="{bx - 32}" y="{by + 33}" {FONT} font-size="12" font-style="italic" fill="#475569">c</text>
    '''

    curves = f'''
    <path d="{path_base}" fill="none" stroke="#1e293b" stroke-width="2" />
    <text x="{bx + 90}" y="{by + 16}" {FONT} font-size="12" font-style="italic" fill="#1e293b">y = f(x)</text>

    <path d="{path_up}" fill="none" stroke="#d92672" stroke-width="2" />
    <text x="{bx + 90}" y="{by - c_px + 10}" {FONT} font-size="12" font-style="italic" fill="#d92672">y = f(x) + c</text>

    <path d="{path_down}" fill="none" stroke="#16a34a" stroke-width="2" />
    <text x="{bx + 90}" y="{by + c_px + 22}" {FONT} font-size="12" font-style="italic" fill="#16a34a">y = f(x) - c</text>

    <path d="{path_right}" fill="none" stroke="#0284c7" stroke-width="2" />
    <text x="{bx + c_px + 90}" y="{by + 16}" {FONT} font-size="12" font-style="italic" fill="#0284c7">y = f(x - c)</text>

    <path d="{path_left}" fill="none" stroke="#ea580c" stroke-width="2" />
    <text x="{bx - c_px - 5}" y="{by - 10}" {FONT} font-size="12" font-style="italic" fill="#ea580c">y = f(x + c)</text>
    '''

    caption = f'''
    <text x="30" y="290" {FONT} font-size="12" font-weight="bold" fill="#0f172a" letter-spacing="0.5">FIGURE 1</text>
    <text x="30" y="304" {FONT} font-size="12" fill="#475569">Translating the graph of f</text>
    '''

    content = axes + dashed + curves + caption
    return svg_wrapper(w, h, content)

# 4. Figure 2: Section 1.3 Stretching and Reflecting
def make_fig_sec1_3_fig2():
    w, h = 540, 310
    ox, oy = 210, 205

    axes = f'''
    <line x1="{ox - 170}" y1="{oy}" x2="{ox + 270}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 80}" x2="{ox}" y2="{oy - 180}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 275}" y="{oy + 14}" {FONT} font-size="13" font-style="italic" fill="#1e293b">x</text>
    <text x="{ox - 12}" y="{oy - 175}" {FONT} font-size="13" font-style="italic" fill="#1e293b">y</text>
    <text x="{ox - 12}" y="{oy + 16}" {FONT} font-size="12" fill="#1e293b">0</text>
    '''

    bx, by = ox + 25, oy - 25
    path_base = f"M {bx} {by} C {bx + 18} {by - 40}, {bx + 40} {by - 40}, {bx + 55} {by - 15} C {bx + 70} {by + 5}, {bx + 85} {by - 5}, {bx + 95} {by - 2}"
    path_stretch = f"M {bx} {by - 45} C {bx + 20} {by - 125}, {bx + 40} {by - 125}, {bx + 55} {by - 75} C {bx + 70} {by - 35}, {bx + 85} {by - 55}, {bx + 95} {by - 50}"
    path_compress = f"M {bx} {by + 10} C {bx + 18} {by - 12}, {bx + 40} {by - 12}, {bx + 55} {by} C {bx + 70} {by + 8}, {bx + 85} {by + 5}, {bx + 95} {by + 6}"
    path_ref_x = f"M {bx} {oy + 25} C {bx + 18} {oy + 65}, {bx + 40} {oy + 65}, {bx + 55} {oy + 40} C {bx + 70} {oy + 20}, {bx + 85} {oy + 30}, {bx + 95} {oy + 27}"
    path_ref_y = f"M {ox - 25} {by} C {ox - 43} {by - 40}, {ox - 65} {by - 40}, {ox - 80} {by - 15} C {ox - 95} {by + 5}, {ox - 110} {by - 5}, {ox - 120} {by - 2}"

    curves = f'''
    <path d="{path_base}" fill="none" stroke="#1e293b" stroke-width="2" />
    <text x="{bx + 102}" y="{by - 10}" {FONT} font-size="12" font-style="italic" fill="#1e293b">y = f(x)</text>

    <path d="{path_stretch}" fill="none" stroke="#d92672" stroke-width="2" />
    <text x="{bx + 90}" y="{by - 100}" {FONT} font-size="12" font-style="italic" fill="#d92672">y = cf(x) (c &gt; 1)</text>

    <path d="{path_compress}" fill="none" stroke="#16a34a" stroke-width="2" />
    <text x="{bx + 102}" y="{by + 14}" {FONT} font-size="12" font-style="italic" fill="#16a34a">y = &#189; f(x)</text>

    <path d="{path_ref_x}" fill="none" stroke="#ea580c" stroke-width="2" />
    <text x="{bx + 102}" y="{oy + 55}" {FONT} font-size="12" font-style="italic" fill="#ea580c">y = -f(x)</text>

    <path d="{path_ref_y}" fill="none" stroke="#0284c7" stroke-width="2" />
    <text x="{ox - 125}" y="{by - 28}" {FONT} font-size="12" font-style="italic" fill="#0284c7">y = f(-x)</text>
    '''

    caption = f'''
    <text x="30" y="290" {FONT} font-size="12" font-weight="bold" fill="#0f172a" letter-spacing="0.5">FIGURE 2</text>
    <text x="30" y="304" {FONT} font-size="12" fill="#475569">Stretching and reflecting the graph of f</text>
    '''

    content = axes + curves + caption
    return svg_wrapper(w, h, content)

# 5. Example 1: Section 1.3 Transformations of sqrt(x)
def make_fig_sec1_3_example1():
    w, h = 660, 190
    panels = []
    labels = ["(a) y = √x", "(b) y = √x - 2", "(c) y = √(x - 2)", "(d) y = -√x", "(e) y = 2√x", "(f) y = √(-x)"]
    
    for i, lbl in enumerate(labels):
        ox = 30 + i * 105
        oy = 115
        panel_axes = f'''
        <line x1="{ox - 15}" y1="{oy}" x2="{ox + 75}" y2="{oy}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
        <line x1="{ox}" y1="{oy + 40}" x2="{ox}" y2="{oy - 65}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
        <text x="{ox + 70}" y="{oy + 14}" {FONT} font-size="11" font-style="italic" fill="#1e293b">x</text>
        <text x="{ox - 10}" y="{oy - 60}" {FONT} font-size="11" font-style="italic" fill="#1e293b">y</text>
        <text x="{ox - 8}" y="{oy + 12}" {FONT} font-size="10" fill="#1e293b">0</text>
        '''
        
        if i == 0:
            pts = " ".join([f"{ox + t} {oy - math.sqrt(t/55.0)*50}" for t in range(0, 60, 2)])
            col = "#0284c7"
            ticks = f'<line x1="{ox + 20}" y1="{oy - 2}" x2="{ox + 20}" y2="{oy + 2}" stroke="#1e293b" />' \
                    f'<text x="{ox + 18}" y="{oy + 12}" {FONT} font-size="9">1</text>' \
                    f'<line x1="{ox - 2}" y1="{oy - 20}" x2="{ox + 2}" y2="{oy - 20}" stroke="#1e293b" />' \
                    f'<text x="{ox - 9}" y="{oy - 18}" {FONT} font-size="9">1</text>'
        elif i == 1:
            pts = " ".join([f"{ox + t} {oy + 25 - math.sqrt(t/55.0)*45}" for t in range(0, 65, 2)])
            col = "#d92672"
            ticks = f'<text x="{ox - 14}" y="{oy + 28}" {FONT} font-size="9">-2</text>'
        elif i == 2:
            pts = " ".join([f"{ox + 22 + t} {oy - math.sqrt(t/45.0)*35}" for t in range(0, 45, 2)])
            col = "#d92672"
            ticks = f'<text x="{ox + 20}" y="{oy + 12}" {FONT} font-size="9">2</text>'
        elif i == 3:
            pts = " ".join([f"{ox + t} {oy + math.sqrt(t/55.0)*40}" for t in range(0, 55, 2)])
            col = "#d92672"
            ticks = ""
        elif i == 4:
            pts = " ".join([f"{ox + t} {oy - math.sqrt(t/55.0)*65}" for t in range(0, 50, 2)])
            col = "#d92672"
            ticks = ""
        elif i == 5:
            pts = " ".join([f"{ox - t} {oy - math.sqrt(t/55.0)*40}" for t in range(0, 55, 2)])
            col = "#d92672"
            ticks = ""

        c_elem = f'<path d="M {pts}" fill="none" stroke="{col}" stroke-width="1.8" />'
        lbl_elem = f'<text x="{ox + 30}" y="172" {FONT} font-size="11" fill="#0f172a" text-anchor="middle">{lbl}</text>'
        panels.append(panel_axes + ticks + c_elem + lbl_elem)

    content = "".join(panels)
    return svg_wrapper(w, h, content)

# 6. Exercises 6-7: Transformations from y = sqrt(3x - x^2)
def make_fig_sec1_3_exercises6_7():
    w, h = 660, 230
    ox1, oy1 = 60, 160
    ox2, oy2 = 280, 160
    ox3, oy3 = 540, 115

    base = f'''
    <line x1="{ox1 - 30}" y1="{oy1}" x2="{ox1 + 130}" y2="{oy1}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <line x1="{ox1}" y1="{oy1 + 30}" x2="{ox1}" y2="{oy1 - 100}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <text x="{ox1 + 132}" y="{oy1 + 12}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox1 - 10}" y="{oy1 - 95}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox1 - 10}" y="{oy1 + 14}" {FONT} font-size="11">0</text>
    <text x="{ox1 + 80}" y="{oy1 + 14}" {FONT} font-size="11">3</text>
    <text x="{ox1 - 22}" y="{oy1 - 42}" {FONT} font-size="11">1.5</text>
    <line x1="{ox1 - 3}" y1="{oy1 - 44}" x2="{ox1 + 3}" y2="{oy1 - 44}" stroke="#1e293b" />
    <path d="M {ox1} {oy1} A 40 40 0 0 1 {ox1 + 80} {oy1}" fill="none" stroke="#0284c7" stroke-width="2" />
    <text x="{ox1 + 60}" y="{oy1 - 55}" {FONT} font-size="12" font-style="italic">y = &#8730;(3x - x&#178;)</text>
    '''

    ex6 = f'''
    <text x="{ox2 - 35}" y="{oy2 - 75}" {FONT} font-size="13" font-weight="bold">6.</text>
    <line x1="{ox2 - 30}" y1="{oy2}" x2="{ox2 + 155}" y2="{oy2}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <line x1="{ox2}" y1="{oy2 + 30}" x2="{ox2}" y2="{oy2 - 110}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <text x="{ox2 + 158}" y="{oy2 + 12}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox2 - 10}" y="{oy2 - 105}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox2 - 10}" y="{oy2 + 14}" {FONT} font-size="11">0</text>
    <text x="{ox2 + 40}" y="{oy2 + 14}" {FONT} font-size="11">2</text>
    <text x="{ox2 + 115}" y="{oy2 + 14}" {FONT} font-size="11">5</text>
    <text x="{ox2 - 14}" y="{oy2 - 75}" {FONT} font-size="11">3</text>
    <line x1="{ox2 - 3}" y1="{oy2 - 78}" x2="{ox2 + 3}" y2="{oy2 - 78}" stroke="#1e293b" />
    <path d="M {ox2 + 40} {oy2} A 37.5 78 0 0 1 {ox2 + 115} {oy2}" fill="none" stroke="#d92672" stroke-width="2" />
    '''

    ex7 = f'''
    <text x="{ox3 - 135}" y="{oy3 - 35}" {FONT} font-size="13" font-weight="bold" fill="#d92672">7.</text>
    <line x1="{ox3 - 130}" y1="{oy3}" x2="{ox3 + 45}" y2="{oy3}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <line x1="{ox3}" y1="{oy3 + 95}" x2="{ox3}" y2="{oy3 - 40}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <text x="{ox3 + 48}" y="{oy3 + 12}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox3 - 10}" y="{oy3 - 35}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox3 - 10}" y="{oy3 + 14}" {FONT} font-size="11">0</text>
    <text x="{ox3 - 95}" y="{oy3 - 8}" {FONT} font-size="11">-4</text>
    <line x1="{ox3 - 90}" y1="{oy3 - 3}" x2="{ox3 - 90}" y2="{oy3 + 3}" stroke="#1e293b" />
    <text x="{ox3 - 28}" y="{oy3 - 8}" {FONT} font-size="11">-1</text>
    <line x1="{ox3 - 22}" y1="{oy3 - 3}" x2="{ox3 - 22}" y2="{oy3 + 3}" stroke="#1e293b" />
    <text x="{ox3 + 6}" y="{oy3 + 28}" {FONT} font-size="11">-1</text>
    <text x="{ox3 + 6}" y="{oy3 + 68}" {FONT} font-size="11">-2.5</text>
    <line x1="{ox3 - 3}" y1="{oy3 + 66}" x2="{ox3 + 3}" y2="{oy3 + 66}" stroke="#1e293b" />
    <path d="M {ox3 - 90} {oy3 + 26} A 34 42 0 0 0 {ox3 - 22} {oy3 + 26}" fill="none" stroke="#d92672" stroke-width="2" />
    '''

    content = base + ex6 + ex7
    return svg_wrapper(w, h, content)

# 7. Figure 2: Section 2.2 Limit Cases (a), (b), (c)
def make_fig_sec2_2_fig2():
    w, h = 640, 220
    panels = []
    labels = ["(a)", "(b)", "(c)"]
    for i, lbl in enumerate(labels):
        ox = 45 + i * 200
        oy = 155
        axes = f'''
        <line x1="{ox - 25}" y1="{oy}" x2="{ox + 160}" y2="{oy}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
        <line x1="{ox}" y1="{oy + 25}" x2="{ox}" y2="{oy - 120}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
        <text x="{ox + 162}" y="{oy + 12}" {FONT} font-size="11" font-style="italic">x</text>
        <text x="{ox - 10}" y="{oy - 115}" {FONT} font-size="11" font-style="italic">y</text>
        <text x="{ox - 10}" y="{oy + 14}" {FONT} font-size="11">0</text>
        '''

        ax, ay = ox + 85, oy - 65
        curve_d = f"M {ox - 15} {oy - 30} Q {ox + 30} {oy + 5}, {ax} {ay} T {ox + 150} {oy - 60}"
        curve = f'<path d="{curve_d}" fill="none" stroke="#0284c7" stroke-width="2" />'

        guidelines = f'''
        <line x1="{ax}" y1="{ay}" x2="{ax}" y2="{oy}" stroke="#1e293b" stroke-width="1.2" stroke-dasharray="4 3" />
        <line x1="{ax}" y1="{ay}" x2="{ox}" y2="{ay}" stroke="#1e293b" stroke-width="1.2" stroke-dasharray="4 3" />
        <text x="{ax - 3}" y="{oy + 15}" {FONT} font-size="12" font-style="italic">a</text>
        <text x="{ox - 12}" y="{ay + 4}" {FONT} font-size="12" font-style="italic">L</text>
        '''

        if i == 0:
            pts = f'<circle cx="{ax}" cy="{ay}" r="3" fill="#0284c7" />'
        elif i == 1:
            pts = f'<circle cx="{ax}" cy="{ay}" r="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.6" />' \
                  f'<circle cx="{ax}" cy="{ay + 32}" r="3" fill="#0284c7" />'
        elif i == 2:
            pts = f'<circle cx="{ax}" cy="{ay}" r="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.6" />'

        lbl_elem = f'<text x="{ox + 75}" y="{oy + 34}" {FONT} font-size="12" fill="#0f172a" text-anchor="middle">{lbl}</text>'
        panels.append(axes + guidelines + curve + pts + lbl_elem)

    caption = f'<text x="40" y="210" {FONT} font-size="12" font-weight="bold" fill="#0f172a">FIGURE 2  <tspan font-style="italic" font-weight="normal">lim<tspan baseline-shift="sub" font-size="9">x&#8594;a</tspan> f(x) = L in all three cases</tspan></text>'
    content = "".join(panels) + caption
    return svg_wrapper(w, h, content)

# 8. Figures 3 & 4: Section 2.2 Numerical limit Example 1
def make_fig_sec2_2_figures3_4():
    w, h = 540, 250
    ox1, oy1 = 70, 195
    ox2, oy2 = 330, 195

    def make_limit_panel(ox, oy, has_dot=False, fig_name="FIGURE 3"):
        axes = f'''
        <line x1="{ox - 25}" y1="{oy}" x2="{ox + 180}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
        <line x1="{ox}" y1="{oy + 25}" x2="{ox}" y2="{oy - 170}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
        <text x="{ox + 185}" y="{oy + 12}" {FONT} font-size="11" font-style="italic">x</text>
        <text x="{ox - 10}" y="{oy - 165}" {FONT} font-size="11" font-style="italic">y</text>
        <text x="{ox - 10}" y="{oy + 14}" {FONT} font-size="11">0</text>
        '''
        hx, hy = ox + 65, oy - 65
        curve_d = f"M {ox + 10} {oy - 145} Q {ox + 35} {oy - 85}, {hx} {hy} T {ox + 160} {oy - 40}"
        curve = f'<path d="{curve_d}" fill="none" stroke="#0284c7" stroke-width="2" />'

        guidelines = f'''
        <line x1="{hx}" y1="{hy}" x2="{hx}" y2="{oy}" stroke="#1e293b" stroke-width="1.1" stroke-dasharray="4 3" />
        <line x1="{hx}" y1="{hy}" x2="{ox}" y2="{hy}" stroke="#1e293b" stroke-width="1.1" stroke-dasharray="4 3" />
        <text x="{hx - 3}" y="{oy + 15}" {FONT} font-size="11">1</text>
        <text x="{ox - 24}" y="{hy + 4}" {FONT} font-size="11">0.5</text>
        <circle cx="{hx}" cy="{hy}" r="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.6" />
        '''

        approaches = f'''
        <path d="M {hx - 22} {oy + 8} L {hx - 8} {oy + 8}" stroke="#d92672" stroke-width="1.5" marker-end="url(#arrow-pink)" />
        <path d="M {hx + 22} {oy + 8} L {hx + 8} {oy + 8}" stroke="#d92672" stroke-width="1.5" marker-end="url(#arrow-pink)" />
        '''

        if has_dot:
            label_fn = f'<text x="{ox + 50}" y="{oy - 110}" {FONT} font-size="12" font-style="italic">y = g(x)</text>'
            dot = f'<circle cx="{hx}" cy="{oy - 130}" r="3" fill="#0284c7" />' \
                  f'<text x="{ox - 14}" y="{oy - 126}" {FONT} font-size="11">2</text>'
        else:
            label_fn = f'<text x="{ox + 45}" y="{oy - 110}" {FONT} font-size="12" font-style="italic">y = (x - 1)/(x&#178; - 1)</text>'
            dot = ''

        caption = f'<text x="{ox + 40}" y="{oy + 44}" {FONT} font-size="12" font-weight="bold">{fig_name}</text>'
        return axes + guidelines + approaches + curve + dot + label_fn + caption

    p1 = make_limit_panel(ox1, oy1, has_dot=False, fig_name="FIGURE 3")
    p2 = make_limit_panel(ox2, oy2, has_dot=True, fig_name="FIGURE 4")
    return svg_wrapper(w, h, p1 + p2)

# 9. Figures 6 & 7: Section 2.2 sin(x)/x and sin(pi/x)
def make_fig_sec2_2_figures6_7():
    w, h = 640, 260
    ox1, oy1 = 140, 165
    ox2, oy2 = 450, 165

    f6_axes = f'''
    <line x1="{ox1 - 110}" y1="{oy1}" x2="{ox1 + 120}" y2="{oy1}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <line x1="{ox1}" y1="{oy1 + 25}" x2="{ox1}" y2="{oy1 - 120}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <text x="{ox1 + 124}" y="{oy1 + 12}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox1 - 10}" y="{oy1 - 115}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox1 - 10}" y="{oy1 + 14}" {FONT} font-size="11">0</text>
    <text x="{ox1 + 75}" y="{oy1 + 14}" {FONT} font-size="11">1</text>
    <line x1="{ox1 + 78}" y1="{oy1 - 3}" x2="{ox1 + 78}" y2="{oy1 + 3}" stroke="#1e293b" />
    <text x="{ox1 - 85}" y="{oy1 + 14}" {FONT} font-size="11">-1</text>
    <line x1="{ox1 - 78}" y1="{oy1 - 3}" x2="{ox1 - 78}" y2="{oy1 + 3}" stroke="#1e293b" />
    <text x="{ox1 - 12}" y="{oy1 - 65}" {FONT} font-size="11">1</text>
    <line x1="{ox1 - 3}" y1="{oy1 - 68}" x2="{ox1 + 3}" y2="{oy1 - 68}" stroke="#1e293b" />
    <path d="M {ox1 - 95} {oy1 - 25} Q {ox1} {oy1 - 80}, {ox1 + 95} {oy1 - 25}" fill="none" stroke="#0284c7" stroke-width="2" />
    <text x="{ox1 + 35}" y="{oy1 - 75}" {FONT} font-size="12" font-style="italic">y = (sin x)/x</text>
    <text x="{ox1 - 30}" y="240" {FONT} font-size="12" font-weight="bold">FIGURE 6</text>
    '''

    f7_axes = f'''
    <line x1="{ox2 - 160}" y1="{oy2}" x2="{ox2 + 160}" y2="{oy2}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <line x1="{ox2}" y1="{oy2 + 55}" x2="{ox2}" y2="{oy2 - 120}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <text x="{ox2 + 164}" y="{oy2 + 12}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox2 - 10}" y="{oy2 - 115}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox2 - 12}" y="{oy2 - 58}" {FONT} font-size="11">1</text>
    <line x1="{ox2 - 3}" y1="{oy2 - 60}" x2="{ox2 + 3}" y2="{oy2 - 60}" stroke="#1e293b" />
    <text x="{ox2 - 16}" y="{oy2 + 38}" {FONT} font-size="11">-1</text>
    <line x1="{ox2 - 3}" y1="{oy2 + 36}" x2="{ox2 + 3}" y2="{oy2 + 36}" stroke="#1e293b" />
    <text x="{ox2 + 65}" y="{oy2 + 14}" {FONT} font-size="11">1</text>
    <line x1="{ox2 + 68}" y1="{oy2 - 3}" x2="{ox2 + 68}" y2="{oy2 + 3}" stroke="#1e293b" />
    <text x="{ox2 - 78}" y="{oy2 + 14}" {FONT} font-size="11">-1</text>
    <line x1="{ox2 - 68}" y1="{oy2 - 3}" x2="{ox2 - 68}" y2="{oy2 + 3}" stroke="#1e293b" />
    '''

    pts = []
    for px in range(-150, -4):
        x_val = px / 68.0
        y_val = math.sin(math.pi / x_val)
        py = oy2 - y_val * 46
        pts.append(f"{ox2 + px:.1f} {py:.1f}")
    path_left = "M " + " L ".join(pts)

    pts_r = []
    for px in range(4, 151):
        x_val = px / 68.0
        y_val = math.sin(math.pi / x_val)
        py = oy2 - y_val * 46
        pts_r.append(f"{ox2 + px:.1f} {py:.1f}")
    path_right = "M " + " L ".join(pts_r)

    f7_curves = f'''
    <path d="{path_left}" fill="none" stroke="#0284c7" stroke-width="1.3" />
    <path d="{path_right}" fill="none" stroke="#0284c7" stroke-width="1.3" />
    <text x="{ox2 + 80}" y="{oy2 - 70}" {FONT} font-size="12" font-style="italic">y = sin(&#960;/x)</text>
    <text x="{ox2 - 30}" y="240" {FONT} font-size="12" font-weight="bold">FIGURE 7</text>
    '''

    content = f6_axes + f7_axes + f7_curves
    return svg_wrapper(w, h, content)

# 10. Figure 10: Section 2.2 Example 7 Piecewise limit graph
def make_fig_sec2_2_fig10():
    w, h = 460, 240
    ox, oy = 80, 175
    u = 30

    axes = f'''
    <line x1="{ox - 40}" y1="{oy}" x2="{ox + 310}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 30}" x2="{ox}" y2="{oy - 150}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <text x="{ox + 315}" y="{oy + 12}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox - 10}" y="{oy - 145}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox - 10}" y="{oy + 14}" {FONT} font-size="11">0</text>
    '''

    ticks_x = []
    for x in range(1, 7):
        px = ox + x * u
        ticks_x.append(f'<line x1="{px}" y1="{oy - 3}" x2="{px}" y2="{oy + 3}" stroke="#1e293b" />'
                       f'<text x="{px - 3}" y="{oy + 15}" {FONT} font-size="11">{x}</text>')
    ticks_y = []
    for y in range(1, 5):
        py = oy - y * u
        ticks_y.append(f'<line x1="{ox - 3}" y1="{py}" x2="{ox + 3}" y2="{py}" stroke="#1e293b" />'
                       f'<text x="{ox - 14}" y="{py + 4}" {FONT} font-size="11">{y}</text>')

    p1_d = f"M {ox - 30} {oy - 10} Q {ox + 10} {oy - 75}, {ox + 2*u} {oy - 3*u}"
    piece1 = f'<path d="{p1_d}" fill="none" stroke="#0284c7" stroke-width="2" />' \
             f'<circle cx="{ox + 2*u}" cy="{oy - 3*u}" r="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.6" />'

    p2_d = f"M {ox + 2*u} {oy - 1*u} Q {ox + 3.5*u} {oy - 1.8*u}, {ox + 5*u} {oy - 2*u} T {ox + 6.5*u} {oy - 1.7*u}"
    piece2 = f'<path d="{p2_d}" fill="none" stroke="#0284c7" stroke-width="2" />' \
             f'<circle cx="{ox + 2*u}" cy="{oy - 1*u}" r="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.6" />'

    pt_isolated = f'<circle cx="{ox + 5*u}" cy="{oy - 1.2*u}" r="3.2" fill="#0284c7" />'
    lbl_fn = f'<text x="{ox + 120}" y="{oy - 105}" {FONT} font-size="12" font-style="italic">y = g(x)</text>'
    caption = f'<text x="25" y="225" {FONT} font-size="12" font-weight="bold">FIGURE 10</text>'

    content = axes + "".join(ticks_x) + "".join(ticks_y) + piece1 + piece2 + pt_isolated + lbl_fn + caption
    return svg_wrapper(w, h, content)

# 11. Figure 1: Section 2.3 Limit Laws from Graphs
def make_fig_sec2_3_fig1():
    w, h = 440, 250
    ox, oy = 150, 135
    u = 24

    grid = []
    for x in range(-3, 5):
        px = ox + x * u
        grid.append(f'<line x1="{px}" y1="{oy - 3*u}" x2="{px}" y2="{oy + 3*u}" stroke="#cbd5e1" stroke-width="0.9" />')
    for y in range(-3, 4):
        py = oy - y * u
        grid.append(f'<line x1="{ox - 3*u}" y1="{py}" x2="{ox + 4*u}" y2="{py}" stroke="#cbd5e1" stroke-width="0.9" />')

    axes = f'''
    <line x1="{ox - 3*u}" y1="{oy}" x2="{ox + 4.4*u}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 3*u}" x2="{ox}" y2="{oy - 3.4*u}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <text x="{ox + 4.4*u}" y="{oy + 14}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox - 10}" y="{oy - 3.4*u}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox - 10}" y="{oy + 14}" {FONT} font-size="10">0</text>
    <text x="{ox + u - 3}" y="{oy + 14}" {FONT} font-size="10">1</text>
    <text x="{ox - 10}" y="{oy - u + 4}" {FONT} font-size="10">1</text>
    '''

    curve_f = f'''
    <path d="M {ox - 3*u} {oy} Q {ox - 2.5*u} {oy - 0.8*u}, {ox - 2*u} {oy - 1*u}" fill="none" stroke="#d92672" stroke-width="2" />
    <circle cx="{ox - 2*u}" cy="{oy - 1*u}" r="3.5" fill="#ffffff" stroke="#d92672" stroke-width="1.6" />
    <circle cx="{ox - 2*u}" cy="{oy - 2*u}" r="3" fill="#d92672" />
    <path d="M {ox - 2*u} {oy - 1*u} C {ox - 1.5*u} {oy - 0.4*u}, {ox - 0.2*u} {oy - 2*u}, {ox + 1*u} {oy - 2*u} C {ox + 1.6*u} {oy - 2*u}, {ox + 2.2*u} {oy}, {ox + 2.5*u} {oy + 0.6*u}" fill="none" stroke="#d92672" stroke-width="2" />
    <text x="{ox + 1.2*u}" y="{oy - 2.3*u}" {FONT} font-size="12" font-style="italic" fill="#d92672">f</text>
    '''

    curve_g = f'''
    <line x1="{ox - 3.2*u}" y1="{oy + 0.6*u}" x2="{ox + 1*u}" y2="{oy + 1.8*u}" stroke="#0284c7" stroke-width="2" />
    <circle cx="{ox + 1*u}" cy="{oy + 1.8*u}" r="3" fill="#0284c7" />
    <circle cx="{ox + 1*u}" cy="{oy + 1.2*u}" r="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.6" />
    <line x1="{ox + 1*u}" y1="{oy + 1.2*u}" x2="{ox + 3*u}" y2="{oy - 1.5*u}" stroke="#0284c7" stroke-width="2" />
    <text x="{ox - 2.2*u}" y="{oy + 1.4*u}" {FONT} font-size="12" font-style="italic" fill="#0284c7">g</text>
    '''

    caption = f'<text x="25" y="235" {FONT} font-size="12" font-weight="bold">FIGURE 1</text>'

    content = "".join(grid) + axes + curve_f + curve_g + caption
    return svg_wrapper(w, h, content)

figures = {
    "sec1_1_figure6_graph_of_function.svg": make_fig_sec1_1_fig6(),
    "sec1_1_figure5_domain_range.svg": make_fig_sec1_1_fig5(),
    "sec1_3_figure1_translations.svg": make_fig_sec1_3_fig1(),
    "sec1_3_figure2_stretching_reflecting.svg": make_fig_sec1_3_fig2(),
    "sec1_3_example1_transformations_sqrt.svg": make_fig_sec1_3_example1(),
    "sec1_3_exercises6_7_transformations.svg": make_fig_sec1_3_exercises6_7(),
    "sec2_2_figure2_limit_cases.svg": make_fig_sec2_2_fig2(),
    "sec2_2_figures3_4_limit_example1.svg": make_fig_sec2_2_figures3_4(),
    "sec2_2_figures6_7_trig_limits.svg": make_fig_sec2_2_figures6_7(),
    "sec2_2_figure10_piecewise_limit.svg": make_fig_sec2_2_fig10(),
    "sec2_3_figure1_limit_laws_graphs.svg": make_fig_sec2_3_fig1(),
}

for name, svg in figures.items():
    filepath = os.path.join(OUTPUT_DIR, name)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Updated {filepath}")
