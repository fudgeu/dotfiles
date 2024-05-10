import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
import subprocess
import json

icon_theme = Gtk.IconTheme.get_default()

icon_set = {}

for obj in Gio.AppInfo.get_all():
    icon = obj.get_icon()
    if icon is None:
        continue
    icon_filename = icon_theme.lookup_by_gicon(icon, 0, 0)
    if icon_filename != None:
        final_filename = icon_filename.get_filename()
        icon_set[icon.to_string()] = final_filename

subprocess.run(["eww", "update", f"icon-set={json.dumps(icon_set)}"])