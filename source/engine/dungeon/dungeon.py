from dungeon.empty_tile import EmptyTile
from dungeon.dice_nets.pos import Pos

class Dungeon():
    """
    The board were the game take place.
    """
    # dungeon fix dimensions
    WIDTH  = 13
    HEIGHT = 19

    def __init__(self, players):
        self.array = self.init_array()
        self.add_monster_lords(players)

    def init_array(self):
        """
        Initialize dungeon array with empty tiles.
        """
        array = []
        for _ in range(self.HEIGHT):
            row = []
            for _ in range(self.WIDTH):
                row.append(EmptyTile())
            array.append(row)
        return array

    def add_monster_lords(self, players):
        """
        Add monster lords from both players into the dungeon
        array.
        """
        # player 1
        tile = players[0].create_ml_tile()
        self.set_tile(tile, Pos(18,6))
        # player 2
        tile = players[1].create_ml_tile()
        self.set_tile(tile, Pos(0,6))

    def set_tile(self, tile, pos):
        """
        Set tile at position pos (y,x), replacing previous 
        tile.
        """
        self.array[pos.y][pos.x] = tile
