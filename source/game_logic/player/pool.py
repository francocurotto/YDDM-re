from dicesets_functions import create_dice_list

class Pool():
    """
    The pool of dice of a player.
    """
    SIZE = 15 # mnumber of dice in the pool
    def __init__(self, filename):
        self.contents = create_dice_list(filename)

    def full(self):
        """
        True if pool is full.
        """
        return len(self.contents) >= self.SIZE

    def empty(self):
        """
        True if pool is empty.
        """
        return len(self.contents) == 0

    def add(self, dice):
        """
        Add dice to pool. If full, ignore and return False.
        """
        if self.full():
            return False
        self.contents.append(dice)
        return True

    def remove(self, i):
        """
        Remove dice in pool at position i. If no dice at that
        position, ignore.
        """
        if 0 <= i < len(self.contents):
            del self.contents[i]
