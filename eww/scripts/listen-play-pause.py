import io
import subprocess

process = subprocess.Popen(
    [
        "playerctl",
        "--follow",
        "status",
    ],
    stdout=subprocess.PIPE,
)

while True:
    line = process.stdout.readline()
    if not line:
        break
    line = line.decode("UTF-8").replace("\n", "")
    is_playing = "true" if line == "Playing" else "false"
    subprocess.run(["eww", "update", f"is-playing={is_playing}"])
    print(is_playing)
