import copy
from dice_list_disp import DiceListDisp
from dice_disp import DiceDisp

class PoolDisp(DiceListDisp):
    """
    Displays a dice pool.
    """
    def __init__(self, pool):
        self.pool = pool
        super().__init__(self.pool.contents)

    def add_dice(self, dice):
        """
        Add dice to pool and update display.
        """
        # make copy to avoid reference errors
        dice_copy = copy.deepcopy(dice)
        success = self.pool.add(dice_copy)
        self.update_add()
        return success

    def remove_dice(self):
        """
        Remove focused dice from pool and update display.
        """
        index = self.get_focus_path()[0]
        self.pool.remove(index)
        self.update_remove()

    def update_add(self):
        """
        Update the display after the addition of a dice.
        """
        # generate list of dice from display
        dice_list = [disp.dice for disp in self.body]
        for dice in self.pool.contents:
            if dice not in dice_list:
                self.body.append(DiceDisp(dice))
                break # assumes only one dice addition per key

    def update_remove(self):
        """
        Update the display after the removal of a dice.
        """
        for disp in self.body:
            if disp.dice not in self.pool.contents:
                self.body.remove(disp)
                break # assumes only ine dice removal per key
