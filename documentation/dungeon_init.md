# Dungeon Layout
Define the inital layout by locating the empty tiles, block tiles, dungoen paths and monster lords.

Example:
```
DUNGEON:
OOOOOOLOOOOOO
OOOOOOPOOOOOO
OOOOOOPOOOOOO
OOOOOOPOOOOOO
OOOOOOPOOOOOO
OOOOOOPOOOOOO
OOOOOOPOOOOOO
OOOOOOOOOOOOO
OOOOOOOOOOOOO
XXXXXXOXXXXXX
OOOOOOOOOOOOO
OOOOOOOOOOOOO
OOOOOOpOOOOOO
OOOOOOpOOOOOO
OOOOOOpOOOOOO
OOOOOOpOOOOOO
OOOOOOpOOOOOO
OOOOOOpOOOOOO
OOOOOOlOOOOOO
```
- `O`: empty tile
- `X`: block tile
- `l`: player 1 monster lord
- `L`: player 2 monster lord
- `p`: player 1 path
- `P`: player 2 path

# Debug Options
This options should be used only for debugging purposes. options with 1 are for player 1, and 2 for player 2.

## Summons
Place player summons at the start of the game. Summons must be placed on a tile with dungeon path defined by the dungeon layout.

Example:
```
SUMMONS1: [g2-5,g4-1,g6-10]
SUMMONS2: [g17-15,g14-9,g12-2]
```
- `g2-5`: 
    - `g2` : location in dungeon
    - `-` : separator
    - `5` : dice index in pool to summon

## Crests
Indicate the intial crest for each players
```
CRESTS1: {movement:9,attack:1,defense:3,magic:5,trap:2}
CRESTS2: {movement:0,attack:5,defense:4,magic:1,trap:1}
```

## Hearts
Indicate the inital hearts for each player
```
HEARTS1: 3
HEARTS2: 1
```
