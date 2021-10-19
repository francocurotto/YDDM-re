import curses

class ANSITranslator():
    """
    Has the function to translate a string with ANSI escape
    values for color, into an object that can be used by 
    curses to print the same colors.
    """
    def __init__(self):
        # curses color definition
        curses.init_pair(1, curses.COLOR_WHITE, # blue bg
                            curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_WHITE, # red bg
                            curses.COLOR_RED)
        curses.init_pair(3, curses.COLOR_BLUE,  # blue fg
                            curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_RED,   # red fg
                            curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_BLACK, # black fg
                            curses.COLOR_BLACK) 

        # ansi-curses translation dict
        self.ansi_dict = {
        "\x1b[0m"          : curses.color_pair(0), # standard
        "\x1b[44m\x1b[37m" : curses.color_pair(1), # blue bg
        "\x1b[41m\x1b[37m" : curses.color_pair(2), # red bg
        "\x1b[34m"         : curses.color_pair(3), # blue fg
        "\x1b[31m"         : curses.color_pair(4), # red fg
        "\x1b[30m"         : curses.color_pair(5), # gray fg
        # bold blue fg
        "\x1b[1m\x1b[34m":curses.A_BOLD+curses.color_pair(3), 
        # bold red fg
        "\x1b[1m\x1b[31m":curses.A_BOLD+curses.color_pair(4), 
        # bold gray fg
        "\x1b[1m\x1b[30m":curses.A_BOLD+curses.color_pair(5),
        "\x1b[1m"          : curses.A_BOLD} # bold white fg

    def get_ctuples(self, line):
        """
        Convert a line that has ANSI escape characters for 
        color in a list of "curses tuples". Each curses tuple
        contains a portion of the line and the curses
        attributes that are equivalent to the ANSI escape
        characters, e.g.:
        ("Hello World!", curses.color_pair(1)).
        """
        ctuple_list = []
        while line:
            ctuple, rest = self.get_first_ctuple(line)
            ctuple_list.append(ctuple)
            line = rest
        return ctuple_list

    def get_first_ctuple(self, line):
        """
        Get the first ctuple of the line and return it with
        the rest of the line.
        """
        # get the ctuple information
        cpair, line = self.translate_ansi(line)
    
        # get ending of ansi application
        NEXT_ANSI = "\x1b["
        i = line.find(NEXT_ANSI)
        # case not next ansi
        if i < 0:
            return (line, cpair), ""
        
        # case next ansi
        return (line[:i], cpair), line[i:]

    def translate_ansi(self, line):
        """
        Translate the ANSI character at the start of the line
        into a curses color pair. The translation is done 
        with the ANSI dictionary. If no ANSI character is
        found at the begining, translate into standard colors
        instead.
        """
        for ansi in self.ansi_dict.keys():
            if line.startswith(ansi):
                # case ansi found
                return self.ansi_dict[ansi], line[len(ansi):]
    
        # case no ansi found, use reset color
        return self.ansi_dict["\x1b[0m"], line
