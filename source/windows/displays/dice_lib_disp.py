from dice_list_disp import DiceListDisp

class DiceLibDisp(DiceListDisp):
    """
    Like DiceListDisp but for the dice library.
    """
    def __init__(self, library):
        dice_list = library.values()
        super().__init__(dice_list, disp_id=True)
