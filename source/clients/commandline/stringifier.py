import yaml

class Stringifier():
    """
    Creates string version of YDDM objects.
    """
    NAMECROP = 15
    def __init__(self, icontype):
        allicons = yaml.full_load(open("ICONS.yaml"))
        self.icontype = icontype
        self.icons = allicons[self.icontype]

    def stringify_dicelist(self, dicelist):
        """
        Creates string version of a list of dice.
        """
        strlist = []
        for i, dice in enumerate(dicelist):
            dice_string  = str(i+1).rjust(2) + ". "
            dice_string += self.stringify_dice_short(dice)
            strlist.append(dice_string)
        return "\n".join(strlist)

    def stringify_dice_short(self, dice):
        """
        Creates string version of a dice. Short version.
        """
        # name, cropped at namecrop characters
        string = dice.card.name[:self.NAMECROP]
        # whitespace to fill chars if name is too short
        string = string.ljust(self.NAMECROP+1)
        # summon type icon
        string += self.icons["TYPE_"+dice.card.type]
        # level value
        string += str(dice.level) + " "
        if dice.card.is_monster():
            # attack value
            string += str(dice.card.attack).rjust(2)
            #attack icon
            string += self.icons["CREST_ATTACK"] + " "
            # defense value
            string += str(dice.card.defense).rjust(2)
            # defense icon
            string += self.icons["CREST_DEFENSE"] + " "
            # life value
            string += str(dice.card.life) 
            # life icon
            string += self.icons["MONSTER_HEART"] + " "
        else: # is item, hence, add align space
            if self.icontype.startswith("emoji"):
                string += 15*" "
            else: # if no emoji icons, correct align
                string += 12*" "
        string += self.stringify_sides(dice)
        return string

    def stringify_sides(self, dice):
        """
        Creates string version of sides of a dice.
        """
        string = ""
        for side in dice.sides:
            string += self.stringify_side(side)
        return string

    def stringify_side(self, side):
        """
        Creates string version of a side.
        """
        string  = self.icons["CREST_"+side.crest.name]
        string += str(side.mult)
        return string

    def stringify_dice(self, dice):
        """
        Creates string version of a dice.
        """
        s  = "NAME:    " + dice.card.name + "\n"
        s += "TYPE:    " + dice.card.type + "\n"
        s += "LEVEL:   " + str(dice.card.level) + "\n"
        if dice.card.is_monster():
            s += "ATTACK:  " + str(dice.card.attack) + "\n"
            s += "DEFENSE: " + str(dice.card.defense) + "\n"
            s += "LIFE:    " + str(dice.card.life) + "\n"
        s += "ABILITY: " + dice.card.ability + "\n"
        s += "DICE:    " + self.stringify_sides(dice)
        return s

    def stringify_dungeon(self, duel):
        """
        Creates string version of the dungeon.
        """
        dungeon = duel.dungeon
        strlist = []

        # create first row (coordinates)
        row1 = self.create_coorstr(dungeon)
        strlist.append("    "+row1+"     ")

        # create second row blocks
        row2 = self.create_blockstr(dungeon)
        strlist.append("  "+row2+"  ")

        # create rest of rows
        for i,row in enumerate(reversed(dungeon.array)):
            # coordinate and block
            rowstr = str(dungeon.HEIGHT-i).rjust(2)
            rowstr += self.icons["TILE_BLOCK"]
            
            # create list of row strings
            for tile in row:
                rowstr += self.stringify_tile(duel, tile)

            # block and coordinate
            rowstr += self.icons["TILE_BLOCK"]
            rowstr += str(dungeon.HEIGHT-i).ljust(2)

            # add to list
            strlist.append(rowstr)

        # create bottom block row
        row22 = self.create_blockstr(dungeon)
        strlist.append("  "+row22+"  ")

        # create last (coordinates)
        row23 = self.create_coorstr(dungeon)
        strlist.append("     "+row23+"    ")

        # join all rows
        string = "\n".join(strlist)
        return string

    def create_coorstr(self, dungeon):
        """
        Create a row of letter coordinates.
        """
        clist = [chr(i) for i in range(97, 97+dungeon.WIDTH)]
        return " ".join(clist)
        
    def create_blockstr(self, dungeon):
        """
        Create a row of blocks.
        """
        return (dungeon.WIDTH+2)*self.icons["TILE_BLOCK"]

    def stringify_tile(self, duel, tile):
        """
        Creates string version of a tile.
        """
        # the tile is empty
        if not tile.is_dungeon():
            return self.icons["TILE_EMPTY"]

        # the tile is a dungeon tile
        content = tile.content
        if content.is_summon():
            return self.stringify_summon_tile(duel, content)
        elif tile.content.is_monster_lord():
            return self.stringify_monster_lord_tile(duel)
        else: # no content in tile
            return self.stringify_path(duel, tile)

    def stringify_summon_tile(self, duel, summon):
        """
        Stringify a tile with a summon in it.
        """
        icon = self.icons["TYPE_"+contents.type]
        if summon in duel.player1.summons:
            return colored(icon, *self.style["p1"])
        if summon in duel.player2.summons:
            return colored(icon, *self.style["p2"])

    def stringify_monster_lord_tile(self, duel):
        """
        Stringify a tile with a monster lord in it.
        """
        icon = self.icons["MONSTER_LORD"]
        if summon in duel.player1.summons:
            return colored(icon, *self.style["p1"])
        if summon in duel.player2.summons:
            return colored(icon, *self.style["p2"])

    def stringify_path_tile(self, duel, tile):
        """
        Stringify a dungeon tile with nothing in it.
        """
        if tile in engine.duel.player1.tiles:
            return self.icons["TILE_PATH1"]
        if tile in engine.duel.player2.tiles:
            return self.icons["TILE_PATH2"]
