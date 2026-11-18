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

# 1. Figure 1: Continuity at a Number a
def make_fig_sec2_5_fig1():
    w, h = 380, 260
    ox, oy = 75, 195
    u = 42

    # Coordinates for a and f(a)
    ax_val = 3.0
    fa_val = 2.7
    px = ox + ax_val * u
    py = oy - fa_val * u

    axes = f'''
    <!-- Coordinate axes -->
    <line x1="{ox - 30}" y1="{oy}" x2="{ox + 260}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 30}" x2="{ox}" y2="{oy - 175}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 265}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 14}" y="{oy - 170}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>
    '''

    # Curve y = f(x)
    # Starts around ox - 20, rises, local crest, local dip, passes through px, py, bends up-right
    # Let's use smooth cubic Bézier path
    curve = f'''
    <!-- Function curve y = f(x) -->
    <path d="M {ox - 20} {oy - 0.5*u} C {ox + 0.8*u} {oy - 1.2*u}, {ox + 1.4*u} {oy - 0.4*u}, {ox + 2.2*u} {oy - 1.2*u} S {px - 0.2*u} {py + 0.3*u}, {px} {py} C {px + 0.4*u} {py - 0.6*u}, {px + 0.8*u} {py - 0.9*u}, {ox + 4.8*u} {py - 1.1*u}"
          fill="none" stroke="#0284c7" stroke-width="2.2" />
    <text x="{ox + 4.0*u}" y="{py - 1.3*u}" {FONT} font-size="13" font-style="italic" fill="#0f172a">y = f(x)</text>

    <!-- Dashed projection guidelines to a and f(a) -->
    <line x1="{px}" y1="{oy}" x2="{px}" y2="{py}" stroke="#0d9488" stroke-width="1.2" stroke-dasharray="4 3" />
    <line x1="{ox}" y1="{py}" x2="{px}" y2="{py}" stroke="#0d9488" stroke-width="1.2" stroke-dasharray="4 3" />

    <!-- Solid point (a, f(a)) -->
    <circle cx="{px}" cy="{py}" r="3.5" fill="#4338ca" />

    <!-- Axis labels a and f(a) -->
    <text x="{px - 4}" y="{oy + 16}" {FONT} font-size="12" font-style="italic" fill="#db2777">a</text>
    <text x="{ox - 24}" y="{py + 4}" {FONT} font-size="12" font-style="italic" fill="#db2777">f(a)</text>

    <!-- Pink approach arrows on x-axis -->
    <line x1="{px - 26}" y1="{oy + 8}" x2="{px - 8}" y2="{oy + 8}" stroke="#db2777" stroke-width="1.5" marker-end="url(#arrow-pink)" />
    <line x1="{px + 26}" y1="{oy + 8}" x2="{px + 8}" y2="{oy + 8}" stroke="#db2777" stroke-width="1.5" marker-end="url(#arrow-pink)" />
    <text x="{px - 58}" y="{oy + 38}" {FONT} font-size="11" fill="#1e293b">As <tspan font-style="italic">x</tspan> approaches <tspan font-style="italic">a</tspan>,</text>

    <!-- Pink approach arrows on y-axis -->
    <line x1="{ox + 8}" y1="{py - 22}" x2="{ox + 8}" y2="{py - 6}" stroke="#db2777" stroke-width="1.5" marker-end="url(#arrow-pink)" />
    <line x1="{ox + 8}" y1="{py + 22}" x2="{ox + 8}" y2="{py + 6}" stroke="#db2777" stroke-width="1.5" marker-end="url(#arrow-pink)" />
    <text x="{ox - 65}" y="{py - 18}" {FONT} font-size="10" fill="#1e293b"><tspan font-style="italic">f(x)</tspan> approaches</text>
    <text x="{ox - 52}" y="{py - 6}" {FONT} font-size="10" fill="#1e293b" font-style="italic">f(a).</text>
    '''

    caption = f'<text x="25" y="245" {FONT} font-size="12" font-weight="bold" fill="#1e293b">FIGURE 1</text>'
    return svg_wrapper(w, h, axes + curve + caption)


