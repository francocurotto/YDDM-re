from dungeon.tiles.tile import Tile

class BlockTile(Tile):
    """
    Tile were dimension and moving is blocked.
    """
    def is_block(self):
        return True
