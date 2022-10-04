# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: October 2022
# ICS3U-Assignment2.py File, Octagon calculator in python.

import sys


def main():
    if len(sys.argv) == 2:
        number = int(sys.argv[1])
    else:
        # input
        number = int(input("Type in any number that you want to see go through the 3X + 1 loop: "))

    # process
    if number < 1:
        print("\nYou can only use positives for 3X+1 problem")
        return

    while number > 1:
        if number % 2:
            number = number * 3 + 1
        else:
            number = int(number / 2)
        print("{:,}".format(number))
    print("\nThe number has stopped on the 1 and 2 infinity loop.")
    print("\n(1×3+1=4, 4:2=2, 2:2=1)")

    print("\n\nDone.")
    return


if __name__ == "__main__":
    main()
