class DuplicatedDice(Exception): pass
"""
Raised when there are duplicated dice in the roll dice list.
"""

class DiceAlreadyUsed(Exception): pass
"""
Raised when trying to roll an already dimensioned dice.
"""

class OOBDimIndex(Exception): pass
"""
Raised when dimension index is out of bounds.
"""

class NotPlayerMonster(Exception): pass
"""
Raised when no player monster is located at specified 
position.
args[0]: position.
"""

class NotOpponentTarget(Exception): pass
"""
Raised when no opponent target is located at specified 
position.
args[0]: position.
"""

class AttackOutOfRange(Exception): pass
"""
Raised when an attack is out of range.
"""

class MonsterInCooldown(Exception): pass
"""
Raised when a monster in cooldown tries to attack.
args[0]: attacking monster name.
"""

class NotPathFound(Exception): pass
"""
Raised when no valid path is found between origin and
destination of a move.
args[0]: origin position.
args[1]: destination position.
"""

class NetUnconnected(Exception):pass
"""
Raised when trying to dimension a net unconnected from 
player's dungeon path.
"""

class OOBTilePos(Exception): pass
"""
Raised when tile position is out of bounds.
args[0]: position
"""

class NotDungeonTile(Exception): pass
"""
Raised when trying to select a position with no dungeon path
while moving/attacking.
args[0]: position
"""

class TileOverlaps(Exception): pass
"""
Raised when trying to dimension a net overlaping an existing
dungeon path.
"""

class NotEnoughCrests(Exception): pass
"""
Raised when player does not has enough crests to perform an
action.
args[0]: crest name
"""
