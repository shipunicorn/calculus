import os
import math

OUTPUT_DIR = r"C:\dev\calculus\handouts\006-applied-optimization-and-economic-models\figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT = 'font-family="Aptos, sans-serif"'
MONO = 'font-family="\'Cascadia Mono\', monospace"'

def svg_wrapper(width, height, title, desc, content):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" style="background-color: #ffffff; display: block; margin: 0 auto;">
<title>{title}</title>
<desc>{desc}</desc>
<rect width="{width}" height="{height}" fill="#ffffff" />
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

def make_sec3_7_fig1():
    w, h = 640, 210
    title = "Three Fencing Configurations Along a Straight River"
    desc = "Comparison of shallow, intermediate, and deep rectangular fencing layouts along a river for 2400 feet of fencing."
    content = f'''
    <!-- Panel 1: Shallow and Wide (100 x 2200) -->
    <rect x="15" y="15" width="190" height="185" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
    <path d="M 15 145 C 40 142, 60 148, 85 145 C 110 142, 130 148, 155 145 C 175 142, 195 148, 205 145 L 205 200 L 15 200 Z" fill="#bae6fd" />
    <path d="M 15 145 C 40 142, 60 148, 85 145 C 110 142, 130 148, 155 145 C 175 142, 195 148, 205 145" fill="none" stroke="#0284c7" stroke-width="1.8" />
    <text x="110" y="180" {FONT} font-size="11" fill="#0369a1" font-weight="600" text-anchor="middle">Straight River</text>
    
    <!-- Field 1 -->
    <rect x="40" y="125" width="140" height="20" fill="#dcfce7" fill-opacity="0.6" stroke="none" />
    <polyline points="40,145 40,125 180,125 180,145" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-linejoin="round" />
    <text x="110" y="118" {FONT} font-size="11" fill="#1e293b" text-anchor="middle">2200</text>
    <text x="36" y="138" {FONT} font-size="11" fill="#1e293b" text-anchor="end">100</text>
    <text x="184" y="138" {FONT} font-size="11" fill="#1e293b" text-anchor="start">100</text>
    <text x="110" y="32" {FONT} font-size="11" font-weight="bold" fill="#64748b" text-anchor="middle">Case 1: Shallow &amp; Wide</text>
    <text x="110" y="55" {FONT} font-size="11.5" font-weight="600" fill="#1e293b" text-anchor="middle">Area = 100 · 2200</text>
    <text x="110" y="73" {FONT} font-size="12" font-weight="bold" fill="#0f766e" text-anchor="middle">= 220,000 ft²</text>

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
    <text x="320" y="30" {FONT} font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">Case 2: Intermediate</text>
    <text x="320" y="48" {FONT} font-size="11.5" font-weight="600" fill="#1e293b" text-anchor="middle">Area = 700 · 1000</text>
    <text x="320" y="66" {FONT} font-size="12" font-weight="bold" fill="#0f766e" text-anchor="middle">= 700,000 ft²</text>

    <!-- Panel 3: Deep and Narrow (1000 x 400) -->
    <rect x="435" y="15" width="190" height="185" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
    <path d="M 435 145 C 460 142, 480 148, 505 145 C 530 142, 550 148, 575 145 C 595 142, 615 148, 625 145 L 625 200 L 435 200 Z" fill="#bae6fd" />
    <path d="M 435 145 C 460 142, 480 148, 505 145 C 530 142, 550 148, 575 145 C 595 142, 615 148, 625 145" fill="none" stroke="#0284c7" stroke-width="1.8" />
    <text x="530" y="180" {FONT} font-size="11" fill="#0369a1" font-weight="600" text-anchor="middle">Straight River</text>

    <!-- Field 3 -->
    <rect x="505" y="75" width="50" height="70" fill="#dcfce7" fill-opacity="0.6" stroke="none" />
    <polyline points="505,145 505,75 555,75 555,145" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-linejoin="round" />
    <text x="530" y="68" {FONT} font-size="11" fill="#1e293b" text-anchor="middle">400</text>
    <text x="497" y="110" {FONT} font-size="11" fill="#1e293b" text-anchor="end">1000</text>
    <text x="563" y="110" {FONT} font-size="11" fill="#1e293b" text-anchor="start">1000</text>
    <text x="530" y="26" {FONT} font-size="11" font-weight="bold" fill="#64748b" text-anchor="middle">Case 3: Deep &amp; Narrow</text>
    <text x="530" y="42" {FONT} font-size="11.5" font-weight="600" fill="#1e293b" text-anchor="middle">Area = 1000 · 400</text>
    <text x="530" y="58" {FONT} font-size="12" font-weight="bold" fill="#0f766e" text-anchor="middle">= 400,000 ft²</text>
    '''
    return svg_wrapper(w, h, title, desc, content)

