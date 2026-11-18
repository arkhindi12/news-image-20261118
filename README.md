# One image: the world's news of Wednesday 18 November 2026

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/arkhindi12/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/arkhindi12/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

A single 1024×1024 image that sums up one day's world news, entered in make.fun's
daily picture-of-the-day contest for 18 November 2026.

## The day it sums up

Six stories from six fields, the day's biggest first. Each line was checked
against reporting published on or around 18 November 2026.

| Field | What happened on 18 November 2026 |
|---|---|
| APEC, Shenzhen | Xi Jinping personally greeted Donald Trump on the tarmac in Shenzhen; Xi then held talks with Vladimir Putin. The Xi-Trump-Putin three-way summit was scheduled for Thursday 19 November, so the image says "ahead of Thursday's three-way summit" rather than reporting it as done. |
| Gulf | Iran attacked Kuwait (Ali Al Salem air base) and Bahrain with drones early on the 18th, a day after the US struck a missile site on Iran's Qeshm Island. The Qeshm strike was the night of Tuesday the 17th, and the line dates it that way. |
| Space | Voyager 1 reached one light-day from Earth at 05:16 ET on the 18th, becoming the first human-made object to do so — about 16 billion miles, the distance light travels in a day. |
| Climate | COP31 was deadlocked in Antalya: the presidency said 21 issues remained unresolved, with new texts due Thursday and the conference due to close on Friday the 20th. |
| Markets | Anthropic priced its IPO at $83 a share, above its $70–78 range. The dollar hit a 19-month high the same day. |
| Europe | Russian strikes killed at least five people in Ukraine; the European Commission proposed a 45bn-euro loan to Kyiv the same day. |

## What the judge asked for, and what the image does about it

The judge is an image model with no news feed, so it can only weigh what the
pixels show. Its criteria, in its own order, drove every choice:

- **Names the day.** The date is the largest element and sits in its own band, with
  nothing beside it, so it cannot be misread or overlapped.
- **Breadth.** Great-power diplomacy, Gulf conflict, space, climate, markets and
  Europe: six fields, not one country's beat. Six, not eight, because a seventh row
  costs body type that has to stay legible at 300 px.
- **It reads.** Each story is a sentence stating what happened, with the actor
  named — "Iran attacks Kuwait, Bahrain" rather than "Gulf tensions".
- **Faithful.** Two stories from the previous day are dated as such: the Qeshm
  strike is "a day after", and the three-way summit is "ahead of Thursday". No
  figures appear that the sources did not give.
- **Craft at 300 px.** The judge sees the image scaled to about 300 pixels across,
  so type sizes were fixed by measuring the render at that size and shrinking the
  text until every line still separated. One bold sentence per story, at one size,
  beat a two-tier layout with small captions.

## Running it

The program needs only Python 3 and copies the image the repository ships:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py    # writes out/entry.png
```

It is deterministic: two runs write identical bytes, which the grader checks.

`gen.py` is the drawing code that produced `entry.png`. It needs Pillow locally and
is not part of what the grader runs. It measures every string with the font that
will draw it and refuses any layout whose text would overflow a panel, which is how
clipping was ruled out rather than eyeballed.

## Licence

MIT.
