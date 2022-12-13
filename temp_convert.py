#!/usr/bin/env python3
# Created by: Katie G
# Created on: December 13th, 2022
# This program will get the user's temperature in celsius,
# then use a separate function to calculate the temperature in
# fahrenheit, then display it back to the user.


# this function will get the user temperature in celsius,
# then it will convert the temperature to fahrenheit, then it will
# display it back to the user.
def fahrenheit():
    # getting the user input in celsius
    user_celsius = input("Please enter your temperature in Celsius! ")

    # try...catch to make sure the user input is a valid float.
    try:
        user_celsius_float = float(user_celsius)

        # converting the user temperature to fahrenheit.
        calculated_fahrenheit = (9 / 5) * user_celsius_float + 32

        # displaying the converted fahrenheit back to the user.
        print(
            "{} in Fahrenheit is {}!".format(user_celsius_float, calculated_fahrenheit)
        )
    except Exception:
        print("Please enter a valid number (decimals accepted!!)")
    finally:
        print("Thank you for using this program!")


# this function will call the fahrenheit function!
def main():
    # calling the fahrenheit function so that it will run.
    fahrenheit()


if __name__ == "__main__":
    main()
