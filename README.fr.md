# Github Chess

[English](README.md) | **Français** | [Español](README.es.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [Русский](README.ru.md)

Échecs communautaires via les Issues GitHub — à toi de jouer !

Les échecs communautaires, propulsés par GitHub Issues

Le conseil vit dans ce README. N'importe qui peut jouer — les mouvements sont soumis comme des problèmes.

Comment jouer

1. Vérifiez le tableau actuel ci-dessous (mise à jour par le robot après chaque déplacement)
2. Ouvrir une [Question](../../issues/new) intitulée avec votre déménagement en notation algébrique — par exemple `chess: e2e4`
3. Un bot valide le mouvement, le joue sur le tableau, et ferme le problème
4. Premier arrivé, premier servi — un déménagement par personne jusqu'à ce que quelqu'un d'autre joue!

Situation actuelle

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

** Blanc à déplacer.** Déplacement : 0

Salle de gloire

Le joueur bouge
|---|---|
*Personne encore — soyez le premier!

Inspiré par la légendaire expérience d'échecs de la communauté timburgaine/timburgaine. 

Comment fonctionne le moteur de jeu

1. Vous ouvrez un problème avec un mouvement en notation algébrique (`e2e4`, `Nf3`, `O-O`)
2. L'Action valide le mouvement avec python-chess
3. L'Etat du Conseil vit dans `game/state.fen` — le README rend
4. Bot répond instantanément avec un mouvement Stockfish-lite (ou aléatoire si non défini)
5. Mises à jour Leaderboard — chaque lecteur apparaît dans `game/players.md`

Référence de notation de déplacement

Vous tapez la signification
|---|---|
`e2e4`=Pion de e2 à e4=
`g1f3`: Chevalier g1→f3
`e1g1`: Château kingside (O-O)
`d7d5q`: Pawn fait la promotion de la reine
`resign`

Pourquoi ça marche ?

La version de Timburgan a frappé 56.000 commits parce que chaque mouvement est un commit *réel* par une personne réelle — la repo reste perpétuellement active dans les flux. Chaque joueur devient un contributeur.

---
## Contribuer

Les pull requests sont les bienvenues : ouvre une PR, elle sera relue et fusionnée. Maintenu par [aixisstudio](https://github.com/aixisstudio), auteur de [Snitch](https://github.com/aixisstudio/Snitch), pare-feu applicatif open source.

## Licence: MIT
