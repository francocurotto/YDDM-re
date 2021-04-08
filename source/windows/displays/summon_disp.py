import urwid

class SummonDisp(urwid.Filler):
    """
    Display summon information in text format.
    """
    def __init__(self, card):
        card_string = create_string(card)
        text = urwid.Text(card_string)
        super().__init__(text, "top")

    def update(self, card):
        """
        Update text with new card infromation.
        """
        card_string = create_string(card)
        self.original_widget.set_text(card_string)

def create_string(card):
    """
    Convert the card information dictionary in a string to
    update the display.
    """
    string  = "NAME:    " + card.name + "\n"
    string += "TYPE:    " + card.type + "\n"
    string += "LEVEL:   " + str(card.level) + "\n"
    if card.is_monster():
        string += "ATTACK:  " + str(card.attack)  + "\n"
        string += "DEFENSE: " + str(card.defense) + "\n"
        string += "LIFE:    " + str(card.life)    + "\n"
    string += "ABILITY: " + card.ability + "\n"
    return string

