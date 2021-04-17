# library vars
library_path      = "dicesets/library.yaml"
starter_pool_path = "dicesets/pools/player/starter.yaml"
saved_pool_path   = "dicesets/pools/player/saved.yaml"

# dice info vars
monster_types = ["DRAGON", "SPELLCASTER", "UNDEAD", "BEAST",
    "WARRIOR"]
crest_dict = {"S" : "SUMMON",
              "M" : "MOVEMENT",
              "A" : "ATTACK",
              "D" : "DEFENSE",
              "G" : "MAGIC",
              "T" : "TRAP"}

# icons var
import yaml
icons = yaml.full_load(open("icons.yaml"))

# urwid pallete palette
palette = [("focused", "standout", "")]