# 2. Figure 2: Example 1 Discontinuities
def make_fig_sec2_5_fig2():
    w, h = 480, 260
    ox, oy = 55, 175
    u = 58

    axes = f'''
    <!-- Coordinate axes -->
    <line x1="{ox - 25}" y1="{oy}" x2="{ox + 6.2*u}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 65}" x2="{ox}" y2="{oy - 150}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 6.3*u}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 14}" y="{oy - 145}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>
    '''

    ticks = ''
    for i in range(1, 6):
        tx = ox + i * u
        ticks += f'''
        <line x1="{tx}" y1="{oy - 3}" x2="{tx}" y2="{oy + 3}" stroke="#1e293b" />
        <text x="{tx - 4}" y="{oy + 16}" {FONT} font-size="11">{i}</text>
        '''

    # Curves and Discontinuities
    # Piece 1: x in [0, 3)
    # Starts at (0, 0.9*u) -> oy - 0.9*u
    # At x = 1 (ox + 1*u): hole at y = 0.5*u -> oy - 0.5*u
    # Crosses x axis around x = 2.15 -> ox + 2.15*u
    # Ends at x = 3 with hole at y = -0.9*u -> oy + 0.9*u
    p1_start = f"M {ox - 0.3*u} {oy - 0.7*u}"
    # Segment from start to hole at x=1
    seg1 = f'''
    <!-- Piece 1: left of x = 1 -->
    <path d="{p1_start} C {ox + 0.2*u} {oy - 0.9*u}, {ox + 0.6*u} {oy - 0.8*u}, {ox + 1.0*u} {oy - 0.45*u}"
          fill="none" stroke="#0284c7" stroke-width="2.2" />
    <!-- Removable hole at x = 1 -->
    <circle cx="{ox + 1.0*u}" cy="{oy - 0.45*u}" r="3.6" fill="#ffffff" stroke="#0284c7" stroke-width="1.8" />
    <!-- Piece 1: between x = 1 and x = 3 -->
    <path d="M {ox + 1.0*u + 3.6} {oy - 0.45*u + 2.0} C {ox + 1.5*u} {oy - 0.1*u}, {ox + 2.1*u} {oy + 0.4*u}, {ox + 3.0*u} {oy + 0.9*u}"
          fill="none" stroke="#0284c7" stroke-width="2.2" />
    <!-- Open circle at x = 3, y = -0.9u -->
    <circle cx="{ox + 3.0*u}" cy="{oy + 0.9*u}" r="3.6" fill="#ffffff" stroke="#0284c7" stroke-width="1.8" />
    '''

    # Piece 2: x in [3, 6]
    # Starts at x = 3 with SOLID dot at y = 0.8u -> oy - 0.8u
    # Curves down to min at x = 5 with HOLE at y = 0.35u -> oy - 0.35u
    # Curves up to x = 5.8
    # Isolated solid dot at x = 5, y = 1.6u -> oy - 1.6u
    seg2 = f'''
    <!-- Piece 2: starts at solid dot at x = 3 -->
    <path d="M {ox + 3.0*u} {oy - 0.8*u} C {ox + 3.5*u} {oy - 0.7*u}, {ox + 4.2*u} {oy - 0.35*u}, {ox + 5.0*u} {oy - 0.35*u}"
          fill="none" stroke="#0284c7" stroke-width="2.2" />
    <!-- Solid dot at x = 3 -->
    <circle cx="{ox + 3.0*u}" cy="{oy - 0.8*u}" r="3.5" fill="#0284c7" />

    <!-- Open circle at local min x = 5 -->
    <circle cx="{ox + 5.0*u}" cy="{oy - 0.35*u}" r="3.6" fill="#ffffff" stroke="#0284c7" stroke-width="1.8" />

    <!-- Curve right of x = 5 -->
    <path d="M {ox + 5.0*u + 3.6} {oy - 0.35*u - 1.5} C {ox + 5.4*u} {oy - 0.5*u}, {ox + 5.7*u} {oy - 0.9*u}, {ox + 5.9*u} {oy - 1.2*u}"
          fill="none" stroke="#0284c7" stroke-width="2.2" />

    <!-- Isolated solid point at x = 5 -->
    <circle cx="{ox + 5.0*u}" cy="{oy - 1.6*u}" r="3.5" fill="#0284c7" />
    '''

    caption = f'<text x="25" y="245" {FONT} font-size="12" font-weight="bold" fill="#1e293b">FIGURE 2</text>'
    return svg_wrapper(w, h, axes + ticks + seg1 + seg2 + caption)


