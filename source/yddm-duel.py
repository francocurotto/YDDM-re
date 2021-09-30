# standard imports
import sys
import yaml
import argparse

# add to python path
sys.path.append("./engine")
sys.path.append("./clients")

# internal imports
from cmdcli.cmd_client import CmdClient
from cursescli.curses_client import CursesClient

# get available icons
icons = yaml.full_load(open("ICONS.yaml"))
icontypes = list(icons.keys())

# dict of available clients
clients = {"cmd":CmdClient, "curses":CursesClient}

# create parser
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--library", 
    default="LIBRARY.yaml", dest="library", 
    help="Dice library file location")
parser.add_argument("-n1", "--name1", 
    default="Player1", dest="name1", 
    help="Player 1 name")
parser.add_argument("-p1", "--pool1", 
    default="dicesets/starter.yaml", dest="poolfile1",
    help="Player 1 pool file")
parser.add_argument("-n2", "--name2", 
    default="Player2", dest="name2", 
    help="Player 2 name")
parser.add_argument("-p2", "--pool2", 
    default="dicesets/starter.yaml", dest="poolfile2",
    help="Player 2 pool file")
icongroup = parser.add_mutually_exclusive_group()
icongroup.add_argument("--ascii", action="store_const", 
    const="ascii", dest="icontype", help="Use ascii icons")
icongroup.add_argument("--unicode", action="store_const", 
    const="unicode", dest="icontype",
    help="Use unicode icons")
icongroup.add_argument("--emoji", action="store_const", 
    const="emoji", dest="icontype", help="Use emoji icons")
clientgroup = parser.add_mutually_exclusive_group()
clientgroup.add_argument("--cmd", action="store_const", 
    const="cmd", dest="client", 
    help="Use commandline client")
clientgroup.add_argument("--curses", action="store_const", 
    const="curses", dest="client", help="Use curses client")
parser.set_defaults(icontype="emoji", client="curses")
args = parser.parse_args()

clients[args.client](args).run()
