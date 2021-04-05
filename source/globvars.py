# library var
library_path = "library.yaml"

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
