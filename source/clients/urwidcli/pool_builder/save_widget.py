import urwid
import yaml

class SaveWidget(urwid.LineBox):
    """
    Window shown with the save dialog.
    """
    def __init__(self, builder, poolname):
        # if no poolname, use default
        if not poolname:
            poolname = "dicesets/.yaml"
        # instruction text
        text = urwid.Text("Enter pool path and name:",
            "center")
        # edit section
        edit = urwid.Edit(edit_text=poolname, 
            edit_pos=poolname.index("."))
        padedit = urwid.Padding(edit, left=5, right=5)
        # save button
        savebut = urwid.Button("Save", save_pool, 
            {"builder":builder, "edit":edit})
        # cancel button
        cancelbut = urwid.Button("Cancel", return_builder,  
            builder)
        # buttons line
        buttons = urwid.Columns([urwid.Divider(),
            (8,savebut), urwid.Divider(), (10,cancelbut), 
            urwid.Divider()])
        # widgets pile
        self.pile = urwid.Pile([urwid.Divider(), text, 
            padedit, urwid.Divider(), buttons, 
            urwid.Divider()])
        super().__init__(self.pile)

def save_pool(button, data):
    # get dice pool indeces
    indeces = []
    for dicewid in data["builder"].builderwid.pool.body:
        indeces.append(dicewid.dice.id)

    # write yaml file
    filename = data["edit"].get_edit_text()
    with open(filename, "w") as f:
        yaml.dump(indeces, f)

    # exit buider
    raise urwid.ExitMainLoop()

def return_builder(button, builder):
    builder.return_builder()
