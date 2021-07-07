class Replier():
    """
    Print the information of a reply of the engine.
    """
    def __init__(self, stringifier):
        self.stringifier = stringifier

    def print_reply(self, reply):
        message = reply["message"]
        
        # reply has roll result
        if "roll" in reply.keys():
            message += " "
            message += self.get_roll_string(reply["roll"])

        # print only if there is a mesage
        if message:
            print(message)

    def get_roll_string(self, roll):
        """
        Get convert roll list into a string.
        """
        return self.stringifier.stringify_roll(roll)
