#!/usr/bin/env python3

import os
import sys

if len(sys.argv) != 2:
    print(f"Usage: {os.path.basename(sys.argv[0])} DATA")
    sys.exit(1)
input_filename = sys.argv[1]

words = {}

with open(input_filename, "r", encoding="iso-8859-1") as my_file:
    for line in my_file:
        word = line.strip().lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

for word in sorted(words.keys()):
    print(f"{words[word]:8d} {word}")
