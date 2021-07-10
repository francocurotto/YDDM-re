def str2index(string, minval, maxval):
    """
    Convert string into an index of a list. minval and maxval 
    are bounds of the index, if out of bound, return None. If 
    string is not convertable, return None.
    """
    # try int conversion
    try:
        i = int(string)-1
    except ValueError:
        print("Cannot convert index " + string)
        return None
    # check boundaries
    if i<minval or i>maxval:
        print("Index " + string + " out of bound")
        return None
    return i

def str2coor(string):
    """
    Convert string of coordinates into a coordinate tuple 
    representing a location in the dungeon. If string is not
    convertible return none.
    """
    # try coordinate conversion
    try:
        # separate coordinates
        x = string[0]; y = string[1:]
        # convert coordinate to ints
        x = ord(x)-97; y = int(y)-1
    except (IndexError, ValueError):
        print("Cannot convert coordinates " + string)
        return
    # check coordinates boundaries
    if x<0 or x>12 or y<0 or y>18:
        print("Coordinates " + string + "out of bound")
        return
    return (y,x)

def str2net(string):
    """
    Convert it into uppercase and heck if string is a valid
    net name.
    """
    nets = ["T1","T2","Z1","Z2","X1","X2","M1","M2","S1",
        "S2","L1"]
    string = string.upper()
    if string not in nets:
        print("Invalid net name " + string)
        return None
    return string

def str2trans(string):
    """
    Convert it into uppercase and check if string is a valid
    transformation name.
    """
    trans = ["TCW", "TAW", "FUD", "FLR"]
    string = string.upper()
    if string not in trans:
        print("Invalid trans name " + string)
        return None
    return string