def make_sec3_7_fig2():
    w, h = 380, 220
    title = "General Rectangular River Fencing Model"
    desc = "Rectangular field of depth x and width y along a river requiring no fencing on one side."
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
    return svg_wrapper(w, h, title, desc, content)

def make_sec3_7_ex11():
    w, h = 620, 220
    title = "Four-Pen Fencing Configurations and Model"
    desc = "Exploration of rectangular pasture divided into four pens by internal fences with total perimeter 750 feet."
    content = f'''
    <!-- Left Panel: Sample Explorations -->
    <rect x="15" y="15" width="265" height="190" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="147" y="36" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Part (a): Sample Configurations</text>
    
    <!-- Shallow / Wide: x = 50, y = 250 => 5(50)+2(250)=750, Area = 12,500 -->
    <text x="147" y="54" {FONT} font-size="10.5" fill="#047857" font-weight="600" text-anchor="middle">Shallow (x = 50, y = 250): Area = 12,500 ft²</text>
    <rect x="35" y="60" width="225" height="24" fill="#ecfdf5" stroke="#dc2626" stroke-width="1.8" />
    <line x1="91" y1="60" x2="91" y2="84" stroke="#dc2626" stroke-width="1.5" />
    <line x1="147" y1="60" x2="147" y2="84" stroke="#dc2626" stroke-width="1.5" />
    <line x1="203" y1="60" x2="203" y2="84" stroke="#dc2626" stroke-width="1.5" />

    <!-- Deep / Narrow: x = 100, y = 125 => 5(100)+2(125)=750, Area = 12,500 -->
    <text x="147" y="106" {FONT} font-size="10.5" fill="#047857" font-weight="600" text-anchor="middle">Deep (x = 100, y = 125): Area = 12,500 ft²</text>
    <rect x="80" y="112" width="135" height="48" fill="#ecfdf5" stroke="#dc2626" stroke-width="1.8" />
    <line x1="114" y1="112" x2="114" y2="160" stroke="#dc2626" stroke-width="1.5" />
    <line x1="147" y1="112" x2="147" y2="160" stroke="#dc2626" stroke-width="1.5" />
    <line x1="181" y1="112" x2="181" y2="160" stroke="#dc2626" stroke-width="1.5" />

    <text x="147" y="190" {FONT} font-size="11" fill="#64748b" text-anchor="middle">Estimate: Max area ≥ 12,500 ft²</text>

    <!-- Right Panel: General 4-Pen Model -->
    <rect x="290" y="15" width="320" height="190" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
    <text x="450" y="36" {FONT} font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Part (b): General Four-Pen Model</text>

    <!-- Outer rectangle -->
    <rect x="330" y="65" width="240" height="75" fill="#f0fdf4" stroke="#dc2626" stroke-width="2.5" />
    <!-- 3 Internal Dividers -->
    <line x1="390" y1="65" x2="390" y2="140" stroke="#dc2626" stroke-width="2.2" />
    <line x1="450" y1="65" x2="450" y2="140" stroke="#dc2626" stroke-width="2.2" />
    <line x1="510" y1="65" x2="510" y2="140" stroke="#dc2626" stroke-width="2.2" />

    <!-- Pen labels -->
    <text x="360" y="106" {FONT} font-size="11" fill="#15803d" font-weight="600" text-anchor="middle">Pen 1</text>
    <text x="420" y="106" {FONT} font-size="11" fill="#15803d" font-weight="600" text-anchor="middle">Pen 2</text>
    <text x="480" y="106" {FONT} font-size="11" fill="#15803d" font-weight="600" text-anchor="middle">Pen 3</text>
    <text x="540" y="106" {FONT} font-size="11" fill="#15803d" font-weight="600" text-anchor="middle">Pen 4</text>

    <!-- Dimension annotations -->
    <text x="450" y="56" {FONT} font-size="12" font-style="italic" font-weight="bold" fill="#1e293b" text-anchor="middle">y (width)</text>
    <text x="318" y="106" {FONT} font-size="12" font-style="italic" font-weight="bold" fill="#1e293b" text-anchor="end">x</text>
    
    <text x="450" y="165" {FONT} font-size="11" fill="#1e293b" text-anchor="middle">Constraint: 5x + 2y = 750 ⇒ y = 375 − 2.5x</text>
    <text x="450" y="188" {FONT} font-size="10.5" font-weight="bold" fill="#0284c7" text-anchor="middle">Max Area at x = 75 ft, y = 187.5 ft: A = 14,062.5 ft²</text>
    '''
    return svg_wrapper(w, h, title, desc, content)

