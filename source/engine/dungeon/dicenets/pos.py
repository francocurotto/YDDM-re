class Pos():
    """
    Defines a position in the y-x plane.
    """
    def __init__(self, y, x):
        self.y = y
        self.x = x

    # isometric transformation functions
    def turn_cw(self):
        """
        Turn position clock-wise 90 degrees.
        """
        self.y, self.x = -1*self.x, self.y

    def turn_aw(self):
        """
        Turn position anti clock-wise 90 degrees.
        """
        self.y, self.x = self.x, -1*self.y

    def flip_ud(self):
        """
        Flip position up-down, that is, in the vertical
        direction.
        """
        self.y = -1*self.y

    def flip_lr(self):
        """
        Flip position left-right, that is, in the horizontal
        direction.
        """
        self.x = -1*self.x

    def get_neighbors(self):
        """
        Return neighbor positions. Neighbors are considered
        positions separated by one unit verically and 
        horizontally only.
        """
        pos_l = Pos(self.y, self.x-1)
        pos_r = Pos(self.y, self.x+1)
        pos_u = Pos(self.y-1, self.x)
        pos_d = Pos(self.y+1, self.x)

        return [pos_l, pos_r, pos_u, pos_d]

    def offset(self, pos):
        """
        Offset position by an amount given by other position.
        """
        self.y += pos.y
        self.x += pos.x

    def distance_to(self, pos2):
        """
        Calculates the manhattan distance to other position 
        pos2.
        """
        return abs(self.y-pos2.y) + abs(self.x-pos2.x) 

    def __eq__(self, other):
        """
        Redefinition of equality.
        """
        if isinstance(other, self.__class__):
            return self.y == other.y and self.x == other.x
        else:
            return False

    def __str__(self):
        """
        Redefinition of str.
        """
        return chr(self.x+97) + str(self.y+1)
