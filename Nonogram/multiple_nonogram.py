import re
import time

first_pattern = r"\*+"  # Match a batch of consecutive asterisks
second_pattern = r"\*+ "  # Match a batch of consecutive asterisks interrupted by a space

# num_columns = 5
# num_rows = 5
# columns = []
# rows = []
# col_parse = '''"5","2,2","1,1","2,2","5"'''
# row_parse = '''"5","2,2","1,1","2,2","5"'''

# num_columns = 8
# num_rows = 11
# columns = []
# rows = []
# col_parse = '''"0","9","9","2,2","2,2","4","4","0"'''
# row_parse = '''"0","4","6","2,2","2,2","6","4","2","2","2","0"'''

num_columns = 30
num_rows = 20
columns = []
rows = []
col_parse = '''"1","1","2","4","7","9","2,8","1,8","8","1,9","2,7","3,4","6,4","8,5","1,11","1,7","8","1,4,8","6,8",
"4,7","2,4","1,4","5","1,4","1,5","7","5","3","1","1"'''
row_parse = '''"8,7,5,7","5,4,3,3","3,3,2,3","4,3,2,2","3,3,2,2","3,4,2,2","4,5,2","3,5,1","4,3,2","3,4,2","4,4,2",
"3,6,2","3,2,3,1","4,3,4,2","3,2,3,2","6,5","4,5","3,3","3,3","1,1"'''

# Parsing of the input
cp = re.findall(r'"(.*?)"', col_parse)  # Split column input
rp = re.findall(r'"(.*?)"', row_parse)  # Split row input

# For each series of numbers in apexes
for e in cp:
    comma_split = e.split(",")  # Separate by commas
    if len(comma_split) == 1:  # If only one number, append a int in columns
        columns.append(int(comma_split[0]))
    else:  # If more than one number, append a list of ints in columns
        to_append = []
        for v in comma_split:
            to_append.append(int(v))
        columns.append(to_append)

# Same thing for rows
for r in rp:
    comma_split = r.split(",")
    if len(comma_split) == 1:
        rows.append(int(comma_split[0]))
    else:
        to_append = []
        for v in comma_split:
            to_append.append(int(v))
        rows.append(to_append)

# For a CSP we need:
# A set of variables
# A set of domain values
# A set of constraints

# For this problem, possible values are asterisk and space.
domain = ['*', ' ']


# A cell is a variable. It has a row, a column and a Value which can be Null, asterisk or space
class Cell:
    def __init__(self, row, column, value=None):
        self.row = row
        self.column = column
        self.value = value


# The list 'table' will contain the list of our variables to which we will assign a value in the domain
table = []

for i in range(num_rows):
    for j in range(num_columns):
        table.append(Cell(i, j))


