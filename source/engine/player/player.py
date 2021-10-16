import yaml
from player.crest_pool import CrestPool
from dungobj.monster_lord import MonsterLord
from dungeon.tiles.dungeon_tile import DungeonTile
from dungobj.dungobj import DungeonObject

class Player():
    """
    The player that is playing the duel.
    """
    DIM_LIMIT = 10
    def __init__(self, playerid, name, dicepool, initfile):
        self.id = playerid
        self.name = name
        self.dicepool = dicepool
        self.crestpool = CrestPool()
        self.ml = MonsterLord()
        self.dimdice = []
        self.summons = []
        self.monsters = []
        self.items = []
        self.tiles = []
        self.set_init(initfile)

    def set_init(self, initfile):
        """
        Set intial state of player given, initialization 
        file.
        """
        initdict = yaml.full_load(open(initfile))
        # get crests init
        try:
            crests = initdict["CRESTS"+str(self.id)]
            for crest, value in crests.items():
                setattr(self.crestpool, crest, value)
        except KeyError:
            pass
        # get hearts init
        try:
            self.ml.hearts = initdict["HEARTS"+str(self.id)]
        except KeyError:
            pass

    def create_tile(self, dungobj=DungeonObject()):
        """
        Create player tile with dungeon object in it.
        """
        tile = DungeonTile(dungobj)
        dungobj.add_to_player(self)
        self.tiles.append(tile)
        return tile

    def create_net_tiles(self, net, summon):
        """
        Create player tiles from net. Put summon in center
        tile.
        """
        tiles = []
        for pos in net.poslist:
            if pos == net.center: # center => add summon
                tiles.append(self.create_tile(summon))
            else: # not center => empty tile
                tiles.append(self.create_tile())
        return tiles

    def create_ml_tile(self):
        """
        Create a player tile with the monster lord in it.
        """
        return self.create_tile(self.ml)

    def hit_dim_limit(self):
        """
        True if player hit the dimension limit.
        """
        return len(self.dimdice) >= self.DIM_LIMIT

    def is_my_target(self, dungobj):
        """
        Returns True if dungobj is players target.
        """
        return dungobj in self.monsters or dungobj is self.ml

    def reset_cooldown(self):
        """
        Reset the coodown from all player monsters.
        """
        for monster in self.monsters:
            monster.cooldown = False
