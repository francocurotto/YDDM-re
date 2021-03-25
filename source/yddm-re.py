import sys
import urwid

# add all modules to path
from functions.module_functions import get_all_modules
modlist = get_all_modules()
[sys.path.append(modname) for modname in modlist]

# import local modules
from main_win import MainWin

# create main window
main_win = MainWin()

# urwid loop
loop = urwid.MainLoop(main_win)
loop.run()

