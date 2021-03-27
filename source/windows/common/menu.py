import urwid

class Menu(urwid.ListBox):
    """
    Generic menu class used in many windows.
    """
    def __init__(self, buttons_params):
        buttons = create_buttons(buttons_params)
        walker = urwid.SimpleFocusListWalker(buttons)
        super().__init__(walker)

    def get_width(self):
        """
        Get menu width given by longest button's label width. 
        """
        width = 0
        for button in self.body:
            # get button through attribute map
            button = button.original_widget
            #TODO: fix for emoji sensitive length
            width = max(width, len(button.label))
        #TODO: remove compensation when custom button gets implemented
        return width+4 # compensate for Button borders
        
def create_buttons(buttons_params):
    """
    Create a list of buttons for the menu. buttons_params is
    a list of tuples containing the the parameters of each 
    button, see urwid Button documentation for details.
    """
    buttons = []
    for params in buttons_params:
        button = urwid.Button(*params)
        button_map = urwid.AttrMap(button, None, 
            focus_map="focused")
        buttons.append(button_map)

    return buttons
