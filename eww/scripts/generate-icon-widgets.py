import json
import subprocess
import time

icon_set = json.loads(
    subprocess.run(["eww", "get", "icon-set"], capture_output=True, text=True).stdout
)

while True:
    windows = json.loads(
        subprocess.run(
            ["hyprctl", "-j", "clients"], capture_output=True, text=True
        ).stdout
    )

    workspace = json.loads(subprocess.run(["hyprctl", "-j", "activeworkspace"], capture_output=True, text=True).stdout)

    # Go through list of all windows, determine it's icon and workspace. Add to results.
    generated_widgets = [[], [], [], [], [], [], [], [], []]
    for window in windows:
        paths = [
            v
            for (k, v) in icon_set.items()
            if window["initialTitle"].lower() in k.lower()
            or window["class"].lower() in k.lower()
        ]
        path = paths[0] if len(paths) >= 1 else ""

        # Add generated widget to workspace list
        generated_widgets[int(window["workspace"]["id"])-1].append(
            f" (image :path '{path}' :image-width 12 :image-height 12 :width 12 :height 12)"
        )

    # Add start to all widgets
    for i in range(0, 9):
        class_name = None
        if workspace['id'] == i+1:
            class_name = 'active-workspace'
        else:
            class_name = 'workspace' if len(generated_widgets[i]) != 0 else 'workspace-empty'

        generated_widgets[i].insert(0, f"(button :class '{class_name}' :onclick 'hyprctl dispatch workspace {i+1}' :vexpand true (box :space-evenly false :spacing 8 :valign 'center' :vexpand true {i+1}")

    # Cap off all templates
    for i in range(0, 9):
        generated_widgets[i].append("))")
        generated_widgets[i] = ''.join(generated_widgets[i])
        print(f"{i}: {generated_widgets[i]}")

    subprocess.run(
        ["eww", "update", f"rendered-window-icons={json.dumps(generated_widgets)}"]
    )

    time.sleep(1)
