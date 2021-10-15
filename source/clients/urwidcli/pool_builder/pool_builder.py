import urwid
from urwidcli.pool_builder.builder_widget import BuilderWidget
from urwidcli.pool_builder.discard_widget import DiscardWidget

class PoolBuilder(urwid.WidgetPlaceholder):
    """
    Main class of the pool builder implemented in urwid.
    """
    def __init__(self, args):
        self.builderwid = BuilderWidget(args)
        self.discardwid = DiscardWidget()
        #super().__init__(self.builderwid)
        super().__init__(urwid.Filler(self.discardwid))
        #super().__init__(urwid.Overlay(self.discardwid, 
        #    self.builderwid, "center", ("relative", 50),
        #    "middle", ("relative", 50)))
