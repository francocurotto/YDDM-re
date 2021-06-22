class DungeonObject():
    """
    Generic object in a dungeon (monsters, items, monter 
    lord).
    """
    # is functions default False
    def is_monster(self):
        return False

    def is_item(self):
        return False

    def is_monster_lord(self):
        return False

    def is_target(self):
        return self.is_monster() or self.is_monster_lord() 


