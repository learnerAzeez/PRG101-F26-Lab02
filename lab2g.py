# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.

SINGLE_LOW_THRESHOLD = 50000
SINGLE_HIGH_THRESHOLD = 100000

MARRIED_LOW_THRESHOLD = 60000
MARRIED_HIGH_THRESHOLD = 120000

income = float(input("Enter your income :"))
status = input("Enter your status (single/married): ")

if status == "single":
    if income <= SINGLE_LOW_THRESHOLD:
        print("Tax rate: 10%")
    elif income <= SINGLE_HIGH_THRESHOLD:
        print("Tax rate: 20%")
    else:
        print("Tax rate: 30%")

elif status == "married":
    if income <= MARRIED_LOW_THRESHOLD:
        print("Tax rate: 10%")
    elif income <= MARRIED_HIGH_THRESHOLD:
        print("Tax rate: 20%")
    else:
        print("Tax rate: 30%")

else:
    print("Invalid status.")