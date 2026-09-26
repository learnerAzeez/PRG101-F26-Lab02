# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

# TO DO 1: Follow the instructions given in README.md file

import sys

if len(sys.argv) == 1:
    print("This script requires exactly two arguments. No arguments were provided!")
elif len(sys.argv) == 3:
    print("hello user, good job, your provided two arguments!")
else:
    print("this script requires exactly two arguments. you provided", len(sys.argv) - 1, "arguments.")