"""A Card Flipping Game

Description
This challenge is about a simple card flipping solitaire game. You're presented with a sequence of cards, some face up,
some face down. You can remove any face up card, but you must then flip the adjacent cards (if any).
The goal is to successfully remove every card. Making the wrong move can get you stuck.

In this challenge, a 1 signifies a face up card, a 0 signifies a face down card, a dot signifies a removed card.
We will also use zero-based indexing, starting from the left, to indicate specific cards.

Input Description
As input you will be given a sequence of 0 and 1, no spaces.

Output Description
Your program must print a sequence of moves that leads to a win. If there is no solution, it must print "no solution".
In general, if there's one solution then there are many possible solutions."""


def backtracking(state, moves):
    if all(i == '.' for i in state):
        return True

    for index, element in enumerate(state):

        temp_state = list(state)

        if element == '1':
            moves.append(index)
            # Removing a card
            temp_state[index] = '.'
            # Flipping left
            if index > 0:
                if temp_state[index - 1] == "0":
                    temp_state[index - 1] = "1"
                elif temp_state[index - 1] == "1":
                    temp_state[index - 1] = "0"
            # Flipping right
            if index < len(state) - 1:
                if temp_state[index + 1] == "0":
                    temp_state[index + 1] = "1"
                elif temp_state[index + 1] == "1":
                    temp_state[index + 1] = "0"
            if backtracking(temp_state, moves):
                return True
            moves.remove(index)

    return False


def run_backtracking(sequence):
    print()
    sequence_as_list = list(sequence)

    print(f"Input: {sequence_as_list}")

    moves = []

    if backtracking(sequence_as_list, moves):
        print("Solution found. Moves:")
        print(moves)
    else:
        print("No solution found")


run_backtracking("0100110")
run_backtracking("01001100111")
run_backtracking("100001100101000")
run_backtracking("010111111111100100101000100110111000101111001001011011000011000")
