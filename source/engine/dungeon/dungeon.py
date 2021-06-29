from dungeon.empty_tile import EmptyTile
from dungeon.dicenets.pos import Pos

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
        self.set_tile(tile, Pos(0,6))
        # player 2
        tile = players[1].create_ml_tile()
        self.set_tile(tile, Pos(18,6))

    def get_tile(self, pos):
        """
        Get tile at position pos (y,x).
        """
        return self.array[pos.y][pos.x]

    def set_tile(self, tile, pos):
        """
        Set tile at position pos (y,x), replacing previous 
        tile.
        """
        self.array[pos.y][pos.x] = tile

    def set_net(self, net, player, summon):
        """
        Set player's net in dungeon with summon at center.
        If unsuccessful, return False and error message. 
        Set summon at center of net.
        """
        # check if net can be correctly dimensioned
        success, message = self.check_net(net, player)
        if not success:
            return success, message

        # if check passed, place the net
        for pos in net.poslist:
            if pos == net.center: # center => add summon
                tile = player.create_tile(summon)
            else: # not center => empty tile
                tile = player.create_tile()
            self.set_tile(tile, pos)
        
        # return success
        return True, ""

    def check_net(self, net, player):
        """
        Check for correct net dimension: check for out of 
        bound, overlaping dungeon path, and unconnected with
        player path. Retrun False and message if it did not
        pass checks.
        """
        # check in bound condition
        for pos in net.poslist:
            if not self.in_bound(pos):
                message = "Dice net out of bound"
                return False, message

        # check no overlaping condition
        for pos in net.poslist:
            if self.overlaps(pos):
                message = "Dice net overlaps dungeon path"
                return False, message

        # check connection with player dungeon condition
        for pos in net.poslist:
            neighbors = self.get_neighbors(pos)
            for neighbor in neighbors:
                if neighbor in player.tiles:
                    # all checks passed
                    return True, ""
        
        # connection check not passed
        message = "Dice net does not connect with " + \
            "dungeon path"
        return False, message

    def in_bound(self, pos):
        """
        Check if a position falls inside the dungeon array.
        """
        in_bound_y = 0 <= pos.y < len(self.array)
        in_bound_x = 0 <= pos.x < len(self.array[0])

        return in_bound_y and in_bound_x

    def overlaps(self, pos):
        """
        Checks if position overlaps with a dungeon tile 
        already existing in the dungeon.
        """
        tile = self.get_tile(pos)
        return tile.is_dungeon()

    def get_neighbors(self, pos):
        """
        get the neighbors tiles from tile at position pos.
        Neighbors are considered tiles that are horizontal
        and vertical adjacent only.
        """
        poslist = pos.get_neighbors()
        tiles = []
        for pos in poslist:
            if self.in_bound(pos):
                tiles.append(self.get_tile(pos))

        return tiles
