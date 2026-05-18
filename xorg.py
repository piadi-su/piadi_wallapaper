import os


def main():
    while True:
        path = input("path: ")
        os.system(f"wal -i {path}")
        os.system(f"xwallpaper --stretch {path}")
        print(os.system(f"realpath {path}"))


if __name__ == "__main__":
    main()
