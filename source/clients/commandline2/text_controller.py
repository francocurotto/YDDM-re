class TextController():
    """
    Input controller for text interface.
    """
    def __init__(self, view):
        self.view = view

    def get_command():
        """
        get command from user text input.
        """
        while True:
            text = self.get_text_input()
            try:
                return self.create_command(text)
            except InvalidCommandText:
                string = self.get_string_reply(text)
                self.view.show_string_reply(string)
