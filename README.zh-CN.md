# Github Chess

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | **中文** | [日本語](README.ja.md) | [Русский](README.ru.md)

通过 GitHub Issues 玩的社区国际象棋 — 该你走了！

_详细内容（列表、链接、描述）以英文维护 — 以下章节为你指引。_

## ♟️ Community chess, powered by GitHub Issues

The board lives in this README. Anyone can play — moves are submitted as Issues.

## 🎮 How to play

1. Check the current board below (updated by the bot after each move)
2. Open an [Issue](../../issues/new) titled with your move in algebraic notation — e.g. `chess: e2e4`
3. A bot validates the move, plays it on the board, and closes the issue
4. First come, first served — one move per person until someone else plays!

## 📋 Current position

```
    a   b   c   d   e   f   g   h
  ┌───┬───┬───┬───┬───┬───┬───┬───┐
8 │ ♜ │ ♞ │ ♝ │ ♛ │ ♚ │ ♝ │ ♞ │ ♜ │ 8
  ├───┼───┼───┼───┼───┼───┼───┼───┤
7 │ ♟ │ ♟ │ ♟ │ ♟ │ ♟ │ ♟ │ ♟ │ ♟ │ 7
  ├───┼───┼───┼───┼───┼───┼───┼───┤
6 │   │   │   │   │   │   │   │   │ 6
  ├───┼───┼───┼───┼───┼───┼───┼───┤
5 │   │   │   │   │   │   │   │   │ 5
  ├───┼───┼───┼───┼───┼───┼───┼───┤
4 │   │   │   │   │   │   │   │   │ 4
  ├───┼───┼───┼───┼───┼───┼───┼───┤
3 │   │   │   │   │   │   │   │   │ 3
  ├───┼───┼───┼───┼───┼───┼───┼───┤
2 │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ 2
  ├───┼───┼───┼───┼───┼───┼───┼───┤
1 │ ♖ │ ♘ │ ♗ │ ♕ │ ♔ │ ♗ │ ♘ │ ♖ │ 1
  └───┴───┴───┴───┴───┴───┴───┴───┘
    a   b   c   d   e   f   g   h
```

**White to move.** Move count: 0

## 🏅 Hall of fame

| Player | Moves |
|---|---|
| *nobody yet — be the first!* | — |

_Inspired by the legendary timburgan/timburgan community chess experiment._

## 🧠 How the game engine works

1. You open an issue with a move in algebraic notation (`e2e4`, `Nf3`, `O-O`)
2. The Action validates the move with python-chess
3. Board state lives in `game/state.fen` — the README renders it
4. Bot replies instantly with a Stockfish-lite move (or random if unset)
5. Leaderboard updates — every player appears in `game/players.md`

## ♟️ Move notation reference

| You type | Meaning |
|---|---|
| `e2e4` | Pawn from e2 to e4 |
| `g1f3` | Knight g1→f3 |
| `e1g1` | Castle kingside (O-O) |
| `d7d5q` | Pawn promotes to queen |
| `resign` | Forfeit |

## 🏆 Why this works

Timburgan's version hit 56,000 commits because each move is a *real* commit by a real person — the repo stays perpetually active in feeds. Every player becomes a contributor.

---
## 贡献

欢迎提交 Pull Request，我们会审查并合并。由 [aixisstudio](https://github.com/aixisstudio) 维护，他也是开源应用防火墙 [Snitch](https://github.com/aixisstudio/Snitch) 的作者。

## 许可证: MIT
