#!/usr/bin/env python3


# This program turns inches into meters.

# 1 inch is equal to 0.0254 meters
# 1 meter is equal to 39.3701 inches

# Ask the user what unit they're giving.
print("What are you giving me?: inches or meters?")
# 'inches' or 'meters' anything else is bad input
unit = input()

if unit == "inches":
    constant = 0.0254
elif unit == "meters":
    constant = 39.3701
else:
    raise ValueError("I don't know what value you want to convert to!")

print(f"How many {unit}?")
answer = float(input()) * constant
print(f"The answer is {answer}!")