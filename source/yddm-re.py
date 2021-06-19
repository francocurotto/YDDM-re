import sys
import urwid
import globvars

# add all modules to path
from functions.module_functions import get_all_modules
modlist = get_all_modules()
[sys.path.append(modname) for modname in modlist]

# import modules
from globvars import palette

# local imports
from main_win import MainWin

# create main window
main_win = MainWin()
globvars.main_win = main_win

# urwid loop
loop = urwid.MainLoop(main_win, palette)
loop.run()

