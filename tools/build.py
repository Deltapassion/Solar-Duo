"""Assemble l'application Solar Duo en un seul fichier HTML autonome.

Source : tools/template.html (+ logo, icône, photo de Payolle en base64)
Résultat : src/solar-duo.html (application de bureau) et docs/app/index.html (version en ligne)

    python tools/build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
T = ROOT / "tools"

sun = (T / "logo" / "sun_fragment.svg").read_text(encoding="utf-8")
fav = (T / "logo" / "fav64.b64").read_text(encoding="utf-8").strip()
photo = (T / "payolle.b64").read_text(encoding="utf-8").strip()

html = ((T / "template.html").read_text(encoding="utf-8")
        .replace("%%SUN%%", sun).replace("%%FAVICON%%", fav).replace("%%PHOTO%%", photo))

for out in (ROOT / "src" / "solar-duo.html", ROOT / "docs" / "app" / "index.html"):
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(out.relative_to(ROOT), len(html), "octets")
