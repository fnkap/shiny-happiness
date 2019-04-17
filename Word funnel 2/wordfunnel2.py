import queue
import time

"""This script is inspired by a reddit post which can be found here:
https://www.reddit.com/r/dailyprogrammer/comments/99d24u/20180822_challenge_366_intermediate_word_funnel_2/

A word funnel is a series of words formed by removing one letter at a time from a starting word,
keeping the remaining letters in order. For the purpose of this challenge, a word is defined as an entry in the enable1 
word list. An example of a word funnel is:

gnash => gash => ash => ah
This word funnel has length 4, because there are 4 words in it.

Given a word, determine the length of the longest word funnel that it starts. You may optionally also return the funnel 
itself (or any funnel tied for the longest, in the case of a tie).

Examples
funnel2("gnash") => 4
funnel2("princesses") => 9
funnel2("turntables") => 5
funnel2("implosive") => 1
funnel2("programmer") => 2

I implemented Breadth First Search and Depth First Search
"""

# Load words from enable1.txt into a list
with open("enable1.txt") as f:
    words = f.readlines()
words = [x.strip() for x in words]


class Node:
    """Class that represent a node in the search three.

    Attributes:
        word (str): The word in this node.
        depth (int): The depth of the node in the three.
        father (Node): The father node.
        """

    def __init__(self, word, depth=1, father=None):
        self.word = word
        self.depth = depth
        self.father = father

    def expand(self):
        """Returns a list of child nodes of this node."""
        word_as_list = list(self.word)
        child_nodes = []
        for index, character in enumerate(word_as_list):
            word_as_list.pop(index)
            new_word_as_str = "".join(word_as_list)
            if new_word_as_str in words:
                child_nodes.append(Node(new_word_as_str, self.depth + 1, self))
            word_as_list.insert(index, character)
        return child_nodes


def search(input_word, algorithm):
    """Searches the tree

    Attributes:
        input_word (str): The word of the input
        algorithm (str): bfs or dfs
    """
    if algorithm == "bfs":
        fringe = queue.Queue()
    else:
        fringe = queue.LifoQueue()

    root_node = Node(input_word)
    fringe.put(root_node)
    solutions = []

    while not fringe.empty():
        node_to_process = fringe.get()
        child_nodes = node_to_process.expand()
        if len(child_nodes) > 0:
            for child in child_nodes:
                fringe.put(child)
        else:
            solutions.append(node_to_process)

    if len(solutions) > 0:
        return solutions
    else:
        return None


def funnel2(word, algorithm="bfs"):
    """Launches the search, calculates execution time, prints output."""
    start_time = time.time()
    print(f"\n\nSearching the funnel for word: {word}")

    solutions = search(word, algorithm)

    maximum = max(solution.depth for solution in solutions)
    print("This word funnel has length {}".format(maximum))
    for solution in solutions:
        if solution.depth == maximum:
            funnel_words = [solution.word]
            father = solution.father
            while father:
                funnel_words.append(father.word)
                father = father.father
            funnel_words.reverse()
            print(" => ".join(funnel_words))
    print("It took {} seconds".format(time.time() - start_time))
    print("Algorithm used: {}".format(algorithm))
    print("=" * 40)


def find10(algorithm):
    """Optional bonus 1
    Find the one word in the word list that starts a funnel of length 10.
    """
    start_time = time.time()
    for word in words:
        print("Checking {}".format(word))
        solutions = search(word, algorithm)
        maximum = max(solution.depth for solution in solutions)

        if maximum >= 10:
            print("The word {} funnel has length {}".format(word, maximum))

            for solution in solutions:
                if solution.depth == maximum:
                    funnel_words = [solution.word]
                    father = solution.father
                    while father:
                        funnel_words.append(father.word)
                        father = father.father
                    funnel_words.reverse()
                    print(" => ".join(funnel_words))

            print("It took {} seconds".format(time.time() - start_time))
            print("Algorithm used: {}".format(algorithm))
            print("=" * 40)
            return
        else:
            print(f"Funnel length: {maximum}")


funnel2("gnash")
funnel2("princesses")
funnel2("turntables")
funnel2("implosive")
funnel2("programmer")
find10("bfs")
