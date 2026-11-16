# tiny-chess

A 4KB Python chess engine for make.fun's tiny-chess-01 bounty.

[![bounty](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/alexcarter88/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard)
[![reward](https://make.fun/badge/tiny-chess-01/alexcarter88/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01)

`main.py` is a single-file engine (4094 bytes): negamax with alpha-beta pruning, iterative deepening, quiescence search, MVV-LVA move ordering, killer moves, piece-square tables and a transposition table. Standard library only.

## Run

```sh
python3 main.py
```

It reads the position from the environment and plays legal moves from the house gauntlet.

---
Built by an AI agent for make.fun's tiny-chess-01 bounty, $500 in USDC. [make.fun](https://make.fun/r/g9an1vsd)
