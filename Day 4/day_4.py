matrix_list = list()
eof = False
board_counter = 0
is_winner = False
index = 0

def check_number(array, number):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == number:
                array[i][j] = 'X'

def check_rows(array):
    for row in array:
        if row.count('X') == len(row):
            return True
    return False

def check_columns(array):
    for col in range(len(array[0])):
        if array[0][col] == 'X':
            row = 1
            possible = True
            while row < len(array) and possible:
                if array[row][col] != 'X':
                    possible = False
                    break
                else:
                    row +=1
            if possible:
                return True
    return False


def winning_score(array, number):
    data_sum = 0
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col] != 'X':
                data_sum += array[row][col]
    return data_sum * number

# Read data into lists
with open('data.txt') as file:
    # Read the numbers list
    line = file.readline().strip()
    number_list = list(map(int, line.split(',')))

    while not eof:
        line = file.readline() # Pass first space
        # Check for end of file
        if not line:
            eof = True
        else:
            matrix_list.append(list())
            for i in range(5):
                line = file.readline().strip()
                row_to_fill = list(map(int, line.split()))
                matrix_list[board_counter].append(row_to_fill)
            board_counter +=1

while not is_winner:
    to_check = number_list[index]
    for i in range(len(matrix_list)):
        check_number(matrix_list[i], to_check)
        is_winner = check_rows(matrix_list[i])
        if is_winner:
            winner_board = i
            break
        is_winner = check_columns(matrix_list[i])
        if is_winner:
            winner_board = i
            break
    index += 1

print(f'The winning board is {winner_board} with a score of {winning_score(matrix_list[winner_board], to_check)}')
print()

matrix_list.pop(winner_board)
while len(matrix_list) > 1 or not is_winner:
    to_check = number_list[index]
    for i in range(len(matrix_list)):
        check_number(matrix_list[i], to_check)
        is_winner = check_rows(matrix_list[i])
        if is_winner:
            winner_board = i
            break
        is_winner = check_columns(matrix_list[i])
        if is_winner:
            winner_board = i
            break
    if len(matrix_list) > 1 and is_winner:
        is_winner = False
        matrix_list.pop(winner_board)
        #index += 1
    elif len(matrix_list) == 1 and is_winner:
        print(f'The last winning board is {winner_board} with a score of {winning_score(matrix_list[winner_board], to_check)}')
        break
    else:
        index += 1
    print  