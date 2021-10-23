# FLY
- type: continuous
- description: Monster has fly property

# ARCHER
- type: continuous
- description: Monster has archer property

# TUNNELING
- type: continuous
- description: Monster has tunneling property

# NEUTRAL
- type: continuous
- description: Monster has no type advantages or disadvantages

# CANCELFLY
- type: continuous
- description: Presents all flying

# CANCELTUNNEL
- type: continuous
- description: Prevents all tunneling

# KILLMONSTER
- type: activation
- parameters:
    

# CURE
- type: activation
- parameters:
    - amount: int
- description: Cures "amount" hearts to a monster

# DAMAGE
- type: activation
- parameters:
    -amount: int
-description: Removes "amount" hearts to a monster

# TIMEMACHINE
- type: activation
-description: Returns monster to its last location

# BUFF
- type: continuous
- parameters:
    - attribute: (attack, defense, life)
    - amount: int
- description: Raises monster "attribute" by "amount"

# DISCARDCREST
- type: activation
- parameters:
    - crest: (movement, attack, defense, magic, trap)
    - amount: int
- description: Destroys "amount" crests of type "crest" in own crest pool

# GLUMINIZER
- type: continuous
- description: Doubles the movement cost of all monsters

# RESURRECT
- type: activation
- description: Resurrects one death monster on own graveyard

# VORTEX
- type: activation
- description: summons a warp wortex

# BLACKHOLE
- type: activation
- description: destroys all monsters in the dungeon
