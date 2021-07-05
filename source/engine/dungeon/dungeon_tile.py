from dungobj.dungobj import DungeonObject

class DungeonTile():
    """
    Tile were monsters can exist and move.
    """
    def __init__(self, content=None):
        if content:
            self.content = content
        else: # if no content use default dungeon object
            self.content = DungeonObject()

    def remove_content(self):
        """
        Remove current content and replace it with generic
        object (no content).
        """
        self.content = DungeonObject()

    def is_dungeon(self):
        return True

    def is_occupied(self):
        return self.content.is_summon() or \
            self.content.is_monster_lord()
        
    
