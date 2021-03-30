import urwid
from menu import Menu

class TitleMenu(urwid.Padding):
    """
    The menu for the title.
    """
    def __init__(self):
        menu = Menu(buttons_params, "center")
        super().__init__(menu, width=menu.get_width(),
            align="center") 

def exit_program(button):
    raise urwid.ExitMainLoop()

buttons_params = [
    ("CPU Versus",   exit_program),
    ("Pool Builder", exit_program),  
    ("Options",      exit_program), 
    ("Quit",         exit_program)]
