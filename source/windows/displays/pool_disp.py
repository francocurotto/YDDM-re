from dice_list_disp import DiceListDisp
from dice_disp import DiceDisp

class PoolDisp(DiceListDisp):
    """
    Displays a dice pool
    """
    LIMIT = 15 # Max size of pool

    def add_dice(self, dice):
        """
        Add dice to list. Check if list is full first. If
        full, return False.
        """
        if self.full():
            return False
        self.body.append(DiceDisp(dice))
        return True

    def remove_dice(self):
        """
        Remove focused dice from list.
        """
        index = self.get_focus_path()[0]
        self.body.pop(index)

    def full(self):
        """
        True if list is full.
        """
        return len(self.body) == self.LIMIT

    def empty(self):
        """
        True if list is empty.
        """
        return len(self.body) == 0
