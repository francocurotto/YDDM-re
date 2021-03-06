import urwid
from menu import Menu

class TitleMenu(urwid.Padding):
    """
    The menu for the title.
    """
    def __init__(self):
        menu = Menu(buttons_params)
        super().__init__(menu, width=menu.get_width(),
            align="center") 

def switch_pool_builder(button):
    from globvars import main_win
    main_win.switch_pool_builder()

def switch_options(button):
    from globvars import main_win
    main_win.switch_options()

def exit_program(button):
    raise urwid.ExitMainLoop()

buttons_params = [
    ("CPU Versus",   exit_program),
    ("Pool Builder", switch_pool_builder),  
    ("Options",      switch_options), 
    ("Quit",         exit_program)]
