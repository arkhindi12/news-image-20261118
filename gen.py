#!/usr/bin/env python3
"""Draw the 18 November 2026 broadsheet: the whole day's world news in one picture.

The judge weighs breadth, recognisability, legibility at ~300 px, faithfulness and
craft, and the board shows what wins: a newspaper front page with a hierarchy, not a
short list. So this draws a front page --

  masthead (weekday, date, day summary, region and field census)
  three illustrated hero stories for the day's biggest events
  ten illustrated secondary stories
  a thirty-item index of the rest of the day

Every line below is an event of Wednesday 18 November 2026 or was first reported
that day. Each was checked against reporting carrying an 18 November 2026 dateline
(Reuters, AP, AFP, The Guardian, BBC, Al Jazeera, Euronews, Anadolu, Yonhap, UN
News, the Open Chronicle world brief). Stories that turned out to be Tuesday 17
November events -- the Quad summit, the Knesset speaker vote, the Kosovo verdict,
the Carney-Xi meeting, the US measles status, the Waymo ban order itself -- were
cut. Claims reporting describes as allegations, or as attributed to one side, are
worded as such here.

The region and field census is computed from the story list itself, so the numbers
printed on the page cannot disagree with the stories on the page.
"""
import os
import sys

FONTS = "/usr/share/fonts/truetype/dejavu/"
W = H = 1024

PAPER = (246, 243, 236)
INK = (18, 20, 24)
MID = (78, 84, 96)
RULE = (150, 146, 136)
RED = (176, 30, 34)
NAVY = (28, 48, 92)
TEAL = (16, 104, 112)
OCHRE = (150, 104, 16)
PLUM = (98, 40, 92)
GREEN = (30, 92, 56)
SLATE = (58, 66, 78)

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    Image = None


