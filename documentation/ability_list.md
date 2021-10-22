


# CURE
- parameters:
    - amount: int
- description: Cures "amount" hearts to a monster

# DAMAGE
- parameters:
    -amount: int
-description: Removes "amount" hearts to a monster

# TIMEMACHINE
-description: Returns monster to its last location

# BUFF
- parameters:
    - attribute: (attack, defense, life)
    - amount: int
- description: Raises monster "attribute" by "amount"

# DISCARDCREST
- parameters:
    - crest: (movement, attack, defense, magic, trap)
    - amount: int
- description: Destroys "amount" crest of type "crest" in own crest pool

# GLUMINIZER
- description: Doubles the movement cost of all monsters

# RESURRECT
- description: Resurrects one death monster on own graveyard

# VORTEX
- description: summons a warp wortex

# BLACKHOLE
- description: destroys all monsters in the dungeon
