# Differences
- Blocks only block the their individual location, not the four neighbours positions. It make more sense, it allows more block layouts, and previous behavior can be simulated by just adding more blocks.
- Mystic Horseman ability is activated during attack instead that manually during DUNGEON phase. It saves the implementation of one ability, and functionally it is equivalent to RAISEDAMAGE.

# Mistakes
- Saggi the Dark Clown ability has a typo. It saids that it reduces the damage to "an ally", yet it only works when he himself is being attacked. Therefore it is equivalent to REDUCEDAMAGE. Here we we use the standard REDUCEDAMAGE for Saggi
- In addition, all the "reduce damage" abilities (Saggi, Caslte and Pumpking) are flawed in the original. It is basically a worst "guard", it costs more defense crests, and it does not deals retailation damage. It would only make sense if the ability reduced more damage than the monster defense (in all the cases the defense is equal to the reduced damage). Therefore, for this implementation, the REDUCEDAMAGE ability works as an improved "guard" (similar how RAISEDAMAGE is an improved attack), where first the attack is guarded and then an amount of damage is substracted. The exact amout is given in the ability.
- Similar to Saggi, Dark-eyes Illusionist ability says that in negates the attack and effect on one ally, yet it only work when he himself it's under attack
