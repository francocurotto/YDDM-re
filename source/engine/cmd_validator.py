class CmdValidator():
    """
    Validate that command dicts are syntactically correct.
    """
    def __init__(self):
        self.reply = {
            "valid"   : False,
            "newturn" : False,
            "endduel" : False,
            "message" : ""}

    def validate(self, cmd):
        """
        Validate syntax, and check for KeyError using 
        try/except. 
        """
        try:
            self.validate_syntax(cmd)
        except KeyError as e:
            self.reply["message"] = "Key " + e.args[0] + \
                " not found in cmd: " + str(cmd)

        return self.reply

    def validate_syntax(self, cmd):
        """
        Validate syntax for command cmd.
        """
        # validate roll command
        if cmd["command"] == "ROLL":
            self.validate_roll(cmd)
        else:
            #TODO: change when all commands are implemented
            self.reply["valid"] = True
            self.reply["message"] = "Unknown command " + \
                cmd["command"]

    def validate_roll(self, cmd):
        """
        Validate roll command.
        """
        # validate for dice size
        if len(cmd["dice"]) != 3:
            self.reply["message"] = "Size of dice set " + \
                str(len(cmd["dice"])) + ", expected 3"
            return
        
        # validate for dice type
        for dice in cmd["dice"]:
            # validate if int
            if not isinstance(dice, int):
                self.reply["message"] = "Dice set item " + \
                "is not int"
                return
            if dice < 0 or dice > 14:
                self.reply["message"] = "Dice set item " + \
                    " out of range (" + str(dice) + ")"
                return

        # all tests passed
        self.reply["valid"] = True
