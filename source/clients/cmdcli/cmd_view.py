from cmdcli.text_view import TextView

class CmdView(TextView):
    def update(self, reply):
        """
        Update view.
        """
        self.show_reply(reply)

    def print_string(self, string, end="\n\n"):
        """
        Print a generic string.
        """
        print(string, end=end)

    def print_header(self):
        """
        Print game header.
        """
        dsm = self.engine.dsm
        header = self.stringifier.stringify_header(dsm)
        self.print_string(header, end="\n")

    def exit_game(self):
        self.print_string("Bye!", end="\n")
        super().exit_game()
