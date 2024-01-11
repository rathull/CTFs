#!/usr/local/bin/python3

import re

PATTERN = "[A-Za-z]{5}-\d+-[r-u]+..x{4,}"

string = input("HEY THERE, what do you want???\n")

if (re.match(PATTERN,string)):
    with open("flag.txt","r") as f:
        print("Gotcha. Here's your flag: " , end="")
        print(f.read(),end="")
else:
    print("GET OUT AND DON'T COME BACK.")

# AAAAA-123-rstuxyxxxx
# cyber{express_yourself_regularly}