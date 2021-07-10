class CmdGen():
    """
    Command generator.
    """
    def __init__(self, engine):
        self.engine = engine

    def str2int(self, i):
        """
        Convert string into int. If string is not convertable
        return None.
        """
        try:
            return int(i)
        except ValueError:
            print("Cannot convert integer")
            return None

    def get_dice(self, dicelist, i):
        """
        Get dice at position i of dicelist.
        """
