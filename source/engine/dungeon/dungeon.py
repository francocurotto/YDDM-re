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
        self.setnet_errors = (TilePosUnboundError, 
                              TileOverlapsError)

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
        Get tile at position pos (y,x). If pos out of bound,
        raise error.
        """
        # rejects negative numbers as out of bound
        if not self.in_bound(pos):
            raise TilePosUnboundError(pos)
        try:
            return self.array[pos.y][pos.x]
        except IndexError:
            raise TilePosUnboundError(pos)

    def in_bound(self, pos):
        """
        True if position is in bound of dungeon.
        """
        in_bound_x = 0 <= pos.x < self.WIDTH
        in_bound_y = 0 <= pos.y < self.HEIGHT
        return in_bound_x and in_bound_y

    def get_content(self, pos):
        """
        Get content of tile at position.
        """
        tile = self.get_tile(pos)
        if not tile.is_dungeon():
            raise NotDungeonTile(pos)
        return tile.content

    def set_tile(self, tile, pos):
        """
        Set tile at position pos (y,x). If tile is already 
        occupied, raise exception.
        """
        # check if tile is already occupied
        if self.get_tile(pos).is_dungeon():
            raise TileOverlapsError
        self.array[pos.y][pos.x] = tile

    def destroy_tile(self, pos):
        """
        Convert tile at postion pos in EmptyTile.
        """
        self.array[pos.y][pos.x] = EmptyTile()

    def set_net(self, net, player, summon):
        """
        Set player's net in dungeon with summon at center.
        """
        # check if net can be connects correctly
        if not self.net_connects(net, player):
            raise NetUnconnectedError

        # set net
        dimpos = []
        tiles = player.create_net_tiles(net, summon)
        for pos, tile in zip(net.poslist, tiles):
            try:
                self.set_tile(tile, pos)
                dimpos.append(pos)
            except self.setnet_errors as e:
                # destroy patrially dimensioned tiles
                [self.destroy_tile(pos) for pos in dimpos]
                raise

    def net_connects(self, net, player):
        """
        Check if net connects with path of player.
        """
        for pos in net.poslist:
            neighbors = self.get_neighbors(pos)
            for neighbor in neighbors:
                if neighbor in player.tiles:
                    return True
        return False

    def get_neighbors(self, pos):
        """
        get the neighbors tiles from tile at position pos.
        Neighbors are considered tiles that are horizontal
        and vertical adjacent only.
        """
        poslist = pos.get_neighbors()
        tiles = []
        for pos in poslist:
            try:
                tiles.append(self.get_tile(pos))
            except TilePosUnboundError:
                pass
        return tiles

    def get_path(self, origin, dest):
        """
        Computes dungeon path from origin to dest. If no path
        can be found return None.
        """
        path = [origin]
        pathqueue = [path]
        visited = []

        # breadth-first search
        while pathqueue:
            # pop current path
            path = pathqueue.pop()
            
            # check path finish condition
            lastpos = path[-1]
            if lastpos == dest:
                return path

            # add path end to visited positions
            visited.append(lastpos)

            # expand path in one tile in all possible 
            # directions and add them to the queue
            newpaths = self.expand_path(path, visited)
            pathqueue += newpaths

        # no path was found
        return None

    def expand_path(self, path, visited):
        """
        Return a list of paths that expand one tile from last
        position of path, in all posible directions according 
        to DDM rules. The rules include:
        - you can only expand through dungeon tiles.
        - you cannot expand through tiles occupied by 
            monsters or monster lords (targets)
        - you can expand through a tile occupied by an item,
            but you can't expand further from that.
        Visited list of positions are used to avoid cycles.
        """
        # get last pos
        lastpos = path[-1]

        # if last tile has an item, you can't expand further
        if self.get_tile(lastpos).content.is_item():
            return []

        newpaths = []
        neighborpos = lastpos.get_neighbors()
        # for each neighbor, check if they satisfy all the 
        # requirements to expand the path
        for pos in neighborpos:
            # 1. must be in bound
            if not self.in_bound(pos):
                continue
            # 2. must be a dungeon tile
            if not self.get_tile(pos).is_dungeon():
                continue
            # 3. must not be ocupied by an obstacle (target)
            if self.get_tile(pos).content.is_target():
                continue
            # 4. must not have been visited before
            if pos in visited:
                continue
            # 5. all conditions are met, add new path
            newpaths.append(path + [pos])

        return newpaths

    def move_dungobj(self, origin, dest):
        """
        Move dungeon object at position origin to postions
        dest. Leave a DungObj at origin.
        """
        dungobj = self.get_tile(origin).content
        self.get_tile(dest).content = dungobj
        self.get_tile(origin).remove_content()

    def remove_summon(self, summon):
        """
        Remove summon from dungeon. Must be searched through
        all tiles.
        """
        for row in self.array:
            for tile in row:
                if tile.is_dungeon():
                    if tile.content is summon:
                        tile.remove_content()
                        return

class NetUnconnectedError(Exception):
    message = "Net do not connect with dungeon path"
class TilePosUnboundError(Exception):
    def __init__(self, pos):
        self.message = "Tile position " + str(pos) + \
            " out of bound"
        super().__init__(self, self.message)
class NotDungeonTile(Exception):
    def __init__(self, pos):
        self.message = "No dungeon at " + str(pos)
        super().__init__(self, self.message)
class TileOverlapsError(Exception):
    message = "Tile overlaps existing dungeon path"
