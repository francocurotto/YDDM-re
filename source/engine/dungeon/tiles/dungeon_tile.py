from dungeon.tiles.tile import Tile
from dungobj.dungobj import DungeonObject

class DungeonTile(Tile):
    """
    Tile were monsters can exist and move.
    """
    def __init__(self, content):
        self.content = content

    def remove_content(self):
        """
        Remove current content and replace it with generic
        object (no content).
        """
        self.content = DungeonObject()

    def is_dungeon(self):
        return True

    def is_occupied(self):
        return self.content.is_content()

    def is_reachable(self):
        return not self.is_occupied() or \
            self.content.is_item()
