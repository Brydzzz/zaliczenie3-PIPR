import sys
import argparse
import csv
from collections import Counter
import json
from rich.prompt import Confirm


def get_column_names(filename):
    with open(filename) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        return csv_reader.fieldnames


def get_number_of_rows(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        return sum(1 for row in reader) - 1


def get_unique_values(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        content = list(reader)
        fieldnames = get_column_names(filename)
        uniques = {}
        for fieldname in fieldnames:
            column_values = [row.get(fieldname) for row in content]
            unique_values_count = len(set(column_values))
            uniques.update({fieldname: unique_values_count})
        return uniques


def count_values(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        content = list(reader)
        fieldnames = get_column_names(filename)
        count = {}
        for fieldname in fieldnames:
            column_values = [row[fieldname] for row in content]
            values_counts = dict(Counter(column_values))
            count.update({fieldname: values_counts})
        return count


def save_to_json(
    csv_paths,
    json_filename,
    if_columns=None,
    if_rows=None,
    if_unique=None,
    if_count=None,
):
    data = {}
    for csv_file in csv_paths:
        file_data = {}
        if if_columns:
            columns = get_column_names(csv_file)
            file_data.update({"columns": columns})
        if if_rows:
            rows = get_number_of_rows(csv_file)
            file_data.update({"rows": rows})
        if if_unique:
            unique = get_unique_values(csv_file)
            file_data.update({"unique": unique})
        if if_count:
            count = count_values(csv_file)
            file_data.update({"count": count})
        data.update({csv_file: file_data})
    with open(json_filename, "w") as file:
        json.dump(data, file, indent=4)


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    parser.add_argument(
        "--columns", action="store_true", help="names of columns"
    )
    parser.add_argument("--rows", action="store_true", help="number of rows")
    parser.add_argument(
        "--unique",
        action="store_true",
        help="number of unique values in each column",
    )
    parser.add_argument(
        "--count",
        action="store_true",
        help="counts occurence of values for each column",
    )
    parser.add_argument(
        "--out", help="save result to .json file", metavar="FILENAME"
    )
    parser.add_argument("-f", action="store_true", help="overwrite .json file")

    args = parser.parse_args(arguments[1:])
    print(args)
    files = args.files
    for csv_file in files:
        if args.columns:
            print(get_column_names(csv_file))
        if args.rows:
            print(get_number_of_rows(csv_file))
        if args.unique:
            print(get_unique_values(csv_file))
        if args.count:
            print(count_values(csv_file))
    if not args.f:
        answer = Confirm.ask(f"The file: {args.out} already exists, overwrite")
        if not answer:
            return

    if args.out:
        save_to_json(
            args.files,
            args.out,
            args.columns,
            args.rows,
            args.unique,
            args.count,
        )


if __name__ == "__main__":
    main(sys.argv)
