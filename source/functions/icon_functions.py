from globvars import icons

def load_icons():
    """
    Load the icon dictionary given the current display 
    settings.
    """
    from settings import display_type
    return icons[display_type]
