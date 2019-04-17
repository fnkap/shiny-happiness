from itertools import combinations

example_input = """6 15
Superman ++ Green Lantern
Superman ++ Wonder Woman
Superman -- Sinestro
Superman -- Cheetah
Superman -- Lex Luthor
Green Lantern ++ Wonder Woman
Green Lantern -- Sinestro
Green Lantern -- Cheetah
Green Lantern -- Lex Luthor
Wonder Woman -- Sinestro
Wonder Woman -- Cheetah
Wonder Woman -- Lex Luthor
Sinestro ++ Cheetah
Sinestro ++ Lex Luthor
Cheetah ++ Lex Luthor"""

challenge_input = """Daenerys Targaryen ++ Jon Snow
Daenerys Targaryen ++ Tyrion Lannister
Daenerys Targaryen ++ Varys
Daenerys Targaryen ++ Jorah Mormont
Daenerys Targaryen ++ Beric Dondarrion
Daenerys Targaryen ++ Sandor “the Hound” Clegane
Daenerys Targaryen ++ Theon and Yara Greyjoy
Daenerys Targaryen -- Sansa Stark
Daenerys Targaryen -- Arya Stark
Daenerys Targaryen -- Bran Stark
Daenerys Targaryen -- The Lords of the North and the Vale
Daenerys Targaryen -- Littlefinger
Daenerys Targaryen -- Cersei Lannister
Daenerys Targaryen -- Jaime Lannister
Daenerys Targaryen -- Euron Greyjoy
Jon Snow ++ Tyrion Lannister
Jon Snow ++ Varys
Jon Snow ++ Jorah Mormont
Jon Snow ++ Beric Dondarrion
Jon Snow ++ Sandor “the Hound” Clegane
Jon Snow -- Theon and Yara Greyjoy
Jon Snow -- Sansa Stark
Jon Snow -- Arya Stark
Jon Snow -- Bran Stark
Jon Snow -- The Lords of the North and the Vale
Jon Snow -- Littlefinger
Jon Snow -- Cersei Lannister
Jon Snow -- Jaime Lannister
Jon Snow -- Euron Greyjoy
Tyrion Lannister ++ Varys
Tyrion Lannister ++ Jorah Mormont
Tyrion Lannister ++ Beric Dondarrion
Tyrion Lannister ++ Sandor “the Hound” Clegane
Tyrion Lannister ++ Theon and Yara Greyjoy
Tyrion Lannister -- Sansa Stark
Tyrion Lannister -- Arya Stark
Tyrion Lannister -- Bran Stark
Tyrion Lannister -- The Lords of the North and the Vale
Tyrion Lannister -- Littlefinger
Tyrion Lannister -- Cersei Lannister
Tyrion Lannister -- Jaime Lannister
Tyrion Lannister -- Euron Greyjoy
Varys ++ Jorah Mormont
Varys ++ Beric Dondarrion
Varys ++ Sandor “the Hound” Clegane
Varys ++ Theon and Yara Greyjoy
Varys -- Sansa Stark
Varys -- Arya Stark
Varys -- Bran Stark
Varys -- The Lords of the North and the Vale
Varys -- Littlefinger
Varys -- Cersei Lannister
Varys -- Jaime Lannister
Varys -- Euron Greyjoy
Jorah Mormont ++ Beric Dondarrion
Jorah Mormont ++ Sandor “the Hound” Clegane
Jorah Mormont ++ Theon and Yara Greyjoy
Jorah Mormont -- Sansa Stark
Jorah Mormont -- Arya Stark
Jorah Mormont -- Bran Stark
Jorah Mormont -- The Lords of the North and the Vale
Jorah Mormont -- Littlefinger
Jorah Mormont -- Cersei Lannister
Jorah Mormont -- Jaime Lannister
Jorah Mormont -- Euron Greyjoy
Beric Dondarrion ++ Sandor “the Hound” Clegane
Beric Dondarrion ++ Theon and Yara Greyjoy
Beric Dondarrion -- Sansa Stark
Beric Dondarrion -- Arya Stark
Beric Dondarrion -- Bran Stark
Beric Dondarrion -- The Lords of the North and the Vale
Beric Dondarrion -- Littlefinger
Beric Dondarrion -- Cersei Lannister
Beric Dondarrion -- Jaime Lannister
Beric Dondarrion -- Euron Greyjoy
Sandor “the Hound” Clegane ++ Theon and Yara Greyjoy
Sandor “the Hound” Clegane -- Sansa Stark
Sandor “the Hound” Clegane -- Arya Stark
Sandor “the Hound” Clegane -- Bran Stark
Sandor “the Hound” Clegane -- The Lords of the North and the Vale
Sandor “the Hound” Clegane -- Littlefinger
Sandor “the Hound” Clegane -- Cersei Lannister
Sandor “the Hound” Clegane -- Jaime Lannister
Sandor “the Hound” Clegane -- Euron Greyjoy
Theon and Yara Greyjoy -- Sansa Stark
Theon and Yara Greyjoy -- Arya Stark
Theon and Yara Greyjoy -- Bran Stark
Theon and Yara Greyjoy -- The Lords of the North and the Vale
Theon and Yara Greyjoy -- Littlefinger
Theon and Yara Greyjoy -- Cersei Lannister
Theon and Yara Greyjoy -- Jaime Lannister
Theon and Yara Greyjoy -- Euron Greyjoy
Sansa Stark ++ Arya Stark
Sansa Stark ++ Bran Stark
Sansa Stark ++ The Lords of the North and the Vale
Sansa Stark ++ Littlefinger
Sansa Stark -- Cersei Lannister
Sansa Stark -- Jaime Lannister
Sansa Stark -- Euron Greyjoy
Arya Stark ++ Bran Stark
Arya Stark ++ The Lords of the North and the Vale
Arya Stark ++ Littlefinger
Arya Stark -- Cersei Lannister
Arya Stark -- Jaime Lannister
Arya Stark -- Euron Greyjoy
Bran Stark ++ The Lords of the North and the Vale
Bran Stark -- Littlefinger
Bran Stark -- Cersei Lannister
Bran Stark -- Jaime Lannister
Bran Stark -- Euron Greyjoy
The Lords of the North and the Vale ++ Littlefinger
The Lords of the North and the Vale -- Cersei Lannister
The Lords of the North and the Vale -- Jaime Lannister
The Lords of the North and the Vale -- Euron Greyjoy
Littlefinger -- Cersei Lannister
Littlefinger -- Jaime Lannister
Littlefinger -- Euron Greyjoy
Cersei Lannister ++ Jaime Lannister
Cersei Lannister ++ Euron Greyjoy
Jaime Lannister ++ Euron Greyjoy"""


