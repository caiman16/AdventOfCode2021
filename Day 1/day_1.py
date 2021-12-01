def depth_increase(previous, current):
    if current > previous:
        return 1
    else:
        return 0

# Start a list for the data
depths = []

# Read file and add elements to a list
with open('data.txt') as file:
    while (line := file.readline().strip()):
        depths.append(int(line))

# Start the initial depth and count
count = 0
previous_depth =depths[0]
# Read all depths
for depth in range(1, len(depths)):
    count += depth_increase(previous_depth, depths[depth])
    previous_depth = depths[depth]

# 2nd part
previous_window = depths[0]+depths[1]+depths[2]
window_count = 0
for depth in range(1, len(depths)-2):
    new_window = depths[depth]+depths[depth+1]+depths[depth+2]
    window_count += depth_increase(previous_window, new_window)
    previous_window = new_window

# Return final count increase
print(f'Final single increse is {count}')
print(f'Final window increse is {window_count}')