from dungobj.dungobj import DungeonObject

class DungeonTile():
    """
    Tile were monsters can exist and move.
    """
    def __init__(self, content=DungeonObject()):
        self.content = content

    def remove_content(self):
        """
        Remove current content and replace it with generic
        object (no content).
        """
        self.content = DungeonObject()

    def is_dungeon(self):
        return True
    