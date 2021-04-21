import os, yaml
from globvars import default_settings_path
from globvars import saved_settings_path

def load_settings():
    """
    Load the game settings from the appropiate file. If prior
    settings are saved, load saved.yaml, else load 
    defaults.yaml.
    """
    if os.path.isfile(saved_settings_path):
        return yaml.full_load(open(saved_settings_path))
    else:
        return yaml.full_load(open(default_settings_path))