def check_constraints(cell, element):
    """This function will check if the element is breaking some constrain if applied to the cell"""

    # Suppose we want to assign the element 'asterisk' to a cell
    # Let's check if the constraints are violated

    if element == "*":
        row_objects = [c for c in table if c.row == cell.row]  # Select all cells in the same row
        column_objects = [c for c in table if c.column == cell.column]  # Select all cells in the same column
        # We are making a list of cells in the same row.
        # We will substitute the element that we want to assign from the domain
        # and check if the constraints are still valid
        row_list = []
        column_list = []
        for c in row_objects:
            if c.value is None:
                row_list.append("0")
                continue
            if c.value == " ":
                row_list.append(" ")
                continue
            if c.value == "*":
                row_list.append("*")
                continue
        for c in column_objects:
            if c.value is None:
                column_list.append("0")
                continue
            if c.value == " ":
                column_list.append(" ")
                continue
            if c.value == "*":
                column_list.append("*")
                continue
        row_list[cell.column] = "*"
        column_list[cell.row] = "*"

        # We are gonna transform the row objects in a string
        # We are gonna use regular expressions to check batches of asterisks

        row_string = "".join(row_list)
        column_string = "".join(column_list)
        row_batch = re.findall(first_pattern, row_string)
        column_batch = re.findall(first_pattern, column_string)

        # Check how many batches are there
        # Return False if there are more batches than the ones allowed in the constraints given

        if type(rows[cell.row]) is not int:
            if len(row_batch) > len(rows[cell.row]):
                return False
        else:
            if len(row_batch) > 1:
                return False
        if type(columns[cell.column]) is not int:
            if len(column_batch) > len(columns[cell.column]):
                return False
        else:
            if len(column_batch) > 1:
                return False

        # Check batches length
        # Return False if the length is more than the length given in the constraints
        if type(rows[cell.row]) is int:
            if len(row_batch[0]) > rows[cell.row]:
                return False
        else:
            for index, val in enumerate(row_batch):
                if len(val) > rows[cell.row][index]:
                    return False

        if type(columns[cell.column]) is int:
            if len(column_batch[0]) > columns[cell.column]:
                return False
        else:
            for index, val in enumerate(column_batch):
                if len(val) > columns[cell.column][index]:
                    return False

        # If last element, checks that all constraints are fulfilled
        count_none = len([c for c in table if c.value is None])
        if count_none == 1:
            asterisks_to_put = 0
            for n in rows:
                if type(n) is int:
                    asterisks_to_put += n
                else:
                    asterisks_to_put += sum(n)
            asterisks_already_put = len([c for c in table if c.value == '*'])
            if asterisks_already_put != asterisks_to_put - 1:
                return False

    # Check the same constraints in the same way we did for the asterisk
    # The thing that changes is the regular expression we use to detect
    # the space that is breaking a batch of asterisks

    if element == " ":
        row_objects = [c for c in table if c.row == cell.row]
        column_objects = [c for c in table if c.column == cell.column]
        row_list = []
        column_list = []
        for c in row_objects:
            if c.value is None:
                row_list.append("0")
                continue
            if c.value == " ":
                row_list.append(" ")
                continue
            if c.value == "*":
                row_list.append("*")
                continue
        for c in column_objects:
            if c.value is None:
                column_list.append("0")
                continue
            if c.value == " ":
                column_list.append(" ")
                continue
            if c.value == "*":
                column_list.append("*")
                continue
        row_list[cell.column] = " "
        column_list[cell.row] = " "
        row_string = "".join(row_list)
        column_string = "".join(column_list)
        row_batch = re.findall(second_pattern, row_string)
        column_batch = re.findall(second_pattern, column_string)

        try:
            # Check batches length
            if type(rows[cell.row]) is int:
                if len(row_batch[0]) - 1 < rows[cell.row]:
                    return False
            else:
                for index, val in enumerate(row_batch):
                    if len(val) - 1 < rows[cell.row][index]:
                        return False

            if type(columns[cell.column]) is int:
                if len(column_batch[0]) - 1 < columns[cell.column]:
                    return False
            else:
                for index, val in enumerate(column_batch):
                    if len(val) - 1 < columns[cell.column][index]:
                        return False

        # If there's still no batch, column_batch will be empty and
        # the previous code will throw an exception.
        # Let's get rid of this
        except IndexError:
            pass

        # If last element, checks that all constraints are fulfilled
        count_none = len([c for c in table if c.value is None])
        if count_none == 1:
            asterisks_to_put = 0
            for n in rows:
                if type(n) is int:
                    asterisks_to_put += n
                else:
                    asterisks_to_put += sum(n)
            asterisks_already_put = len([c for c in table if c.value == '*'])
            if asterisks_already_put != asterisks_to_put:
                return False

    return True


def select_unassigned(list_of_variables):
    for cell in list_of_variables:
        if cell.value is None:
            return cell
    return None


def backtracking_search(list_of_variables):
    solution = recursive_backtracking(list_of_variables)
    if solution:
        print("Solution found:")
        for row in range(num_rows):
            row_string = [c.value for c in list_of_variables if c.row == row]
            print('|'.join(row_string))
    else:
        print("Couldn't find any solution")


def recursive_backtracking(list_of_variables):
    selected_cell = select_unassigned(list_of_variables)
    if selected_cell is None:
        return list_of_variables
    for element in domain:
        if check_constraints(selected_cell, element):
            selected_cell.value = element
            result = recursive_backtracking(list_of_variables)
            if result:
                return result
            selected_cell.value = None
        else:
            continue
    return None


start = time.time()
backtracking_search(table)
print("Solved in {} seconds".format(time.time() - start))
