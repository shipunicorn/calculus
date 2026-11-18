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
  <marker id="arrow-sky" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0284c7" />
  </marker>
  <marker id="arrow-pink" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#db2777" />
  </marker>
</defs>
{content}
</svg>'''

# -------------------------------------------------------------
# 1. Figure 1: The Area Problem - Region S under y = f(x)
# -------------------------------------------------------------
def make_fig1_area_under_curve():
    w, h = 480, 300
    ox, oy = 50, 240
    
    # Axes
    content = [
        f'<line x1="{ox - 20}" y1="{oy}" x2="{ox + 390}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="{oy + 20}" x2="{ox}" y2="{oy - 200}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="{ox + 395}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>',
        f'<text x="{ox - 16}" y="{oy - 195}" {FONT} font-size="12" font-style="italic">y</text>',
        f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>',
    ]
    
    xa, xb = ox + 70, ox + 320
    
    # Curve points for a continuous curve that dips and rises
    # S(x) from xa to xb
    pts = []
    num_steps = 50
    for i in range(num_steps + 1):
        t = i / num_steps
        x = xa + t * (xb - xa)
        # Smooth function: y starts high, dips, then rises slightly
        # normalized t in [0, 1]
        y_val = 150 - 60 * math.sin(math.pi * t * 0.9 + 0.3) + 30 * math.cos(2 * math.pi * t)
        y = oy - y_val
        pts.append((x, y))
        
    path_d = f"M {xa} {oy} L {pts[0][0]} {pts[0][1]} "
    for px, py in pts[1:]:
        path_d += f"L {px:.1f} {py:.1f} "
    path_d += f"L {xb} {oy} Z"
    
    # Shaded region S
    content.append(f'<path d="{path_d}" fill="#e0f2fe" stroke="none" />')
    
    # Curve
    curve_d = f"M {pts[0][0]} {pts[0][1]} "
    for px, py in pts[1:]:
        curve_d += f"L {px:.1f} {py:.1f} "
    content.append(f'<path d="{curve_d}" fill="none" stroke="#0284c7" stroke-width="2.2" />')
    
    # Vertical boundary lines
    content.append(f'<line x1="{xa}" y1="{oy}" x2="{pts[0][0]}" y2="{pts[0][1]}" stroke="#1e293b" stroke-width="1.2" />')
    content.append(f'<line x1="{xb}" y1="{oy}" x2="{pts[-1][0]}" y2="{pts[-1][1]}" stroke="#1e293b" stroke-width="1.2" />')
    
    # Labels
    content.append(f'<text x="{xa - 4}" y="{oy + 18}" {FONT} font-size="12" font-style="italic">a</text>')
    content.append(f'<text x="{xb - 4}" y="{oy + 18}" {FONT} font-size="12" font-style="italic">b</text>')
    content.append(f'<text x="{xa - 32}" y="{oy - 100}" {FONT} font-size="11" font-style="italic">x = a</text>')
    content.append(f'<text x="{xb + 8}" y="{oy - 70}" {FONT} font-size="11" font-style="italic">x = b</text>')
    content.append(f'<text x="{ox + 180}" y="{oy - 65}" {FONT} font-size="14" font-weight="bold" fill="#0369a1" font-style="italic">S</text>')
    content.append(f'<text x="{xb - 20}" y="{pts[-1][1] - 12}" {FONT} font-size="12" font-style="italic">y = f(x)</text>')
    
    return svg_wrapper(w, h, "\n".join(content))

# -------------------------------------------------------------
# 2. Figure 2: Straight-Sided Areas (Rectangle, Triangle, Polygon)
# -------------------------------------------------------------
def make_fig2_straight_sided_areas():
    w, h = 640, 180
    content = []
    
    # (a) Rectangle
    rx, ry, rw, rh = 40, 50, 130, 70
    content.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.6" />')
    content.append(f'<text x="{rx - 14}" y="{ry + rh/2 + 4}" {FONT} font-size="12" font-style="italic">w</text>')
    content.append(f'<text x="{rx + rw/2 - 2}" y="{ry + rh + 16}" {FONT} font-size="12" font-style="italic">l</text>')
    content.append(f'<text x="{rx + rw/2 - 16}" y="{ry + rh + 38}" {FONT} font-size="12" font-style="italic">A = lw</text>')
    
    # (b) Triangle
    tx, ty, tb, th = 230, 120, 130, 70
    t_pts = f"{tx},{ty} {tx + tb},{ty} {tx + 75},{ty - th}"
    content.append(f'<polygon points="{t_pts}" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.6" />')
    # Altitude dashed line
    content.append(f'<line x1="{tx + 75}" y1="{ty - th}" x2="{tx + 75}" y2="{ty}" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 3" />')
    # Right-angle mark
    content.append(f'<polyline points="{tx + 75},{ty - 8} {tx + 83},{ty - 8} {tx + 83},{ty}" fill="none" stroke="#64748b" stroke-width="1.0" />')
    content.append(f'<text x="{tx + 65}" y="{ty - th/2 + 4}" {FONT} font-size="12" font-style="italic">h</text>')
    content.append(f'<text x="{tx + tb/2 - 3}" y="{ty + 16}" {FONT} font-size="12" font-style="italic">b</text>')
    content.append(f'<text x="{tx + tb/2 - 20}" y="{ty + 38}" {FONT} font-size="12" font-style="italic">A = &#189;bh</text>')
    
    # (c) Polygon triangulated into 4 triangles
    px, py = 450, 45
    # Vertex coordinates of a 5-sided polygon with a central hub or triangulated from bottom vertex
    # In Stewart Figure 2: an irregular pentagon/hexagon divided from one vertex or interior point into A1, A2, A3, A4
    # Image 2 shows a polygon with bottom vertex (hub) connected to top vertices dividing into A1, A2, A3, A4
    hub = (px + 70, py + 75)
    v0 = (px + 10, py + 60)
    v1 = (px + 25, py + 15)
    v2 = (px + 70, py + 5)
    v3 = (px + 115, py + 15)
    v4 = (px + 135, py + 55)
    
    # Draw triangles
    tris = [
        (hub, v0, v1, "A&#8321;", px + 33, py + 52),
        (hub, v1, v2, "A&#8322;", px + 54, py + 34),
        (hub, v2, v3, "A&#8323;", px + 84, py + 34),
        (hub, v3, v4, "A&#8324;", px + 105, py + 52),
    ]
    for h_pt, p1, p2, lbl, lx, ly in tris:
        pts_str = f"{h_pt[0]},{h_pt[1]} {p1[0]},{p1[1]} {p2[0]},{p2[1]}"
        content.append(f'<polygon points="{pts_str}" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.4" />')
        content.append(f'<text x="{lx}" y="{ly}" {FONT} font-size="11" font-weight="bold" fill="#0369a1">{lbl}</text>')
        
    content.append(f'<text x="{px + 15}" y="{py + 113}" {FONT} font-size="12" font-style="italic">A = A&#8321; + A&#8322; + A&#8323; + A&#8324;</text>')
    
    return svg_wrapper(w, h, "\n".join(content))

# -------------------------------------------------------------
# 3. Figure 3: Parabola Region S (y = x^2 from 0 to 1)
# -------------------------------------------------------------
def make_fig3_parabola_region():
    w, h = 360, 280
    ox, oy = 60, 220
    scale = 180
    
    content = [
        f'<line x1="{ox - 20}" y1="{oy}" x2="{ox + scale + 50}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="{oy + 20}" x2="{ox}" y2="{oy - scale - 30}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="{ox + scale + 55}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>',
        f'<text x="{ox - 16}" y="{oy - scale - 25}" {FONT} font-size="12" font-style="italic">y</text>',
        f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>',
    ]
    
    # Tick at 1 on x-axis
    content.append(f'<line x1="{ox + scale}" y1="{oy - 3}" x2="{ox + scale}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />')
    content.append(f'<text x="{ox + scale - 3}" y="{oy + 18}" {FONT} font-size="11">1</text>')
    
    # Region S under y = x^2
    pts = []
    num_steps = 40
    for i in range(num_steps + 1):
        x_val = i / num_steps
        px = ox + x_val * scale
        py = oy - (x_val ** 2) * scale
        pts.append((px, py))
        
    path_d = f"M {ox} {oy} "
    for px, py in pts:
        path_d += f"L {px:.1f} {py:.1f} "
    path_d += f"L {ox + scale} {oy} Z"
    
    content.append(f'<path d="{path_d}" fill="#e0f2fe" stroke="none" />')
    
    # Extended parabola curve beyond 1
    ext_pts = []
    for i in range(num_steps + 6):
        x_val = (i / num_steps) * 1.12
        px = ox + x_val * scale
        py = oy - (x_val ** 2) * scale
        ext_pts.append((px, py))
    curve_d = f"M {ox} {oy} "
    for px, py in ext_pts:
        curve_d += f"L {px:.1f} {py:.1f} "
    content.append(f'<path d="{curve_d}" fill="none" stroke="#0284c7" stroke-width="2.2" />')
    
    # Vertical line at x = 1
    content.append(f'<line x1="{ox + scale}" y1="{oy}" x2="{ox + scale}" y2="{oy - scale}" stroke="#1e293b" stroke-width="1.2" />')
    
    # Point (1, 1)
    content.append(f'<circle cx="{ox + scale}" cy="{oy - scale}" r="3.2" fill="#0284c7" />')
    content.append(f'<text x="{ox + scale + 5}" y="{oy - scale + 4}" {FONT} font-size="11">(1, 1)</text>')
    
    # Label curve & region
    content.append(f'<text x="{ox + scale/2 - 10}" y="{oy - scale*0.65}" {FONT} font-size="12" font-style="italic">y = x&#178;</text>')
    content.append(f'<text x="{ox + scale*0.65}" y="{oy - scale*0.25}" {FONT} font-size="14" font-weight="bold" fill="#0369a1" font-style="italic">S</text>')
    
    return svg_wrapper(w, h, "\n".join(content))

# -------------------------------------------------------------
# 4. Figure 4: (a) 4 Strips; (b) 4 Right-Endpoint Rectangles (R4)
# -------------------------------------------------------------
def make_fig4_parabola_four_strips():
    w, h = 640, 310
    
    def panel(ox, oy, is_rectangles):
        scale = 160
        lines = [
            f'<line x1="{ox - 15}" y1="{oy}" x2="{ox + scale + 45}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
            f'<line x1="{ox}" y1="{oy + 15}" x2="{ox}" y2="{oy - scale - 30}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
            f'<text x="{ox + scale + 50}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>',
            f'<text x="{ox - 16}" y="{oy - scale - 25}" {FONT} font-size="12" font-style="italic">y</text>',
            f'<text x="{ox - 12}" y="{oy + 16}" {FONT} font-size="10">0</text>',
        ]
        
        # Subdivisions at 1/4, 2/4, 3/4, 1
        ticks = [("&#188;", 0.25), ("&#189;", 0.5), ("&#190;", 0.75), ("1", 1.0)]
        for lbl, t in ticks:
            px = ox + t * scale
            lines.append(f'<line x1="{px}" y1="{oy - 3}" x2="{px}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />')
            lines.append(f'<text x="{px - 4}" y="{oy + 16}" {FONT} font-size="10">{lbl}</text>')
            
        if not is_rectangles:
            # Panel (a): 4 strips
            # Shaded region under curve
            pts = []
            for i in range(41):
                xv = i / 40
                pts.append((ox + xv * scale, oy - (xv ** 2) * scale))
            p_d = f"M {ox} {oy} " + " ".join([f"L {px:.1f} {py:.1f}" for px, py in pts]) + f" L {ox + scale} {oy} Z"
            lines.append(f'<path d="{p_d}" fill="#e0f2fe" stroke="none" />')
            
            # Vertical lines dividing strips
            for t in [0.25, 0.5, 0.75, 1.0]:
                px = ox + t * scale
                py = oy - (t ** 2) * scale
                lines.append(f'<line x1="{px}" y1="{oy}" x2="{px}" y2="{py}" stroke="#1e293b" stroke-width="1.2" />')
                
            # Strip labels S1, S2, S3, S4
            # Strip 1: callout arrow since it's narrow
            lines.append(f'<text x="{ox + 0.12*scale - 12}" y="{oy - 0.15*scale}" {FONT} font-size="11" font-style="italic" fill="#0369a1">S&#8321;</text>')
            lines.append(f'<path d="M {ox + 0.12*scale - 2} {oy - 0.12*scale} L {ox + 0.14*scale} {oy - 0.03*scale}" fill="none" stroke="#0369a1" stroke-width="1" marker-end="url(#arrow-sky)" />')
            
            lines.append(f'<text x="{ox + 0.35*scale - 12}" y="{oy - 0.3*scale}" {FONT} font-size="11" font-style="italic" fill="#0369a1">S&#8322;</text>')
            lines.append(f'<path d="M {ox + 0.35*scale - 2} {oy - 0.25*scale} L {ox + 0.36*scale} {oy - 0.12*scale}" fill="none" stroke="#0369a1" stroke-width="1" marker-end="url(#arrow-sky)" />')

            lines.append(f'<text x="{ox + 0.60*scale - 3}" y="{oy - 0.25*scale}" {FONT} font-size="11" font-style="italic" fill="#0369a1">S&#8323;</text>')
            lines.append(f'<text x="{ox + 0.85*scale - 3}" y="{oy - 0.45*scale}" {FONT} font-size="11" font-style="italic" fill="#0369a1">S&#8324;</text>')
        else:
            # Panel (b): 4 right-endpoint rectangles
            for i in range(4):
                x_left = ox + (i / 4) * scale
                x_right = ox + ((i + 1) / 4) * scale
                w_rect = scale / 4
                h_rect = (((i + 1) / 4) ** 2) * scale
                lines.append(f'<rect x="{x_left}" y="{oy - h_rect}" width="{w_rect}" height="{h_rect}" fill="#bae6fd" stroke="#0284c7" stroke-width="1.2" fill-opacity="0.75" />')
                
        # Parabola curve
        ext_pts = []
        for i in range(46):
            xv = (i / 40) * 1.1
            ext_pts.append((ox + xv * scale, oy - (xv ** 2) * scale))
        c_d = f"M {ox} {oy} " + " ".join([f"L {px:.1f} {py:.1f}" for px, py in ext_pts])
        lines.append(f'<path d="{c_d}" fill="none" stroke="#0284c7" stroke-width="2.0" />')
        
        # Point (1, 1)
        lines.append(f'<circle cx="{ox + scale}" cy="{oy - scale}" r="3" fill="#0284c7" />')
        lines.append(f'<text x="{ox + scale + 4}" y="{oy - scale + 4}" {FONT} font-size="10">(1, 1)</text>')
        lines.append(f'<text x="{ox + scale*0.45}" y="{oy - scale*0.8}" {FONT} font-size="11" font-style="italic">y = x&#178;</text>')
        
        return lines

    content = []
    # Panel (a)
    content.extend(panel(50, 230, False))
    content.append(f'<text x="120" y="275" {FONT} font-size="12" font-weight="bold">(a)</text>')
    
    # Panel (b)
    content.extend(panel(370, 230, True))
    content.append(f'<text x="440" y="275" {FONT} font-size="12" font-weight="bold">(b)</text>')
    
    return svg_wrapper(w, h, "\n".join(content))

# -------------------------------------------------------------
# 5. Figure 5: Left-Endpoint Rectangles (L4)
# -------------------------------------------------------------
def make_fig5_parabola_left_endpoints():
    w, h = 380, 290
    ox, oy = 60, 220
    scale = 170
    
    content = [
        f'<line x1="{ox - 15}" y1="{oy}" x2="{ox + scale + 45}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="{oy + 15}" x2="{ox}" y2="{oy - scale - 30}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="{ox + scale + 50}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>',
        f'<text x="{ox - 16}" y="{oy - scale - 25}" {FONT} font-size="12" font-style="italic">y</text>',
        f'<text x="{ox - 12}" y="{oy + 16}" {FONT} font-size="10">0</text>',
    ]
    
    ticks = [("&#188;", 0.25), ("&#189;", 0.5), ("&#190;", 0.75), ("1", 1.0)]
    for lbl, t in ticks:
        px = ox + t * scale
        content.append(f'<line x1="{px}" y1="{oy - 3}" x2="{px}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />')
        content.append(f'<text x="{px - 4}" y="{oy + 16}" {FONT} font-size="10">{lbl}</text>')
        
    # 4 left-endpoint rectangles:
    # i = 0: height 0
    # i = 1, 2, 3
    for i in range(4):
        x_left = ox + (i / 4) * scale
        w_rect = scale / 4
        h_rect = ((i / 4) ** 2) * scale
        if h_rect > 0:
            content.append(f'<rect x="{x_left}" y="{oy - h_rect}" width="{w_rect}" height="{h_rect}" fill="#bae6fd" stroke="#0284c7" stroke-width="1.2" fill-opacity="0.75" />')
        else:
            # Show flat base line for collapsed rectangle
            content.append(f'<line x1="{x_left}" y1="{oy}" x2="{x_left + w_rect}" y2="{oy}" stroke="#0284c7" stroke-width="2" />')
            
    # Parabola curve
    ext_pts = []
    for i in range(46):
        xv = (i / 40) * 1.1
        ext_pts.append((ox + xv * scale, oy - (xv ** 2) * scale))
    c_d = f"M {ox} {oy} " + " ".join([f"L {px:.1f} {py:.1f}" for px, py in ext_pts])
    content.append(f'<path d="{c_d}" fill="none" stroke="#0284c7" stroke-width="2.0" />')
    
    # Vertical line at x = 1 up to curve
    content.append(f'<line x1="{ox + scale}" y1="{oy}" x2="{ox + scale}" y2="{oy - scale}" stroke="#1e293b" stroke-width="1.2" />')
    
    # Point (1, 1)
    content.append(f'<circle cx="{ox + scale}" cy="{oy - scale}" r="3" fill="#0284c7" />')
    content.append(f'<text x="{ox + scale + 4}" y="{oy - scale + 4}" {FONT} font-size="10">(1, 1)</text>')
    content.append(f'<text x="{ox + scale*0.4}" y="{oy - scale*0.75}" {FONT} font-size="11" font-style="italic">y = x&#178;</text>')
    
    return svg_wrapper(w, h, "\n".join(content))

# -------------------------------------------------------------
# 6. Figure 6: Eight Rectangles (a) L8; (b) R8
# -------------------------------------------------------------
def make_fig6_parabola_eight_rectangles():
    w, h = 640, 310
    
    def panel(ox, oy, use_right):
        scale = 160
        lines = [
            f'<line x1="{ox - 15}" y1="{oy}" x2="{ox + scale + 45}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
            f'<line x1="{ox}" y1="{oy + 15}" x2="{ox}" y2="{oy - scale - 30}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
            f'<text x="{ox + scale + 50}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>',
            f'<text x="{ox - 16}" y="{oy - scale - 25}" {FONT} font-size="12" font-style="italic">y</text>',
            f'<text x="{ox - 12}" y="{oy + 16}" {FONT} font-size="10">0</text>',
        ]
        
        # Ticks at 1/8 and 1
        lines.append(f'<line x1="{ox + scale/8}" y1="{oy - 3}" x2="{ox + scale/8}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />')
        lines.append(f'<text x="{ox + scale/8 - 4}" y="{oy + 16}" {FONT} font-size="10">&#8539;</text>')
        lines.append(f'<line x1="{ox + scale}" y1="{oy - 3}" x2="{ox + scale}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />')
        lines.append(f'<text x="{ox + scale - 3}" y="{oy + 16}" {FONT} font-size="10">1</text>')
        
        # 8 rectangles
        w_rect = scale / 8
        for i in range(8):
            x_left = ox + i * w_rect
            idx = (i + 1) if use_right else i
            h_rect = ((idx / 8) ** 2) * scale
            if h_rect > 0:
                lines.append(f'<rect x="{x_left}" y="{oy - h_rect}" width="{w_rect}" height="{h_rect}" fill="#bae6fd" stroke="#0284c7" stroke-width="1.0" fill-opacity="0.75" />')
            else:
                lines.append(f'<line x1="{x_left}" y1="{oy}" x2="{x_left + w_rect}" y2="{oy}" stroke="#0284c7" stroke-width="1.5" />')
                
        # Parabola curve
        ext_pts = []
        for i in range(46):
            xv = (i / 40) * 1.1
            ext_pts.append((ox + xv * scale, oy - (xv ** 2) * scale))
        c_d = f"M {ox} {oy} " + " ".join([f"L {px:.1f} {py:.1f}" for px, py in ext_pts])
        lines.append(f'<path d="{c_d}" fill="none" stroke="#0284c7" stroke-width="2.0" />')
        
        # Point (1, 1)
        lines.append(f'<circle cx="{ox + scale}" cy="{oy - scale}" r="3" fill="#0284c7" />')
        lines.append(f'<text x="{ox + scale + 4}" y="{oy - scale + 4}" {FONT} font-size="10">(1, 1)</text>')
        lines.append(f'<text x="{ox + scale*0.4}" y="{oy - scale*0.8}" {FONT} font-size="11" font-style="italic">y = x&#178;</text>')
        
        return lines

    content = []
    # Panel (a): L8
    content.extend(panel(50, 230, False))
    content.append(f'<text x="80" y="275" {FONT} font-size="12" font-weight="bold">(a) Using left endpoints</text>')
    
    # Panel (b): R8
    content.extend(panel(370, 230, True))
    content.append(f'<text x="400" y="275" {FONT} font-size="12" font-weight="bold">(b) Using right endpoints</text>')
    
    return svg_wrapper(w, h, "\n".join(content))

# -------------------------------------------------------------
# 7. Figure 7: Parabola with n Approximating Rectangles (Rn)
# -------------------------------------------------------------
def make_fig7_parabola_n_rectangles():
    w, h = 400, 310
    ox, oy = 60, 230
    scale = 180
    n = 16
    
    content = [
        f'<line x1="{ox - 15}" y1="{oy}" x2="{ox + scale + 50}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="{oy + 15}" x2="{ox}" y2="{oy - scale - 30}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="{ox + scale + 55}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>',
        f'<text x="{ox - 16}" y="{oy - scale - 25}" {FONT} font-size="12" font-style="italic">y</text>',
        f'<text x="{ox - 12}" y="{oy + 16}" {FONT} font-size="10">0</text>',
    ]
    
    w_rect = scale / n
    for i in range(n):
        x_left = ox + i * w_rect
        h_rect = (((i + 1) / n) ** 2) * scale
        content.append(f'<rect x="{x_left}" y="{oy - h_rect}" width="{w_rect}" height="{h_rect}" fill="#bae6fd" stroke="#0284c7" stroke-width="0.8" fill-opacity="0.75" />')
        
    # Parabola curve
    ext_pts = []
    for i in range(46):
        xv = (i / 40) * 1.1
        ext_pts.append((ox + xv * scale, oy - (xv ** 2) * scale))
    c_d = f"M {ox} {oy} " + " ".join([f"L {px:.1f} {py:.1f}" for px, py in ext_pts])
    content.append(f'<path d="{c_d}" fill="none" stroke="#0284c7" stroke-width="2.0" />')
    
    # Tick at 1/n and 1
    content.append(f'<line x1="{ox + w_rect}" y1="{oy - 3}" x2="{ox + w_rect}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />')
    # Callout line for 1/n
    content.append(f'<line x1="{ox + w_rect}" y1="{oy + 3}" x2="{ox + w_rect - 10}" y2="{oy + 25}" stroke="#64748b" stroke-width="1.0" />')
    content.append(f'<text x="{ox + w_rect - 18}" y="{oy + 38}" {FONT} font-size="10" font-style="italic">1/n</text>')
    
    content.append(f'<line x1="{ox + scale}" y1="{oy - 3}" x2="{ox + scale}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />')
    content.append(f'<text x="{ox + scale - 3}" y="{oy + 16}" {FONT} font-size="10">1</text>')
    
    # Point (1, 1)
    content.append(f'<circle cx="{ox + scale}" cy="{oy - scale}" r="3" fill="#0284c7" />')
    content.append(f'<text x="{ox + scale + 4}" y="{oy - scale + 4}" {FONT} font-size="10">(1, 1)</text>')
    content.append(f'<text x="{ox + scale*0.35}" y="{oy - scale*0.8}" {FONT} font-size="11" font-style="italic">y = x&#178;</text>')
    
    return svg_wrapper(w, h, "\n".join(content))

# -------------------------------------------------------------
# 8. Figure 13: General Area with Sample Points x_i*
# -------------------------------------------------------------
def make_fig13_sample_points():
    w, h = 580, 310
    ox, oy = 50, 240
    
    content = [
        f'<line x1="{ox - 20}" y1="{oy}" x2="{ox + 480}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="{oy + 20}" x2="{ox}" y2="{oy - 200}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="{ox + 485}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>',
        f'<text x="{ox - 16}" y="{oy - 195}" {FONT} font-size="12" font-style="italic">y</text>',
        f'<text x="{ox - 14}" y="{oy + 16}" {FONT} font-size="11">0</text>',
    ]
    
    # Subintervals from a to b
    xa = ox + 60
    xb = ox + 430
    sub_w = (xb - xa) / 8  # 8 subintervals
    
    # Smooth continuous function curve
    def f_curve(x_coord):
        t = (x_coord - xa) / (xb - xa)
        # Curve starts around 140, dips to 85, rises to 150, drops to 70
        y_val = 145 - 90 * math.sin(math.pi * t * 0.9 + 0.4) + 40 * math.cos(2 * math.pi * t)
        return y_val
        
    # Sample point fractions within each subinterval
    # e.g., slightly irregular positions inside [x_{i-1}, x_i]
    sample_offsets = [0.45, 0.6, 0.4, 0.55, 0.65, 0.5, 0.4, 0.7]
    
    # Draw rectangles based on f(x_i*)
    for i in range(8):
        x_left = xa + i * sub_w
        x_star = x_left + sample_offsets[i] * sub_w
        y_star = oy - f_curve(x_star)
        h_rect = f_curve(x_star)
        
        # Rectangle
        content.append(f'<rect x="{x_left}" y="{y_star}" width="{sub_w}" height="{h_rect}" fill="#bae6fd" stroke="#0284c7" stroke-width="1.2" fill-opacity="0.65" />')
        
        # Sample point marker & vertical dashed guideline
        content.append(f'<line x1="{x_star}" y1="{oy}" x2="{x_star}" y2="{y_star}" stroke="#0369a1" stroke-width="1.0" stroke-dasharray="3 3" />')
        content.append(f'<circle cx="{x_star}" cy="{y_star}" r="2.5" fill="#0369a1" />')
        
    # Smooth function curve over top
    pts = []
    for i in range(101):
        xc = xa + (i / 100) * (xb - xa)
        pts.append((xc, oy - f_curve(xc)))
    c_d = f"M {pts[0][0]:.1f} {pts[0][1]:.1f} " + " ".join([f"L {px:.1f} {py:.1f}" for px, py in pts[1:]])
    content.append(f'<path d="{c_d}" fill="none" stroke="#0284c7" stroke-width="2.2" />')
    
    # Boundary and interval tick labels
    content.append(f'<text x="{xa - 4}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">a</text>')
    content.append(f'<text x="{xa + sub_w - 6}" y="{oy + 16}" {FONT} font-size="10" font-style="italic">x&#8321;</text>')
    content.append(f'<text x="{xa + 2*sub_w - 6}" y="{oy + 16}" {FONT} font-size="10" font-style="italic">x&#8322;</text>')
    content.append(f'<text x="{xa + 3*sub_w - 6}" y="{oy + 16}" {FONT} font-size="10" font-style="italic">x&#8323;</text>')
    
    content.append(f'<text x="{xa + 4*sub_w - 10}" y="{oy + 16}" {FONT} font-size="10" font-style="italic">x<sub>i-1</sub></text>')
    content.append(f'<text x="{xa + 5*sub_w - 5}" y="{oy + 16}" {FONT} font-size="10" font-style="italic">x<sub>i</sub></text>')
    content.append(f'<text x="{xa + 7*sub_w - 10}" y="{oy + 16}" {FONT} font-size="10" font-style="italic">x<sub>n-1</sub></text>')
    content.append(f'<text x="{xb - 4}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">b</text>')
    
    # Sample point labels under x-axis with small arrows or ticks
    content.append(f'<text x="{xa + sample_offsets[0]*sub_w - 6}" y="{oy + 30}" {FONT} font-size="10" font-style="italic">x&#8321;*</text>')
    content.append(f'<text x="{xa + sub_w + sample_offsets[1]*sub_w - 6}" y="{oy + 30}" {FONT} font-size="10" font-style="italic">x&#8322;*</text>')
    content.append(f'<text x="{xa + 2*sub_w + sample_offsets[2]*sub_w - 6}" y="{oy + 30}" {FONT} font-size="10" font-style="italic">x&#8323;*</text>')
    content.append(f'<text x="{xa + 4*sub_w + sample_offsets[4]*sub_w - 6}" y="{oy + 30}" {FONT} font-size="10" font-style="italic">x<sub>i</sub>*</text>')
    content.append(f'<text x="{xa + 7*sub_w + sample_offsets[7]*sub_w - 6}" y="{oy + 30}" {FONT} font-size="10" font-style="italic">x<sub>n</sub>*</text>')
    
    # Delta x brace / label over the ith interval
    idx_i = 4
    x_i_left = xa + idx_i * sub_w
    x_i_right = xa + (idx_i + 1) * sub_w
    bracket_y = oy - f_curve(x_i_left + sample_offsets[idx_i]*sub_w) - 25
    content.append(f'<line x1="{x_i_left}" y1="{bracket_y}" x2="{x_i_right}" y2="{bracket_y}" stroke="#1e293b" stroke-width="1.0" />')
    content.append(f'<line x1="{x_i_left}" y1="{bracket_y - 3}" x2="{x_i_left}" y2="{bracket_y + 3}" stroke="#1e293b" stroke-width="1.0" />')
    content.append(f'<line x1="{x_i_right}" y1="{bracket_y - 3}" x2="{x_i_right}" y2="{bracket_y + 3}" stroke="#1e293b" stroke-width="1.0" />')
    content.append(f'<text x="{x_i_left + sub_w/2 - 8}" y="{bracket_y - 6}" {FONT} font-size="11" font-style="italic">&#916;x</text>')
    
    # f(xi*) label
    content.append(f'<text x="{x_i_left + sample_offsets[idx_i]*sub_w + 3}" y="{oy - f_curve(x_i_left + sample_offsets[idx_i]*sub_w) + 20}" {FONT} font-size="10" font-style="italic">f(x<sub>i</sub>*)</text>')
    
    return svg_wrapper(w, h, "\n".join(content))

# -------------------------------------------------------------
# 9. Figure 14: Lower and Upper Sums (Inscribed & Circumscribed)
# -------------------------------------------------------------
def make_fig14_lower_upper_sums():
    w, h = 420, 260
    ox, oy = 50, 210
    
    content = [
        f'<line x1="{ox - 15}" y1="{oy}" x2="{ox + 330}" y2="{oy}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<line x1="{ox}" y1="{oy + 15}" x2="{ox}" y2="{oy - 170}" stroke="#1e293b" stroke-width="1.4" marker-end="url(#arrow)" />',
        f'<text x="{ox + 335}" y="{oy + 14}" {FONT} font-size="12" font-style="italic">x</text>',
        f'<text x="{ox - 16}" y="{oy - 165}" {FONT} font-size="12" font-style="italic">y</text>',
        f'<text x="{ox - 12}" y="{oy + 16}" {FONT} font-size="10">0</text>',
    ]
    
    xa = ox + 40
    xb = ox + 260
    sub_w = (xb - xa) / 4  # 4 subintervals
    
    # Function with a dip in the middle
    def f_curve(xc):
        t = (xc - xa) / (xb - xa)
        # starts high (~130), drops to min (~30) around t=0.35, rises to peak (~100) around t=0.75, drops to 80
        return 120 - 150 * t + 320 * (t**2) - 210 * (t**3) + 20
        
    # In each of 4 subintervals: calculate min and max
    for i in range(4):
        x_left = xa + i * sub_w
        x_right = xa + (i + 1) * sub_w
        
        # sample 20 points in subinterval to find min and max
        sample_ys = [f_curve(x_left + (j/20)*sub_w) for j in range(21)]
        y_min = min(sample_ys)
        y_max = max(sample_ys)
        
        # Lower rectangle (inscribed)
        content.append(f'<rect x="{x_left}" y="{oy - y_min}" width="{sub_w}" height="{y_min}" fill="#bae6fd" stroke="#0284c7" stroke-width="1.2" fill-opacity="0.8" />')
        
        # Upper rectangle (circumscribed) outline / transparent fill
        content.append(f'<rect x="{x_left}" y="{oy - y_max}" width="{sub_w}" height="{y_max}" fill="none" stroke="#0284c7" stroke-width="1.2" stroke-dasharray="4 3" />')
        
    # Function curve
    pts = []
    for i in range(81):
        xc = xa + (i / 80) * (xb - xa)
        pts.append((xc, oy - f_curve(xc)))
    c_d = f"M {pts[0][0]:.1f} {pts[0][1]:.1f} " + " ".join([f"L {px:.1f} {py:.1f}" for px, py in pts[1:]])
    content.append(f'<path d="{c_d}" fill="none" stroke="#0284c7" stroke-width="2.2" />')
    
    # Boundary ticks
    content.append(f'<line x1="{xa}" y1="{oy - 3}" x2="{xa}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />')
    content.append(f'<text x="{xa - 4}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">a</text>')
    content.append(f'<line x1="{xb}" y1="{oy - 3}" x2="{xb}" y2="{oy + 3}" stroke="#1e293b" stroke-width="1.2" />')
    content.append(f'<text x="{xb - 4}" y="{oy + 16}" {FONT} font-size="11" font-style="italic">b</text>')
    
    return svg_wrapper(w, h, "\n".join(content))

# -------------------------------------------------------------
# Generate all
# -------------------------------------------------------------
figs = {
    "sec4_1_figure1_area_under_curve.svg": make_fig1_area_under_curve(),
    "sec4_1_figure2_straight_sided_areas.svg": make_fig2_straight_sided_areas(),
    "sec4_1_figure3_parabola_region.svg": make_fig3_parabola_region(),
    "sec4_1_figure4_parabola_four_strips.svg": make_fig4_parabola_four_strips(),
    "sec4_1_figure5_parabola_left_endpoints.svg": make_fig5_parabola_left_endpoints(),
    "sec4_1_figure6_parabola_eight_rectangles.svg": make_fig6_parabola_eight_rectangles(),
    "sec4_1_figure7_parabola_n_rectangles.svg": make_fig7_parabola_n_rectangles(),
    "sec4_1_figure13_sample_points.svg": make_fig13_sample_points(),
    "sec4_1_figure14_lower_upper_sums.svg": make_fig14_lower_upper_sums(),
}

for filename, svg_data in figs.items():
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_data)
    print(f"Generated: {filepath}")
