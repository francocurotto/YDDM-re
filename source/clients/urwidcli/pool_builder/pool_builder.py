import urwid
from urwidcli.pool_builder.builder_widget import BuilderWidget
from urwidcli.pool_builder.save_widget import SaveWidget
from urwidcli.pool_builder.discard_widget import DiscardWidget

class PoolBuilder(urwid.WidgetPlaceholder):
    """
    Main class of the pool builder implemented in urwid.
    """
    def __init__(self, args):
        self.poolname = args.pool
        self.builderwid = BuilderWidget(args)
        super().__init__(self.builderwid)

    def keypress(self, size, key):
        action = super().keypress(size, key)
        if action == "QUIT":
            self.open_quit_dialog()

    def open_quit_dialog(self):
        if self.builderwid.pool.is_full():
            # add save dialog on top
            savewid = SaveWidget(self, self.poolname)
            self.original_widget = urwid.Overlay(
                savewid, self.builderwid, "center", 50,
                "middle", "pack")
        else:
            # add dicard dialog on top
            discardwid = DiscardWidget(self)
            self.original_widget = urwid.Overlay(
                discardwid, self.builderwid, "center", 50,
                "middle", "pack")

    def return_builder(self):
        """
        Return to builder widget.
        """
        self.original_widget = self.builderwid
