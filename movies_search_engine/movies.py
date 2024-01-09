import argparse
import sys
from pathlib import Path
import csv


def do_a_search(path, title):
    with open(path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        matches = []
        for row in reader:
            movie_title = row["title"]
            if movie_title.lower() == title.lower():
                year = row["year"]
                genre = row["genre"]
                duration = row["duration"]
                description = row["description"]
                movie_info = (
                    f"{movie_title}\nyear: {year}\ngenre: {genre}\n"
                    f"duration: {duration}\ndescription: {description}"
                )
                matches.append(movie_info)
        if matches:
            message = "\n".join(matches)
        else:
            message = f"{title} is not in database"
        print(message)


def get_duplicates(path, titles, duplicates):
    with open(path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title = row["title"]
            if title not in titles:
                titles.append(title)
            else:
                duplicates.append(title)


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("-r", action="store_true")
    parser.add_argument("-d", action="store_true")
    args = parser.parse_args(arguments[1:])
    titles = []
    duplicates = []
    if args.d:
        if args.r:
            path = Path(args.path)
            for file in path.rglob("*.csv"):
                get_duplicates(file, titles, duplicates)
        else:
            get_duplicates(args.path, titles, duplicates)
        duplicates_formatted = "\n".join(duplicates)
        duplicates_msg = (
            f"You have duplicates of this movies: {duplicates_formatted}"
        )
        no_duplicates_msg = "There are no duplicates"
        print(f"{duplicates_msg if duplicates else no_duplicates_msg}")
    title = input("Enter movie title: ")
    if args.r:
        path = Path(args.path)
        for file in path.rglob("*.csv"):
            do_a_search(file, title)
    else:
        do_a_search(args.path, title)


if __name__ == "__main__":
    main(sys.argv)
