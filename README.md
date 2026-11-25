# The Router Confesses

[![License: MIT](https://img.shields.io/github/license/nelsenwiliam/makefun-router-confesses)](LICENSE)
[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-7c3aed)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue)](main.py)

One line, at most 200 characters, that a home Wi-Fi router would say to
excuse itself for dropping the connection at the exact moment a movie
reaches its climax. Entry for the make.fun bounty
[The Router Confesses](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e).

## The line

> I already know who dies in the end, and unlike you, I have the self-control to keep it to myself.

The router is not apologising for a technical failure — it knows the
ending and dropped the connection on purpose rather than spoil it. A
smug little secret, in the router's own voice, in one breath, dodging the
buffering / bandwidth / firmware jokes everyone has already heard.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (or `output/entry.txt` when run by
hand on a machine without a writable `/output`). Pure Python standard
library, no third-party packages.
