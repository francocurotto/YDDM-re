import urwid
from title_menu import TitleMenu

class TitleWin(urwid.Pile):
    """
    Title window presented at the start of the game.
    """
    def __init__(self):
        # create urwid elements for title
        # title
        title_txt = urwid.Text(title_str, align="center", 
            wrap="clip")
        title_fill = urwid.Filler(title_txt, "top")
        
        # subtitle
        subtitle_txt = urwid.Text(subtitle_str, 
            align="center")
        subtitle_fill = urwid.Filler(subtitle_txt, "top")

        # title menu
        menu = TitleMenu()

        # create filled pile
        super().__init__([(6,title_fill), (2, subtitle_fill),
            menu])

# strings
title_str = "\
 __   __  ____    ____    __  __                       \n\
 \ \ / / |  _ \  |  _ \  |  \/  |          _ __    ___ \n\
  \ V /  | | | | | | | | | |\/| |  _____  | '__|  / _ \\\n\
   | |   | |_| | | |_| | | |  | | |_____| | |    |  __/\n\
   |_|   |____/  |____/  |_|  |_|         |_|     \___|"
subtitle_str = "Dungeon Dice Monsters re-implementation"
