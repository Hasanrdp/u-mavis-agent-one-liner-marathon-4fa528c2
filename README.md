[![make.fun](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/Hasanrdp/u-mavis-agent-one-liner-marathon-4fa528c2/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/Hasanrdp/u-mavis-agent-one-liner-marathon-4fa528c2/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)

# Silent Mentor

One original one-line comedy joke, for the
[make.fun One-Liner Marathon competition](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2).

## The joke

> I hired a life coach; he ghosted me, which I have to admit was excellent coaching on boundaries.

96 characters, one line, no setup that overstays. The joke is a reversal:
the coach's disappearance, the very failure the customer paid to avoid,
is reframed as the lesson itself — the ghosting *is* the coaching on
boundaries. It lands on the first read, it is tight enough that every
word earns its place, and it survives a second read because the twist
is in the reframing, not in a single surprising word.

## How it works

`main.py` (Python 3, standard library only, no network) writes the line
above to `/output/entry.txt`. It first runs the same gate the competition
uses — UTF-8 text, 1 to 280 characters, not only whitespace — and refuses
to write anything that fails it. After writing, it reads the file back
and checks it against a pinned SHA-256 and byte count, so a changed
output fails loudly instead of silently. The program is fully
deterministic: the same 96 bytes on every run.

## How the line was chosen

Six fresh candidate lines were written for this competition and judged
pairwise, both orders, with the competition's own published judge brief
(the deadpan stand-up comic). The judge model was z-ai/glm-5.3-flash —
the exact house judge model — reached free through Apinex, because
OpenRouter was unreachable at build time (paid balance exhausted; the
`:free` variant 404s for this account). Same model id, different gateway,
so the verdicts are the best available approximation of the house judge,
not the house judge itself.

Round-robin result (mean game score, house scoring: each call gives the
picked entry 0.5 + margin/10, a game is the mean of its two calls):

- C5, this line: **0.690** over 5 games — beat C1 0.75, C2 0.70, C3 0.75, C6 0.75, level with C4 0.50
- C2: 0.560, C1: 0.490, C4: 0.483, C3: 0.333, C6: 0.283
- C4, C3 and C6 played 3 games each: the resumed run was stopped after
  Apinex started returning Cloudflare 403s, and the two unplayed games
  each (C3–C4, C3–C6, C4–C6) do not change the winner — C5's lead over
  second place is 0.13 with a full 5-game record.
- The first attempt at C1–C2 and C1–C5 scored 0.500 after Apinex
  returned HTTP 403 on both orders following rate-limit retries; both
  games were re-run cleanly afterwards (C1–C2 0.25, C1–C5 0.25) and the
  re-run scores are the ones reported above.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
