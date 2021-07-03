from emoji import UNICODE_EMOJI_ENGLISH

class Stringifier():
    """
    Creates string version of YDDM objects.
    """
    NAMECROP = 15
    def __init__(self, icons):
        self.icons = icons

    def stringify_pool(self, pool):
        """
        Creates string version of pool.
        """
        strlist = []
        for i, dice in enumerate(pool.contents):
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
            testicon = self.icons["TYPE_DRAGON"]
            if testicon in UNICODE_EMOJI_ENGLISH:
                string += 15*" "
            else: # if no emoji icons, correct align
                string += 12*" "
        string += self.stringify_sides(dice)
        return string

    def stringify_sides(self, dice):
        """
        Creates string version of a sides.
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
