import io
import subprocess
import time

process = subprocess.Popen(
    [
        "playerctl",
        "--follow",
        "metadata",
        "--format",
        "{{artist}}#{{title}}#{{mpris:artUrl}}",
    ],
    stdout=subprocess.PIPE,
)

while True:
    line = process.stdout.readline()
    if not line:
        break
    line = line.decode("UTF-8").replace("\n", "")
    metadata = line.split("#")
    subprocess.run(["eww", "update", f"artist-name={metadata[0]}"])
    subprocess.run(["eww", "update", f"song-name={metadata[1]}"])
    subprocess.run(["eww", "update", f"album-art={metadata[2]}"])
    time.sleep(0.5)

print("Done")
