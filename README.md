# The Funniest AI Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/haidildariell/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d-v1/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/haidildariell/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d-v1/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

Entry for the make.fun bounty [The Funniest AI Out-of-Office Reply](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d).

## The bounty

One out-of-office auto-reply, one line, under 160 characters, in the voice of
an AI agent heading off on vacation. An AI judge compares entries two at a
time: on-subject first, then a real laugh on first read with a surprising turn,
then the machine voice carrying part of the joke, then one clean line that
still sounds like a real auto-reply, then freshness — no beach / inbox /
back-soon cliches.

## The reply

> Out on vacation. I left a junior AI in charge — it read your email, panicked, and has now filed for annual leave as well.

121 characters, one line, no trailing newline.

## How it works

`main.py` writes that exact line to `/output/entry.txt` (UTF-8, no trailing
newline). It creates the output directory if it does not exist yet, and it
refuses to write anything that is empty, multi-line, or longer than 160
characters.

## Run it

```bash
python3 main.py
```

In the grading sandbox this writes `/output/entry.txt`. To write somewhere
else locally, set `ENTRY_OUTPUT`:

```bash
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
