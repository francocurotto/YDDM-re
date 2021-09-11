class Generator():
    """
    Generic generator.
    """
    def __init__(self):
        self.info = infodict[self.key]
        self.desc = descdict[self.key]

infodict = {
    "p" : "print info:       p [ARG1 ARG2]",
    "r" : "roll dice:        r D1 D2 D3",
    "d" : "dimension dice:   d D N XY [T1 T2]",
    "s" : "skip summon/cast: s",
    "m" : "move monster:     m XY1 XY2",
    "a" : "attack target:    a XY1 XY2",
    "g" : "guard attack:     g",
    "w" : "wait attack:      w",
    "e" : "end turn:         e",
    "c" : "cast ability:     c [ARG1 ...]",
    "j" : "jump to warp:     j XY1 XY2",
    "q" : "quit game:        q"}

printdesc = "\
- PRINT COMMANDS: p [ARG1 ARG2]\n\
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
- ROLL COMMAND: r D1 D2 D3\n\
    - r D1 D2 D3: roll dice D1, D2 and D3 from dice pool"

dimdesc = "\
- DIM COMMAND: d D N XY [T1 T2]\n\
    - d D N XY [T1 T2]: dimension dice D from\n\
        candidates, using net N, at position XY, and\n\
        optionally apply transformations T1, T2 to net\n\
        before dimension."

skipdesc = "\
- SKIP COMMAND: s\n\
    - s: skip dimension or cast"

movedesc = "\
- MOVE COMMAND: m XY1 XY2\n\
    - m XY1 XY2: move monster at position XY1 to position\n\
        XY2."

attackdesc = "\
- ATTACK COMMAND: a XY1 XY2\n\
    - a XY1 XY2: make monster at position XY1 attack target\n\
        at position XY2."

guarddesc = "\
- GUARD COMMAND: g\n\
    - g: guard against attack"

waitdesc = "\
- WAIT COMMAND: w\n\
    - w: do not reply to an attack"

endturndesc = "\
- ENDTURN COMMAND: e\n\
    - e: end turn"

quitdesc = "\
- QUIT COMMAND: q\n\
    - q: quit game"

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
