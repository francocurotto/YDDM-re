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
parser.add_argument("-i", "--icons", choices=icontypes,
    default="emoji", dest="icontype", 
    help="Type of icons to use.")
parser.add_argument("-c", "--client", choices=clients.keys(),
    default="curses", dest="client", 
    help="Client for user interface.")
args = parser.parse_args()

clients[args.client](args).run()
