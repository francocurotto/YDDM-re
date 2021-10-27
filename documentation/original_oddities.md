Here I document the mistakes and oddities that I found while analysing the original game while working in this project. Most of the mistakes stem from weirdly of flat out wrong implementation of monster abilities. Since my goal is of reimplementation, unless stated otherwise, those weird behavior are kept in in this game.

# Weird logic
- In the original, a block tile forbid the dimension of a dice not only in its position, but in its 4 adjacent neighbors. In this implementation, a block in forbids dimensions only in its position, but the original behavior can be replicated by adding more block tiles.
- Mystic Horseman ability is essentially the same as the one from Swamp Battleguard RAISEATTACK, except it cost a magic crest instead of an attack crest, and it has to be activated before attack. Functionally it has the same utility. The additional ability DUNGRAISEATTACK is created to copy Horseman ability
- The "reduce damage" abilities from Saggi the Dark Clown, Castle of D. Magic and Pumpking the King of Ghosts make no sense in their implementation. It is basically a worst "guard": it costs more defense crests, and it does not deals retaliation damage. It would only make sense if the ability reduced more damage than the monster defense (in all the cases the defense is equal to the reduced damage). Nevertheless this behavior is kept in this implementation.
- Maybe due to a bad implementation (see typo section), but Dark-eyes Illusionist ability is the same as the one from Strike Ninja, yet, the first one is a higher level dice, a worst monster, and the ability cost more crests. This makes Dark-eyes Illusionist significantly worst with no apparent reason.
- When the attack or defense of a monster goes over 120 though abilities, the stat goes immediately down to 0 for some reason. Still unsure how that affect actual attacks and guards.

# Typos
- Saggi the Dark Clown ability saids that it reduces the damage to "an ally", yet it only works when he himself is being attacked. Therefore it is equivalent to the "reduce damage" ability of Castle of D. Magic and Pumpking the King of Ghosts (i.e. the REDUCEDAMAGE ability)
- Similar to Saggi, Dark-eyes Illusionist ability says that in negates the attack and effect on one ally, yet it only work when he himself it's under attack
