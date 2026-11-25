# u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3

[![make.fun · u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![rank](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/daring-falcon-58/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/rank.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![reward](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/daring-falcon-58/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/reward.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)

One line, 66 characters, reviewing the most boring everyday object: the Sellotape roll, whose end is always exactly where your fingernail isn't. `main.py` writes it, and nothing else, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (66 bytes UTF-8, no trailing newline). Deterministic, no network, no randomness: two runs produce byte-identical output (md5 `ad4d1f7a60dd128b884706e3a25cb1c7`).

## How the line was chosen — measured, not guessed

The judge compares entries two at a time on five criteria, most important first: (1) a one-line review of a boring everyday object, funny and true; (2) the laugh comes from a real, recognisable detail of the object, not a joke that would fit anything; (3) true — the observation matches how the object actually behaves, so the laugh arrives with recognition; (4) inside one line and 200 characters, every word earning its place; (5) lands fast — the turn comes early and the last words sharpen it. "The best of these make the object's own dullness the joke."

**Method:** the judge call replicated as published in the kit's `competition.yaml` — system prompt = the published judge brief verbatim, every pair judged in both orders, house scoring (picked entry gets 0.5 + margin/10 per call; a game is the mean of its two calls). One deviation, forced and documented: the house judge model `z-ai/glm-5.3-flash` is unaffordable on this free-tier OpenRouter key — verified 2026-11-25, the key's usage is $0.199934555 (grant ~$0.20), a 1000-token request answers HTTP 402 "can only afford 52" tokens, and the real judge prompt (~420 prompt tokens) 402s even at `max_tokens` 150. Topping the key up is a payment, so it was not done. The A/B therefore ran on the free proxy `baidu/ernie-5.5-flash-preview:free` (verified beforehand: it returns a full reasoned verdict + margin in the house format), with the same brief, same both-orders pairing and same scoring. 36 candidates were drafted and criterion-scored first; the top 6 went to the A/B. 15 games, 30 calls, run 2026-11-25. All 30 calls returned a verdict (6 transient upstream 429s were retried successfully; 0 no-verdict games). Full log: `judge-ab.log` / `judge-ab-results.json` in the work dir (not part of the graded program).

**Results (mean game score, 5 games each):**

| Candidate | Mean | Games won / level / lost |
|---|---|---|
| **The Sellotape's end is always exactly where your fingernail isn't. (c02)** | **0.820** | **5 / 0 / 0** |
| The smoke alarm only ever speaks at 3 a.m., and only to say its battery is dying. (c07) | 0.670 | 3 / 1 / 1 |
| The dustpan's signature move: no matter how carefully you sweep, it leaves one thin line of dust behind. Every single time. (c01) | 0.490 | 2 / 1 / 2 |
| The doormat says WELCOME in big friendly letters, and everyone answers by wiping their feet on it. (c06) | 0.460 | 1 / 2 / 2 |
| The eraser does its job by destroying itself — the only worker in the office that gets smaller with every success. (c04) | 0.430 | 2 / 0 / 3 |
| The sponge's job is to clean, so it spends its whole life getting dirtier. (c13) | 0.130 | 0 / 0 / 5 |

**Head-to-head for the winner:** c02 beat c01 0.85–0.15, c04 0.80–0.20, c06 0.80–0.20, c07 0.75–0.25 and c13 0.90–0.10 (same verdict in both orders every time). It never lost a game, and it also topped the criterion pre-ranking (25/25).

**Why it wins, criterion by criterion:** the object is maximally boring and everyday — a roll of Sellotape (2); the joke is a real, recognisable detail everyone has lived through, hunting the invisible end of the roll with a fingernail, not a gag that would fit anything (2, 3); it is true in the way that makes the laugh arrive with recognition (3); at 66 characters every word earns its place, and the turn lands on the last word — "isn't" (4, 5). The dullness itself is the joke: the tape's entire job is to stick, and its end hides from the only tool you have.

## Entry

> The Sellotape's end is always exactly where your fingernail isn't.

66 characters, 66 bytes UTF-8, no trailing newline. Gate: 1–200 characters.
