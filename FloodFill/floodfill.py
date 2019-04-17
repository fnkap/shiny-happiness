"""Flood fill algorithm.

Inspired by https://en.wikipedia.org/wiki/Flood_fill

Flood fill, also called seed fill, is an algorithm that determines the area connected to a given node in a
multi-dimensional array. It is used in the "bucket" fill tool of paint programs to fill connected, similarly-colored
areas with a different color, and in games such as Go and Minesweeper for determining which pieces are cleared."""

import queue
from colorama import init, Fore, Style

# Initialize colorama to color the input and the output
init()

# A list of rows representing the input of the algorithm
my_input = [['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]


class Node:
    """Represents a node of the input.

    Attributes:
        row (int): The number of the row.
        column (int): The number of the column.
        color (string): One of (Y, G, W, R, B, X, M)"""

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color


# A list of Node objects representing the input
nodes = []

# A list of positions to check for recursive flood fill with 8 directions
movements = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for r, _row in enumerate(my_input):
    for c, _color in enumerate(_row):
        nodes.append(Node(row=r, column=c, color=_color))


def flood_fill(node, target_color, replacement_color):
    """Run flood fill algorithm on node"""

    # Check constraints. If not fulfilled, return.
    if target_color == replacement_color:
        print("Error: target color is equal to replacement color")
        return
    if node.color != target_color:
        print("Error: node color is not equal to target color")
        return
    node.color = replacement_color

    # Using a FIFO queue
    q = queue.Queue()

    # Put the root node in to the queue
    q.put(node)

    while not q.empty():
        n = q.get()

        # Check if, for every movement allowed, the selected node is of the same color.
        # If found, replace the color and put in into the queue.
        for move in movements:
            selected_node = next(
                (x for x in nodes if (x.row == (n.row + move[0])) and (x.column == n.column + move[1])), None)
            if selected_node:
                if selected_node.color == target_color:
                    selected_node.color = replacement_color
                    q.put(selected_node)


def get_color(letter):
    """A fuction that maps letters to colors for colored output."""
    if letter == "Y":
        return Fore.YELLOW + letter + Style.RESET_ALL
    if letter == "G":
        return Fore.GREEN + letter + Style.RESET_ALL
    if letter == "W":
        return Fore.WHITE + letter + Style.RESET_ALL
    if letter == "R":
        return Fore.RED + letter + Style.RESET_ALL
    if letter == "B":
        return Fore.BLUE + letter + Style.RESET_ALL
    if letter == "X":
        return Fore.BLACK + letter + Style.RESET_ALL
    if letter == "M":
        return Fore.MAGENTA + letter + Style.RESET_ALL


if __name__ == "__main__":

    # Printing colored input
    print("Your input is:\n\n")

    for _row in my_input:
        colored_row = list(map(get_color, _row))
        print(" ".join(colored_row))

    # Giving some space in the output
    print()

    # Select a cell by row and column to start flood fill.
    # Indexes are zero-based.
    target_row = 9
    target_column = 3
    target_node = next((x for x in nodes if (x.row == target_row) and (x.column == target_column)), None)

    if not target_node:
        print(f"Can't find the node in the row {target_row} and column {target_column}")
        exit()

    num_rows = len(my_input)

    print("Target color: {}".format(target_node.color))
    print("Running flood fill.\n\n")

    # Parameters are hardcoded for example purposes
    flood_fill(target_node, 'X', 'M')

    # Printing result
    print("Printing result.\n")
    for i in range(num_rows):
        _row = [item.color for item in nodes if item.row == i]
        colored_row = list(map(get_color, _row))
        print(" ".join(colored_row))