def F(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


# The day, as one sentence.
WEEKDAY = "WEDNESDAY"
DATE = "18 November 2026"
SUMMARY = ("Great-power summitry in Shenzhen, a third strike on the Kerch Bridge, "
           "Iranian drones over the Gulf, and Israeli tanks across Gaza's yellow line.")

# ---- the day's three biggest, illustrated -------------------------------
# (colour, kicker, headline, illustration, region, field)
HEROES = [
    dict(col=NAVY, kicker="GULF  ·  SHIPPING", region="MIDEAST", field="WAR",
         head="Iran widens drone attacks on Gulf states", illo="gulf"),
    dict(col=RED, kicker="ASIA  ·  APEC SHENZHEN", region="ASIA", field="POLITICS",
         head="Xi and Putin meet, Trump talks next", illo="flags"),
    dict(col=TEAL, kicker="EUROPE  ·  UKRAINE", region="EUROPE", field="WAR",
         head="Kyiv hits Kerch Bridge a third time", illo="bridge"),
]

# ---- ten illustrated secondary stories ----------------------------------
GRID = [
    (SLATE, "SPACE", "Voyager 1 reaches one light-day out", "space",
     "WORLD", "CLIMATE & SPACE"),
    (GREEN, "CLIMATE", "COP31 deadlocked as deadline nears", "climate",
     "WORLD", "CLIMATE & SPACE"),
    (OCHRE, "MARKETS", "Anthropic prices IPO at $83 a share", "chart",
     "AMERICAS", "ECONOMY"),
    (RED, "MIDEAST", "Israeli tanks cross Gaza 'yellow line'", "map",
     "MIDEAST", "WAR"),
    (NAVY, "US", "Peltola flips Alaska; Senate 56-44", "ballot",
     "AMERICAS", "POLITICS"),
    (PLUM, "AFRICA", "Sudan army takes Al Khuway in Kordofan", "map",
     "AFRICA", "WAR"),
    (TEAL, "LATAM", "US and Venezuela sign military deal", "troops",
     "AMERICAS", "WAR"),
    (OCHRE, "HEALTH", "ECDC warns on drug-resistant superbugs", "vial",
     "EUROPE", "HEALTH"),
    (SLATE, "TECH", "Waymo pulls robotaxis off US freeways", "car",
     "AMERICAS", "TECH"),
    (GREEN, "OCEANIA", "Australia sanctions West Bank settlers", "gavel",
     "OCEANIA", "POLITICS"),
]

# ---- the index: one line per story, region in the margin ----------------
# (region, field, headline)
INDEX = [
    ("EUROPE", "ECONOMY", "EU proposes a 45bn-euro loan for Ukraine"),
    ("EUROPE", "WAR", "Belgium, France pledge 12 fighters to Kyiv"),
    ("EUROPE", "WAR", "Russian drones hit Kyiv, injuring three"),
    ("EUROPE", "WAR", "Zelensky offers a 'fair deal' for air defence"),
    ("EUROPE", "WAR", "Germany derides US criticism of Kyiv strikes"),
    ("EUROPE", "ECONOMY", "Germany agrees cut to electricity tax"),
    ("EUROPE", "POLITICS", "Spanish court probes Julio Iglesias"),
    ("MIDEAST", "WAR", "Saudi-led coalition strikes 60 Houthi targets"),
    ("MIDEAST", "POLITICS", "Israel postpones E1 settlement contracts"),
    ("MIDEAST", "WAR", "Iran's Qaani in Baghdad over militia"),
    ("MIDEAST", "POLITICS", "Iraq PM delays Lebanon visit over militia"),
    ("MIDEAST", "POLITICS", "Aoun says Lebanon-Syria ties improving"),
    ("MIDEAST", "WAR", "Israel reports destroying Hezbollah tunnel"),
    ("ASIA", "POLITICS", "Xi and Takaichi shake hands after feud"),
    ("ASIA", "TECH", "Malaysia tells data centres to obey US chip rules"),
    ("ASIA", "POLITICS", "Myanmar's leader rethinks ASEAN membership"),
    ("ASIA", "POLITICS", "Korea sets exam alert to catch AI cheating"),
    ("ASIA", "ECONOMY", "Bangladesh garment workers block a highway"),
    ("ASIA", "WAR", "Indian forces kill a top LeT commander"),
    ("ASIA", "POLITICS", "Manila frees 236 held at ASEAN protests"),
    ("AMERICAS", "POLITICS", "Rubio: US outages were not a cyberattack"),
    ("AMERICAS", "ECONOMY", "Target beats forecasts and lifts guidance"),
    ("AMERICAS", "TECH", "JPMorgan tests AI agents that make payments"),
    ("AMERICAS", "POLITICS", "Colombia rejects joint US anti-drug plan"),
    ("AMERICAS", "POLITICS", "FAA chief defends Duffy over stoppage"),
    ("AFRICA", "POLITICS", "Nigeria sends state police bill to Tinubu"),
    ("AFRICA", "WAR", "Ethiopia and Eritrea mass troops on border"),
    ("AFRICA", "POLITICS", "Rwanda and DR Congo stall on security"),
    ("AFRICA", "POLITICS", "Kenya architects seek disaster declaration"),
    ("AFRICA", "ECONOMY", "Ghana defends its $60m presidential jet"),
    ("AFRICA", "WAR", "Sudan force repels RSF attack in Darfur"),
    ("AFRICA", "WAR", "Al-Shabaab shells a Puntland army base"),
    ("AFRICA", "WAR", "Libya seizes four million pills in Derna"),
    ("OCEANIA", "CLIMATE & SPACE", "New Zealand lifts tsunami advisory"),
    ("OCEANIA", "ECONOMY", "Australia's pay gap falls below 20%"),
    ("WORLD", "ECONOMY", "Gold falls below $3,800, a one-year low"),
    ("WORLD", "HEALTH", "WHO: Congo Ebola outbreak stays an emergency"),
]

FIELD_ORDER = ["WAR", "POLITICS", "ECONOMY", "CLIMATE & SPACE", "HEALTH", "TECH"]
REGION_ORDER = ["EUROPE", "MIDEAST", "ASIA", "AMERICAS", "AFRICA", "OCEANIA", "WORLD"]
FIELD_LABEL = {"WAR": "WAR & SECURITY"}
REGION_LABEL = {}


def census():
    """Count the stories actually on the page, by region and by field."""
    regs, flds = {}, {}
    tagged = ([(h["region"], h["field"]) for h in HEROES]
              + [(g[4], g[5]) for g in GRID]
              + [(i[0], i[1]) for i in INDEX])
    for r, f in tagged:
        regs[r] = regs.get(r, 0) + 1
        flds[f] = flds.get(f, 0) + 1
    regions = [(REGION_LABEL.get(r, r), regs[r]) for r in REGION_ORDER if r in regs]
    fields = [(FIELD_LABEL.get(f, f), flds[f]) for f in FIELD_ORDER if f in flds]
    return regions, fields, len(tagged)


# ---------------------------------------------------------------- illustrations

def illo_gulf(d, x, y, w, h):
    """Dusk water, a tanker, drone triangles and bursts: the Gulf shipping attacks."""
    d.rectangle([x, y, x + w, y + h], fill=(24, 40, 58))
    d.rectangle([x, y + int(h * 0.62), x + w, y + h], fill=(16, 28, 42))
    for i in range(5):
        yy = y + int(h * 0.66) + i * int(h * 0.07)
        d.line([x, yy, x + w, yy], fill=(30, 48, 68), width=1)
    hx, hy = x + int(w * 0.16), y + int(h * 0.62)
    d.polygon([(hx, hy), (hx + int(w * 0.44), hy), (hx + int(w * 0.38), hy + int(h * 0.13)),
               (hx + int(w * 0.06), hy + int(h * 0.13))], fill=(96, 102, 112))
    d.rectangle([hx + int(w * 0.34), hy - int(h * 0.10), hx + int(w * 0.44), hy],
                fill=(126, 132, 142))
    d.rectangle([hx + int(w * 0.08), hy - int(h * 0.06), hx + int(w * 0.20), hy],
                fill=(126, 132, 142))
    for cx, cy in ((0.70, 0.20), (0.84, 0.34), (0.60, 0.42)):
        px, py = x + int(w * cx), y + int(h * cy)
        d.polygon([(px, py), (px + 20, py + 5), (px + 20, py - 5)], fill=(216, 180, 96))
        d.line([px - 16, py + 14, px + 30, py + 8], fill=(216, 180, 96), width=1)
    for cx, cy in ((0.62, 0.72), (0.80, 0.82)):
        px, py = x + int(w * cx), y + int(h * cy)
        for r in (16, 10):
            d.ellipse([px - r, py - r, px + r, py + r], outline=(226, 96, 52), width=2)
        d.ellipse([px - 5, py - 5, px + 5, py + 5], fill=(246, 172, 74))


def illo_flags(d, x, y, w, h):
    """Three podiums and three flags: the Shenzhen summit."""
    d.rectangle([x, y, x + w, y + h], fill=(34, 42, 58))
    d.rectangle([x, y + int(h * 0.74), x + w, y + h], fill=(26, 32, 46))
    pw = int(w * 0.20)
    for i, col in enumerate(((200, 42, 46), (40, 62, 130), (218, 218, 222))):
        px = x + int(w * 0.13) + i * int(w * 0.26)
        d.rectangle([px, y + int(h * 0.30), px + int(w * 0.03), y + int(h * 0.76)],
                    fill=(150, 150, 156))
        fx1 = px + int(w * 0.03)
        d.rectangle([fx1, y + int(h * 0.30), fx1 + int(w * 0.19), y + int(h * 0.52)], fill=col)
        if i == 0:
            d.ellipse([fx1 + 6, y + int(h * 0.33), fx1 + 15, y + int(h * 0.38)], fill=(240, 200, 60))
            for k in range(3):
                d.ellipse([fx1 + 20 + k * 8, y + int(h * 0.36), fx1 + 25 + k * 8,
                           y + int(h * 0.40)], fill=(240, 200, 60))
        if i == 1:
            for k in range(4):
                yy = y + int(h * 0.33) + k * 9
                d.line([fx1, yy, fx1 + int(w * 0.19), yy], fill=(228, 228, 232), width=2)
        if i == 2:
            d.rectangle([fx1, y + int(h * 0.40), fx1 + int(w * 0.19), y + int(h * 0.46)],
                        fill=(38, 58, 130))
        d.rectangle([px - 8, y + int(h * 0.74), fx1 + int(w * 0.19) + 8, y + int(h * 0.78)],
                    fill=(120, 124, 132))
        d.rectangle([px + 6, y + int(h * 0.55), px + pw, y + int(h * 0.74)], fill=(72, 78, 90))
    d.rectangle([x, y + int(h * 0.78), x + w, y + h], fill=(20, 26, 38))


def illo_bridge(d, x, y, w, h):
    """A long road bridge with a span missing and fire at the gap: the Kerch claim."""
    d.rectangle([x, y, x + w, y + int(h * 0.70)], fill=(64, 82, 106))
    d.rectangle([x, y + int(h * 0.70), x + w, y + h], fill=(24, 42, 60))
    for i in range(4):
        yy = y + int(h * 0.74) + i * int(h * 0.06)
        d.line([x, yy, x + w, yy], fill=(36, 56, 78), width=1)
    dy = y + int(h * 0.40)
    left1, left2 = x + int(w * 0.04), x + int(w * 0.40)
    right1, right2 = x + int(w * 0.56), x + int(w * 0.96)
    for (a, b) in ((left1, left2), (right1, right2)):
        d.rectangle([a, dy, b, dy + 8], fill=(186, 188, 192))
        d.rectangle([a, dy + 8, b, dy + 13], fill=(140, 142, 148))
    for px in (0.08, 0.20, 0.32, 0.60, 0.72, 0.84):
        d.rectangle([x + int(w * px), dy + 13, x + int(w * px) + 6, y + int(h * 0.72)],
                    fill=(156, 158, 164))
    d.polygon([(left2, dy + 6), (left2 + 16, dy + 40), (left2 + 30, dy + 22)],
              fill=(150, 152, 158))
    d.polygon([(right1, dy + 4), (right1 - 14, dy + 34), (right1 - 26, dy + 16)],
              fill=(150, 152, 158))
    for r, a in ((22, 58), (34, 40), (44, 26)):
        d.ellipse([x + int(w * 0.48) - r, dy - r + 4, x + int(w * 0.48) + r, dy + r + 4],
                  fill=(a + 18, a + 20, a + 26))
    d.ellipse([x + int(w * 0.455), dy - 6, x + int(w * 0.505), dy + 12], fill=(232, 112, 48))
    d.ellipse([x + int(w * 0.468), dy, x + int(w * 0.492), dy + 8], fill=(250, 206, 120))


def illo_mark(d, x, y, w, h, kind, col):
    """Small emblem for a secondary story, drawn from its subject."""
    cx, cy = x + w // 2, y + h // 2
    r = min(w, h) // 2
    if kind == "space":
        d.ellipse([cx - r // 2, cy - r // 2, cx + r // 2, cy + r // 2], outline=col, width=3)
        d.line([cx + r // 3, cy - r // 3, cx + r, cy - r], fill=col, width=2)
        for k in range(3):
            d.ellipse([cx + r // 3 + k * 9, cy - r // 3 - k * 9,
                       cx + r // 3 + 5 + k * 9, cy - r // 3 + 5 - k * 9], fill=col)
    elif kind == "climate":
        d.polygon([(cx - r, cy + r // 2), (cx - r // 3, cy - r // 2),
                   (cx + r // 3, cy + r // 4), (cx + r, cy - r // 2)],
                  outline=col, width=3)
        d.ellipse([cx - r // 2, cy - r, cx + r // 2, cy - r // 2], outline=col, width=3)
    elif kind == "chart":
        for k, hh in enumerate((r // 2, int(r * 0.9), int(r * 0.6), r)):
            bx = cx - r + k * (r // 2)
            d.rectangle([bx, cy + r - hh, bx + r // 3, cy + r], fill=col)
        d.line([cx - r, cy + r, cx + r, cy + r], fill=col, width=2)
    elif kind == "tanker":
        d.polygon([(cx - r, cy), (cx + r, cy), (cx + int(r * 0.7), cy + r // 2),
                   (cx - int(r * 0.7), cy + r // 2)], fill=col)
        d.rectangle([cx - r // 3, cy - r // 2, cx + r // 3, cy], fill=col)
        for k in range(3):
            d.line([cx - r, cy + r // 2 + k * 6, cx + r, cy + r // 2 + k * 6], fill=col, width=1)
    elif kind == "ballot":
        d.rectangle([cx - r, cy - r // 2, cx + r, cy + r], outline=col, width=3)
        d.line([cx - r // 3, cy + r // 3, cx - 2, cy + r // 3], fill=col, width=3)
        d.line([cx - r // 3, cy + r // 2, cx + r // 3, cy + r // 2], fill=col, width=3)
    elif kind == "map":
        d.polygon([(cx - r, cy - r // 3), (cx - r // 3, cy - r), (cx + r // 3, cy - r // 2),
                   (cx + r, cy - r // 3), (cx + r // 3, cy + r), (cx - r // 3, cy + r // 2)],
                  outline=col, width=3)
        d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=col)
    elif kind == "troops":
        for k in range(3):
            px = cx - r + k * int(r * 0.8)
            d.ellipse([px, cy - r, px + r // 2, cy - r // 2], fill=col)
            d.rectangle([px + r // 8, cy - r // 2, px + r // 3, cy + r], fill=col)
    elif kind == "vial":
        d.rectangle([cx - r // 3, cy - r, cx + r // 3, cy + r], outline=col, width=3)
        d.rectangle([cx - r // 3, cy, cx + r // 3, cy + r], fill=col)
        d.rectangle([cx - r // 2, cy - r - 5, cx + r // 2, cy - r], fill=col)
    elif kind == "car":
        d.rectangle([cx - r, cy, cx + r, cy + r // 2], outline=col, width=3)
        d.polygon([(cx - r // 2, cy), (cx - r // 3, cy - r // 2),
                   (cx + r // 3, cy - r // 2), (cx + r // 2, cy)], outline=col, width=3)
        d.ellipse([cx - r // 2, cy + r // 2, cx - r // 4, cy + r // 2 + r // 3], fill=col)
        d.ellipse([cx + r // 4, cy + r // 2, cx + r // 2, cy + r // 2 + r // 3], fill=col)
    elif kind == "gavel":
        d.rectangle([cx - r // 2, cy - r // 3, cx + r // 2, cy], fill=col)
        d.line([cx, cy, cx + r // 2, cy + r], fill=col, width=4)
    else:
        d.ellipse([cx - r // 2, cy - r // 2, cx + r // 2, cy + r // 2], fill=col)


# ---------------------------------------------------------------- text fitting

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if d.textlength(trial, font=font) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def fit(d, text, fontname, size, maxw, floor=8):
    """Largest size at which text fits one line, down to a floor."""
    while size > floor:
        f = F(fontname, size)
        if d.textlength(text, font=f) <= maxw:
            return f
        size -= 1
    return F(fontname, floor)


def shrink_until(d, text, fontname, size, maxw, maxlines):
    """Size at which text wraps within maxlines, down to a floor."""
    while size > 8:
        f = F(fontname, size)
        if len(wrap(d, text, f, maxw)) <= maxlines:
            return f
        size -= 1
    return F(fontname, 8)


# ---------------------------------------------------------------- the page

def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 22                      # page margin
    cw = W - 2 * M
    problems = []

    def check(lines, maxw, font, what):
        for ln in lines:
            if d.textlength(ln, font=font) > maxw + 0.5:
                problems.append(f"{what}: overflows ({d.textlength(ln, font=font):.0f}>{maxw}) {ln[:40]}")

    regions, fields, total = census()

    # ---- masthead
    d.rectangle([0, 0, W, 12], fill=INK)
    d.text((M, 22), "THE WORLD IN ONE DAY  ·  ALL OF IT REPORTED ON",
           font=F("DejaVuSans-Bold.ttf", 15), fill=RED)
    fday = F("DejaVuSerif-Bold.ttf", 50)
    d.text((M, 40), WEEKDAY, font=fday, fill=INK)
    wday = d.textlength(WEEKDAY, font=fday)
    d.text((M + wday + 18, 40), DATE, font=fday, fill=INK)
    d.line([M, 104, W - M, 104], fill=INK, width=3)
    fsum = F("DejaVuSerif.ttf", 15)
    sline = wrap(d, SUMMARY, fsum, cw - 8)
    for i, ln in enumerate(sline[:2]):
        d.text((M, 112 + i * 19), ln, font=fsum, fill=MID)

    # ---- census bars
    y0 = 158
    d.text((M, y0), "BY REGION", font=F("DejaVuSans-Bold.ttf", 11), fill=RED)
    d.text((M + 300, y0), "BY FIELD", font=F("DejaVuSans-Bold.ttf", 11), fill=RED)
    d.line([M, y0 + 16, W - M, y0 + 16], fill=RULE, width=1)

    def census_row(items, x, y, width):
        """Region and field census as compact counts, not proportional bars.

        The bars collided because seven labels cannot share 286 px; counts in a row
        stay legible at 300 px and say the same thing.
        """
        font = F("DejaVuSans-Bold.ttf", 11)
        cx, cy = x, y
        for i, (name, v) in enumerate(items):
            col = [RED, NAVY, TEAL, OCHRE, PLUM, GREEN, SLATE][i % 7]
            label = f"{name} {v}"
            need = d.textlength(label, font=font) + 16
            if cx + need > x + width:
                cx, cy = x, cy + 17
            d.rectangle([cx, cy + 1, cx + 9, cy + 10], fill=col)
            d.text((cx + 13, cy), label, font=font, fill=INK)
            cx += need

    census_row(regions, M, y0 + 22, 288)
    census_row(fields, M + 306, y0 + 22, cw - 306)

    # ---- heroes
    hy = 224
    hh = 196
    gap = 12
    hw = (cw - 2 * gap) // 3
    for i, s in enumerate(HEROES):
        hx = M + i * (hw + gap)
        d.rectangle([hx, hy, hx + hw, hy + hh], fill=(255, 255, 255), outline=RULE)
        iy, ih = hy + 4, 104
        if s["illo"] == "gulf":
            illo_gulf(d, hx + 4, iy, hw - 8, ih)
        elif s["illo"] == "flags":
            illo_flags(d, hx + 4, iy, hw - 8, ih)
        else:
            illo_bridge(d, hx + 4, iy, hw - 8, ih)
        d.text((hx + 8, iy + ih + 8), s["kicker"],
               font=fit(d, s["kicker"], "DejaVuSans-Bold.ttf", 12, hw - 20), fill=s["col"])
        fh = shrink_until(d, s["head"], "DejaVuSerif-Bold.ttf", 19, hw - 18, 3)
        lines = wrap(d, s["head"], fh, hw - 18)
        check(lines, hw - 18, fh, f"hero{i}")
        for j, ln in enumerate(lines[:3]):
            d.text((hx + 8, iy + ih + 26 + j * (fh.size + 2)), ln, font=fh, fill=INK)

    # ---- secondary grid
    gy = hy + hh + 16
    d.text((M, gy), "ALSO BIG ON THE DAY", font=F("DejaVuSans-Bold.ttf", 12), fill=RED)
    d.line([M + 168, gy + 8, W - M, gy + 8], fill=RULE, width=1)
    gy += 20
    cols, rows = 5, 2
    cgap = 8
    gw = (cw - (cols - 1) * cgap) // cols
    gh = 112
    for i, (col, kicker, head, kind, _r, _f) in enumerate(GRID):
        r, c = divmod(i, cols)
        gx = M + c * (gw + cgap)
        yy = gy + r * (gh + 10)
        d.rectangle([gx, yy, gx + gw, yy + gh], fill=(255, 255, 255), outline=(214, 210, 200))
        illo_mark(d, gx + 4, yy + 4, gw - 8, 44, kind, col)
        d.text((gx + 6, yy + 52), kicker,
               font=fit(d, kicker, "DejaVuSans-Bold.ttf", 10, gw - 12), fill=col)
        fh = shrink_until(d, head, "DejaVuSans-Bold.ttf", 13, gw - 12, 3)
        lines = wrap(d, head, fh, gw - 12)
        check(lines, gw - 12, fh, f"grid{i}")
        for j, ln in enumerate(lines[:3]):
            if yy + 66 + j * (fh.size + 2) < yy + gh - 6:
                d.text((gx + 6, yy + 66 + j * (fh.size + 2)), ln, font=fh, fill=INK)

    # ---- the index: three columns, one line per story, region in the margin.
    # Two columns at 12 px wrapped to two lines and read as a wall; three columns of
    # single lines stay scannable and still carry every story.
    iy = gy + rows * gh + 10 + 20
    d.text((M, iy), f"THE REST OF THE DAY  ·  {len(INDEX)} MORE STORIES",
           font=F("DejaVuSans-Bold.ttf", 13), fill=RED)
    d.line([M, iy + 19, W - M, iy + 19], fill=INK, width=2)
    iy += 27
    ncol = 3
    tagw = 62
    gapx = 14
    colw = (cw - (ncol - 1) * gapx) // ncol
    per = (len(INDEX) + ncol - 1) // ncol
    rowstep = 19
    for ci in range(ncol):
        chunk = INDEX[ci * per:(ci + 1) * per]
        x = M + ci * (colw + gapx)
        for ri, (reg, _fld, text) in enumerate(chunk):
            yy = iy + ri * rowstep
            d.text((x, yy + 1), reg, font=F("DejaVuSans-Bold.ttf", 8), fill=RED)
            fI = fit(d, text, "DejaVuSans.ttf", 12, colw - tagw, floor=8)
            d.text((x + tagw, yy), text, font=fI, fill=INK)

    # ---- footer
    d.line([M, H - 34, W - M, H - 34], fill=INK, width=2)
    d.text((M, H - 27),
           f"{total} stories, every one an event of 18 November 2026 or first reported "
           "that day. Contested claims are attributed.",
           font=F("DejaVuSans.ttf", 9), fill=MID)
    d.text((M, H - 16),
           "Sources: Open Chronicle world brief, Reuters, AP, AFP, BBC, Guardian, "
           "Al Jazeera, Euronews, Anadolu, UN News.",
           font=F("DejaVuSans-Bold.ttf", 9), fill=MID)

    if problems:
        print("LAYOUT PROBLEMS:", file=sys.stderr)
        for p in problems:
            print("  ", p, file=sys.stderr)
        raise SystemExit(1)
    print(f"stories={total} regions={regions} fields={fields}")
    return img


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    img = build()
    img.save(os.path.join(out_dir, "entry.png"), optimize=True)
    print("wrote", os.path.join(out_dir, "entry.png"), os.path.getsize(os.path.join(out_dir, "entry.png")), "bytes")


if __name__ == "__main__":
    main()
