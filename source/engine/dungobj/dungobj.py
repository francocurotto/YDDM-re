class DungeonObject():
    """
    Generic object in a dungeon (monsters, items, monster
    lord).
    """
    # is functions default False
    def is_summon(self):
        return False

    def is_monster(self):
        return False

    def is_item(self):
        return False

    def is_monster_lord(self):
        return False

    def is_target(self):
        return self.is_monster() or self.is_monster_lord() 

    def is_content(self):
        return self.is_summon or self.is_monster_lord()

    def add_to_player(self, player):
        pass