def parse_input(inp, _friends, _enemies, _people):
    """Parses the input into a friends and enemies list of tuples"""
    inp_split = inp.split("\n")
    for row in inp_split[1:]:
        if "--" in row:
            person1 = row.split(" -- ")[0].strip()
            person2 = row.split(" -- ")[1].strip()
            _enemies.append((person1, person2))
        else:
            person1 = row.split(" ++ ")[0].strip()
            person2 = row.split(" ++ ")[1].strip()
            _friends.append((person1, person2))
        _people.add(person1)
        _people.add(person2)


if __name__ == "__main__":
    friends = []
    enemies = []
    people = set()
    parse_input(challenge_input, friends, enemies, people)

    people_list = list(people)

    # Getting every possible combination of three people in the list of people

    _combinations = list(combinations(range(len(people_list)), 3))

    _combinations = [list(c) for c in _combinations]

    for c in _combinations:
        f = 0  # Number of friendship relations in a sub graph of three elements
        e = 0  # Number of hatred relations in a sub graph of three elements
        first = people_list[c[0]]
        second = people_list[c[1]]
        third = people_list[c[2]]

        # Checking for every couple if they are friends or enemies

        if (first, second) in friends or (second, first) in friends:
            f += 1
        if (first, third) in friends or (third, first) in friends:
            f += 1
        if (second, third) in friends or (third, second) in friends:
            f += 1
        if (first, second) in enemies or (second, first) in enemies:
            e += 1
        if (first, third) in enemies or (third, first) in enemies:
            e += 1
        if (second, third) in enemies or (third, second) in enemies:
            e += 1

        # If we find three friends or one friend and two enemies in a sub graph
        # we know that this sub graph is balanced, and we can keep searching.
        # Else, we found an unbalanced sub graph, we print it and exit.

        if (f == 3) or (f == 1 and e == 2):
            continue
        else:
            print("This graph is unbalanced.")
            print("Analyzing these three entries:\n"
                  f"{first} | {second} | {third}\n"
                  "I found:")
            print(f"Friends: {f}\nEnemies: {e}")
            exit()
    print("Balanced")
