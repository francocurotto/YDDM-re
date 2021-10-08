# standard imports
import sys
import argparse
import urwid

# add to python path
sys.path.append("./engine")
sys.path.append("./clients")

# internal imports
from urwidcli.poolbuilder import PoolBuilder

# create parser
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--library", 
    default="LIBRARY.yaml", dest="library", 
    help="Dice library file location")
parser.add_argument("-p", "--pool", 
    default="dicesets/starter.yaml", dest="pool",
    help="Pool file to create/modify")
icongroup = parser.add_mutually_exclusive_group()
icongroup.add_argument("--ascii", action="store_const", 
    const="ascii", dest="icontype", help="Use ascii icons")
icongroup.add_argument("--unicode", action="store_const", 
    const="unicode", dest="icontype",
    help="Use unicode icons")
icongroup.add_argument("--emoji", action="store_const", 
    const="emoji", dest="icontype", help="Use emoji icons")
parser.set_defaults(icontype="unicode")
args = parser.parse_args()

# start urwid loop
palette = [("focused", "standout", "")]
urwid.MainLoop(PoolBuilder(args), palette).run()
