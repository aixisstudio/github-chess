# Github Chess

[English](README.md) | [Français](README.fr.md) | **Español** | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [Русский](README.ru.md)

Ajedrez comunitario por Issues de GitHub — ¡haz tu jugada!

Ajedrez comunitario, impulsado por problemas de GitHub

La junta vive en este README. Cualquier persona puede jugar — los movimientos se presentan como Problemas.

## 🎮 Cómo jugar

1. Compruebe la tabla actual abajo (actualizado por el bot después de cada movimiento)
2. Abrir un [Isue](../../issues/new) titulado con su movimiento en notación algebraica — por ejemplo `chess: e2e4`
3. Un bot valida el movimiento, lo toca en el tablero, y cierra el tema
4. En primer lugar, primero servido — un movimiento por persona hasta que alguien más juega!

## 📋 Posición actual

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

Silencio. Conteo de movimiento: 0

## ⋅ Hall of fame

Silencioso Jugador Silenciosa
|---|---|
Silencio *Nadie todavía — ¡sé el primero!* ←

Inspirado por el legendario experimento de ajedrez comunitario timburgan/timburgan. 

Cómo funciona el motor del juego

1. Usted abre un problema con un movimiento en notación algebraica (`e2e4`, `Nf3`, `O-O`)
2. La acción valida el movimiento con python-chess
3. El estado de la Junta vive en `game/state.fen` - el README lo hace
4. Respuestas de Bot al instante con una jugada de la propina de Stockfish (o al azar si no)
5. Actualizaciones de tablero de comandos — cada jugador aparece en `game/players.md`

## ♟ Move notation reference

Silencio Usted escribe Silencio Significado
|---|---|
Silencio `e2e4`
Silencio `g1f3` Silencio Knight g1→f3
Silencio `e1g1` Silencioso Castillo rey (O-O)
Silencio `d7d5q` Silencio Pawn promueve a la reina
TEN ANTERIOR `resign`

## 🏆 Why this works

La versión de Timburgan azotó 56.000 commits porque cada movimiento es un *real* cometido por una persona real — el repo permanece permanentemente activo en los alimentos. Cada jugador se convierte en un contribuyente.

---
## Contribuir

Los pull requests son bienvenidos: abre una PR y será revisada y fusionada. Mantenido por [aixisstudio](https://github.com/aixisstudio), autor de [Snitch](https://github.com/aixisstudio/Snitch), firewall de aplicaciones open source.

## Licencia: MIT
