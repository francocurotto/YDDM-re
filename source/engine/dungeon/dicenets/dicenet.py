from dungeon.dicenets.pos import Pos

# constants
trans = ["TCW", "TAW", "FUD", "FLR"]

class DiceNet():
    """
    Positions of the tiles created when a dice is dimensioned
    (unfolded).
    """
    def __init__(self):
        self.center = self.get_center()
        self.transdict = {} # map keys to functions
        self.transfunc = [self.turn_cw, self.turn_aw,
            self.flip_lr, self.flip_ud]
        for name, func in zip(trans, self.transfunc):
            self.transdict[name] = func

    def get_center(self):
        """
        Returns the center position of net given by Pos(0,0).
        """
        for pos in self.poslist:
            if pos == Pos(0,0):
                return pos

    def apply_trans(self, translist):
        """
        Apply a list of transformations, identified by 
        strings to the net.
        """
        for trans in translist:
            self.transdict[trans]()

    def offset(self, offset):
        """
        Move all positions on net an offset amount. 
        """
        for pos in self.poslist:
            pos.offset(offset)
        
    def turn_cw(self):
        """
        Turn all positions on net clock-wise 90 degrees.
        """
        for pos in self.poslist:
            pos.turn_cw()

    def turn_aw(self):
        """
        Turn all positions on net anti clock-wise 90 degrees.
        """
        for pos in self.poslist:
            pos.turn_aw()

    def flip_lr(self):
        """
        Turn all positions on net left-right.
        """
        for pos in self.poslist:
            pos.flip_lr()

    def flip_ud(self):
        """
        Turn all positions on net up-down.
        """
        for pos in self.poslist:
            pos.flip_ud()
