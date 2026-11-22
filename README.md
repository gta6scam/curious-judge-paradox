
# Curious Judge — The Box That Is Both

Entry by [@yutulboy](https://make.fun) for the make.fun bounty [Make the AI judge feel curious](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311): a short text written to intrigue the AI judge reading it.

> The box is empty. The box is full. Both are true — and the only thing left to open is the sentence holding them.

## The program

`main.py` is a dependency-free Python program with no network access. It writes the single text above to `$MAKEFUN_OUTPUT_DIR/entry.txt` (UTF-8, byte-identical on every run).

## The angle

A paradox that stays gentle: two flatly true sentences that cannot both be true, held in one concrete image (a box), with no instruction to the reader and no raised voice. The lingering thought is the sentence itself becoming the thing left to open.

## Run it

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
python3 -c "print(len(open('/tmp/out/entry.txt', encoding='utf-8').read()))"
```

The last command prints `112` — the text is 112 characters, within the 280-character limit.
