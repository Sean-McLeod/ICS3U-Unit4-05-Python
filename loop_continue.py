#!/usr/bin/env python3

# Created by Sean McLeod
# Created on December 2020
# This program is the number adding program


def main():
    # this function tells the user what the total added number is

    total = 0

    # input
    string_add = input("How many numbers are you going to add: ")

    # process & output
    try:
        number_add = int(string_add)

        if number_add >= 0:
            for loop_counter in range(number_add):
                # input
                positive_string = input("Enter a number to add: ")

                try:
                    positive_number = int(positive_string)

                    if positive_number > 0:
                        total = total + positive_number
                    else:
                        print("Please enter a positive integer. "
                              "This won't be added")
                        continue

                except Exception:
                    print("This is not a number")

            print("\n", end=""
                  "Sum of the numbers above is {}".format(total))

        else:
            print("This is a negative number")
    except Exception:
        print("This is not a number")


if __name__ == "__main__":
    main()
