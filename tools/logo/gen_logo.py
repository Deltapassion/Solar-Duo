"""Génère le logo SOLAR DUO : soleil de mai (style drapeau argentin)."""
import math

GOLD = "#F6B40E"
BROWN = "#85340A"
CELESTE = "#74ACDF"

def straight_ray(angle, r0, r1, half_w):
    """Rayon droit triangulaire."""
    a = math.radians(angle)
    p = lambda r, da: (r * math.cos(a + da), r * math.sin(a + da))
    w = half_w / r0
    pts = [p(r0, -w), p(r1, 0), p(r0, w)]
    return "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts) + " Z"

def wavy_ray(angle, r0, r1, half_w, amp, waves=1.5, n=60):
    """Rayon flamboyant (ondulé), effilé."""
    a = math.radians(angle)
    ca, sa = math.cos(a), math.sin(a)
    # repère local : u = radial, v = tangentiel
    left, right = [], []
    for i in range(n + 1):
        t = i / n
        r = r0 + (r1 - r0) * t
        c = amp * math.sin(t * waves * 2 * math.pi) * (0.3 + 0.7 * t) * (1 - t * 0.15)
        w = half_w * (1 - t) ** 0.9
        for side, lst in ((1, left), (-1, right)):
            v = c + side * w
            lst.append((r * ca - v * sa, r * sa + v * ca))
    pts = left + right[::-1]
    return "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts) + " Z"

def sun(cx=0, cy=0, scale=1.0, sw=2.2):
    R = 100  # rayon du disque
    out = [f'<g transform="translate({cx},{cy}) scale({scale})" stroke="{BROWN}" stroke-width="{sw}" stroke-linejoin="round">']
    rays = []
    for k in range(32):
        ang = -90 + k * 360 / 32
        if k % 2 == 0:
            rays.append(straight_ray(ang, R - 6, 205, 15))
        else:
            rays.append(wavy_ray(ang, R - 6, 195, 10, 9))
    out.append(f'<path fill="{GOLD}" d="{" ".join(rays)}"/>')
    out.append(f'<circle r="{R}" fill="{GOLD}"/>')
    # visage façon emoji (yeux ovales, grand sourire ouvert, joues roses)
    f = []
    for sx in (-1, 1):
        x = 34 * sx
        f.append(f'<ellipse cx="{x}" cy="-22" rx="10" ry="16" fill="#3b1a06" stroke="none"/>')
        f.append(f'<ellipse cx="{x+3}" cy="-29" rx="3.6" ry="5" fill="#fff" stroke="none"/>')
        f.append(f'<ellipse cx="{62*sx}" cy="22" rx="15" ry="10" fill="#ff5c8a" fill-opacity="0.5" stroke="none"/>')
    f.append(f'<path d="M-50,14 Q0,26 50,14 Q46,72 0,74 Q-46,72 -50,14 Z" fill="#6b1d06" stroke="{BROWN}" stroke-width="3" stroke-linejoin="round"/>')
    f.append('<path d="M-44,18 Q0,28 44,18 L42,28 Q0,37 -42,28 Z" fill="#fff" stroke="none"/>')
    f.append('<path d="M-24,62 Q0,46 24,62 Q12,73 0,73 Q-12,73 -24,62 Z" fill="#e8505b" stroke="none"/>')
    out.append('<g>' + "".join(f) + "</g>")
    out.append("</g>")
    return "\n".join(out)

def svg_icon():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-215 -215 430 430" width="512" height="512">\n'
            f'<title>Solar Duo</title>\n{sun()}\n</svg>\n')

def svg_icon_photo(photo_b64):
    """Icône carrée : soleil sur la photo de Payolle (coins arrondis)."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
<title>Solar Duo</title>
<defs><clipPath id="r"><rect width="512" height="512" rx="96"/></clipPath>
<radialGradient id="halo" cx=".5" cy=".46" r=".5"><stop offset="0" stop-color="#fff" stop-opacity=".35"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient></defs>
<g clip-path="url(#r)">
  <image href="data:image/jpeg;base64,{photo_b64}" width="512" height="512" preserveAspectRatio="xMidYMid slice"/>
  <rect width="512" height="512" fill="url(#halo)"/>
</g>
{sun(256, 246, 1.12)}
</svg>
'''

def svg_full(photo_b64=None):
    RED = "#D7261E"
    bg = (f'<image href="data:image/jpeg;base64,{photo_b64}" x="0" y="0" width="1200" height="420" preserveAspectRatio="xMidYMid slice"/>'
          if photo_b64 else f'<rect width="1200" height="420" fill="{CELESTE}"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420">
<title>Solar Duo</title>
<defs>
  <clipPath id="c"><rect width="1200" height="420" rx="36"/></clipPath>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#fff" stop-opacity=".25"/><stop offset=".55" stop-color="#fff" stop-opacity="0"/>
    <stop offset=".8" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".45"/>
  </linearGradient>
</defs>
<g clip-path="url(#c)">{bg}<rect width="1200" height="420" fill="url(#fade)"/></g>
{sun(215, 190, 0.78)}
<g font-family="Montserrat, 'Segoe UI', Arial, sans-serif" font-weight="800" stroke="#fff" stroke-width="10" stroke-linejoin="round" paint-order="stroke">
  <text x="420" y="200" font-size="150" fill="{RED}" letter-spacing="4">SOLAR</text>
  <text x="424" y="305" font-size="100" fill="{CELESTE}" letter-spacing="30">DUO</text>
</g>
<text x="40" y="395" font-family="'Segoe UI', Arial, sans-serif" font-size="28" font-weight="600" fill="#fff">Dimensionnement d'installations solaires</text>
</svg>
'''

if __name__ == "__main__":
    import sys
    d = sys.argv[1] if len(sys.argv) > 1 else "."
    open(f"{d}/solar-duo-logo.svg", "w").write(svg_icon())
    import base64
    ph = base64.b64encode(open(sys.argv[2], "rb").read()).decode() if len(sys.argv) > 2 else None
    open(f"{d}/solar-duo-logo-nom.svg", "w").write(svg_full(ph))
    if len(sys.argv) > 3:
        sq = base64.b64encode(open(sys.argv[3], "rb").read()).decode()
        open(f"{d}/solar-duo-icone.svg", "w").write(svg_icon_photo(sq))
    # fragment pour l'appli
    open(f"{d}/sun_fragment.svg", "w").write(sun())
