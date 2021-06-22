# standard imports
import sys
import yaml
import argparse

# add engine to python path
sys.path.append("./engine")

# internal imports
from clients.commandline.cliclient import CliClient

# get available icons
icons = yaml.full_load(open("clients/ICONS.yaml"))
icontypes = list(icons.keys())

# create parser
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--library", 
    default="LIBRARY.yaml", dest="library", 
    help="Dice library file location")
parser.add_argument("-p1", "--pool1", 
    default="dicesets/starter.yaml", dest="poolfile1",
    help="Player 1 pool file")
parser.add_argument("-p2", "--pool2", 
    default="dicesets/starter.yaml", dest="poolfile2",
    help="Player 2 pool file")
parser.add_argument("-i", "--icons", choices=icontypes,
    default="unicode", dest="icontype", 
    help="Type of icons to use.")
args = parser.parse_args()

CliClient(args).run()
