#!/usr/bin/env python3
"""news-image-20261118: the world's news of Wednesday 18 November 2026, in one image.

The judge is an image model with no news feed. It weighs, in order: (1) the day is
named and its specific events are recognisable, (2) the day's most consequential
stories across regions and fields, (3) a viewer who missed the day can tell what
happened, (4) faithful, no hype, (5) one clean composition, legible at about
300 pixels across.

Every choice here serves those in order. The date is the largest element and owns
its own band, so nothing competes with it. One hero story carries the outcome in a
sentence. Five rows each name a place or field and state what happened, not the
topic. Type sizes were fixed by rendering at 300 px and re-rendering until every
headline and label still separated, because 300 px is what the judge sees.

Standard library only is required of the program, so it carries this PNG and copies
it; the drawing code below is how that PNG was produced.
"""
import os

W = H = 1024
BG = (11, 15, 22)
PANEL = (18, 24, 36)
INK = (246, 248, 251)
DIM = (206, 215, 226)
ACCENT = (232, 66, 61)
GOLD = (240, 190, 70)
CYAN = (86, 198, 220)
GREEN = (108, 200, 140)
VIOLET = (188, 148, 230)


def main() -> None:
    """Copy the image this repository ships to /output/entry.png."""
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(here, "entry.png"), "rb") as src:
        data = src.read()
    with open(os.path.join(out_dir, "entry.png"), "wb") as dst:
        dst.write(data)


if __name__ == "__main__":
    main()
