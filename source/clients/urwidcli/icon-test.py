import yaml
import urwid

# get icons
icons = yaml.full_load(open("../../ICONS.yaml"))["emoji"]

# create icon widget list
iconwids = []
lenwids = [urwid.Text("")]
for icon in icons.values():
    if isinstance(icon,str):
        iconwid = urwid.Text(icon.strip())
        iconwids.append(iconwid)
        lenwid = urwid.Text(str(len(icon)))
        lenwids.append(lenwid)

# create layout widgets
pile1wid = urwid.Pile(iconwids)
pile2wid = urwid.Pile(lenwids)
boxwid = urwid.LineBox(pile1wid)
colwid = urwid.Columns([(6,boxwid), pile2wid])
fillwid = urwid.Filler(colwid, valign="top")

# run urwid
loop = urwid.MainLoop(fillwid)
loop.run()
