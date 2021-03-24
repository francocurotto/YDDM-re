import urwid

# strings
title_str = "\
 __   __  ____    ____    __  __                        \n\
 \ \ / / |  _ \  |  _ \  |  \/  |          _ __    ___  \n\
  \ V /  | | | | | | | | | |\/| |  _____  | '__|  / _ \ \n\
   | |   | |_| | | |_| | | |  | | |_____| | |    |  __/ \n\
   |_|   |____/  |____/  |_|  |_|         |_|     \___| "
subtitle_str = "Dungeon Dice Monsters re-implementation"

# urwid elements
# title
title_txt = urwid.Text(title_str, align="center", wrap="clip")
title_fill = urwid.Filler(title_txt, "top")
#subtitle
subtitle_txt = urwid.Text(subtitle_str, align="center")
subtitle_fill = urwid.Filler(subtitle_txt, "top")
#
pile = urwid.Pile([(6,title_fill), subtitle_fill])

# uwrwid loop
loop = urwid.MainLoop(pile)
loop.run()

