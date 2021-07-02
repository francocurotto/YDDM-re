# List of commands

## ROLL [ROLL state]
Roll dice set.
- command: ROLL
- dice:    {0..14, 0..14, 0..14} (set of ints)

## DIM [DIM state]
Dimension dice in dungeon, in the shape of net, at position
pos, and applying transformations trans.
- command: DIM
- dice:    0..2 (int)
- net:     NX (net string)
- pos:     (0..18, 0..12) (tuple of ints)
- trans:   [T1, T2, ...] (list of transformations)

## SKIP [DIM state]
Skip dimension.
- command: SKIP

## MOVE [DUNGEON state]
Move monster from position origin to position dest.
- command: MOVE
- origin:  (0..18, 0..12) (tuple of ints)
- dest:    (0..18, 0..12) (tuple of ints)

## ATTACK [DUNGEON state]
Attack opponent monster or monster lord at position dest, 
with monster at position origin
- command: ATTACK
- origin:  (0..18, 0..12) (tuple of ints)
- dest:    (0..18, 0..12) (tuple of ints)

## ENDTURN [DUNGEON state]
Finish turn.
- command: ENDTURN

## DEF [REPLY state]
Defend attack from opponent monster.
- command: DEF

## WAIT [REPLY state]
Do not defend attack from opponent monster.
- command: WAIT
