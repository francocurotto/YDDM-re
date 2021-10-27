# Common Abilities
## TUNNELING
Can move through other monsters, but not items.

## FLY
Can move through other monsters, but not items. Cannot be in the same position as other monster. Other monsters can move through them. They can only be attacked by monster with the ability FLY or ARCHER. Movement cost is 2 crests per square.

## ARCHER
Can attack monster with the ability FLY.

## NEUTRAL
No type advantages or disadvantages.

# Dimension Abilities
## DIMCURE (AMOUNT, NMONSTERS, COSTCREST, COST)
Cures AMOUNT hearts to NMONSTERS number of player monsters.
Cost: COST x COSTCTREST

## DIMCUREALL (AMOUNT) 
Cures AMOUNT hearts to all player monsters.

## DIMKILLWEAKEST
Destroys the monster with the least attack. If multiple options, choose one

## DIMKILLTUNNEL (COSTCREST, COST)
Destroys one tunnel monster in dungeon.
Cost: COST x COSTCREST

## DIMKILLTUNNELALL (COSTCREST, COST)
Destroys all tunnel monster in dungeon.
Cost: COST x COSTCREST

## DIMADDCREST (CREST, AMOUNT)
Add AMOUNT CREST crests to player crest pool.

## DIMTRADECREST (COST)
Trade COST number of same crests for one crest of any type.

## EXODIA
Wins the game if "R Leg of Forbidden", "L Leg of Forbidden", "L Arm of Forbidden" and "R Arm of Forbidden" are in dungeon and you control them.

## DIMBUFFDEADTYPE (TYPE)
For each dead monster of type TYPE add the attack and defense (original attack/deffense) of the dead monster to the summoned monster.

# Continuous Abilities
## STOPFLY
Stop all FLY abilities.

## STOPTUNNEL
Stop all TUNNELING abilities.

## TURNSLOWTYPE (TYPE)
Make all monsters of type TYPE move only once every two turns. The turn for all monsters is universal, starting from the opponent turn after the dimension of the monster with the ability. Two or more of instances of this ability can be stacked to cancel movement completely.

## BUFFTYPE (TYPE, ATTR, AMOUNT)
Raise ATTR of all TYPE monsters in dungeon by AMOUNT.

## PROTECTTYPE (TYPE)
Reduce all damage done to monster of type TYPE in dungeon to 0.

## FROZEN
Monster cannot move.

## MOVELIMIT (LIMIT)
Monster can move a maximum of LIMIT tiles per turn.

# Battle Abilities
## RAISEATTACK (MAX)
Attack and raise attack during battle by 10x the number of extra attack crests. The maxumum payed crests is MAX
Cost: (2..MAX) x ATTACK

## REDUCEDAMAGE (COSTCREST, COST, AMOUNT)
Reduce damage dealt during attack (without guarding) by AMOUNT.
Cost: COST x COSTCREST

## SHIFTDAMAGE (COSTCREST, COST)
Shift damage dealt by an attack to another monster completely, as if the attacker were attaking the selected monster without guarding.
Cost: COST x COSTCREST

## NEGATEATTACK (COSTCREST, COST) 
Negate attack amied to self.
Cost: COST x COSTCREST

# Standing Abilities
## DUNGRAISEATTACK (COSTCREST, COST, AMOUNT)
Once per turn, raise attack during next battle by AMOUNT.
Cost: COST x COSTCREST

## BUFFSELF (ATTR, COSTCREST, COST, AMOUNT)
Once per turn, increase ATTR by AMOUNT.
Cost: COST x COSTCREST

## TRADEHEARTS (AMOUNT, COSTCREST, COST)
Removes AMOUNT number of hearts from self and opponent monster. If no opponent monster available, ability cannot be used.
Cost: COST x COSTCREST

## STEALMONSTER (COSTCREST, COST)
Destroy monster. Select an opponent monster and gain control of the monster indefinitely. Move the controlled monster to the original position of monster.
Cost: COST x COSTCREST

## MINDCONTROL (COSTCREST, COST)
Gain control of one opponent monster till the end of the turn.
Cost: COST x COSTCREST
