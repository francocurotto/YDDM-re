import urwid

class Dice(urwid.AttrMap):
    """
    Displays dice information in a single line.
    """
    def __init__(self, stringifier, index, dice):
        # list of widgets in column
        colwidgets = []

        # create index widget
        #colwidgets.append(urwid.Text(index))
        colwidgets.append(("pack", urwid.Text(index)))

        # create name widget
        namewid = urwid.Text(dice.card.name, wrap="clip")
        #colwidgets.append(namewid)
        colwidgets.append((stringifier.NAMECROP, namewid))

        # create type widget
        typestr = stringifier.stringify_type(dice)
        typewid = urwid.Text(typestr, wrap="clip")
        #colwidgets.append(typewid)
        #colwidgets.append(("pack", typewid))
        colwidgets.append((5, typewid))

        if dice.card.is_monster():
            # create attack widget
            attackstr = stringifier.stringify_attack(dice)
            attackwid = urwid.Text(attackstr, wrap="clip")
            #colwidgets.append(attackwid)
            #colwidgets.append(("pack", attackwid))
            colwidgets.append((4, attackwid))

            # create defense widget
            defensestr = stringifier.stringify_defense(dice)
            defensewid = urwid.Text(defensestr)
            #colwidgets.append(defensewid)
            #colwidgets.append(("pack", defensewid))
            #colwidgets.append((6, defensewid))

            # create life widget
            lifestr = stringifier.stringify_life(dice)
            lifewid = urwid.Text(lifestr)
            #colwidgets.append(lifewid)
            #colwidgets.append(("pack", lifewid))
            #colwidgets.append((5, lifewid))
        else: # is item, hence, add align widgets
            if stringifier.icontype.startswith("emoji"):
                alignwid = urwid.Text(4*" ")
            else: # if no emoji icons, correct align
                alignwid = urwid.Text(3*" ")
            #for _ in range(3):
                #colwidgets.append(("pack", alignwid))

        # create sides widget
        sidesstr = stringifier.stringify_sides(dice)
        sideswid = urwid.Text(sidesstr,wrap="clip")
        #colwidgets.append(sideswid)
        #colwidgets.append(("pack", sideswid))
        #colwidgets.append((29,sideswid))

        # create column and finish widget
        columns = urwid.Columns(colwidgets, dividechars=1)
        super().__init__(columns, None)
