#!/usr/bin/python3
import sys
from matrix.myutils.somePython import showMatrix


def dmsg(msg):
    sys.stdout.write("%s\n" % msg)
    sys.stdout.flush()


def main():
    item = int(sys.argv[1])
    rows = int(sys.argv[2])
    columns = int(sys.argv[3])
    ret = showMatrix(item, rows, columns)
    dmsg(ret)


if __name__ == "__main__":
    main()