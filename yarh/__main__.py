from . import parser
import sys


def main():
    if len(sys.argv) == 1:
        print("compile yarh to html")
        print("usage: yarh -- [YARH_STRING]")
        print("       yarh <YARH_FILE>...")
        print("       yarh <YARH_FILE>... -- [YARH_STRING]")
        return 1
    fromfile = True
    for arg in sys.argv[1:]:
        if arg == "--":
            fromfile = False
            continue
        if fromfile:
            f = open(arg, "r")
            print(parser.parseyarh(f.read()).html())
        else:
            print(parser.parseyarh(arg).html())
            fromfile = True
            break
    if not fromfile:
        print(parser.parseyarh(sys.stdin.read()).html())
    return 0


if __name__ == "__main__":
    sys.exit(main())
