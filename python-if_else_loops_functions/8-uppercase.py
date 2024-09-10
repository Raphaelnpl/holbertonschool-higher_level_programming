#!/usr/bin/python3

def uppercase(str):
    for char in str:
        # Check if the character is lowercase using its ASCII value
        if ord(char) >= 97 and ord(char) <= 122:
            # Convert it to uppercase by subtracting 32 from its ASCII value
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        # Print each character without a new line
        print("{}".format(upper_char), end="")
    # Print a new line at the end
    print("")
