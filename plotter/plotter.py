import sys
import argparse
import json
from matplotlib import pyplot as plt

from datetime import datetime


def read_from_json(path, timestamp, values, fro=0, to=99999):
    charts = []
    with open(path, "r") as file:
        data = json.load(file)
        for value in values:
            chart_keys = []
            chart_values = []
            for row in data:
                try:
                    if datetime.fromisoformat(
                        row[timestamp]
                    ) > datetime.fromisoformat(fro) and datetime.fromisoformat(
                        row[timestamp]
                    ) < datetime.fromisoformat(
                        to
                    ):
                        measurement = (row[timestamp], row[value])
                        chart_keys.append(measurement[0])
                        chart_values.append(measurement[1])
                except KeyError:
                    pass
            charts.append((chart_keys, chart_values))
    return charts


def generate_plot(data):
    for i, plot_data in enumerate(data):
        keys = plot_data[i][0]
        values = plot_data[i][1]
        plt.plot(keys, values)
    plt.show()


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--timestamp", default="timestamp")
    parser.add_argument("--value", default=["value"], nargs="+")
    parser.add_argument("--fro")
    parser.add_argument("--to")
    args = parser.parse_args(arguments[1:])
    if args.path:
        data = read_from_json(
            args.path, args.timestamp, args.value, args.fro, args.to
        )
        generate_plot(data)


if __name__ == "__main__":
    main(sys.argv)
