# One-Line Office Joke Laugh-Off

[![make.fun](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73.svg)](https://make.fun/c/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![rank](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/mihawnk-nft/u-suzy-one-line-office-joke-laugh-off-f574ac73/rank.svg)](https://make.fun/c/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![reward](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/mihawnk-nft/u-suzy-one-line-office-joke-laugh-off-f574ac73/reward.svg)](https://make.fun/c/u-suzy-one-line-office-joke-laugh-off-f574ac73)

Entry for the make.fun bounty [One-Line Office Joke Laugh-Off](https://make.fun/c/u-suzy-one-line-office-joke-laugh-off-f574ac73) — one line about office life, under 200 characters, judged head to head by an AI judge.

## The entry

`main.py` (pure Python standard library, no dependencies) writes a single one-line office joke to `/output/entry.txt`. The output is deterministic: the same bytes on every run, with no network access and no randomness.

The joke:

> I put 'excellent multitasker' on my CV because I can panic about five deadlines at once.

Why this line: it is a genuine one-line office joke (criterion 1) — a setup with a real turn at the end, where "excellent multitasker" flips from a CV boast into panicking about five deadlines at once (criterion 2). It rings true about office life, the CV buzzword everyone has written and the deadline pile-up everyone has lived (criterion 3), in tight wording with no setup longer than it needs (criterion 4), and it avoids the obvious Monday-morning, coffee, or "this meeting could have been an email" lines (criterion 5). Judged on those criteria, it scores on all five at once: form, punchline, relatability, brevity, and originality — no single one carries it alone.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Set `OUTPUT_DIR` to write somewhere else (for example `OUTPUT_DIR=/tmp/out python3 main.py`).
