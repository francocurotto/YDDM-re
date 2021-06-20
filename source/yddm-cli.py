import yaml
import argparse
from clients.commandline.cliclient import CliClient

# get available icons
icons = yaml.full_load(open("clients/ICONS.yaml"))
icon_types = list(icons.keys())

# create parser
parser = argparse.ArgumentParser()
parser.add_argument("-p1", default = "dicesets/starter.yaml",
    dest="poolfile1", help="Player 1 pool file")
parser.add_argument("-p2", default = "dicesets/starter.yaml",
    dest="poolfile2", help="Player 2 pool file")
parser.add_argument("-i", choices=icon_types, 
    default="unicode", dest="icontype",
    help="Type of icons to use.")
args = parser.parse_args()

CliClient(args).run()
