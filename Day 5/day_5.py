coordinates = list()

def build_map(instructions):
    '''
    Take the coordinates and return a map matrix with 0 for height
    '''
    max_x = 0
    max_y = 0
    for i in range(len(instructions)):
        for j in range(2):
            if instructions[i][j][1] > max_x:
                max_x = instructions[i][j][1]
            if instructions[i][j][0] > max_y:
                max_y = instructions[i][j][0]
    rows, columns = max_x + 1, max_y + 1
    return [([0]*columns) for i in range(rows)]

def add_horizontals(full_map, point1, point2):
    start = 0
    end = 0
    row = point1[1]
    if point1[0] < point2[0]:
        start, end = point1[0], point2[0]
    else:
        start, end = point2[0], point1[0]
    for i in range(start, end+1):
        full_map[row][i] += 1
    return full_map

def add_verticals(full_map, point1, point2):
    start = 0
    end = 0
    column = point1[0]
    if point1[1] < point2[1]:
        start, end = point1[1], point2[1]
    else:
        start, end = point2[1], point1[1]
    for i in range(start, end+1):
        full_map[i][column] += 1
    return full_map

def add_diagonals(full_map, point1, point2):
    if point1[0] < point2[0]:
        col=point1[0]
        row=point1[1]
        end_col=point2[0]
        end_row=point2[1]
    else:
        col=point2[0]
        row=point2[1]
        end_col=point1[0]
        end_row=point1[1]
    while col <= end_col:
        full_map[row][col] += 1
        col +=1
        if end_row <= row:
            row -= 1
        else:
            row += 1
    return full_map

def add_heights(full_map):
    total = 0
    for i in range(len(full_map)):
        for j in range(len(full_map[0])):
            if full_map[i][j] > 1:
                total += 1
    return total

with open('data.txt') as file:
    while (line := file.readline().strip()):
        coordinates_temp = list()
        pairs = line.split(' -> ')
        pair1, pair2 = pairs[0].split(','), pairs[1].split(',')
        for i in range(2):
            pair1[i] = int(pair1[i])
            pair2[i] = int(pair2[i])
        coordinates_temp.append(pair1), coordinates_temp.append(pair2)
        coordinates.append(coordinates_temp)

floor_map = build_map(coordinates)

for i in range(len(coordinates)):
    if coordinates[i][0][1] == coordinates[i][1][1]:
        floor_map = add_horizontals(floor_map, coordinates[i][0], coordinates[i][1])
    elif coordinates[i][0][0] == coordinates[i][1][0]:
        floor_map = add_verticals(floor_map, coordinates[i][0], coordinates[i][1])

part1_total = add_heights(floor_map)
print(f'There are {part1_total} points higher than 1 in horizontal and vertcial lines only')

for i in range(len(coordinates)):
    if coordinates[i][0][1] != coordinates[i][1][1]:
        if coordinates[i][0][0] != coordinates[i][1][0]:
            floor_map = add_diagonals(floor_map, coordinates[i][0], coordinates[i][1])

part2_total = add_heights(floor_map)

print(f'There are {part2_total} points higher than 1 in all lines')
