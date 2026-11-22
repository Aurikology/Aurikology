"""Builds the static images for the profile README into assets/.

Run: py -3 src/build.py   (from the repo root). No dependencies.
Live images (activity card, snake) are made by .github/workflows/profile.yml on the `output` branch.
Every number on a card comes from that project's README. Change a number there first.
"""
import pathlib
from xml.sax.saxutils import escape

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)

FONT = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'Cascadia Code', 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

THEMES = {
    "dark": dict(bg="#0d1117", panel="#161b22", border="#30363d", text="#e6edf3", soft="#c9d1d9",
                 muted="#8b949e", c1="#fbbf24", c2="#f472b6", chip="#21262d", glow=".26", up="#3fb950", down="#f85149"),
    "light": dict(bg="#ffffff", panel="#ffffff", border="#d0d7de", text="#1f2328", soft="#31373d",
                  muted="#59636e", c1="#b45309", c2="#be185d", chip="#f6f8fa", glow=".14", up="#1a7f37", down="#cf222e"),
}


def grad(t: dict, gid: str = "g") -> str:
    return (f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0" stop-color="{t["c1"]}"/><stop offset="1" stop-color="{t["c2"]}"/></linearGradient>')


# --------------------------------------------------------------------------- header

PHRASES = [
    "pexi: steal or ripoff, from one photo",
    "kore: cognitive load from EEG, in C++",
    "nq-quant: backtests that refuse to lie",
]


def typing(t: dict, x: int, y: int) -> str:
    slot, total = 4.6, 4.6 * len(PHRASES)
    out = [f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="25" fill="{t["c1"]}" font-weight="700">$</text>']
    for i, phrase in enumerate(PHRASES):
        start, end = slot * i, slot * i + 4.1
        spans = []
        for j, ch in enumerate(phrase):
            on = (start + 0.25 + 0.055 * j) / total
            off = end / total
            spans.append(
                f'<tspan fill-opacity="0">{escape(ch)}<animate attributeName="fill-opacity" values="0;1;0" '
                f'keyTimes="0;{on:.4f};{off:.4f}" calcMode="discrete" dur="{total}s" repeatCount="indefinite"/></tspan>')
        out.append(f'<text x="{x + 30}" y="{y}" font-family="{MONO}" font-size="25" fill="{t["soft"]}" '
                   f'xml:space="preserve">{"".join(spans)}</text>')
    return "".join(out)


def scope(t: dict) -> str:
    """Oscilloscope trace on the right: a signal being measured, his whole theme."""
    x0, x1, cy = 830, 1150, 150
    grid = "".join(f'<line x1="{x}" y1="40" x2="{x}" y2="260" stroke="{t["border"]}" stroke-width="1"/>' for x in range(x0, x1 + 1, 40))
    grid += "".join(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{t["border"]}" stroke-width="1"/>' for y in range(40, 261, 44))
    import math
    pts = []
    for i in range(161):
        x = x0 + i * 2
        y = cy - 34 * math.sin(i / 7.5) * (0.55 + 0.45 * math.sin(i / 23)) - 12 * math.sin(i / 2.3)
        pts.append(f"{x},{y:.1f}")
    trace = " ".join(pts)
    return (f'<rect x="{x0 - 10}" y="30" width="{x1 - x0 + 20}" height="240" rx="14" fill="{t["panel"]}" fill-opacity=".7" stroke="{t["border"]}"/>'
            f'{grid}'
            f'<polyline points="{trace}" fill="none" stroke="url(#g)" stroke-width="3" stroke-linejoin="round" '
            f'stroke-dasharray="900" stroke-dashoffset="900"><animate attributeName="stroke-dashoffset" values="900;0;0;-900" '
            f'keyTimes="0;.45;.7;1" dur="6s" repeatCount="indefinite"/></polyline>'
            f'<text x="{x0 + 4}" y="58" font-family="{MONO}" font-size="14" fill="{t["muted"]}">256 Hz</text>'
            f'<text x="{x1 - 4}" y="256" text-anchor="end" font-family="{MONO}" font-size="14" fill="{t["muted"]}">measured, then trusted</text>')


def header(t: dict) -> str:
    W, H = 1200, 300
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>{grad(t)}
<radialGradient id="g1"><stop offset="0" stop-color="{t["c1"]}" stop-opacity="{t["glow"]}"/><stop offset="1" stop-color="{t["c1"]}" stop-opacity="0"/></radialGradient>
<radialGradient id="g2"><stop offset="0" stop-color="{t["c2"]}" stop-opacity="{t["glow"]}"/><stop offset="1" stop-color="{t["c2"]}" stop-opacity="0"/></radialGradient>
<pattern id="dots" width="26" height="26" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.3" fill="{t["muted"]}" fill-opacity=".28"/></pattern>
<clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#frame)">
<rect width="{W}" height="{H}" fill="{t["bg"]}"/>
<rect width="{W}" height="{H}" fill="url(#dots)"/>
<circle cx="160" cy="30" r="330" fill="url(#g1)"><animate attributeName="cx" values="160;330;160" dur="16s" repeatCount="indefinite"/></circle>
<circle cx="1000" cy="290" r="380" fill="url(#g2)"><animate attributeName="cy" values="290;190;290" dur="18s" repeatCount="indefinite"/></circle>
{scope(t)}
</g>
<rect x=".75" y=".75" width="{W - 1.5}" height="{H - 1.5}" rx="18" fill="none" stroke="{t["border"]}" stroke-width="1.5"/>
<text x="70" y="136" font-family="{FONT}" font-size="88" font-weight="800" letter-spacing="-2.5" fill="url(#g)">Aurik Disler</text>
<text x="74" y="188" font-family="{FONT}" font-size="27" fill="{t["text"]}">Software Engineering @ Queen's. I build systems</text>
<text x="74" y="222" font-family="{FONT}" font-size="27" fill="{t["text"]}">that get measured before they're trusted.</text>
{typing(t, 74, 270)}
</svg>'''


# --------------------------------------------------------------------------- project cards

def chips(t: dict, items: list[str], x: int, y: int) -> str:
    out, cx = [], x
    for it in items:
        w = int(len(it) * 8.6 + 26)
        out.append(f'<rect x="{cx}" y="{y}" width="{w}" height="30" rx="15" fill="{t["chip"]}" stroke="{t["border"]}"/>'
                   f'<text x="{cx + w / 2}" y="{y + 20}" text-anchor="middle" font-family="{FONT}" font-size="15" '
                   f'fill="{t["soft"]}">{escape(it)}</text>')
        cx += w + 8
    return "".join(out)


def icon_box(inner: str) -> str:
    return (f'<rect x="28" y="30" width="60" height="60" rx="15" fill="url(#g)" fill-opacity=".14" stroke="url(#g)" stroke-width="1.5"/>'
            f'<g transform="translate(28 30)">{inner}</g>')


ICONS = {
    "pexi": '<path d="M14 30 L30 14 H46 V30 L30 46 Z" fill="none" stroke="url(#g)" stroke-width="3" stroke-linejoin="round"/><circle cx="39" cy="21" r="3.5" fill="url(#g)"/>',
    "kore": '<path d="M8 32 H17 L21 20 L27 44 L33 14 L38 38 L42 28 H52" fill="none" stroke="url(#g)" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>',
    "quant": ('<path d="M18 14 V46 M30 20 V42 M42 12 V36" stroke="url(#g)" stroke-width="2.5" stroke-linecap="round"/>'
              '<rect x="14" y="22" width="8" height="16" rx="1.5" fill="url(#g)"/><rect x="26" y="26" width="8" height="10" rx="1.5" fill="url(#g)"/>'
              '<rect x="38" y="16" width="8" height="14" rx="1.5" fill="url(#g)"/>'),
    "solgraph": ('<path d="M16 42 L30 18 L44 40 Z M30 18 V32" fill="none" stroke="url(#g)" stroke-width="2.5"/>'
                 '<circle cx="30" cy="18" r="5" fill="url(#g)"/><circle cx="16" cy="42" r="5" fill="url(#g)"/>'
                 '<circle cx="44" cy="40" r="5" fill="url(#g)"/><circle cx="30" cy="33" r="4" fill="url(#g)"/>'),
}


def visual(t: dict, key: str) -> str:
    x, y, w, h = 372, 26, 202, 124
    frame = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{t["bg"]}" stroke="{t["border"]}"/>'
    if key == "pexi":
        # A price tag whose verdict flips between STEAL and RIPOFF.
        tag = (f'<path d="M{x + 30} {y + 28} H{x + 128} L{x + 152} {y + 62} L{x + 128} {y + 96} H{x + 30} Z" '
               f'fill="{t["chip"]}" stroke="url(#g)" stroke-width="2"/>'
               f'<circle cx="{x + 132}" cy="{y + 62}" r="5" fill="{t["bg"]}" stroke="{t["muted"]}" stroke-width="1.5"/>'
               f'<text x="{x + 44}" y="{y + 58}" font-family="{MONO}" font-size="24" font-weight="700" fill="{t["text"]}">$24.99</text>'
               f'<text x="{x + 44}" y="{y + 82}" font-family="{FONT}" font-size="12.5" fill="{t["muted"]}">5.18M checked</text>')
        verdict = ""
        for i, (word, col) in enumerate((("STEAL", t["up"]), ("RIPOFF", t["down"]))):
            vals = "1;1;0;0" if i == 0 else "0;0;1;1"
            verdict += (f'<g opacity="{1 if i == 0 else 0}"><rect x="{x + 112}" y="{y + 92}" width="78" height="24" rx="12" fill="{col}"/>'
                        f'<text x="{x + 151}" y="{y + 109}" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="800" fill="#ffffff">{word}</text>'
                        f'<animate attributeName="opacity" values="{vals}" keyTimes="0;.49;.5;1" calcMode="discrete" dur="4s" repeatCount="indefinite"/></g>')
        return frame + tag + verdict
    if key == "kore":
        # Two EEG channels feeding theta and alpha bars.
        import math
        lines = ""
        for ch in range(2):
            cy = y + 32 + ch * 34
            pts = " ".join(f"{x + 12 + i * 1.6:.1f},{cy - 9 * math.sin(i / (3.2 + ch)) - 4 * math.sin(i / 1.3 + ch):.1f}" for i in range(70))
            lines += f'<polyline points="{pts}" fill="none" stroke="url(#g)" stroke-width="2" stroke-linejoin="round"/>'
            lines += f'<text x="{x + 12}" y="{cy + 22}" font-family="{MONO}" font-size="10.5" fill="{t["muted"]}">ch{ch + 1}</text>'
        bars = ""
        for i, (label, lo, hi) in enumerate((("θ", 30, 78), ("α", 62, 26))):
            bx = x + 140 + i * 28
            base = y + 102
            bars += (f'<rect x="{bx}" y="{base - lo}" width="18" height="{lo}" rx="3" fill="url(#g)">'
                     f'<animate attributeName="height" values="{lo};{hi};{lo}" dur="3s" repeatCount="indefinite"/>'
                     f'<animate attributeName="y" values="{base - lo};{base - hi};{base - lo}" dur="3s" repeatCount="indefinite"/></rect>'
                     f'<text x="{bx + 9}" y="{base + 16}" text-anchor="middle" font-family="{FONT}" font-size="13" fill="{t["soft"]}">{label}</text>')
        return frame + lines + bars
    if key == "quant":
        # Candles with a bootstrap confidence band.
        candles = ""
        series = [(50, 70, 44, 76), (68, 58, 52, 74), (58, 72, 54, 80), (72, 64, 60, 78), (64, 84, 60, 90),
                  (84, 78, 72, 88), (78, 92, 74, 98), (92, 86, 80, 100)]
        for i, (o, c, lo, hi) in enumerate(series):
            cx = x + 22 + i * 21
            col = t["up"] if c > o else t["down"]
            top, bot = y + 120 - max(o, c), y + 120 - min(o, c)
            candles += (f'<line x1="{cx}" y1="{y + 120 - hi}" x2="{cx}" y2="{y + 120 - lo}" stroke="{col}" stroke-width="1.5"/>'
                        f'<rect x="{cx - 5}" y="{top}" width="10" height="{max(2, bot - top)}" rx="1.5" fill="{col}">'
                        f'<animate attributeName="opacity" values="0;1;1" keyTimes="0;{(i + 1) / 10:.2f};1" dur="3.5s" repeatCount="indefinite"/></rect>')
        band = (f'<path d="M{x + 14} {y + 74} C{x + 80} {y + 62} {x + 130} {y + 48} {x + 190} {y + 30} '
                f'L{x + 190} {y + 54} C{x + 130} {y + 70} {x + 80} {y + 84} {x + 14} {y + 92} Z" fill="url(#g)" fill-opacity=".18"/>'
                f'<text x="{x + 188}" y="{y + 116}" text-anchor="end" font-family="{MONO}" font-size="10.5" fill="{t["muted"]}">95% CI</text>')
        return frame + band + candles
    if key == "solgraph":
        nodes = [(x + 40, y + 34), (x + 102, y + 26), (x + 166, y + 44), (x + 62, y + 92), (x + 132, y + 98), (x + 100, y + 62)]
        edges = [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (0, 3), (2, 4), (1, 2)]
        out = frame
        for i, (a, b) in enumerate(edges):
            (ax, ay), (bx, by) = nodes[a], nodes[b]
            out += (f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{t["muted"]}" stroke-width="1.6" stroke-opacity=".7"/>')
        out += (f'<circle r="4" fill="{t["c1"]}"><animateMotion dur="2.4s" repeatCount="indefinite" '
                f'path="M{nodes[0][0]} {nodes[0][1]} L{nodes[5][0]} {nodes[5][1]} L{nodes[4][0]} {nodes[4][1]}"/></circle>')
        for i, (nx, ny) in enumerate(nodes):
            r = 11 if i == 5 else 7
            out += f'<circle cx="{nx}" cy="{ny}" r="{r}" fill="{t["chip"]}" stroke="url(#g)" stroke-width="2"/>'
        return out
    return frame


CARDS = {
    "pexi": dict(title="Pexi", tag="Co-founder · iOS on TestFlight",
                 pitch=["Point your phone at a price tag: Gemini",
                        "names the product, a price engine says",
                        "steal or ripoff, or refuses to guess."],
                 stat="5.18M-product catalogue · ~1,000 commits",
                 chips=["TypeScript", "Next.js", "Capacitor", "Gemini"]),
    "kore": dict(title="KORE", tag="Founder · EEG wearable",
                 pitch=["C++ DSP core turns a 256 Hz two-channel",
                        "EEG stream into a theta/alpha load index,",
                        "called from Flutter over Dart FFI."],
                 stat="361 tests · parity-checked against Dart",
                 chips=["C++17", "DSP", "Dart FFI", "Flutter"]),
    "quant": dict(title="nq-quant", tag="Backtester that won't fool itself",
                  pitch=["Look-ahead-free Nasdaq futures backtests:",
                         "pessimistic fills, bootstrap CIs and a",
                         "permutation test against random entries."],
                  stat="10x faster replays · 293.6 s → 29.0 s",
                  chips=["Python", "NumPy", "pandas", "Hypothesis"]),
    "solgraph": dict(title="SolGraph", tag="Read-only Solana AI assistant",
                     pitch=["LangChain agent over a graph of wallets",
                            "and transfers, plus hybrid RAG over the",
                            "docs. Holds no keys; a test enforces it."],
                     stat="Recall@5 82.9% → 91.4% on 35 questions",
                     chips=["LangChain", "Apache AGE", "pgvector", "Docker"]),
}


def card(t: dict, key: str) -> str:
    c = CARDS[key]
    W, H = 600, 330
    pitch = "".join(f'<text x="30" y="{196 + i * 28}" font-family="{FONT}" font-size="19.5" fill="{t["soft"]}">{escape(l)}</text>'
                    for i, l in enumerate(c["pitch"]))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>{grad(t)}<clipPath id="frame"><rect width="{W}" height="{H}" rx="16"/></clipPath></defs>
<g clip-path="url(#frame)"><rect width="{W}" height="{H}" fill="{t["panel"]}"/><rect width="{W}" height="4" fill="url(#g)"/></g>
<rect x=".75" y=".75" width="{W - 1.5}" height="{H - 1.5}" rx="16" fill="none" stroke="{t["border"]}" stroke-width="1.5"/>
{icon_box(ICONS[key])}
<text x="104" y="66" font-family="{FONT}" font-size="28" font-weight="800" fill="{t["text"]}">{escape(c["title"])}</text>
<text x="104" y="92" font-family="{FONT}" font-size="16" fill="{t["muted"]}">{escape(c["tag"])}</text>
<text x="30" y="150" font-family="{FONT}" font-size="17" font-weight="700" fill="url(#g)">{escape(c["stat"])}</text>
{visual(t, key)}
{pitch}
{chips(t, c["chips"], 30, 284)}
</svg>'''


# --------------------------------------------------------------------------- also built

ALSO = [
    ("AI Cultural Translator", "An arrival companion for newcomers to Canada.", "Next.js · Vercel · live"),
    ("Slash", "A trading mentor that coaches by a written rulebook.", "Electron · Claude · NQ futures"),
    ("128Tick Server Simulation", "Heap vs contiguous memory under a 128-tick budget.", "C++17 · CMake · std::chrono"),
    ("SmartCV · QMIND", "Co-led 5 people on an LLM resume pipeline.", "Python · FastAPI · CUCAI 2026"),
]


def also(t: dict) -> str:
    W, H = 1200, 400
    tiles = ""
    for i, (name, line, hl) in enumerate(ALSO):
        x, y = 24 + (i % 2) * 588, 70 + (i // 2) * 160
        tiles += (f'<rect x="{x}" y="{y}" width="564" height="144" rx="14" fill="{t["panel"]}" stroke="{t["border"]}" stroke-width="1.5"/>'
                  f'<rect x="{x}" y="{y + 22}" width="4" height="100" rx="2" fill="url(#g)"/>'
                  f'<text x="{x + 28}" y="{y + 46}" font-family="{FONT}" font-size="25" font-weight="800" fill="{t["text"]}">{escape(name)}</text>'
                  f'<text x="{x + 28}" y="{y + 82}" font-family="{FONT}" font-size="19" fill="{t["soft"]}">{escape(line)}</text>'
                  f'<text x="{x + 28}" y="{y + 118}" font-family="{FONT}" font-size="17" font-weight="700" fill="url(#g)">{escape(hl)}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>{grad(t)}</defs>
<text x="26" y="40" font-family="{FONT}" font-size="26" font-weight="800" fill="{t["text"]}">Also built</text>
<text x="168" y="40" font-family="{FONT}" font-size="18" fill="{t["muted"]}">some code is private, happy to walk through it</text>
{tiles}
</svg>'''


def main() -> None:
    for name, t in THEMES.items():
        (OUT / f"header-{name}.svg").write_text(header(t), encoding="utf-8", newline="")
        (OUT / f"also-{name}.svg").write_text(also(t), encoding="utf-8", newline="")
        for key in CARDS:
            (OUT / f"card-{key}-{name}.svg").write_text(card(t, key), encoding="utf-8", newline="")
    for p in sorted(OUT.glob("*.svg")):
        print(f"{p.name:28} {p.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