# 3. Four types of discontinuities from Example 2
def make_fig_sec2_5_example2_panels():
    w, h = 640, 480
    
    # 4 panels: (a) top-left, (b) top-right, (c) bottom-left, (d) bottom-right
    # Panel (a): f(x) = (x^2 - x - 2)/(x - 2) = x + 1 (x != 2)
    ox1, oy1 = 120, 160
    u1 = 28
    panel_a = f'''
    <g>
      <!-- Subtitle -->
      <text x="30" y="28" {FONT} font-size="12" font-weight="bold" fill="#0f172a">(a) Removable Discontinuity: f(x) = (x² - x - 2) / (x - 2)</text>
      <!-- Axes -->
      <line x1="{ox1 - 90}" y1="{oy1}" x2="{ox1 + 150}" y2="{oy1}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
      <line x1="{ox1}" y1="{oy1 + 60}" x2="{ox1}" y2="{oy1 - 120}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
      <text x="{ox1 + 155}" y="{oy1 + 12}" {FONT} font-size="11" font-style="italic">x</text>
      <text x="{ox1 - 12}" y="{oy1 - 115}" {FONT} font-size="11" font-style="italic">y</text>
      <text x="{ox1 - 10}" y="{oy1 + 12}" {FONT} font-size="10">0</text>
      
      <!-- Ticks -->
      <line x1="{ox1 + 2*u1}" y1="{oy1 - 3}" x2="{ox1 + 2*u1}" y2="{oy1 + 3}" stroke="#1e293b" />
      <text x="{ox1 + 2*u1 - 3}" y="{oy1 + 14}" {FONT} font-size="10">2</text>
      <line x1="{ox1 - 3}" y1="{oy1 - 3*u1}" x2="{ox1 + 3}" y2="{oy1 - 3*u1}" stroke="#1e293b" />
      <text x="{ox1 - 12}" y="{oy1 - 3*u1 + 4}" {FONT} font-size="10">3</text>
      <line x1="{ox1 - 3}" y1="{oy1 - 1*u1}" x2="{ox1 + 3}" y2="{oy1 - 1*u1}" stroke="#1e293b" />
      <text x="{ox1 - 12}" y="{oy1 - 1*u1 + 4}" {FONT} font-size="10">1</text>

      <!-- Guidelines -->
      <line x1="{ox1 + 2*u1}" y1="{oy1}" x2="{ox1 + 2*u1}" y2="{oy1 - 3*u1}" stroke="#94a3b8" stroke-dasharray="3 3" />
      <line x1="{ox1}" y1="{oy1 - 3*u1}" x2="{ox1 + 2*u1}" y2="{oy1 - 3*u1}" stroke="#94a3b8" stroke-dasharray="3 3" />

      <!-- Line y = x + 1 with hole at (2, 3) -->
      <line x1="{ox1 - 2.5*u1}" y1="{oy1 + 1.5*u1}" x2="{ox1 + 1.88*u1}" y2="{oy1 - 2.88*u1}" stroke="#0284c7" stroke-width="2.2" />
      <line x1="{ox1 + 2.12*u1}" y1="{oy1 - 3.12*u1}" x2="{ox1 + 4.2*u1}" y2="{oy1 - 5.2*u1}" stroke="#0284c7" stroke-width="2.2" />
      <circle cx="{ox1 + 2*u1}" cy="{oy1 - 3*u1}" r="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.8" />
      <text x="{ox1 + 2*u1 + 8}" y="{oy1 - 3*u1 + 2}" {FONT} font-size="10" fill="#64748b">(2, 3) hole</text>
    </g>
    '''

    # Panel (b): f(x) = 1/x^2 (x != 0), f(0) = 1
    ox2, oy2 = 440, 160
    u2 = 30
    panel_b = f'''
    <g>
      <!-- Subtitle -->
      <text x="350" y="28" {FONT} font-size="12" font-weight="bold" fill="#0f172a">(b) Infinite Discontinuity: f(x) = 1/x²</text>
      <!-- Axes -->
      <line x1="{ox2 - 110}" y1="{oy2}" x2="{ox2 + 130}" y2="{oy2}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
      <line x1="{ox2}" y1="{oy2 + 30}" x2="{ox2}" y2="{oy2 - 120}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
      <text x="{ox2 + 135}" y="{oy2 + 12}" {FONT} font-size="11" font-style="italic">x</text>
      <text x="{ox2 - 12}" y="{oy2 - 115}" {FONT} font-size="11" font-style="italic">y</text>
      <text x="{ox2 - 10}" y="{oy2 + 12}" {FONT} font-size="10">0</text>

      <!-- Curve y = 1/x^2 -->
      <path d="M {ox2 - 3.2*u2} {oy2 - 0.1*u2} Q {ox2 - 1.0*u2} {oy2 - 1.0*u2}, {ox2 - 0.3*u2} {oy2 - 3.8*u2}"
            fill="none" stroke="#0284c7" stroke-width="2.2" />
      <path d="M {ox2 + 3.2*u2} {oy2 - 0.1*u2} Q {ox2 + 1.0*u2} {oy2 - 1.0*u2}, {ox2 + 0.3*u2} {oy2 - 3.8*u2}"
            fill="none" stroke="#0284c7" stroke-width="2.2" />

      <!-- Point (0, 1) -->
      <line x1="{ox2 - 3}" y1="{oy2 - 1*u2}" x2="{ox2 + 3}" y2="{oy2 - 1*u2}" stroke="#1e293b" />
      <text x="{ox2 - 12}" y="{oy2 - 1*u2 + 4}" {FONT} font-size="10">1</text>
      <circle cx="{ox2}" cy="{oy2 - 1*u2}" r="3.5" fill="#0284c7" />
      <text x="{ox2 + 8}" y="{oy2 - 1*u2 + 4}" {FONT} font-size="10" fill="#64748b">(0, 1)</text>
      <text x="{ox2 + 20}" y="{oy2 - 3.2*u2}" {FONT} font-size="10" fill="#e11d48">x = 0 Asymptote</text>
    </g>
    '''

    # Panel (c): f(x) = (x^2 - x - 2)/(x - 2) for x != 2, f(2) = 1
    ox3, oy3 = 120, 390
    u3 = 28
    panel_c = f'''
    <g>
      <!-- Subtitle -->
      <text x="30" y="258" {FONT} font-size="12" font-weight="bold" fill="#0f172a">(c) Removable (Displaced Point): f(2) = 1</text>
      <!-- Axes -->
      <line x1="{ox3 - 90}" y1="{oy3}" x2="{ox3 + 150}" y2="{oy3}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
      <line x1="{ox3}" y1="{oy3 + 60}" x2="{ox3}" y2="{oy3 - 120}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
      <text x="{ox3 + 155}" y="{oy3 + 12}" {FONT} font-size="11" font-style="italic">x</text>
      <text x="{ox3 - 12}" y="{oy3 - 115}" {FONT} font-size="11" font-style="italic">y</text>
      <text x="{ox3 - 10}" y="{oy3 + 12}" {FONT} font-size="10">0</text>

      <!-- Ticks -->
      <line x1="{ox3 + 2*u3}" y1="{oy3 - 3}" x2="{ox3 + 2*u3}" y2="{oy3 + 3}" stroke="#1e293b" />
      <text x="{ox3 + 2*u3 - 3}" y="{oy3 + 14}" {FONT} font-size="10">2</text>
      <line x1="{ox3 - 3}" y1="{oy3 - 3*u3}" x2="{ox3 + 3}" y2="{oy3 - 3*u3}" stroke="#1e293b" />
      <text x="{ox3 - 12}" y="{oy3 - 3*u3 + 4}" {FONT} font-size="10">3</text>
      <line x1="{ox3 - 3}" y1="{oy3 - 1*u3}" x2="{ox3 + 3}" y2="{oy3 - 1*u3}" stroke="#1e293b" />
      <text x="{ox3 - 12}" y="{oy3 - 1*u3 + 4}" {FONT} font-size="10">1</text>

      <!-- Guidelines -->
      <line x1="{ox3 + 2*u3}" y1="{oy3}" x2="{ox3 + 2*u3}" y2="{oy3 - 3*u3}" stroke="#94a3b8" stroke-dasharray="3 3" />
      <line x1="{ox3}" y1="{oy3 - 3*u3}" x2="{ox3 + 2*u3}" y2="{oy3 - 3*u3}" stroke="#94a3b8" stroke-dasharray="3 3" />

      <!-- Line y = x + 1 with hole at (2, 3) -->
      <line x1="{ox3 - 2.5*u3}" y1="{oy3 + 1.5*u3}" x2="{ox3 + 1.88*u3}" y2="{oy3 - 2.88*u3}" stroke="#0284c7" stroke-width="2.2" />
      <line x1="{ox3 + 2.12*u3}" y1="{oy3 - 3.12*u3}" x2="{ox3 + 4.2*u3}" y2="{oy3 - 5.2*u3}" stroke="#0284c7" stroke-width="2.2" />
      <circle cx="{ox3 + 2*u3}" cy="{oy3 - 3*u3}" r="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.8" />

      <!-- Displaced point at (2, 1) -->
      <circle cx="{ox3 + 2*u3}" cy="{oy3 - 1*u3}" r="3.5" fill="#0284c7" />
      <text x="{ox3 + 2*u3 + 8}" y="{oy3 - 1*u3 + 4}" {FONT} font-size="10" fill="#0284c7">f(2) = 1</text>
      <text x="{ox3 + 2*u3 + 8}" y="{oy3 - 3*u3 + 2}" {FONT} font-size="10" fill="#64748b">(2, 3) hole</text>
    </g>
    '''

    # Panel (d): f(x) = [[x]] greatest integer function
    ox4, oy4 = 440, 390
    u4 = 25
    steps = ''
    for n in range(-2, 3):
        x_start = ox4 + n * u4
        x_end = ox4 + (n + 1) * u4
        y_val = oy4 - n * u4
        steps += f'''
        <line x1="{x_start}" y1="{y_val}" x2="{x_end - 3.5}" y2="{y_val}" stroke="#0284c7" stroke-width="2.2" />
        <circle cx="{x_start}" cy="{y_val}" r="3.2" fill="#0284c7" />
        <circle cx="{x_end}" cy="{y_val}" r="3.2" fill="#ffffff" stroke="#0284c7" stroke-width="1.6" />
        '''
    panel_d = f'''
    <g>
      <!-- Subtitle -->
      <text x="350" y="258" {FONT} font-size="12" font-weight="bold" fill="#0f172a">(d) Jump Discontinuities: f(x) = ⟦x⟧</text>
      <!-- Axes -->
      <line x1="{ox4 - 80}" y1="{oy4}" x2="{ox4 + 100}" y2="{oy4}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
      <line x1="{ox4}" y1="{oy4 + 70}" x2="{ox4}" y2="{oy4 - 90}" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow)" />
      <text x="{ox4 + 105}" y="{oy4 + 12}" {FONT} font-size="11" font-style="italic">x</text>
      <text x="{ox4 - 12}" y="{oy4 - 85}" {FONT} font-size="11" font-style="italic">y</text>
      <text x="{ox4 - 10}" y="{oy4 + 12}" {FONT} font-size="10">0</text>
      
      <!-- Steps -->
      {steps}
    </g>
    '''

    return svg_wrapper(w, h, panel_a + panel_b + panel_c + panel_d)


