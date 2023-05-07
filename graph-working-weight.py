"""Graph the working weight for a given exercise over time."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import sys


if __name__ == "__main__":
    argc = len(sys.argv)
    path = sys.argv[1]
    if argc != 3:
        print("usage:", sys.argv[0], "filepath exercisename")
        quit(1)

    # Handle filepath arg
    logs = Path(path)
    if not logs.is_file():
        print("Error: filepath doesn't point to a regular file, or filepath doesn't exist, or filepath is a broken symlink.",
              file=sys.stderr)
        quit(1)

    # Handle exercisename arg
    exercise_name = sys.argv[2]

    # Open log and collect workouts where exercise was done
    log = pd.read_excel(path)
    dates = []
    intesity = []

    for row in log.iterrows():
        if row[1][2] == exercise_name:
            volume = 0
            best = 0.0
            for i in range(3, len(row[1])):
                if not pd.isna(row[1][i]):
                    set = str(row[1][i]).strip().split("@")
                    if len(set) < 2:
                        print("Error: Something wrong with set notation, ",
                              set, file=sys.stderr)
                        quit(1)
                    if float(set[1]) > best:
                        best = float(set[1])
            dates.append(row[1][0])
            intesity.append(best)

    # Create graph
    fig, ax = plt.subplots()
    ax.plot(dates, intesity)
    ax.set(xlabel="Date", ylabel="Intensity (lb)",
           title="Working weight over time for "+exercise_name)
    ax.grid()
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')

    fig.savefig("wwot-graph.png")
