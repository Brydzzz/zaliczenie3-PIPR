import csv
from random import randint, choice


def create_example_one_file(filename):
    info_options = ["last month", "this week", "never", "today"]
    with open(f"{filename}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "value", "info"])
        for i in range(1, 100):
            value = randint(1, 50)
            info = choice(info_options)
            writer.writerow([i, value, info])


def create_example_two_file(filename):
    with open(f"{filename}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["key", "value", "timestamp"])
        for i in range(1, 34):
            key = f"{randint(1, 1489):04}"
            value = randint(1, 50)
            writer.writerow([key, value, i])


if __name__ == "__main__":
    create_example_one_file("file")
    create_example_two_file("other")
