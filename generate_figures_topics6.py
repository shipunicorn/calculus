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
  <marker id="arrow-orange" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#ea580c" />
  </marker>
</defs>
{content}
</svg>'''

# -------------------------------------------------------------------
# 1. Section 3.7 Figure 1: Three Fencing Configurations
# -------------------------------------------------------------------
def make_sec3_7_fig1():
    w, h = 640, 210
    
    # We draw 3 panels side by side
    # Panel centers: 110, 320, 530. River line at y = 160.
    content = f'''
    <!-- Panel 1: Shallow & Wide (100 x 2200) -->
    <rect x="15" y="15" width="190" height="185" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
    <path d="M 15 145 C 40 142, 60 148, 85 145 C 110 142, 130 148, 155 145 C 175 142, 195 148, 205 145 L 205 200 L 15 200 Z" fill="#bae6fd" />
    <path d="M 15 145 C 40 142, 60 148, 85 145 C 110 142, 130 148, 155 145 C 175 142, 195 148, 205 145" fill="none" stroke="#0284c7" stroke-width="1.8" />
    <text x="110" y="180" {FONT} font-size="11" fill="#0369a1" font-weight="600" text-anchor="middle">Straight River</text>
    
    <!-- Field 1 -->
    <rect x="35" y="125" width="150" height="20" fill="#dcfce7" fill-opacity="0.6" stroke="none" />
    <polyline points="35,145 35,125 185,125 185,145" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-linejoin="round" />
    <text x="110" y="118" {FONT} font-size="11" fill="#1e293b" text-anchor="middle">2200</text>
    <text x="26" y="138" {FONT} font-size="11" fill="#1e293b" text-anchor="end">100</text>
    <text x="194" y="138" {FONT} font-size="11" fill="#1e293b" text-anchor="start">100</text>
    <text x="110" y="55" {FONT} font-size="11.5" font-weight="600" fill="#1e293b" text-anchor="middle">Area = 100 · 2200</text>
    <text x="110" y="73" {FONT} font-size="12" font-weight="bold" fill="#0f766e" text-anchor="middle">= 220,000 ft²</text>
    <text x="110" y="32" {FONT} font-size="11" font-weight="bold" fill="#64748b" text-anchor="middle">Case 1: Shallow &amp; Wide</text>

    <!-- Panel 2: Intermediate (700 x 1000) -->
    <rect x="225" y="15" width="190" height="185" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
    <path d="M 225 145 C 250 142, 270 148, 295 145 C 320 142, 340 148, 365 145 C 385 142, 405 148, 415 145 L 415 200 L 225 200 Z" fill="#bae6fd" />
    <path d="M 225 145 C 250 142, 270 148, 295 145 C 320 142, 340 148, 365 145 C 385 142, 405 148, 415 145" fill="none" stroke="#0284c7" stroke-width="1.8" />
    <text x="320" y="180" {FONT} font-size="11" fill="#0369a1" font-weight="600" text-anchor="middle">Straight River</text>

    <!-- Field 2 -->
    <rect x="270" y="85" width="100" height="60" fill="#dcfce7" fill-opacity="0.6" stroke="none" />
    <polyline points="270,145 270,85 370,85 370,145" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-linejoin="round" />
    <text x="320" y="78" {FONT} font-size="11" fill="#1e293b" text-anchor="middle">1000</text>
    <text x="262" y="118" {FONT} font-size="11" fill="#1e293b" text-anchor="end">700</text>
    <text x="378" y="118" {FONT} font-size="11" fill="#1e293b" text-anchor="start">700</text>
    <text x="320" y="45" {FONT} font-size="11.5" font-weight="600" fill="#1e293b" text-anchor="middle">Area = 700 · 1000</text>
    <text x="320" y="63" {FONT} font-size="12" font-weight="bold" fill="#0f766e" text-anchor="middle">= 700,000 ft²</text>
    <text x="320" y="30" {FONT} font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">Case 2: Intermediate</text>

    <!-- Panel 3: Deep & Narrow (1000 x 400) -->
    <rect x="435" y="15" width="190" height="185" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
    <path d="M 435 145 C 460 142, 480 148, 505 145 C 530 142, 550 148, 575 145 C 595 142, 615 148, 625 145 L 625 200 L 435 200 Z" fill="#bae6fd" />
    <path d="M 435 145 C 460 142, 480 148, 505 145 C 530 142, 550 148, 575 145 C 595 142, 615 148, 625 145" fill="none" stroke="#0284c7" stroke-width="1.8" />
    <text x="530" y="180" {FONT} font-size="11" fill="#0369a1" font-weight="600" text-anchor="middle">Straight River</text>

    <!-- Field 3 -->
    <rect x="505" y="60" width="50" height="85" fill="#dcfce7" fill-opacity="0.6" stroke="none" />
    <polyline points="505,145 505,60 555,60 555,145" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-linejoin="round" />
    <text x="530" y="53" {FONT} font-size="11" fill="#1e293b" text-anchor="middle">400</text>
    <text x="497" y="105" {FONT} font-size="11" fill="#1e293b" text-anchor="end">1000</text>
    <text x="563" y="105" {FONT} font-size="11" fill="#1e293b" text-anchor="start">1000</text>
    <text x="530" y="38" {FONT} font-size="11.5" font-weight="600" fill="#1e293b" text-anchor="middle">Area = 1000 · 400</text>
    <text x="530" y="53" {FONT} font-size="12" font-weight="bold" fill="#0f766e" text-anchor="middle" y="32" style="display:none">= 400,000 ft²</text>
    <text x="530" y="24" {FONT} font-size="11" font-weight="bold" fill="#64748b" text-anchor="middle">Case 3: Deep &amp; Narrow</text>
    <text x="530" y="38" {FONT} font-size="11.5" font-weight="600" fill="#1e293b" text-anchor="middle">Area = 1000 · 400</text>
    <text x="530" y="54" {FONT} font-size="12" font-weight="bold" fill="#0f766e" text-anchor="middle">= 400,000 ft²</text>
    '''
    return svg_wrapper(w, h, content)

# -------------------------------------------------------------------
# 2. Section 3.7 Figure 2: General River Fencing Model
# -------------------------------------------------------------------
def make_sec3_7_fig2():
    w, h = 380, 220
    content = f'''
    <!-- Background field -->
    <rect x="20" y="20" width="340" height="180" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
    
    <!-- River -->
    <path d="M 20 150 C 60 146, 110 154, 160 148 C 210 144, 260 154, 310 148 C 335 145, 350 150, 360 148 L 360 200 L 20 200 Z" fill="#bae6fd" />
    <path d="M 20 150 C 60 146, 110 154, 160 148 C 210 144, 260 154, 310 148 C 335 145, 350 150, 360 148" fill="none" stroke="#0284c7" stroke-width="2" />
    <text x="190" y="180" {FONT} font-size="12" fill="#0369a1" font-weight="bold" text-anchor="middle">Straight River (No fencing required)</text>

    <!-- Fenced Area -->
    <rect x="90" y="60" width="200" height="88" fill="#dcfce7" fill-opacity="0.7" stroke="none" />
    <polyline points="90,148 90,60 290,60 290,148" fill="none" stroke="#dc2626" stroke-width="3" stroke-linejoin="round" />
    
    <!-- Labels -->
    <text x="190" y="50" {FONT} font-size="13" font-style="italic" font-weight="600" fill="#1e293b" text-anchor="middle">y (width)</text>
    <text x="75" y="108" {FONT} font-size="13" font-style="italic" font-weight="600" fill="#1e293b" text-anchor="end">x</text>
    <text x="305" y="108" {FONT} font-size="13" font-style="italic" font-weight="600" fill="#1e293b" text-anchor="start">x</text>
    
    <text x="190" y="105" {FONT} font-size="15" font-weight="bold" fill="#0f766e" text-anchor="middle">A = xy</text>
    <text x="190" y="125" {FONT} font-size="11" fill="#475569" text-anchor="middle">Total fencing: 2x + y = 2400</text>
    '''
    return svg_wrapper(w, h, content)

# -------------------------------------------------------------------
# 3. Section 3.7 Exercise 11: Four Pens Fencing
# -------------------------------------------------------------------
def make_sec3_7_ex11():
    w, h = 620, 220
    content = f'''
    <!-- Left Panel: Sample Explorations -->
    <rect x="15" y="15" width="260" height="190" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="145" y="36" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Part (a): Sample Configurations</text>
    
    <!-- Shallow / Wide: x = 50, y = 250 => 5(50)+2(250)=750, Area = 12,500 -->
    <rect x="35" y="55" width="220" height="30" fill="#ecfdf5" stroke="#dc2626" stroke-width="2" />
    <line x1="90" y1="55" x2="90" y2="85" stroke="#dc2626" stroke-width="1.8" />
    <line x1="145" y1="55" x2="145" y2="85" stroke="#dc2626" stroke-width="1.8" />
    <line x1="200" y1="55" x2="200" y2="85" stroke="#dc2626" stroke-width="1.8" />
    <text x="145" y="73" {FONT} font-size="10" fill="#047857" font-weight="600" text-anchor="middle">Shallow: x = 50, y = 250 → Area = 12,500 ft²</text>

    <!-- Deep / Narrow: x = 100, y = 125 => 5(100)+2(125)=750, Area = 12,500 -->
    <rect x="75" y="105" width="140" height="60" fill="#ecfdf5" stroke="#dc2626" stroke-width="2" />
    <line x1="110" y1="105" x2="110" y2="165" stroke="#dc2626" stroke-width="1.8" />
    <line x1="145" y1="105" x2="145" y2="165" stroke="#dc2626" stroke-width="1.8" />
    <line x1="180" y1="105" x2="180" y2="165" stroke="#dc2626" stroke-width="1.8" />
    <text x="145" y="138" {FONT} font-size="10" fill="#047857" font-weight="600" text-anchor="middle">Deep: x = 100, y = 125</text>
    <text x="145" y="152" {FONT} font-size="10" fill="#047857" font-weight="600" text-anchor="middle">Area = 12,500 ft²</text>

    <text x="145" y="190" {FONT} font-size="10.5" fill="#64748b" text-anchor="middle">Estimate: Max area ≥ 12,500 ft²</text>

    <!-- Right Panel: General 4-Pen Model -->
    <rect x="295" y="15" width="310" height="190" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="450" y="36" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Part (b): General Four-Pen Model</text>

    <!-- Outer rectangle -->
    <rect x="330" y="65" width="240" height="85" fill="#f0fdf4" stroke="#dc2626" stroke-width="2.5" />
    <!-- 3 Internal Dividers (5 vertical fence segments total) -->
    <line x1="390" y1="65" x2="390" y2="150" stroke="#dc2626" stroke-width="2.2" />
    <line x1="450" y1="65" x2="450" y2="150" stroke="#dc2626" stroke-width="2.2" />
    <line x1="510" y1="65" x2="510" y2="150" stroke="#dc2626" stroke-width="2.2" />

    <!-- Pen labels -->
    <text x="360" y="112" {FONT} font-size="11" fill="#15803d" font-weight="600" text-anchor="middle">Pen 1</text>
    <text x="420" y="112" {FONT} font-size="11" fill="#15803d" font-weight="600" text-anchor="middle">Pen 2</text>
    <text x="480" y="112" {FONT} font-size="11" fill="#15803d" font-weight="600" text-anchor="middle">Pen 3</text>
    <text x="540" y="112" {FONT} font-size="11" fill="#15803d" font-weight="600" text-anchor="middle">Pen 4</text>

    <!-- Dimension annotations -->
    <text x="450" y="56" {FONT} font-size="12" font-style="italic" font-weight="bold" fill="#1e293b" text-anchor="middle">y (width)</text>
    <text x="318" y="112" {FONT} font-size="12" font-style="italic" font-weight="bold" fill="#1e293b" text-anchor="end">x</text>
    
    <text x="450" y="175" {FONT} font-size="11" fill="#1e293b" text-anchor="middle">Constraint: 5x + 2y = 750  ⇒  y = 375 − 2.5x</text>
    <text x="450" y="193" {FONT} font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">Max Area at x = 75 ft, y = 187.5 ft: A = 14,062.5 ft²</text>
    '''
    return svg_wrapper(w, h, content)

# -------------------------------------------------------------------
# 4. Section 3.7 Exercise 35: Wire Cut into Square and Triangle
# -------------------------------------------------------------------
def make_sec3_7_ex35():
    w, h = 580, 220
    content = f'''
    <!-- Top: 10 m Wire -->
    <rect x="20" y="15" width="540" height="70" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="290" y="34" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Total Wire Length = 10 m</text>
    
    <!-- Wire line -->
    <line x1="50" y1="52" x2="270" y2="52" stroke="#0284c7" stroke-width="5" stroke-linecap="round" />
    <line x1="280" y1="52" x2="530" y2="52" stroke="#ea580c" stroke-width="5" stroke-linecap="round" />
    <!-- Cut indicator -->
    <line x1="275" y1="42" x2="275" y2="62" stroke="#dc2626" stroke-width="2" stroke-dasharray="3 2" />
    <text x="275" y="73" {FONT} font-size="10" fill="#dc2626" font-weight="bold" text-anchor="middle">Cut</text>
    
    <text x="160" y="44" {FONT} font-size="11" font-style="italic" fill="#0284c7" font-weight="600" text-anchor="middle">x (for square)</text>
    <text x="405" y="44" {FONT} font-size="11" font-style="italic" fill="#ea580c" font-weight="600" text-anchor="middle">10 − x (for equilateral triangle)</text>

    <!-- Bottom Left: Square -->
    <rect x="50" y="98" width="220" height="110" rx="6" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1" />
    <rect x="75" y="120" width="55" height="55" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5" />
    <text x="102" y="113" {FONT} font-size="11" font-style="italic" fill="#0284c7" text-anchor="middle">x / 4</text>
    <text x="66" y="152" {FONT} font-size="11" font-style="italic" fill="#0284c7" text-anchor="end">x / 4</text>
    <text x="195" y="135" {FONT} font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">Square</text>
    <text x="195" y="155" {FONT} font-size="11" fill="#1e293b" text-anchor="middle">Perimeter = x</text>
    <text x="195" y="175" {FONT} font-size="11.5" font-weight="600" fill="#0f766e" text-anchor="middle">Area = x² / 16</text>

    <!-- Bottom Right: Equilateral Triangle -->
    <rect x="310" y="98" width="220" height="110" rx="6" fill="#fff7ed" stroke="#fed7aa" stroke-width="1" />
    <polygon points="360,175 420,175 390,123" fill="#ffedd5" stroke="#ea580c" stroke-width="2.5" />
    <text x="390" y="190" {FONT} font-size="11" font-style="italic" fill="#ea580c" text-anchor="middle">(10 − x) / 3</text>
    <text x="475" y="135" {FONT} font-size="12" font-weight="bold" fill="#c2410c" text-anchor="middle">Equilateral Δ</text>
    <text x="475" y="155" {FONT} font-size="11" fill="#1e293b" text-anchor="middle">Perimeter = 10 − x</text>
    <text x="475" y="175" {FONT} font-size="11.5" font-weight="600" fill="#0f766e" text-anchor="middle">Area = √3/36 · (10 − x)²</text>
    '''
    return svg_wrapper(w, h, content)

# -------------------------------------------------------------------
# 5. Section 3.7 Exercise 56: Tangent Line Hypotenuse to y = 4 - x^2
# -------------------------------------------------------------------
def make_sec3_7_ex56():
    w, h = 460, 320
    ox, oy = 70, 270
    ux, uy = 130, 42
    
    # Parabola y = 4 - x^2 from x = 0 to x = 2
    # At a = 2 / sqrt(3) ~ 1.155:
    # y = 4 - 4/3 = 8/3 ~ 2.667
    # y-intercept = a^2 + 4 = 16/3 ~ 5.333 -> py = oy - 5.333 * uy = 270 - 224 = 46
    # x-intercept = (a^2 + 4)/(2a) = (16/3) / (4/sqrt(3)) = 4/sqrt(3) ~ 2.309 -> px = ox + 2.309 * ux = 70 + 300 = 370
    
    pts_parabola = []
    for step in range(0, 105):
        x_val = step * 0.02
        y_val = 4 - x_val**2
        pts_parabola.append(f"{ox + x_val * ux:.1f},{oy - y_val * uy:.1f}")
    poly_parabola = " ".join(pts_parabola)

    a_val = 2.0 / math.sqrt(3)
    y_val = 4 - a_val**2
    pt_tan_x = ox + a_val * ux
    pt_tan_y = oy - y_val * uy
    x_int_px = ox + (4.0 / math.sqrt(3)) * ux
    y_int_py = oy - (16.0 / 3.0) * uy

    content = f'''
    <!-- Triangle in 1st quadrant formed by tangent line -->
    <polygon points="{ox},{oy} {x_int_px:.1f},{oy} {ox},{y_int_py:.1f}" fill="#fdf2f8" stroke="none" />

    <!-- Axes -->
    <line x1="{ox - 20}" y1="{oy}" x2="{ox + 340}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 20}" x2="{ox}" y2="{oy - 250}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 345}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 15}" y="{oy - 245}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 15}" {FONT} font-size="11">0</text>

    <!-- Ticks -->
    <line x1="{ox + ux}" y1="{oy - 3}" x2="{ox + ux}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{ox + ux - 3}" y="{oy + 16}" {FONT} font-size="11">1</text>
    <line x1="{ox + 2*ux}" y1="{oy - 3}" x2="{ox + 2*ux}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{ox + 2*ux - 3}" y="{oy + 16}" {FONT} font-size="11">2</text>
    
    <line x1="{ox - 3}" y1="{oy - 4*uy}" x2="{ox + 3}" y2="{oy - 4*uy}" stroke="#1e293b" stroke-width="1.2" />
    <text x="{ox - 15}" y="{oy - 4*uy + 4}" {FONT} font-size="11">4</text>

    <!-- Parabola y = 4 - x^2 -->
    <polyline points="{poly_parabola}" fill="none" stroke="#0284c7" stroke-width="2.5" />
    <text x="{ox + 0.5*ux}" y="{oy - 3.8*uy}" {FONT} font-size="12" font-weight="bold" fill="#0284c7">y = 4 − x²</text>

    <!-- Tangent Hypotenuse -->
    <line x1="{ox}" y1="{y_int_py:.1f}" x2="{x_int_px:.1f}" y2="{oy}" stroke="#db2777" stroke-width="2.5" />
    
    <!-- Tangent point P -->
    <circle cx="{pt_tan_x:.1f}" cy="{pt_tan_y:.1f}" r="4" fill="#db2777" />
    <text x="{pt_tan_x + 10:.1f}" y="{pt_tan_y - 8:.1f}" {FONT} font-size="11" font-weight="600" fill="#db2777">P(a, 4 − a²)</text>

    <!-- Intercept labels -->
    <circle cx="{ox}" cy="{y_int_py:.1f}" r="3" fill="#db2777" />
    <text x="{ox + 8}" y="{y_int_py + 4:.1f}" {FONT} font-size="10.5" font-weight="600" fill="#9d174d">(0, a² + 4)</text>
    
    <circle cx="{x_int_px:.1f}" cy="{oy}" r="3" fill="#db2777" />
    <text x="{x_int_px:.1f}" y="{oy + 18}" {FONT} font-size="10.5" font-weight="600" fill="#9d174d" text-anchor="middle">((a² + 4)/(2a), 0)</text>

    <!-- Annotation badge -->
    <rect x="230" y="30" width="190" height="65" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
    <text x="240" y="48" {FONT} font-size="11" font-weight="bold" fill="#1e293b">Optimal Tangency:</text>
    <text x="240" y="65" {FONT} font-size="11" fill="#475569">a = 2/√3 ≈ 1.155</text>
    <text x="240" y="82" {FONT} font-size="11.5" font-weight="bold" fill="#be185d">Min Area = 32√3 / 9 ≈ 6.16</text>
    '''
    return svg_wrapper(w, h, content)

# -------------------------------------------------------------------
# 6. Section 3.9 Figure 1: Family of Antiderivatives y = x^3/3 + C
# -------------------------------------------------------------------
def make_sec3_9_fig1():
    w, h = 460, 340
    ox, oy = 180, 180
    ux, uy = 65, 30

    # Curves for C in [3, 2, 1, 0, -1, -2]
    curves = [
        (3, "#db2777", "y = x³/3 + 3"),
        (2, "#ea580c", "y = x³/3 + 2"),
        (1, "#0284c7", "y = x³/3 + 1"),
        (0, "#16a34a", "y = x³/3"),
        (-1, "#8b5cf6", "y = x³/3 − 1"),
        (-2, "#64748b", "y = x³/3 − 2")
    ]

    paths_svg = []
    for c_val, col, lbl in curves:
        pts = []
        for step in range(-110, 115):
            x = step * 0.015
            y = (x**3) / 3.0 + c_val
            px = ox + x * ux
            py = oy - y * uy
            if 15 <= py <= 325:
                pts.append(f"{px:.1f},{py:.1f}")
        poly = " ".join(pts)
        paths_svg.append(f'<polyline points="{poly}" fill="none" stroke="{col}" stroke-width="2" />')
        # Label at right end
        end_x = ox + 1.65 * ux
        end_y = oy - ((1.65**3)/3.0 + c_val) * uy
        paths_svg.append(f'<text x="{end_x + 8:.1f}" y="{end_y + 4:.1f}" {FONT} font-size="10.5" font-weight="600" fill="{col}">{lbl}</text>')

    content = f'''
    <!-- Axes -->
    <line x1="{ox - 130}" y1="{oy}" x2="{ox + 160}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 140}" x2="{ox}" y2="{oy - 155}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="{ox + 165}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 15}" y="{oy - 150}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>

    <!-- Curves -->
    {"".join(paths_svg)}

    <!-- Annotation badge -->
    <rect x="15" y="20" width="135" height="48" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="22" y="37" {FONT} font-size="10.5" font-weight="bold" fill="#1e293b">Family of Curves</text>
    <text x="22" y="53" {FONT} font-size="10" fill="#475569">Same slope at each x</text>
    '''
    return svg_wrapper(w, h, content)

# -------------------------------------------------------------------
# 7. Section 3.9 Figure 2: Example 5 (Sketching Antiderivative)
# -------------------------------------------------------------------
def make_sec3_9_fig2():
    w, h = 620, 260
    
    # Left: f(x)
    ox1, oy1 = 50, 180
    ux1, uy1 = 45, 60
    
    # Right: F(x) with F(0) = 2
    ox2, oy2 = 350, 180
    ux2, uy2 = 45, 30

    # Model for f(x):
    # f(0) = -1.5, root at x=1, local max at x=2 (val=1), root at x=3, local min at x=4 (val=-0.5), decaying to 0
    pts_f = []
    for step in range(0, 110):
        x = step * 0.05
        # polynomial-exponential shape:
        y = - (x - 1) * (x - 3) * math.exp(-0.5 * x) - (1.5 if x < 0.1 else 0)
        # Let's use smooth interpolation
        # f(x) = (2*x - x^2 - 1) for initial, or cubic spline:
        # At x=0: y=-1. At x=1: y=0. At x=2: y=1. At x=3: y=0. At x=4: y=-0.4. At x=5: y=-0.1.
        y = -(x - 1)*(x - 3)*(1.3 - 0.2*x)*math.exp(-0.4*x)
        pts_f.append(f"{ox1 + x * ux1:.1f},{oy1 - y * uy1:.1f}")
    poly_f = " ".join(pts_f)

    # Sketched F(x): starts at (0, 2), min at x=1, max at x=3, levels off
    pts_F = []
    # numerical integration of f(x)
    curr_F = 2.0
    dx = 0.05
    for step in range(0, 110):
        x = step * dx
        y_f = -(x - 1)*(x - 3)*(1.3 - 0.2*x)*math.exp(-0.4*x)
        pts_F.append(f"{ox2 + x * ux2:.1f},{oy2 - curr_F * uy2:.1f}")
        curr_F += y_f * dx
    poly_F = " ".join(pts_F)

    content = f'''
    <!-- Left Panel: y = f(x) -->
    <rect x="15" y="15" width="280" height="230" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="155" y="35" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Given Derivative y = f(x)</text>

    <!-- Axes Left -->
    <line x1="{ox1 - 10}" y1="{oy1}" x2="{ox1 + 230}" y2="{oy1}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <line x1="{ox1}" y1="{oy1 + 40}" x2="{ox1}" y2="{oy1 - 120}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <text x="{ox1 + 235}" y="{oy1 + 14}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox1 - 12}" y="{oy1 - 115}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox1 - 10}" y="{oy1 + 14}" {FONT} font-size="10">0</text>

    <!-- Ticks Left -->
    <line x1="{ox1 + ux1}" y1="{oy1 - 3}" x2="{ox1 + ux1}" y2="{oy1 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 + ux1 - 3}" y="{oy1 + 14}" {FONT} font-size="10">1</text>
    <line x1="{ox1 + 2*ux1}" y1="{oy1 - 3}" x2="{ox1 + 2*ux1}" y2="{oy1 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 + 2*ux1 - 3}" y="{oy1 + 14}" {FONT} font-size="10">2</text>
    <line x1="{ox1 + 3*ux1}" y1="{oy1 - 3}" x2="{ox1 + 3*ux1}" y2="{oy1 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 + 3*ux1 - 3}" y="{oy1 + 14}" {FONT} font-size="10">3</text>
    <line x1="{ox1 + 4*ux1}" y1="{oy1 - 3}" x2="{ox1 + 4*ux1}" y2="{oy1 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 + 4*ux1 - 3}" y="{oy1 + 14}" {FONT} font-size="10">4</text>

    <!-- Curve f(x) -->
    <polyline points="{poly_f}" fill="none" stroke="#0284c7" stroke-width="2.2" />
    <text x="{ox1 + 2.2*ux1}" y="{oy1 - 1.1*uy1}" {FONT} font-size="11.5" font-weight="bold" fill="#0284c7">y = f(x)</text>

    <!-- Right Panel: Sketched Antiderivative y = F(x) -->
    <rect x="315" y="15" width="290" height="230" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="460" y="35" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Sketched Antiderivative y = F(x)</text>

    <!-- Axes Right -->
    <line x1="{ox2 - 10}" y1="{oy2}" x2="{ox2 + 230}" y2="{oy2}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <line x1="{ox2}" y1="{oy2 + 20}" x2="{ox2}" y2="{oy2 - 140}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <text x="{ox2 + 235}" y="{oy2 + 14}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox2 - 12}" y="{oy2 - 135}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox2 - 10}" y="{oy2 + 14}" {FONT} font-size="10">0</text>

    <!-- Ticks Right -->
    <line x1="{ox2 + ux2}" y1="{oy2 - 3}" x2="{ox2 + ux2}" y2="{oy2 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox2 + ux2 - 3}" y="{oy2 + 14}" {FONT} font-size="10">1</text>
    <line x1="{ox2 + 2*ux2}" y1="{oy2 - 3}" x2="{ox2 + 2*ux2}" y2="{oy2 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox2 + 2*ux2 - 3}" y="{oy2 + 14}" {FONT} font-size="10">2</text>
    <line x1="{ox2 + 3*ux2}" y1="{oy2 - 3}" x2="{ox2 + 3*ux2}" y2="{oy2 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox2 + 3*ux2 - 3}" y="{oy2 + 14}" {FONT} font-size="10">3</text>
    <line x1="{ox2 + 4*ux2}" y1="{oy2 - 3}" x2="{ox2 + 4*ux2}" y2="{oy2 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox2 + 4*ux2 - 3}" y="{oy2 + 14}" {FONT} font-size="10">4</text>

    <!-- Initial point (0, 2) -->
    <circle cx="{ox2}" cy="{oy2 - 2*uy2}" r="3.5" fill="#db2777" />
    <text x="{ox2 - 12}" y="{oy2 - 2*uy2 + 4}" {FONT} font-size="10" font-weight="bold" fill="#db2777">2</text>

    <!-- Curve F(x) -->
    <polyline points="{poly_F}" fill="none" stroke="#db2777" stroke-width="2.2" />
    <text x="{ox2 + 2.8*ux2}" y="{oy2 - 3.4*uy2}" {FONT} font-size="11.5" font-weight="bold" fill="#db2777">y = F(x)</text>

    <!-- Guidelines at x=1 and x=3 -->
    <line x1="{ox2 + ux2}" y1="{oy2}" x2="{ox2 + ux2}" y2="{oy2 - 1.4*uy2}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2" />
    <text x="{ox2 + ux2}" y="{oy2 - 0.7*uy2}" {FONT} font-size="9.5" fill="#475569" text-anchor="middle">Local Min</text>

    <line x1="{ox2 + 3*ux2}" y1="{oy2}" x2="{ox2 + 3*ux2}" y2="{oy2 - 3.1*uy2}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2" />
    <text x="{ox2 + 3*ux2}" y="{oy2 - 2.2*uy2}" {FONT} font-size="9.5" fill="#475569" text-anchor="middle">Local Max</text>
    '''
    return svg_wrapper(w, h, content)

# -------------------------------------------------------------------
# 8. Section 3.9 Exercise 43: Antiderivative Matching (b is antiderivative)
# -------------------------------------------------------------------
def make_sec3_9_ex43():
    w, h = 460, 300
    ox, oy = 90, 190
    ux, uy = 65, 45

    # Pink curve f: starts negative for small x, crosses x-axis at x ~ 1.5, increases into Q1
    # b: starts decreasing, horizontal tangent at x ~ 1.5, then increases (concave up) -> b' = f!
    # a: starts very negative, strictly increasing through x-axis
    # c: starts positive, reaches maximum around x ~ 1.5, then decreases into Q4
    
    pts_f = []
    pts_b = []
    pts_a = []
    pts_c = []
    for step in range(-10, 80):
        x = step * 0.05
        # f(x) = 1.2 * (x - 1.5)
        # smoother:
        f_val = 0.8 * (x - 1.4) + 0.3 * (x - 1.4)**2
        b_val = 0.4 * (x - 1.4)**2 + 0.1 * (x - 1.4)**3 + 0.2
        a_val = 2.2 * math.log(max(0.1, x + 0.5)) - 1.5
        c_val = -0.5 * (x - 1.4)**2 + 1.8
        
        px = ox + x * ux
        if px <= 430:
            pts_f.append(f"{px:.1f},{oy - f_val * uy:.1f}")
            pts_b.append(f"{px:.1f},{oy - b_val * uy:.1f}")
            if oy - a_val * uy <= 280:
                pts_a.append(f"{px:.1f},{oy - a_val * uy:.1f}")
            pts_c.append(f"{px:.1f},{oy - c_val * uy:.1f}")

    content = f'''
    <!-- Axes -->
    <line x1="{ox - 40}" y1="{oy}" x2="{ox + 330}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 80}" x2="{ox}" y2="{oy - 160}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <text x="{ox + 335}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 15}" y="{oy - 155}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>

    <!-- Curves -->
    <polyline points="{" ".join(pts_a)}" fill="none" stroke="#1e293b" stroke-width="2" />
    <text x="140" y="65" {FONT} font-size="12" font-weight="bold" fill="#1e293b">a</text>

    <polyline points="{" ".join(pts_c)}" fill="none" stroke="#16a34a" stroke-width="2" />
    <text x="320" y="270" {FONT} font-size="12" font-weight="bold" fill="#16a34a">c</text>

    <polyline points="{" ".join(pts_b)}" fill="none" stroke="#0284c7" stroke-width="2.5" />
    <text x="325" y="70" {FONT} font-size="13" font-weight="bold" fill="#0284c7">b</text>

    <polyline points="{" ".join(pts_f)}" fill="none" stroke="#db2777" stroke-width="2.5" />
    <text x="240" y="55" {FONT} font-size="13" font-weight="bold" fill="#db2777">f</text>

    <!-- Highlight box -->
    <rect x="250" y="15" width="190" height="42" rx="5" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1" />
    <text x="260" y="32" {FONT} font-size="11" font-weight="bold" fill="#0369a1">Antiderivative: Curve b</text>
    <text x="260" y="47" {FONT} font-size="10" fill="#475569">f &lt; 0 ⇒ b decreases; f &gt; 0 ⇒ b increases</text>
    '''
    return svg_wrapper(w, h, content)

# -------------------------------------------------------------------
# 9. Section 3.9 Exercise 44: Antiderivative Matching (a is antiderivative)
# -------------------------------------------------------------------
def make_sec3_9_ex44():
    w, h = 460, 300
    ox, oy = 80, 190
    ux, uy = 65, 50

    # Pink curve f: starts high positive, strictly decreases across x-axis at x ~ 1.2, stays negative and levels off to 0
    # a: starts at origin, increases to a local maximum at x ~ 1.2 (where f = 0), then decreases asymptotically to 0 -> a' = f!
    # b: starts at origin, dips negative, rises
    # c: starts very negative, strictly increases through x-axis
    
    pts_f = []
    pts_a = []
    pts_b = []
    pts_c = []
    for step in range(0, 80):
        x = step * 0.05
        f_val = 3.0 * math.exp(-1.2 * x) - 0.4
        a_val = 1.8 * x * math.exp(-0.8 * x)
        b_val = -1.2 * x * math.exp(-0.9 * x) + 0.1 * x**1.5
        c_val = 2.0 * math.log(max(0.08, x + 0.3)) + 0.8
        
        px = ox + x * ux
        if px <= 430:
            pts_f.append(f"{px:.1f},{oy - f_val * uy:.1f}")
            pts_a.append(f"{px:.1f},{oy - a_val * uy:.1f}")
            pts_b.append(f"{px:.1f},{oy - b_val * uy:.1f}")
            pts_c.append(f"{px:.1f},{oy - c_val * uy:.1f}")

    content = f'''
    <!-- Axes -->
    <line x1="{ox - 30}" y1="{oy}" x2="{ox + 340}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 80}" x2="{ox}" y2="{oy - 160}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />
    <text x="{ox + 345}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 15}" y="{oy - 155}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 14}" {FONT} font-size="11">0</text>

    <!-- Curves -->
    <polyline points="{" ".join(pts_c)}" fill="none" stroke="#16a34a" stroke-width="2" />
    <text x="145" y="270" {FONT} font-size="12" font-weight="bold" fill="#16a34a">c</text>

    <polyline points="{" ".join(pts_b)}" fill="none" stroke="#0284c7" stroke-width="2" />
    <text x="120" y="240" {FONT} font-size="12" font-weight="bold" fill="#0284c7">b</text>

    <polyline points="{" ".join(pts_f)}" fill="none" stroke="#db2777" stroke-width="2.5" />
    <text x="110" y="70" {FONT} font-size="13" font-weight="bold" fill="#db2777">f</text>

    <polyline points="{" ".join(pts_a)}" fill="none" stroke="#1e293b" stroke-width="2.5" />
    <text x="190" y="85" {FONT} font-size="13" font-weight="bold" fill="#1e293b">a</text>

    <!-- Highlight box -->
    <rect x="250" y="15" width="190" height="42" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="260" y="32" {FONT} font-size="11" font-weight="bold" fill="#1e293b">Antiderivative: Curve a</text>
    <text x="260" y="47" {FONT} font-size="10" fill="#475569">Peak of a occurs exactly where f = 0</text>
    '''
    return svg_wrapper(w, h, content)

# -------------------------------------------------------------------
# 10. Section 3.9 Exercise 45: Antiderivative Sketch for Oscillating f(x)
# -------------------------------------------------------------------
def make_sec3_9_ex45():
    w, h = 620, 240
    
    ox1, oy1 = 45, 140
    ux1, uy1 = 55, 45
    
    ox2, oy2 = 345, 170
    ux2, uy2 = 55, 25

    # f(x) in Exercise 45: starts at 0, dips to local min in Q4, crosses at x=1.6, peaks in Q1 around x=2.3, crosses at x=3.0, dips slightly, approaches 0
    pts_f = []
    pts_F = []
    curr_F = 1.0
    dx = 0.04
    for step in range(0, 115):
        x = step * dx
        # f model: damped oscillating function
        y_f = -2.2 * math.sin(1.8 * x) * math.exp(-0.45 * x)
        pts_f.append(f"{ox1 + x * ux1:.1f},{oy1 - y_f * uy1:.1f}")
        pts_F.append(f"{ox2 + x * ux2:.1f},{oy2 - curr_F * uy2:.1f}")
        curr_F += y_f * dx

    content = f'''
    <!-- Left: f(x) -->
    <rect x="15" y="15" width="280" height="210" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="155" y="35" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Given Function y = f(x)</text>

    <line x1="{ox1 - 10}" y1="{oy1}" x2="{ox1 + 235}" y2="{oy1}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <line x1="{ox1}" y1="{oy1 + 65}" x2="{ox1}" y2="{oy1 - 70}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <text x="{ox1 + 240}" y="{oy1 + 14}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox1 - 12}" y="{oy1 - 65}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox1 - 10}" y="{oy1 + 14}" {FONT} font-size="10">0</text>

    <!-- Ticks -->
    <line x1="{ox1 + ux1}" y1="{oy1 - 3}" x2="{ox1 + ux1}" y2="{oy1 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 + ux1 - 3}" y="{oy1 + 14}" {FONT} font-size="10">1</text>
    
    <polyline points="{" ".join(pts_f)}" fill="none" stroke="#0284c7" stroke-width="2.2" />
    <text x="{ox1 + 2.5*ux1}" y="{oy1 - 1.1*uy1}" {FONT} font-size="11.5" font-weight="bold" fill="#0284c7">y = f(x)</text>

    <!-- Right: Sketched F(x) with F(0) = 1 -->
    <rect x="315" y="15" width="290" height="210" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="460" y="35" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Sketched Antiderivative F(x), F(0) = 1</text>

    <line x1="{ox2 - 10}" y1="{oy2}" x2="{ox2 + 235}" y2="{oy2}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <line x1="{ox2}" y1="{oy2 + 25}" x2="{ox2}" y2="{oy2 - 120}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <text x="{ox2 + 240}" y="{oy2 + 14}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox2 - 12}" y="{oy2 - 115}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox2 - 10}" y="{oy2 + 14}" {FONT} font-size="10">0</text>

    <!-- Initial point (0, 1) -->
    <circle cx="{ox2}" cy="{oy2 - 1.0 * uy2}" r="3.5" fill="#db2777" />
    <text x="{ox2 - 12}" y="{oy2 - 1.0 * uy2 + 4}" {FONT} font-size="10" font-weight="bold" fill="#db2777">1</text>

    <polyline points="{" ".join(pts_F)}" fill="none" stroke="#db2777" stroke-width="2.2" />
    <text x="{ox2 + 2.8*ux2}" y="{oy2 - 2.8*uy2}" {FONT} font-size="11.5" font-weight="bold" fill="#db2777">y = F(x)</text>

    <text x="460" y="205" {FONT} font-size="10" fill="#64748b" text-anchor="middle">Inflections align with extrema of f; extrema align with zeros of f</text>
    '''
    return svg_wrapper(w, h, content)

# -------------------------------------------------------------------
# 11. Section 3.9 Exercise 46: Velocity Function and Position Function
# -------------------------------------------------------------------
def make_sec3_9_ex46():
    w, h = 620, 240
    
    ox1, oy1 = 45, 170
    ux1, uy1 = 40, 70
    
    ox2, oy2 = 345, 170
    ux2, uy2 = 40, 25

    # v(t): starts at 0, ramps up to plateau (constant v), ramps down, goes negative, returns to 0
    # s(t): integral of v(t)
    pts_v = []
    pts_s = []
    curr_s = 0.5
    dt = 0.04
    for step in range(0, 140):
        t = step * dt
        # piecewise / smooth approximation of velocity profile:
        if t < 1.0:
            v_val = 0.9 * (1.0 - math.cos(math.pi * t)) / 2.0
        elif t < 2.0:
            v_val = 0.9
        elif t < 3.2:
            v_val = 0.9 * math.cos(math.pi * (t - 2.0) / 1.2)
        elif t < 4.4:
            v_val = -0.35 * math.sin(math.pi * (t - 3.2) / 1.2)
        else:
            v_val = 0.0
            
        pts_v.append(f"{ox1 + t * ux1:.1f},{oy1 - v_val * uy1:.1f}")
        pts_s.append(f"{ox2 + t * ux2:.1f},{oy2 - curr_s * uy2:.1f}")
        curr_s += v_val * dt

    content = f'''
    <!-- Left: Velocity v(t) -->
    <rect x="15" y="15" width="280" height="210" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="155" y="35" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Velocity Profile v(t)</text>

    <line x1="{ox1 - 10}" y1="{oy1}" x2="{ox1 + 235}" y2="{oy1}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <line x1="{ox1}" y1="{oy1 + 35}" x2="{ox1}" y2="{oy1 - 95}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <text x="{ox1 + 240}" y="{oy1 + 14}" {FONT} font-size="11" font-style="italic">t</text>
    <text x="{ox1 - 12}" y="{oy1 - 90}" {FONT} font-size="11" font-style="italic">v</text>
    <text x="{ox1 - 10}" y="{oy1 + 14}" {FONT} font-size="10">0</text>

    <polyline points="{" ".join(pts_v)}" fill="none" stroke="#0284c7" stroke-width="2.3" />
    <text x="{ox1 + 1.5*ux1}" y="{oy1 - 1.05*uy1}" {FONT} font-size="11" font-weight="bold" fill="#0369a1">Steady velocity (plateau)</text>

    <!-- Right: Position s(t) -->
    <rect x="315" y="15" width="290" height="210" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="460" y="35" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Position Function s(t)</text>

    <line x1="{ox2 - 10}" y1="{oy2}" x2="{ox2 + 235}" y2="{oy2}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <line x1="{ox2}" y1="{oy2 + 20}" x2="{ox2}" y2="{oy2 - 125}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <text x="{ox2 + 240}" y="{oy2 + 14}" {FONT} font-size="11" font-style="italic">t</text>
    <text x="{ox2 - 12}" y="{oy2 - 120}" {FONT} font-size="11" font-style="italic">s</text>
    <text x="{ox2 - 10}" y="{oy2 + 14}" {FONT} font-size="10">0</text>

    <polyline points="{" ".join(pts_s)}" fill="none" stroke="#16a34a" stroke-width="2.3" />
    <text x="{ox2 + 3.0*ux2}" y="{oy2 - 3.8*uy2}" {FONT} font-size="11.5" font-weight="bold" fill="#16a34a">s(t)</text>
    <text x="{ox2 + 1.1*ux2}" y="{oy2 - 2.0*uy2}" {FONT} font-size="10.5" fill="#15803d" font-weight="600">Linear segment (constant slope)</text>

    <text x="460" y="205" {FONT} font-size="10" fill="#64748b" text-anchor="middle">s(t) peaks where v = 0; decreases when v &lt; 0</text>
    '''
    return svg_wrapper(w, h, content)

# -------------------------------------------------------------------
# 12. Section 3.9 Exercise 47: Step Derivative f'(x) and Continuous f(x)
# -------------------------------------------------------------------
def make_sec3_9_ex47():
    w, h = 620, 260
    
    ox1, oy1 = 55, 170
    ux1, uy1 = 60, 45
    
    ox2, oy2 = 355, 170
    ux2, uy2 = 60, 45

    content = f'''
    <!-- Left: Step derivative f'(x) -->
    <rect x="15" y="15" width="280" height="230" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="155" y="35" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Given Derivative y = f'(x)</text>

    <!-- Axes Left -->
    <line x1="{ox1 - 15}" y1="{oy1}" x2="{ox1 + 215}" y2="{oy1}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <line x1="{ox1}" y1="{oy1 + 45}" x2="{ox1}" y2="{oy1 - 120}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <text x="{ox1 + 220}" y="{oy1 + 14}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox1 - 12}" y="{oy1 - 115}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox1 - 10}" y="{oy1 + 14}" {FONT} font-size="10">0</text>

    <!-- Ticks Left -->
    <line x1="{ox1 + ux1}" y1="{oy1 - 3}" x2="{ox1 + ux1}" y2="{oy1 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 + ux1 - 3}" y="{oy1 + 14}" {FONT} font-size="10">1</text>
    <line x1="{ox1 + 2*ux1}" y1="{oy1 - 3}" x2="{ox1 + 2*ux1}" y2="{oy1 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 + 2*ux1 - 3}" y="{oy1 + 14}" {FONT} font-size="10">2</text>
    <line x1="{ox1 + 3*ux1}" y1="{oy1 - 3}" x2="{ox1 + 3*ux1}" y2="{oy1 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 + 3*ux1 - 3}" y="{oy1 + 14}" {FONT} font-size="10">3</text>

    <line x1="{ox1 - 3}" y1="{oy1 - uy1}" x2="{ox1 + 3}" y2="{oy1 - uy1}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 - 15}" y="{oy1 - uy1 + 4}" {FONT} font-size="10">1</text>
    <line x1="{ox1 - 3}" y1="{oy1 - 2*uy1}" x2="{ox1 + 3}" y2="{oy1 - 2*uy1}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 - 15}" y="{oy1 - 2*uy1 + 4}" {FONT} font-size="10">2</text>
    <line x1="{ox1 - 3}" y1="{oy1 + uy1}" x2="{ox1 + 3}" y2="{oy1 + uy1}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 - 18}" y="{oy1 + uy1 + 4}" {FONT} font-size="10">−1</text>

    <!-- Segments of f'(x) -->
    <!-- Segment 1: y = 2 for [0, 1) -->
    <line x1="{ox1}" y1="{oy1 - 2*uy1}" x2="{ox1 + ux1}" y2="{oy1 - 2*uy1}" stroke="#db2777" stroke-width="2.5" />
    <circle cx="{ox1}" cy="{oy1 - 2*uy1}" r="3.2" fill="#db2777" />
    <circle cx="{ox1 + ux1}" cy="{oy1 - 2*uy1}" r="3.2" fill="#ffffff" stroke="#db2777" stroke-width="1.8" />

    <!-- Segment 2: y = 1 for (1, 2) -->
    <line x1="{ox1 + ux1}" y1="{oy1 - uy1}" x2="{ox1 + 2*ux1}" y2="{oy1 - uy1}" stroke="#db2777" stroke-width="2.5" />
    <circle cx="{ox1 + ux1}" cy="{oy1 - uy1}" r="3.2" fill="#ffffff" stroke="#db2777" stroke-width="1.8" />
    <circle cx="{ox1 + 2*ux1}" cy="{oy1 - uy1}" r="3.2" fill="#ffffff" stroke="#db2777" stroke-width="1.8" />

    <!-- Segment 3: y = -1 for (2, 3] -->
    <line x1="{ox1 + 2*ux1}" y1="{oy1 + uy1}" x2="{ox1 + 3*ux1}" y2="{oy1 + uy1}" stroke="#db2777" stroke-width="2.5" />
    <circle cx="{ox1 + 2*ux1}" cy="{oy1 + uy1}" r="3.2" fill="#ffffff" stroke="#db2777" stroke-width="1.8" />
    <circle cx="{ox1 + 3*ux1}" cy="{oy1 + uy1}" r="3.2" fill="#db2777" />

    <text x="{ox1 + 1.8*ux1}" y="{oy1 - 1.6*uy1}" {FONT} font-size="11.5" font-weight="bold" fill="#db2777">y = f'(x)</text>

    <!-- Right: Continuous Antiderivative f(x) with f(0) = -1 -->
    <rect x="315" y="15" width="290" height="230" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="460" y="35" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Continuous Antiderivative f(x)</text>

    <!-- Axes Right -->
    <line x1="{ox2 - 15}" y1="{oy2}" x2="{ox2 + 225}" y2="{oy2}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <line x1="{ox2}" y1="{oy2 + 45}" x2="{ox2}" y2="{oy2 - 120}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <text x="{ox2 + 230}" y="{oy2 + 14}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox2 - 12}" y="{oy2 - 115}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox2 - 10}" y="{oy2 + 14}" {FONT} font-size="10">0</text>

    <!-- Ticks Right -->
    <line x1="{ox2 + ux2}" y1="{oy2 - 3}" x2="{ox2 + ux2}" y2="{oy2 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox2 + ux2 - 3}" y="{oy2 + 14}" {FONT} font-size="10">1</text>
    <line x1="{ox2 + 2*ux2}" y1="{oy2 - 3}" x2="{ox2 + 2*ux2}" y2="{oy2 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox2 + 2*ux2 - 3}" y="{oy2 + 14}" {FONT} font-size="10">2</text>
    <line x1="{ox2 + 3*ux2}" y1="{oy2 - 3}" x2="{ox2 + 3*ux2}" y2="{oy2 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox2 + 3*ux2 - 3}" y="{oy2 + 14}" {FONT} font-size="10">3</text>

    <line x1="{ox2 - 3}" y1="{oy2 - uy2}" x2="{ox2 + 3}" y2="{oy2 - uy2}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox2 - 15}" y="{oy2 - uy2 + 4}" {FONT} font-size="10">1</text>
    <line x1="{ox2 - 3}" y1="{oy2 - 2*uy2}" x2="{ox2 + 3}" y2="{oy2 - 2*uy2}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox2 - 15}" y="{oy2 - 2*uy2 + 4}" {FONT} font-size="10">2</text>
    <line x1="{ox2 - 3}" y1="{oy2 + uy2}" x2="{ox2 + 3}" y2="{oy2 + uy2}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox2 - 18}" y="{oy2 + uy2 + 4}" {FONT} font-size="10">−1</text>

    <!-- Continuous path: (0, -1) -> (1, 1) -> (2, 2) -> (3, 1) -->
    <polyline points="{ox2},{oy2 + uy2} {ox2 + ux2},{oy2 - uy2} {ox2 + 2*ux2},{oy2 - 2*uy2} {ox2 + 3*ux2},{oy2 - uy2}" fill="none" stroke="#0284c7" stroke-width="2.5" stroke-linejoin="round" />
    
    <circle cx="{ox2}" cy="{oy2 + uy2}" r="3.5" fill="#0284c7" />
    <text x="{ox2 + 6}" y="{oy2 + uy2 + 12}" {FONT} font-size="9.5" font-weight="600" fill="#0369a1">(0, −1)</text>

    <circle cx="{ox2 + ux2}" cy="{oy2 - uy2}" r="3.5" fill="#0284c7" />
    <text x="{ox2 + ux2 + 5}" y="{oy2 - uy2 - 4}" {FONT} font-size="9.5" font-weight="600" fill="#0369a1">(1, 1)</text>

    <circle cx="{ox2 + 2*ux2}" cy="{oy2 - 2*uy2}" r="3.5" fill="#0284c7" />
    <text x="{ox2 + 2*ux2}" y="{oy2 - 2*uy2 - 8}" {FONT} font-size="9.5" font-weight="600" fill="#0369a1" text-anchor="middle">(2, 2)</text>

    <circle cx="{ox2 + 3*ux2}" cy="{oy2 - uy2}" r="3.5" fill="#0284c7" />
    <text x="{ox2 + 3*ux2 + 6}" y="{oy2 - uy2 + 4}" {FONT} font-size="9.5" font-weight="600" fill="#0369a1">(3, 1)</text>

    <!-- Slopes on segments -->
    <text x="{ox2 + 0.45*ux2}" y="{oy2 - 0.1*uy2}" {FONT} font-size="10" font-weight="bold" fill="#0284c7">m = 2</text>
    <text x="{ox2 + 1.4*ux2}" y="{oy2 - 1.7*uy2}" {FONT} font-size="10" font-weight="bold" fill="#0284c7">m = 1</text>
    <text x="{ox2 + 2.55*ux2}" y="{oy2 - 1.7*uy2}" {FONT} font-size="10" font-weight="bold" fill="#0284c7">m = −1</text>
    '''
    return svg_wrapper(w, h, content)

# -------------------------------------------------------------------
# 13. Section 3.9 Exercise 48: f(x) = 2x - 3√x and F(x) = x² - 2x^(3/2) + 1
# -------------------------------------------------------------------
def make_sec3_9_ex48():
    w, h = 620, 260
    
    ox1, oy1 = 50, 150
    ux1, uy1 = 55, 45
    
    ox2, oy2 = 350, 150
    ux2, uy2 = 55, 35

    # f(x) = 2x - 3*sqrt(x) on [0, 4]
    # min at x = 9/16 = 0.5625, f = -1.125
    # root at x = 9/4 = 2.25
    # f(4) = 8 - 6 = 2
    pts_f = []
    for step in range(0, 85):
        x = step * 0.05
        y = 2 * x - 3 * math.sqrt(x)
        pts_f.append(f"{ox1 + x * ux1:.1f},{oy1 - y * uy1:.1f}")

    # F(x) = x^2 - 2 * x^(1.5) + 1 on [0, 4]
    # F(0) = 1
    # IP at x = 0.5625
    # min at x = 2.25, F = -0.6875
    # F(4) = 16 - 16 + 1 = 1
    pts_F = []
    for step in range(0, 85):
        x = step * 0.05
        y = x**2 - 2 * (x**1.5) + 1
        pts_F.append(f"{ox2 + x * ux2:.1f},{oy2 - y * uy2:.1f}")

    content = f'''
    <!-- Left: f(x) = 2x - 3√x -->
    <rect x="15" y="15" width="280" height="230" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="155" y="35" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">f(x) = 2x − 3√x</text>

    <!-- Axes Left -->
    <line x1="{ox1 - 10}" y1="{oy1}" x2="{ox1 + 230}" y2="{oy1}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <line x1="{ox1}" y1="{oy1 + 65}" x2="{ox1}" y2="{oy1 - 110}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <text x="{ox1 + 235}" y="{oy1 + 14}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox1 - 12}" y="{oy1 - 105}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox1 - 10}" y="{oy1 + 14}" {FONT} font-size="10">0</text>

    <!-- Ticks Left -->
    <line x1="{ox1 + ux1}" y1="{oy1 - 3}" x2="{ox1 + ux1}" y2="{oy1 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 + ux1 - 3}" y="{oy1 + 14}" {FONT} font-size="10">1</text>
    <line x1="{ox1 + 2*ux1}" y1="{oy1 - 3}" x2="{ox1 + 2*ux1}" y2="{oy1 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 + 2*ux1 - 3}" y="{oy1 + 14}" {FONT} font-size="10">2</text>
    <line x1="{ox1 + 3*ux1}" y1="{oy1 - 3}" x2="{ox1 + 3*ux1}" y2="{oy1 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 + 3*ux1 - 3}" y="{oy1 + 14}" {FONT} font-size="10">3</text>
    <line x1="{ox1 + 4*ux1}" y1="{oy1 - 3}" x2="{ox1 + 4*ux1}" y2="{oy1 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox1 + 4*ux1 - 3}" y="{oy1 + 14}" {FONT} font-size="10">4</text>

    <polyline points="{" ".join(pts_f)}" fill="none" stroke="#0284c7" stroke-width="2.3" />
    <circle cx="{ox1 + 2.25*ux1}" cy="{oy1}" r="3.2" fill="#0284c7" />
    <text x="{ox1 + 2.25*ux1}" y="{oy1 + 15}" {FONT} font-size="9.5" fill="#0369a1" font-weight="bold" text-anchor="middle">2.25 (Zero)</text>

    <circle cx="{ox1 + 0.5625*ux1}" cy="{oy1 + 1.125*uy1}" r="3.2" fill="#0284c7" />
    <text x="{ox1 + 0.5625*ux1}" y="{oy1 + 1.125*uy1 + 14}" {FONT} font-size="9.5" fill="#0369a1" font-weight="bold" text-anchor="middle">Min (0.56, −1.13)</text>

    <!-- Right: F(x) = x² - 2x^(3/2) + 1 -->
    <rect x="315" y="15" width="290" height="230" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="460" y="35" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">F(x) = x² − 2x^(3/2) + 1</text>

    <!-- Axes Right -->
    <line x1="{ox2 - 10}" y1="{oy2}" x2="{ox2 + 230}" y2="{oy2}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <line x1="{ox2}" y1="{oy2 + 45}" x2="{ox2}" y2="{oy2 - 110}" stroke="#1e293b" stroke-width="1.3" marker-end="url(#arrow)" />
    <text x="{ox2 + 235}" y="{oy2 + 14}" {FONT} font-size="11" font-style="italic">x</text>
    <text x="{ox2 - 12}" y="{oy2 - 105}" {FONT} font-size="11" font-style="italic">y</text>
    <text x="{ox2 - 10}" y="{oy2 + 14}" {FONT} font-size="10">0</text>

    <!-- Ticks Right -->
    <line x1="{ox2 + ux2}" y1="{oy2 - 3}" x2="{ox2 + ux2}" y2="{oy2 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox2 + ux2 - 3}" y="{oy2 + 14}" {FONT} font-size="10">1</text>
    <line x1="{ox2 + 2*ux2}" y1="{oy2 - 3}" x2="{ox2 + 2*ux2}" y2="{oy2 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox2 + 2*ux2 - 3}" y="{oy2 + 14}" {FONT} font-size="10">2</text>
    <line x1="{ox2 + 3*ux2}" y1="{oy2 - 3}" x2="{ox2 + 3*ux2}" y2="{oy2 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox2 + 3*ux2 - 3}" y="{oy2 + 14}" {FONT} font-size="10">3</text>
    <line x1="{ox2 + 4*ux2}" y1="{oy2 - 3}" x2="{ox2 + 4*ux2}" y2="{oy2 + 3}" stroke="#1e293b" stroke-width="1" />
    <text x="{ox2 + 4*ux2 - 3}" y="{oy2 + 14}" {FONT} font-size="10">4</text>

    <!-- Start point (0, 1) -->
    <circle cx="{ox2}" cy="{oy2 - uy2}" r="3.5" fill="#db2777" />
    <text x="{ox2 - 12}" y="{oy2 - uy2 + 4}" {FONT} font-size="10" font-weight="bold" fill="#db2777">1</text>

    <polyline points="{" ".join(pts_F)}" fill="none" stroke="#db2777" stroke-width="2.3" />

    <!-- Min at x = 2.25 -->
    <circle cx="{ox2 + 2.25*ux2}" cy="{oy2 + 0.6875*uy2}" r="3.2" fill="#db2777" />
    <text x="{ox2 + 2.25*ux2}" y="{oy2 + 0.6875*uy2 + 14}" {FONT} font-size="9.5" fill="#9d174d" font-weight="bold" text-anchor="middle">Min at x = 2.25</text>

    <!-- Inflection at x = 0.56 -->
    <circle cx="{ox2 + 0.5625*ux2}" cy="{oy2 - 0.13*uy2}" r="2.8" fill="#db2777" />
    <text x="{ox2 + 0.5625*ux2 + 8}" y="{oy2 - 0.2*uy2}" {FONT} font-size="9" fill="#9d174d">IP (0.56)</text>
    '''
    return svg_wrapper(w, h, content)

def main():
    figs = {
        "sec3_7_fig1_fencing_cases.svg": make_sec3_7_fig1(),
        "sec3_7_fig2_fencing_general.svg": make_sec3_7_fig2(),
        "sec3_7_ex11_four_pens.svg": make_sec3_7_ex11(),
        "sec3_7_ex35_wire_shapes.svg": make_sec3_7_ex35(),
        "sec3_7_ex56_tangent_triangle.svg": make_sec3_7_ex56(),
        "sec3_9_fig1_antiderivatives_family.svg": make_sec3_9_fig1(),
        "sec3_9_fig2_sketch_antiderivative.svg": make_sec3_9_fig2(),
        "sec3_9_ex43_antiderivative_matching.svg": make_sec3_9_ex43(),
        "sec3_9_ex44_antiderivative_matching.svg": make_sec3_9_ex44(),
        "sec3_9_ex45_antiderivative_sketch.svg": make_sec3_9_ex45(),
        "sec3_9_ex46_velocity_position.svg": make_sec3_9_ex46(),
        "sec3_9_ex47_step_derivative.svg": make_sec3_9_ex47(),
        "sec3_9_ex48_graph_comparison.svg": make_sec3_9_ex48(),
    }
    for filename, content in figs.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()
