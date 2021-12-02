# Initialize position, depth and directions
position = [0, 0]
position_2 = [0, 0]
aim = 0
directions = list()

# Read file and add tupled elements to a list
with open('data.txt') as file:
    while (line := file.readline().strip()):
        directions.append(tuple(i for i in line.split()))


def move(instruction, position):
    way = instruction[0]
    step = int(instruction[1])
    if way[0] == 'u':
        position[1] -= step
    elif way[0] == 'd':
        position[1] += step
    elif way[0] == 'f':
        position[0] += step
    else:
        print('Wrong direction')
    return position

def move_2(instruction, position, aim):
    way = instruction[0]
    step = int(instruction[1])
    if way[0] == 'f':
        position[0] += step
        position[1] += step * aim
    elif way[0] == 'u':
        aim -= step
    elif way[0] == 'd':
        aim += step
    return position, aim

for i in directions:
    position = move(i, position)
    position_2, aim = move_2(i, position_2, aim)

print(f'Final position with 1 is ({position[0]} forward, {position[1]} depth). The multipication is {position[0] * position[1]}')
print(f'Final position with 2 is ({position_2[0]} forward, {position_2[1]} depth). The multipication is {position_2[0] * position_2[1]}')