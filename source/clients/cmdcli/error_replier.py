class ErrorReplier():
    """
    Converts an error reply from the engine into a text 
    reply.
    """
    def __init__(self, engine):
        self.engine = engine
        self.errordict = {
            "InvalidCommand"    : self.gen_InvalidCommand,
            "DuplicatedDice"    : self.gen_DuplicatedDice,
            "DiceAlreadyUsed"   : self.gen_DiceAlreadyUsed,
            "OOBDinIndex"       : self.gen_OOBDimIndex,
            "NotPlayerMonster"  : self.gen_NotPlayerMonster,
            "NotOpponentTarget" : self.gen_NotOpponentTarget,
            "AttackOutOfRange"  : self.gen_AttackOutOfRange,
            "MonsterInCooldown" : self.gen_MonsterInCooldown,
            "NotPathFound"      : self.gen_NotPathFound,
            "NetUnconnected"    : self.gen_NetUnconnected,
            "OOBTilePos"        : self.gen_OOBTilePos,
            "NotDungeonTile"    : self.gen_NotDungeonTile,
            "TileOverlaps"      : self.gen_TileOverlaps,
            "NotEnoughCrests"   : self.gen_NotEnoughCrests}

    def gen_string(self, reply):
        """
        Generates reply string using the errordict.
        """
        return self.errordict[reply["error"]](reply["args"])

    def gen_InvalidCommand(self, args):
        return "Invalid command " + args[0] + " at state " +\
            self.engine.dsm.state.name

    def gen_DuplicatedDice(self, args):
        return "Duplicated dice in roll"

    def gen_DiceAlreadyUsed(self, args):
        return "Dice already dimensioned"

    def gen_OOBDimIndex(self, args):
        return "Invalid dimension index"
        
    def gen_NotPlayerMonster(self, args):
        return "No player monster at " + strpos(args[0])

    def gen_NotOpponentTarget(self, args):
        return "No opponent target at " + strpos(args[0])

    def gen_AttackOutOfRange(self, args):
       return "Attack is out of range"

    def gen_MonsterInCooldown(self, args):
        return  args[0] + " already attacked this turn"

    def gen_NotPathFound(self, args):
        return "No path found between " + strpos(args[0]) + \
            " and " + strpos(args[1])

    def gen_NetUnconnected(self, args):
        return "Net do not connect with dungeon path"

    def gen_OOBTilePos(self, args):
        return "Net out of bound"

    def gen_NotDungeonTile(self, args):
        return "No dungeon at " + strpos(args[0])

    def gen_TileOverlaps(self, args):
        return "Tile overlaps existing dungeon path"

    def gen_NotEnoughCrests(self, args):
        return "Not enough " + args[0] + " crests"

def strpos(pos):
    """
    Convert position in tuple into nice coordinates.
    """
    return chr(pos[1]+97) + str(pos[0]+1)
