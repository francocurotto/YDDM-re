class CmdChecker():
    """
    Checks if command dicts are syntactically correct.
    """
    def __init__(self):
        self.reply = {
            "valid"   : False,
            "message" : ""}

    def check(self, cmd):
        """
        Check if command cmd is syntactically correct.
        """
        # check command key
        if "command" not in cmd.keys():
            self.reply["message"] = 
                "No command key in command"
            return self.reply
        
        # check for roll command
        elif cmd["command"] == "ROLL":
            self.check_roll(cmd)

