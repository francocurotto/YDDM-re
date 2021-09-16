from cmdcli.replier import Replier
from cmdcli.error_replier import ErrorReplier

class TextView():
    """
    Output view for text interface.
    """
    def __init__(self, engine, stringifier):
        self.engine = engine
        self.stringifier = stringifier
        self.replier = Replier(self.engine, self.stringifier)
        self.ereplier = ErrorReplier(self.engine)

    def show_reply(self, reply):
        """
        Create reply message.
        """
        if reply["valid"]: # case valid command
            string = self.replier.gen_string(reply)
            #self.print_string(reply["message"])
        else: # case invalid reply
            string = self.ereplier.gen_string(reply)
        self.print_string(string)

    def exit_game(self):
        """
        Finish game script.
        """
        exit()
