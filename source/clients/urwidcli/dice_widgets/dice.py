import urwid

class Dice(urwid.AttrMap):
    """
    Displays dice information in a single line.
    """
    def __init__(self, index, dice, stringifier):
        self.dice = dice
        # list of widgets in column
        colwidgets = []

        # create index widget
        colwidgets.append(("pack", urwid.Text(index)))

        # create name widget
        namewid = DiceName(self.dice.card.name, wrap="clip")
        colwidgets.append(namewid)
        #colwidgets.append((stringifier.NAMECROP, namewid))

        # create type widget
        typestr = stringifier.stringify_type(self.dice)
        typewid = urwid.Text(typestr, wrap="clip")
        colwidgets.append(("pack", typewid))

        if self.dice.card.is_monster():
            # create attack widget
            attackstr = stringifier.stringify_attack(
                self.dice)
            attackwid = urwid.Text(attackstr, wrap="clip")
            colwidgets.append(("pack", attackwid))

            # create defense widget
            defensestr = stringifier.stringify_defense(
                self.dice)
            defensewid = urwid.Text(defensestr)
            colwidgets.append(("pack", defensewid))

            # create life widget
            lifestr = stringifier.stringify_life(self.dice)
            lifewid = urwid.Text(lifestr)
            colwidgets.append(("pack", lifewid))
        else: # is item, hence, add align widgets
            alignwid = urwid.Text(3*" ")
            for _ in range(3):
                colwidgets.append(("pack", alignwid))

        # create sides widget
        sidesstr = stringifier.stringify_sides(self.dice)
        sideswid = urwid.Text(sidesstr,wrap="clip")
        colwidgets.append(("pack", sideswid))

        # create column and finish widget
        columns = urwid.Columns(colwidgets, dividechars=1)
        super().__init__(columns, None, focus_map="focused")

class DiceName(urwid.Text):
    """
    Makes dice name selectable for proper scrolling in dice 
    list.
    """
    _selectable = True
    def keypress(self, size, key):
        return key
