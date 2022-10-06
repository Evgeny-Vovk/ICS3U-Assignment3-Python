# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: October 2022
# ICS3U-Assignment3.py File, 3X+1 problem in python.


def main():
    # input
    initial_number = int(input("Type in any number that you want to see go through the 3X + 1 loop: "))
    number = initial_number
    step = 0

    # process
    if number < 1:
        print("\nYou can only use positives for 3X+1 problem.")
        return

    while number > 1:
        if number % 2:
            print("{:,} × 3 + 1 =".format(number), end="")
            number = number * 3 + 1
        else:
            print("{:,} : 2 =".format(number), end="")
            number = int(number / 2)
        print(" {:,}".format(number))
        step += 1
        print("Step {:,}\n".format(step))
    print("\nThe 3X + 1 problem has been resolved in ", end="")
    print("{0:,} steps, starting from number {1:,}.".format(step, initial_number))

    print("\n\nDone.")
    return


if __name__ == "__main__":
    main()
