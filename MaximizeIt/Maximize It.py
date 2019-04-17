import itertools
import math

"""Maximize It!

Exercise from https://www.hackerrank.com/challenges/maximize-it/problem

You are given a function . You are also given  lists. The  list consists of  elements.

You have to pick one element from each list so that the value from the equation below is maximized: 

S = (f(X1) + f(X2) + ... + f(Xk)) % M

Xi denotes the element picked from the  list . Find the maximized value obtained Smax.

% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. 
You add the squares of the chosen elements and perform the modulo operation. 
The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains 2 space separated integers K and M. 
The next K lines each contains an integer Ni, denoting the number of elements in the ith list,
followed by Ni space separated integers denoting the elements in the list.

Constraints

1≤K≤7
1≤M≤1000
1≤Ni≤7
1≤Magnitude of elements in list≤9

Output Format

Output a single integer denoting the value .

Sample Input

3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

Sample Output
206

"""

sample_input = """3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10"""

# Get input from sample_input
# map applies a function to all the items in a list
K, M = map(int, sample_input.split("\n")[0].split(" "))
my_input = []
for line in sample_input.split("\n")[1:]:
    numbers = list(map(int, line.split(" ")))
    my_input.append(numbers)

print(f"K = {K}")
print(f"M = {M}")
print(f"Lists = {my_input}")


def f(x):
    return x * x


def s(args):
    to_sum = [f(x) for x in args]
    return sum(to_sum) % M


def magnitude(x):
    return int(math.log10(x))


# Validate the input checking the constraints
# First constraint 1≤K≤7
if K not in range(1, 8):
    print("\n\nThe value of K is not in the range 1-7")
    exit()

# Second constraint 1≤M≤1000
if M not in range(1, 1001):
    print("\n\nThe value of M is not in the range 1-1000")
    exit()

# Third constraint 1≤Ni≤7
for index, _list in enumerate(my_input):
    if len(_list) not in range(1, 8):
        print(f"\n\nThe list {index + 1} is not in range 1-7")
        exit()

    # Fourth constraint 1≤Magnitude of elements in list≤9
    for e in _list:
        if magnitude(e) not in range(0, 10):
            print(f"\n\nElement {e} not in range 1-10^9")
            exit()

if __name__ == "__main__":
    results = []
    for element in itertools.product(*my_input):
        elements_as_list = list(element)
        results.append(s(elements_as_list))
    maximum = max(results)
    print(f"\n\nThe result is: {maximum}\n\n")
