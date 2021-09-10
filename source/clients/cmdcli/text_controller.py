from cmdcli.generators.cmd_gen import CmdGenerator
from cmdcli.generators.cmd_gen import NotEnoughCmdArgs
from cmdcli.generators.cmd_gen import InvalidCommandKey
from cmdcli.generators.print_gen import PrintGenerator
from cmdcli.generators.sanitize_functs import *
from duel.roll_state import DuplicatedDice

class TextController():
    """
    Input controller for text interface.
    """
    def __init__(self, view, engine, stringifier):
        self.view = view
        self.engine = engine
        self.cmdgen = CmdGenerator()
        self.printgen = PrintGenerator(engine, stringifier)
        self.cmderrors = (IndexValueError, OOBIndexError,
            CoordinatesError, OOBCoordinatesError, 
            NetValueError, TransValueError, 
            DuplicatedDice, NotEnoughCmdArgs,
            InvalidCommandKey)

    def get_command(self):
        """
        get command from user text input.
        """
        while True:
            text = self.get_text_input()
            split = text.split()
            try:
                if not split: # empty command
                    self.view.print_string("", end="")
                elif split[0] == "l": # list commands
                    self.list_commands()
                elif split[0] == "p": # print command
                    self.run_print_command(split)
                elif split[0] == "q": # quit command
                    self.view.exit_game()
                else: # engine command
                    return self.cmdgen.create_command(split)
            except self.cmderrors as e:
                self.view.print_string(e.message)

    def list_commands(self):
        """
        Print list of all commands.
        """
        # get print commands
        strlist = [self.printgen.desc]
        # get engine commands
        strlist += self.cmdgen.list_commands()
        # quit command
        strlist += [quitdesc]
        # print list
        self.view.print_string("\n\n".join(strlist))

    def run_print_command(self, split):
        """
        Run print command.
        """
        string = self.printgen.get_string(split[1:])
        self.view.print_string(string)

quitdesc = "\
- QUIT COMMAND: q\n\
    - q: quit game"
