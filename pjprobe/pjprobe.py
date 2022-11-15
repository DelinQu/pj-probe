#!/usr/bin/env python3
# coding=utf-8
from __future__ import print_function, annotations
import re
import subprocess
from typing import List, Tuple, Dict
import argparse
import sys
from colorama import init
import os
from .termgraph import chart
from .termgraph import check_data
from .termgraph import print_categories  # type: ignore

VERSION = "0.0.1"

init()

# ANSI escape SGR Parameters color codes
AVAILABLE_COLORS = {
    "red": 91,
    "blue": 94,
    "green": 92,
    "magenta": 95,
    "yellow": 93,
    "black": 90,
    "cyan": 96,
}

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
UNITS = ["", "K", "M", "B", "T"]
DELIM = ","
TICK = "▇"
SM_TICK = "▏"

try:
    range = xrange  # type: ignore
except NameError:
    pass


def init_args() -> Dict:
    """Parse and return the arguments."""
    parser = argparse.ArgumentParser(description="draw basic graphs on terminal")
    parser.add_argument("--title", default="GPU Visual", help="Title of graph")
    parser.add_argument("--user", default="qudelin", help="username")
    parser.add_argument("--partition", default="optimal", help="your partition")
    parser.add_argument("--type", default="reserved", help="reserved or spot")
    parser.add_argument(
        "--show_others",
        action="store_true",
        default=True,
        help="Display the other gpu number",
    )
    parser.add_argument(
        "--width", type=int, default=50, help="width of graph in characters default:50"
    )
    parser.add_argument("--format", default="{:<5.2f}", help="format specifier to use.")
    parser.add_argument(
        "--suffix", default="", help="string to add as a suffix to all data points."
    )
    parser.add_argument("--no-labels", action="store_true", help="Do not print the label column")
    parser.add_argument("--no-values", action="store_true", help="Do not print the values at end")
    parser.add_argument(
        "--space-between",
        action="store_true",
        help="Print a new line after every field",
    )
    parser.add_argument(
        "--color", nargs="*", default=["blue", "red", "yellow"], help="Graph bar color( s )"
    )
    parser.add_argument("--vertical", action="store_true", help="Vertical graph")
    parser.add_argument("--stacked", action="store_true", help="Stacked bar graph")
    parser.add_argument("--histogram", action="store_true", help="Histogram")
    parser.add_argument("--bins", default=5, type=int, help="Bins of Histogram")
    parser.add_argument(
        "--different-scale",
        action="store_true",
        help="Categories have different scales.",
    )
    parser.add_argument("--start-dt", help="Start date for Calendar chart")
    parser.add_argument("--custom-tick", default="", help="Custom tick mark, emoji approved")
    parser.add_argument("--delim", default="", help="Custom delimiter, default , or space")
    parser.add_argument(
        "--verbose", action="store_true", help="Verbose output, helpful for debugging"
    )
    parser.add_argument(
        "--label-before",
        action="store_true",
        default=False,
        help="Display the values before the bars",
    )
    parser.add_argument("--version", action="store_true", help="Display version and exit")
    if len(sys.argv) == 1:
        if sys.stdin.isatty():
            parser.print_usage()
            sys.exit(2)

    args = vars(parser.parse_args())

    if args["custom_tick"] != "":
        global TICK, SM_TICK
        TICK = args["custom_tick"]
        SM_TICK = ""

    if args["delim"] != "":
        global DELIM
        DELIM = args["delim"]

    return args


def get_nodes(
    user="$",
    partition="optimal",
    type="reserved",
) -> dict:
    try:
        ret = subprocess.check_output(
            f"squeue -p {partition} | grep {type} | grep {user}", shell=True
        ).decode("ascii")
    except:
        return {}

    lines = ret.split("\n")

    gpu_pattern = r"gpu:(.+?)"
    node_pattern = r"gpu:\S (.+\w)"

    node_gpu = {}

    for line in lines:
        node = re.findall(node_pattern, line)
        gpu = re.findall(gpu_pattern, line)

        if len(gpu) == 0:
            continue

        if node[0] in node_gpu:
            node_gpu[node[0]] += int(gpu[0])
        else:
            node_gpu[node[0]] = int(gpu[0])

    return node_gpu


def get_data(args: Dict) -> Tuple[List, List, List, List]:
    """Get data from a file or stdin and returns it.

    Filename includes (categories), labels and data.
    We append categories and labels to lists.
    Data are inserted to a list of lists due to the categories.

    i.e.
    labels = ['2001', '2002', '2003', ...]
    categories = ['boys', 'girls']
    data = [ [20.4, 40.5], [30.7, 100.0], ...]"""

    all_nodes = get_nodes(user="$", partition=args["partition"], type=args["type"])
    user_nodes = get_nodes(user=args["user"], partition=args["partition"], type=args["type"])

    if all_nodes == {}:
        print("Here is no process on {} machine!".format(args["type"]))
        return [], [], [], []

    labels = list(all_nodes)
    categories = ["ALL", "OTHERS", args["user"]] if args["show_others"] else ["ALL", args["user"]]
    data = list()
    for i, (k, v) in enumerate(all_nodes.items()):
        data.append([v])
        if args["show_others"]:
            data[i].append(v if k not in user_nodes else v - user_nodes[k])
        data[i].append(0 if k not in user_nodes else user_nodes[k])

    # Check that all data are valid. (i.e. There are no missing values.)
    colors = check_data(labels, data, args)
    if categories:
        # Print categories' names above the graph.
        print_categories(categories, colors)

    return categories, labels, data, colors


def main():
    """Main function."""
    args = init_args()

    if args["version"]:
        print("termgraph v{}".format(VERSION))
        sys.exit()

    os.system("svp list {}".format(args["partition"]))
    _, labels, data, colors = get_data(args)

    try:
        chart(colors, data, args, labels)
    except:
        pass


if __name__ == "__main__":
    main()
