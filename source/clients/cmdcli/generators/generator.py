class Generator():
    """
    Generic generator.
    """
    def __init__(self):
        self.info = infodict[self.key]
        self.desc = descdict[self.key]

infodict = {
    "p" : "- p [ARG1 ARG2]   : print info",
    "r" : "- r D1 D2 D3      : roll dice",
    "d" : "- d D N XY [T1 T2]: dimension dice",
    "s" : "- s               : skip summon/cast",
    "m" : "- m XY1 XY2       : move monster",
    "a" : "- a XY1 XY2       : attack target",
    "g" : "- g               : guard attack",
    "w" : "- w               : wait attack",
    "e" : "- e               : end turn",
    "c" : "- c [ARG1 ...]    : cast ability",
    "j" : "- j XY1 XY2       : jump to warp",
    "q" : "- q               : quit game"}

printdesc = "\
PRINT COMMANDS: p [ARG1 ARG2]\n\
    - p:        print this help\n\
    - p cmd     print command list\n\
    - p cmd CMD print command CMD description\n\
    - p p:      print own dice pool\n\
    - p op:     print opponent dice pool\n\
    - p p INT:  print dice at INT in own dice pool\n\
    - p op INT: print dice at INT in opponent dice pool\n\
    - p d:      print dungeon\n\
    - p d XY:   print object in dungeon at position XY\n\
    - p c:      print own crest pool\n\
    - p oc:     print opponent crest pool\n\
    - p s:      print summon candidates\n\
    - p n:      print nets\n\
    - p t:      print transformations"
                    
rolldesc = "\
ROLL COMMAND: r D1 D2 D3\n\
    Roll dice D1, D2 and D3 from dice pool"

dimdesc = "\
- DIM COMMAND: d D N XY [T1 T2]\n\
    Dimension dice D from candidates, using net N, at\n\
    position XY, and optionally apply transformations T1,\n\
    T2 to net before dimension"

skipdesc = "\
- SKIP COMMAND: s\n\
    Skip dimension or cast"

movedesc = "\
- MOVE COMMAND: m XY1 XY2\n\
    Move monster at position XY1 to position XY2"

attackdesc = "\
- ATTACK COMMAND: a XY1 XY2\n\
    Make monster at position XY1 attack target at position XY2"

guarddesc = "\
- GUARD COMMAND: g\n\
    Guard against attack"

waitdesc = "\
- WAIT COMMAND: w\n\
    Do not reply to an attack"

endturndesc = "\
- ENDTURN COMMAND: e\n\
    End turn"

quitdesc = "\
- QUIT COMMAND: q\n\
    Quit game"

descdict = {
    "p" : printdesc,
    "r" : rolldesc,
    "d" : dimdesc,
    "s" : skipdesc,
    "m" : movedesc,
    "a" : attackdesc,
    "g" : guarddesc,
    "w" : waitdesc,
    "e" : endturndesc,
    "c" : None, # TODO: finish description
    "j" : None,
    "q" : quitdesc}
