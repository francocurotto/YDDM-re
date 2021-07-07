from stringifier import Stringifier

class Replier():
    """
    Print the information of a reply of the engine.
    """
    def __init__(self, icontype):
        self.stringifier = Stringifier(icontype)

    def print_reply(self, reply):
        message = reply["message"]
        
        # reply has roll result
        if "roll" in reply.keys():
            message += get_roll_string(reply["roll"])

        return message

    def get_roll_string(roll):
        """
        Get convert roll list into a string.
        """
        return self.stringifier.stringify_roll(roll)
