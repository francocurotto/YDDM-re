import urwid
from title_menu import TitleMenu

class TitleWin(urwid.Filler):
    """
    Title window presented at the start of the game.
    """
    def __init__(self):
        # create urwid elements for title
        # title
        title = urwid.Text(title_str, align="center", 
            wrap="clip")
        
        # subtitle
        subtitle = urwid.Text(subtitle_str, align="center")

        # title menu
        menu = TitleMenu()

        # create filled pile
        div = urwid.Divider()
        pile = urwid.Pile([title, div, subtitle, div, menu])

        super().__init__(pile, valign="top")

# strings
title_str = "\
 __   __  ____    ____    __  __                       \n\
 \ \ / / |  _ \  |  _ \  |  \/  |          _ __    ___ \n\
  \ V /  | | | | | | | | | |\/| |  _____  | '__|  / _ \\\n\
   | |   | |_| | | |_| | | |  | | |_____| | |    |  __/\n\
   |_|   |____/  |____/  |_|  |_|         |_|     \___|"
subtitle_str = "Dungeon Dice Monsters re-implementation"
