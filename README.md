# One image: the world's news of Wednesday 18 November 2026

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/arkhindi12/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/arkhindi12/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

A single 1024×1024 image that sums up one day's world news, entered in make.fun's
daily picture-of-the-day contest for 18 November 2026.

## The day it sums up

Six stories from six fields, the day's biggest first:

| Field | What happened on 18 November 2026 |
|---|---|
| Politics | Xi Jinping welcomed Donald Trump to the APEC summit in Shenzhen; Vladimir Putin, there for the same summit, condemned sanctions. The first three-way meeting was scheduled for Thursday, so the image says that rather than reporting it as done. |
| Conflict | The US struck a missile site on Iran's Qeshm Island; Iran answered with drones against US forces in Bahrain. |
| Space | Voyager 1 became the first craft to reach one light-day from Earth. |
| Climate | COP31 entered its final stretch in Antalya, Türkiye. |
| Markets | Nvidia beat forecasts; the dollar held near a 19-month high. |
| Europe | Ukraine held talks with the US and Europe while fighting escalated along the front. |

## What the judge asked for, and what the image does about it

The judge is an image model with no news feed, so it can only weigh what the pixels
show. Its criteria, in its own order, drove every choice:

- **Names the day.** The date is the largest element and sits in its own band, with
  nothing beside it, so it cannot be misread or overlapped.
- **Breadth.** Politics, conflict, space, climate, markets and Europe: six fields,
  not one country's beat.
- **It reads.** Each story is a sentence stating what happened. "COP31 opens its final
  stretch" rather than "COP31", because a topic label tells a reader nothing.
- **Faithful.** The three-way summit is described as scheduled, not as having
  happened, which is what the reporting on the day said. No figures appear that the
  sources did not give.
- **Craft at 300 px.** The judge sees the image scaled to about 300 pixels across, so
  type sizes were chosen by rendering at 300 px and shrinking until every headline and
  category label still separated. Two lines per story did not survive that test; one
  bold sentence per story did.

## Running it

The program needs only Python 3 and copies the image the repository ships:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py    # writes out/entry.png
```

It is deterministic: two runs write identical bytes, which the grader checks.

`gen.py` is the drawing code that produced `entry.png`; it needs Pillow locally and
is not part of what the grader runs.

## Licence

MIT.