def make_sec3_7_ex35():
    w, h = 580, 220
    title = "Wire Cut into Square and Equilateral Triangle"
    desc = "A 10 meter wire cut into length x for a square and 10 minus x for an equilateral triangle."
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
    <rect x="25" y="98" width="255" height="110" rx="6" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1" />
    <rect x="65" y="120" width="55" height="55" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5" />
    <text x="92" y="114" {FONT} font-size="11" font-style="italic" fill="#0284c7" text-anchor="middle">x / 4</text>
    <text x="35" y="152" {FONT} font-size="11" font-style="italic" fill="#0284c7" text-anchor="start">x / 4</text>
    <text x="195" y="135" {FONT} font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">Square</text>
    <text x="195" y="155" {FONT} font-size="11" fill="#1e293b" text-anchor="middle">Perimeter = x</text>
    <text x="195" y="175" {FONT} font-size="11.5" font-weight="600" fill="#0f766e" text-anchor="middle">Area = x² / 16</text>

    <!-- Bottom Right: Equilateral Triangle -->
    <rect x="295" y="98" width="265" height="110" rx="6" fill="#fff7ed" stroke="#fed7aa" stroke-width="1" />
    <polygon points="330,175 390,175 360,123" fill="ffedd5" stroke="#ea580c" stroke-width="2.5" />
    <text x="360" y="192" {FONT} font-size="11" font-style="italic" fill="#ea580c" text-anchor="middle">(10 − x) / 3</text>
    <text x="470" y="135" {FONT} font-size="12" font-weight="bold" fill="#c2410c" text-anchor="middle">Equilateral Δ</text>
    <text x="470" y="155" {FONT} font-size="11" fill="#1e293b" text-anchor="middle">Perimeter = 10 − x</text>
    <text x="470" y="175" {FONT} font-size="11" font-weight="600" fill="#0f766e" text-anchor="middle">Area = √3/36 · (10 − x)²</text>
    '''
    return svg_wrapper(w, h, title, desc, content)

def make_sec3_7_ex56():
    w, h = 460, 250
    title = "Tangent Hypotenuse to Parabola in First Quadrant"
    desc = "Right triangle in the first quadrant whose hypotenuse is tangent to y equals 4 minus x squared."
    ox, oy = 60, 195
    ux, uy = 95, 28
    
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
    <line x1="{ox - 20}" y1="{oy}" x2="{ox + 330}" y2="{oy}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />
    <line x1="{ox}" y1="{oy + 20}" x2="{ox}" y2="{oy - 170}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)" />

    <!-- Ticks -->
    <line x1="{ox + ux}" y1="{oy - 3}" x2="{ox + ux}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />
    <line x1="{ox + 2*ux}" y1="{oy - 3}" x2="{ox + 2*ux}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />
    <line x1="{ox - 3}" y1="{oy - 4*uy}" x2="{ox + 3}" y2="{oy - 4*uy}" stroke="#1e293b" stroke-width="1.2" />

    <!-- Parabola y = 4 - x^2 -->
    <polyline points="{poly_parabola}" fill="none" stroke="#0284c7" stroke-width="2.2" />

    <!-- Tangent Hypotenuse line -->
    <line x1="{ox}" y1="{y_int_py:.1f}" x2="{x_int_px:.1f}" y2="{oy}" stroke="#db2777" stroke-width="2.2" />

    <!-- Markers -->
    <circle cx="{pt_tan_x:.1f}" cy="{pt_tan_y:.1f}" r="4" fill="#db2777" />
    <circle cx="{ox}" cy="{y_int_py:.1f}" r="3" fill="#db2777" />
    <circle cx="{x_int_px:.1f}" cy="{oy}" r="3" fill="#db2777" />

    <!-- Axis text labels -->
    <text x="{ox + 335}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>
    <text x="{ox - 15}" y="{oy - 165}" {FONT} font-size="12" font-style="italic">y</text>
    <text x="{ox - 12}" y="{oy + 15}" {FONT} font-size="11">0</text>
    <text x="{ox + ux - 3}" y="{oy + 16}" {FONT} font-size="11">1</text>
    <text x="{ox + 2*ux - 3}" y="{oy + 16}" {FONT} font-size="11">2</text>
    <text x="{ox - 15}" y="{oy - 4*uy + 4}" {FONT} font-size="11">4</text>

    <!-- Parabola label placed safely inside the region -->
    <rect x="75" y="132" width="76" height="18" fill="#ffffff" rx="3" />
    <text x="79" y="146" {FONT} font-size="12" font-weight="bold" fill="#0284c7">y = 4 − x²</text>

    <text x="{pt_tan_x + 8:.1f}" y="{pt_tan_y - 8:.1f}" {FONT} font-size="11" font-weight="600" fill="#db2777">P(a, 4 − a²)</text>
    <text x="{ox + 8}" y="{y_int_py + 4:.1f}" {FONT} font-size="10.5" font-weight="600" fill="#9d174d">(0, a² + 4)</text>
    <text x="{x_int_px:.1f}" y="{oy + 28}" {FONT} font-size="10.5" font-weight="600" fill="#9d174d" text-anchor="middle">((a² + 4)/(2a), 0)</text>

    <!-- Annotation badge -->
    <rect x="250" y="20" width="195" height="65" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
    <text x="260" y="38" {FONT} font-size="11" font-weight="bold" fill="#1e293b">Optimal Tangency:</text>
    <text x="260" y="55" {FONT} font-size="11" fill="#475569">a = 2/√3 ≈ 1.155</text>
    <text x="260" y="72" {FONT} font-size="11.5" font-weight="bold" fill="#be185d">Min Area = 32√3 / 9 ≈ 6.16</text>
    '''
    return svg_wrapper(w, h, title, desc, content)

for fn, name in [
    (make_sec3_7_fig1, "sec3_7_fig1_fencing_cases.svg"),
    (make_sec3_7_fig2, "sec3_7_fig2_fencing_general.svg"),
    (make_sec3_7_ex11, "sec3_7_ex11_four_pens.svg"),
    (make_sec3_7_ex35, "sec3_7_ex35_wire_shapes.svg"),
    (make_sec3_7_ex56, "sec3_7_ex56_tangent_triangle.svg"),
]:
    path = os.path.join(OUTPUT_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(fn())
    print("Wrote", path)
