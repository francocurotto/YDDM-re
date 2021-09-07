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
        raise IndexValueError(string)
    # check boundaries
    if i<minval or i>maxval:
        raise OOBIndexError(string)
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
        raise CoordinatesError(string)
    # check coordinates boundaries
    if x<0 or x>12 or y<0 or y>18:
        raise OOBCoordinatesError(string)
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
        raise NetValueError(string)
    return string

def str2trans(string):
    """
    Convert it into uppercase and check if string is a valid
    transformation name.
    """
    trans = ["TCW", "TAW", "FUD", "FLR"]
    string = string.upper()
    if string not in trans:
        raise TransValueError(string)
    return string

class IndexValueError(Exception):
    def __init__(self, string):
       self.message = "Cannot convert index " + string
       super().__init__(self, self.message)
class OOBIndexError(Exception):
    def __init__(self, string):
       self.message = "Index " + string + " out of bound"
       super().__init__(self, self.message)
class CoordinatesError(Exception):
    def __init__(self, string):
       self.message = "Cannot convert coordinates " + string
       super().__init__(self, self.message)
class OOBCoordinatesError(Exception):
    def __init__(self, string):
       self.message = "Coordinates " + string + " out of bound"
       super().__init__(self, self.message)
class NetValueError(Exception):
    def __init__(self, string):
       self.message = "Invalid net name " + string
       super().__init__(self, self.message)
class TransValueError(Exception):
    def __init__(self, string):
       self.message = "Invalid trans name " + string
       super().__init__(self, self.message)
