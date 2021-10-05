from settings_functions import load_settings

def load_icons():
    """
    Load the icon dictionary given the current display 
    settings.
    """
    from globvars import icons
    settings = load_settings()
    return icons[settings["display_type"]]
