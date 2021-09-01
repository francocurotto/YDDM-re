from commandline.text_view import TextView

class CliView(TextView):
    def print_string(self, string, end="\n\n"):
        """
        Print a generic string.
        """
        print(string, end=end)
