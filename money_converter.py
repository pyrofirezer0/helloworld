# we want to convert change in one denomination increments into full cash value starting from penny's all the way up.
# first I'm going to create my list of variables and there int value

# first thing I need to establish is what the input will mean when its put in

# Ask the user what unit they're giving.
print("What are you giving me?: pennies, nickles,"
      "dimes, quarters, penniesRoll, nicklesRoll,"
      "dimesRoll, quartersRoll, oneDollar, fiveDollar,"
      "tenDollar, twentyDollar, fiftyDollar, hundredDollar?")
# that is the only acceptable input anything else is bad input
unit = input()
# now to state how we are going to get the data through input and and use the variable names to create a function and then I'm going to create a other dictiionary to add alias
money_dict = {'penny': 0.01, 'Penny': 0.01, 'p': 0.01, 'P': 0.01, 'pennys': 0.01, 'Pennys': 0.01, 'pennies': 0.01, "Nickles": 0.05, "nickles"}

# originally I had 15 if else statements here but now I'm using a dictionary
if unit == "pennies" or "Penny's" or "Pennies" or "p" or "P":
    c1 = 0.01
elif unit == "nickles" or "Nickles" or "m" or "N":
    c1 = 0.05
elif unit == "dimes" or "Dimes" or "d" or "D":
    c1 = 0.10
elif unit == "quarters" or "q" or "Q":
    c1 = 0.25
elif unit == "penniesRoll" or "Pennyrolls" or "pr" or "PR":
    c1 = 0.50
elif unit == "nickleRoll" or "Nicklerolls" or "nr" or "NR":
    c1 = 2.00
elif unit == "dimeRoll" or "Dimerolls" or "dr" or "DR":
    c1 = 5.00
elif unit == "quarterRoll" or "Quarterroll" or "qr" or "QR":
    c1 = 10.00
elif unit == "dollar" or "Onedollar" or "O" or "o":
    c1 = 1.00
elif unit == "fivedollar" or "Fivedollar" or "F" or "f":
    c1 = 5.00
elif unit == "tenDollar" or "tenDollar" or "T" or "t":
    c1 = 10.00
elif unit == "Twentydollar" or "Twentydollar" or "tw" or "TW":
    c1 = 20.00
elif unit == "Fifty" or "fifty" or "fiftydollar" or "FT" or "ft":
    c1 = 50.00
elif unit == "Hundred" or "hundred" or "h" or "H":
    c1 = 100.00
else:
    raise ValueError("incorrect input value")

print(f"how many {unit}? ")
count = float(input())
answer = count * c1
print(f"your {count} comes to {answer}")
