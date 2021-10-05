import urwid
from duel import Duel

class VersusCpuWin(urwid.Frame):
    """
    Window where a duel versus the CPU is played.
    """
    def __init__(self):
        # create duel
        self.duel = Duel
        
        # create the pool and summon display
        self.pool_disp = PoolDisp(self.duel.player.pool)
        dice = self.pool_disp.focus.dice
        self.summon_disp = SummonDisp(dice)

        # column 1 contains pool and summon displays
        self.col1 = urwid.Pile([self.pool_disp, 
            self.summon_disp])

        # body collects all principal widgets
        self.body = urwid.Columns([col1])

        super().__init__(body)
