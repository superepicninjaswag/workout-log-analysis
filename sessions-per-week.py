"""Graph sessions per week."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import sys


if __name__ == "__main__":
    argc = len(sys.argv)
    path = sys.argv[1]
    if argc != 2:
        print("usage:", sys.argv[0], "filepath")
        quit(1)

    # Handle filepath arg
    logs = Path(path)
    if not logs.is_file():
        print(
            "Error: filepath doesn't point to a regular file, or filepath doesn't exist, or filepath is a broken symlink.",
            file=sys.stderr,
        )
        quit(1)

    # Open log and collect workouts where exercise was done
    log = pd.read_excel(path)
    weeks = {}
    days = []

    for row in log.iterrows():
        year = row[1][0].year
        week = row[1][0].week
        if year == 2023:
            if row[1][0].day_of_year in days:
                continue
            else:
                days.append(row[1][0].day_of_year)

            if week in weeks:
                weeks[week] += 1
            else:
                weeks[week] = 1

    # Create graph
    fig, ax = plt.subplots()
    ax.plot(weeks.keys(), weeks.values())
    ax.set(
        xlabel="Week",
        ylabel="Sessions",
        title="Sessions per week",
    )
    ax.grid()
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment="right")

    fig.savefig("sessions-graph.png")
