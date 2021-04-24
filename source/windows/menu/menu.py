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
            width = max(width, len(button.get_text()[0]))
        return width
        
class ListEntry(urwid.Text):
    """
    Used instead of urwid default buttons to remove cursor.
    Extracted from: https://stackoverflow.com/a/56759094
    """
    _selectable = True
    signals = ["click"]

    def __init__(self, label, on_press=None, user_data=None):
        super().__init__(label, align="center")
        if on_press is not None:
            urwid.connect_signal(self, 'click', on_press, 
                user_data)

    def keypress(self, size, key):
        """
        Send 'click' signal on 'activate' command.
        """
        if self._command_map[key] != urwid.ACTIVATE:
            return key

        self._emit('click')

    def mouse_event(self, size, event, button, x, y, focus):
        """
        Send 'click' signal on button 1 press.
        """
        if button != 1 or not urwid.util.is_mouse_press(event):
            return False

        self._emit('click')
        return True

def create_buttons(buttons_params):
    """
    Create a list of buttons for the menu. buttons_params is
    a list of tuples containing the the parameters of each 
    button (ListEntry). The parameters are the same as for
    urwid button(label, on_press, user_data). Align defines
    the alignment of the buttons in the menu.
    """
    buttons = []
    for params in buttons_params:
        button = ListEntry(*params)
        button.set_align_mode("center")
        button_map = urwid.AttrMap(button, None, 
            focus_map="focused")
        buttons.append(button_map)

    return buttons
