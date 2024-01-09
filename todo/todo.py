import sys
import argparse
import requests
import json
from matplotlib import pyplot as plt

API_LINK = "https://jsonplaceholder.typicode.com/todos"


def reset():
    data = requests.get(API_LINK).json()
    with open("todos.json", "w") as file:
        json.dump(data, file, indent=4)


def user_todos(json_filename, user_id):
    with open(json_filename, "r") as file:
        data = json.load(file)
        for row in data:
            if row["userId"] == user_id:
                print(row["title"])


def display_all_todos(json_filename):
    with open(json_filename, "r") as file:
        data = json.load(file)
        for row in data:
            is_completed = "" if row["completed"] else "not "
            user_id = row["userId"]
            title = row["title"]
            print(
                f"User with userId:{user_id}"
                f" has {is_completed}completed task {title}"
            )


def list_not_completed(json_filename, user_id):
    with open(json_filename, "r") as file:
        data = json.load(file)
        for row in data:
            if row["userId"] == user_id and not row["completed"]:
                print(row["title"])


def toggle_todo(json_filename, task_id):
    with open(json_filename, "r") as file:
        data = json.load(file)
        for row in data:
            if row["id"] == task_id:
                row["completed"] = False if row["completed"] else True
    with open(json_filename, "w") as file:
        json.dump(data, file, indent=4)


def get_completed_stats(json_filename):
    with open(json_filename, "r") as file:
        data = json.load(file)
        tasks_bools = []
        for row in data:
            tasks_bools.append(row["completed"])
        completed = tasks_bools.count(True)
        not_completed = tasks_bools.count(False)
    return completed, not_completed


def bar_plot(json_filename):
    completed, not_completed = get_completed_stats(json_filename)
    plot_keys = ["completed", "not completed"]
    plot_values = [completed, not_completed]
    plt.bar(plot_keys, plot_values, width=0.6)
    plt.xlabel("Tasks Status")
    plt.ylabel("No. of tasks")
    plt.show()


def pie_plot(json_filename):
    data = get_completed_stats(json_filename)
    labels = ["completed", "not completed"]
    plt.pie(
        data,
        labels=labels,
        colors=["#aa65c7", "#14a34b"],
        autopct="%1.1f%%",
    )
    plt.show()


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("path", default="todos.json", nargs="?")
    parser.add_argument("--reset", action="store_true")
    parser.add_argument("--user", type=int)
    parser.add_argument("--list-not-completed", type=int)
    parser.add_argument("--toggle-todo", type=int)
    parser.add_argument("--bar-plot", action="store_true")
    parser.add_argument("--pie-plot", action="store_true")
    args = parser.parse_args(arguments[1:])
    if args.reset:
        reset()
    if args.user:
        user_todos(args.path, args.user)
    if len(arguments[1:]) == 0:
        display_all_todos(args.path)
    if args.list_not_completed:
        list_not_completed(args.path, args.list_not_completed)
    if args.toggle_todo:
        toggle_todo(args.path, args.toggle_todo)
    if args.bar_plot:
        bar_plot(args.path)
    if args.pie_plot:
        pie_plot(args.path)


if __name__ == "__main__":
    main(sys.argv)
