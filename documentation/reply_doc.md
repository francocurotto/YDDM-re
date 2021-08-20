# Reply documentation

The reply is a dictionary returned by the "update" function 
of the engine. It gives information about the result of a 
command execution.

# Reply Keys
## Mandatory Keys
- valid: True if the command is a legal move in the game, 
    i.e., it changed the state of the duel
- message: A string with text on the result of the command
- flags: list of strings that indicate the ocurrence of an
    event triggered by the command. List of flags:
        - NEWTURN: the current player ended it's turn
        - MLATTACK: the current player attacked the opponent
            monster lord
        - ENDDUEL: The duel ended

## Optional Keys
- roll: A list with the result of the roll in a serialized 
    format, e.g.:
    [{"crest":"SUMMON","mult":1},
     {"crest":"ATTACK","mult":2},
     {"crest":"DEFENSE","mult":3}]
