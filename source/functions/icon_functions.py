from settings_functions import load_settings

def load_icons():
    """
    Load the icon dictionary given the current display 
    settings.
    """
    display_type = load_settings()
    return icons[settings["display_type"]]
