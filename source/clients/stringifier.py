import yaml
from termcolor import colored

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

    def stringify_dicepool(self, player):
        """
        Creates string version of a player dice pool.
        """
        strlist = []
        for i, dice in enumerate(player.dicepool):
            dice_string  = str(i+1).rjust(2) + ". "
            dice_string += self.stringify_dice_short(dice)
            if dice in player.dimdice:
                dice_string  = colored(dice_string, "grey")
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
        # type+level+ability
        string += self.stringify_type(dice) + " "
        # level value
        if dice.card.is_monster():
            string += self.stringify_attack(dice) + " "
            string += self.stringify_defense(dice) + " "
            string += self.stringify_life(dice) + " "
        else: # is item, hence, add align space
            if self.icontype.startswith("emoji"):
                string += 15*" "
            else: # if no emoji icons, correct align
                string += 12*" "
        string += self.stringify_sides(dice)
        return string

    def stringify_type(self, dice):
        """
        Creates string version of type of dice.
        """
        string = self.icons["TYPE_"+dice.card.type]
        string += str(dice.level)
        string += "  " # TODO: add ability icon
        return string

    def stringify_attack(self, dice):
        """
        Creates string version of attack of dice.
        """
        string = str(dice.card.attack).rjust(2)
        string += self.icons["CREST_ATTACK"]
        return string

    def stringify_defense(self, dice):
        """
        Creates string version of attack of dice.
        """
        string = str(dice.card.defense).rjust(2)
        string += self.icons["CREST_DEFENSE"]
        return string

    def stringify_life(self, dice):
        """
        Creates string version of life of dice.
        """
        string = str(dice.card.life).rjust(2)
        string += self.icons["MONSTER_HEART"]
        return string

    def stringify_sides(self, dice):
        """
        Creates string version of sides of a dice.
        """
        strlist = []
        for side in dice.sides:
            strlist.append(self.stringify_side(side))
        string = ",".join(strlist)
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
            return self.stringify_empty_tile()
        # the tile is a dungeon tile
        content = tile.content
        if content.is_summon():
            return self.stringify_summon_tile(duel, content)
        elif tile.content.is_monster_lord():
            return self.stringify_ml_tile(duel, content)
        else: # no content in tile
            return self.stringify_path_tile(duel, tile)

    def stringify_empty_tile(self):
        """
        Creates a string version of an empty tile.
        """
        icon = self.icons["TILE_EMPTY"]
        colors = self.icons["COLORS_EMPTY"]
        return colored(icon, *colors)

    def stringify_summon_tile(self, duel, summon):
        """
        Creates a string version of a tile with a summon in 
        it.
        """
        icon = self.icons["TYPE_"+summon.type]
        if summon in duel.player1.summons:
            colors = self.icons["COLORS_SUMMON_P1"]
        if summon in duel.player2.summons:
            colors = self.icons["COLORS_SUMMON_P2"]
        return colored(icon, *colors)

    def stringify_ml_tile(self, duel, monster_lord):
        """
        Creates a string version of a tile with a monster 
        lord in it.
        """
        icon = self.icons["MONSTER_LORD"]
        if monster_lord is duel.player1.ml:
            colors = self.icons["COLORS_SUMMON_P1"]
        if monster_lord is duel.player2.ml:
            colors = self.icons["COLORS_SUMMON_P2"]
        return colored(icon, *colors)

    def stringify_path_tile(self, duel, tile):
        """
        Creates a string version a dungeon tile with no
        content.
        """
        if tile in duel.player1.tiles:
            icon = self.icons["TILE_PATH_P1"]
            colors = self.icons["COLORS_PATH_P1"]
        if tile in duel.player2.tiles:
            icon = self.icons["TILE_PATH_P2"]
            colors = self.icons["COLORS_PATH_P2"]
        return colored(icon, *colors)

    def stringify_dungobj(self, duel, dungobj):
        """
        Creates a string version of a dungeon object.
        """
        if dungobj.is_summon():
            return self.stringify_summon(dungobj)
        elif dungobj.is_monster_lord():
            return self.stringify_monster_lord(duel, dungobj)

    def stringify_summon(self, summon):
        """
        Creates a string version of a summon.
        """
        s  = "NAME:    " + summon.name + "\n"
        s += "TYPE:    " + summon.type + "\n"
        s += "LEVEL:   " + str(summon.level) + "\n"
        if summon.is_monster():
            s += "ATTACK:  " + colorize_attr(summon.attack,
                summon.card.attack) + "\n"
            s += "DEFENSE: " + colorize_attr(summon.defense,
                summon.card.defense) + "\n"
            s += "LIFE:    " + colorize_attr(summon.life,
                summon.card.life) + "\n"
        s += "ABILITY: " + summon.ability
        return s

    def stringify_monster_lord(self, duel, monster_lord):
        """
        Creates a string version of a summon.
        """
        string = self.icons["MONSTER_LORD"] + " "
        # current hearts
        for _ in range(monster_lord.hearts):
            if monster_lord is duel.player1.ml:
                icon = self.icons["HEART_P1"]
                colors = self.icons["COLORS_HEART_P1"]
            if monster_lord is duel.player2.ml:
                icon = self.icons["HEART_P2"]
                colors = self.icons["COLORS_HEART_P2"]
            string += colored(icon, *colors)
        # dead hearts
        for _ in range(3 - monster_lord.hearts):
            icon = self.icons["NOHEART"]
            colors = self.icons["COLORS_NOHEART"]
            string += colored(icon, *colors)
        return string

    def stringify_crestpool(self, crestpool):
        """
        Creates a string version of crestpool.
        """
        # movement crest
        string  = self.icons["CREST_MOVEMENT"] + ":"
        string += str(crestpool.movement).rjust(2) + "|"
        # attack crest
        string += self.icons["CREST_ATTACK"] + ":"
        string += str(crestpool.attack).rjust(2) + "|"
        # defense crest
        string += self.icons["CREST_DEFENSE"] + ":"
        string += str(crestpool.defense).rjust(2) + "|"
        # magic crest
        string += self.icons["CREST_MAGIC"] + ":"
        string += str(crestpool.magic).rjust(2) + "|"
        # trap crest
        string += self.icons["CREST_TRAP"] + ":"
        string += str(crestpool.trap).rjust(2)
        return string

    def stringify_roll(self, roll):
        """
        Creates a string from a roll reply.
        """
        strlist = []
        for side in roll:
            crest = self.icons["CREST_"+side["crest"]]
            mult  = str(side["mult"])
            strlist.append(crest+mult)
        string = " ".join(strlist)
        return string

    def stringify_pos(self, pos):
        """
        Creates a string from as pos tuple
        """
        return chr(pos[1]+97) + str(pos[0]+1)

    def stringify_nets(self, player):
        """
        Creates a string with all nets.
        """
        # get path icon
        pid = player.id
        icon = self.icons["TILE_PATH_P"+str(pid)]
        colors = self.icons["COLORS_PATH_P"+str(pid)]
        dtile = colored(icon, *colors)
        # get summon icon
        icon = self.icons["TYPE_SUMMON"]
        colors = self.icons["COLORS_SUMMON_P"+str(pid)]
        stile = colored(icon, *colors)
        # generate string
        string = netstr
        string = string.replace("[]", dtile)
        string = string.replace("()", stile)
        return string

    def stringify_trans(self):
        """
        Creates a string with the description of all the
        transformations.
        """
        string = "TCW: Turn clockwise\n" + \
                 "TAW: Turn anti-clockwise\n" + \
                 "FUD: Flip up-down\n" + \
                 "FLR: Flip left-right"
        return string

    def stringify_header(self, dsm):
        """
        Creates a string of a summary of the current state
        of the game.
        """
        string  = "<"
        string += str(dsm.state.player.name)
        string += "[p"
        string += str(dsm.state.player.id)
        string += "] | state:"
        string += dsm.state.name
        string += " | turn:"
        string += str(dsm.turn)
        string += "> (p:print command)"
        return string

def colorize_attr(attr, original):
    """
    Colorize an attribute (attack, defense, life), to
    indicate disparity with original.
    """
    if attr > original:
        return colored(str(attr),"cyan")+"/"+str(original)
    elif attr < original:
        return colored(str(attr),"red")+"/"+str(original)
    else:
        return str(attr)+"/"+str(original)

netstr = "\
  T1     T2     Z1     Z2     X1     X2   \n\
[][][] [][]   [][]   [][]     []     []   \n\
  ()     ()[]   ()     ()   []()[] []()   \n\
  []     []     []     [][]   []     [][] \n\
  []     []     [][]   []     []     []   \n\
                                          \n\
  M1   M2     S1     S2     L1            \n\
[][]   []     []     []     []            \n\
  ()   []()   []()[] []()   []            \n\
  [][]   [][]   []     [][] ()[]          \n\
    []     []   []     []     []          \n\
                              []          "
