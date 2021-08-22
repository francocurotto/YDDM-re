# Reply documentation

The reply is a dictionary returned by the "update" function 
of the engine. It gives information about the result of a 
command execution.

# Reply Keys
- valid: True if the command is a legal move in the game, 
    i.e., it changed the state of the duel

- message: A string with text on the result of the command

- flags: list of strings that indicate the ocurrence of an
    event triggered by the command. List of flags:

    - ROLL:     the current player rolled the dice
    - MLATTACK: the current player attacked the opponent 
                monster lord
    - NEWTURN:  the current player ended it's turn
    - ENDDUEL:  The duel ended
