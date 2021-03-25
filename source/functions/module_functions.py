import os

def get_all_modules():
    """
    Get all the possible existing modules starting from 
    current path.
    """
    # get all folders starting from current path
    dirlist = [dirtuple[0] for dirtuple in os.walk(".")]

    # remove invalid module folders
    modlist = [] 
    for dirname in dirlist: 
        if not dirname.endswith("/__pycache__"):
            modlist.append(dirname)
    return modlist
