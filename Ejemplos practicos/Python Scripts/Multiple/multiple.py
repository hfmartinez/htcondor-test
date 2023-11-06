#!/usr/bin/env python3

import os
import sys
import operator

if len(sys.argv) != 3:
    print(f"Usage: {os.path.basename(sys.argv[0])} DATA NUM_WORDS")
    sys.exit(1)
input_filename = sys.argv[1]
num_words = int(sys.argv[2])

words = {}

with open(input_filename, "r") as my_file:
    for line in my_file:
        line_words = line.split()
        for word in line_words:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

sorted_words = sorted(words.items(), key=operator.itemgetter(1))
for word in sorted_words[-num_words:]:
    print(f"{word[0]} {word[1]:8d}")
