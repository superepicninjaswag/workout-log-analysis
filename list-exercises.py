"""Retrieve the names of all the exercises I did and how many times I did them"""
from pathlib import Path

import pandas as pd
import sys


if __name__ == "__main__":
    argc = len(sys.argv)
    path = sys.argv[1]
    if argc != 2 and argc != 3:
        print("usage:", sys.argv[0], "filepath [max]")
        quit(1)

    # Handle log file path
    logs = Path(path)
    if not logs.is_file():
        print("Error: filepath doesn't point to a regular file, or filepath doesn't exist, or filepath is a broken symlink.",
              file=sys.stderr)
        quit(1)

    # Handle max count arg
    if argc == 3:
        try:
            max_count = int(sys.argv[2])
            if max_count < 1:
                raise ValueError
        except ValueError:
            print("Error:", "Invalid number. Please provide a positive integer.",
                  file=sys.stderr)
            quit(1)

    data = pd.read_excel(path)
    count = {}
    for lift in data["Lift"]:
        if lift in count:
            count[lift] += 1
        else:
            count[lift] = 1

    for lift in count:
        if argc == 2:
            print(lift, count[lift])
        elif count[lift] <= max_count:
            print(lift, count[lift])
