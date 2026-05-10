import subprocess

while True:
    color = input("path: ")
    subprocess.run([
        "wal",
        "-i",
        color
        ], check=True)

