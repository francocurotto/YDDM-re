class CliView():
    def print_string(self, string):
        """
        Print a generic string.
        """
        if not string:
            print("", end="")
        else:
            print(string+"\n")