# 4. Intermediate Value Theorem (IVT) Figure
def make_fig_sec2_5_ivt():
    w, h = 420, 260
    ox, oy = 65, 195
    u = 48

    axes = f'''
    <!-- Coordinate axes -->
    <line x1="{ox - 25}" y1="{oy}" x2="{ox + 6.5*u}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 30}" x2="{ox}" y2="{oy - 170}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 6.6*u}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 14}" y="{oy - 165}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>
    '''

    ax = ox + 1.0 * u
    bx = ox + 5.2 * u
    fa_y = oy - 0.6 * u
    fb_y = oy - 3.0 * u
    ny = oy - 1.8 * u
    # Point where curve crosses N
    cx = ox + 3.1 * u

    content = f'''
    <!-- Line y = N -->
    <line x1="{ox}" y1="{ny}" x2="{ox + 6.0*u}" y2="{ny}" stroke="#e11d48" stroke-width="1.4" stroke-dasharray="5 3" />
    <text x="{ox - 18}" y="{ny + 4}" {FONT} font-size="12" font-style="italic" fill="#e11d48">N</text>
    <text x="{ox + 5.5*u}" y="{ny - 8}" {FONT} font-size="11" font-style="italic" fill="#e11d48">y = N</text>

    <!-- Curve y = f(x) connecting (a, f(a)) and (b, f(b)) -->
    <path d="M {ax} {fa_y} C {ax + 1.2*u} {fa_y - 0.4*u}, {cx - 0.8*u} {ny + 0.3*u}, {cx} {ny} C {cx + 0.9*u} {ny - 0.4*u}, {bx - 1.0*u} {fb_y + 0.6*u}, {bx} {fb_y}"
          fill="none" stroke="#0284c7" stroke-width="2.4" />
    <text x="{bx + 8}" y="{fb_y - 4}" {FONT} font-size="12" font-style="italic" fill="#0f172a">y = f(x)</text>

    <!-- Guidelines for a, b, c -->
    <line x1="{ax}" y1="{oy}" x2="{ax}" y2="{fa_y}" stroke="#64748b" stroke-dasharray="3 3" />
    <line x1="{ox}" y1="{fa_y}" x2="{ax}" y2="{fa_y}" stroke="#64748b" stroke-dasharray="3 3" />
    <text x="{ax - 4}" y="{oy + 16}" {FONT} font-size="12" font-style="italic">a</text>
    <text x="{ox - 24}" y="{fa_y + 4}" {FONT} font-size="11" font-style="italic">f(a)</text>

    <line x1="{bx}" y1="{oy}" x2="{bx}" y2="{fb_y}" stroke="#64748b" stroke-dasharray="3 3" />
    <line x1="{ox}" y1="{fb_y}" x2="{bx}" y2="{fb_y}" stroke="#64748b" stroke-dasharray="3 3" />
    <text x="{bx - 4}" y="{oy + 16}" {FONT} font-size="12" font-style="italic">b</text>
    <text x="{ox - 24}" y="{fb_y + 4}" {FONT} font-size="11" font-style="italic">f(b)</text>

    <!-- Value c on x axis -->
    <line x1="{cx}" y1="{oy}" x2="{cx}" y2="{ny}" stroke="#64748b" stroke-dasharray="3 3" />
    <text x="{cx - 3}" y="{oy + 16}" {FONT} font-size="12" font-style="italic" fill="#0284c7">c</text>

    <!-- Endpoints and intersection -->
    <circle cx="{ax}" cy="{fa_y}" r="3.5" fill="#0284c7" />
    <circle cx="{bx}" cy="{fb_y}" r="3.5" fill="#0284c7" />
    <circle cx="{cx}" cy="{ny}" r="4.0" fill="#e11d48" />
    <text x="{cx + 8}" y="{ny + 16}" {FONT} font-size="11" fill="#e11d48">(c, N)</text>
    '''

    caption = f'<text x="25" y="245" {FONT} font-size="12" font-weight="bold" fill="#1e293b">INTERMEDIATE VALUE THEOREM</text>'
    return svg_wrapper(w, h, axes + content + caption)


def main():
    figs = {
        "sec2_5_figure1_continuity_definition.svg": make_fig_sec2_5_fig1(),
        "sec2_5_figure2_discontinuities_example1.svg": make_fig_sec2_5_fig2(),
        "sec2_5_figure3_example2_discontinuity_types.svg": make_fig_sec2_5_example2_panels(),
        "sec2_5_figure_ivt.svg": make_fig_sec2_5_ivt(),
    }
    for filename, content in figs.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Wrote {filepath}")

if __name__ == "__main__":
    main()
