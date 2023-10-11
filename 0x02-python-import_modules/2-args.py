#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Get the number of command-line arguments (excluding the script name itself)
    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Loop through the command-line arguments and print them
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
