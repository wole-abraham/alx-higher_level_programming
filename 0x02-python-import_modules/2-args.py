#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv
    if len(sys.argv) < 2:
        print("0 arguments.")
    elif len(sys.argv)-1 == 1:
        argv = sys.argv
        print("{} argument:".format(len(argv)-1))
        print("{}: {} ".format(len(argv)-1, argv[len(argv)-1]))
    else:
        print("{} arguments:".format(len(argv)-1))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
