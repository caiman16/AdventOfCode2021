with open('./data.txt') as file:
    line = file.readline().strip()
    positions = list(map(int, line.split(',')))

# Setup teh minimum fuel, while also calculating the fuel to move to position 0
min_fuel = sum(positions)
best_position = 0

for i in range(1, len(positions)):
    current_fuel = 0
    for position in positions:
        displacement = abs(position - i)
        current_fuel += displacement
        if current_fuel > min_fuel:
            break
    if current_fuel < min_fuel:
        min_fuel = current_fuel
        best_position = i

print(f'For part 1, the best position is {best_position} with total fuel consumption of {min_fuel}')

# New minimum fuel for position 0
min_fuel1 = sum(positions)*sum(positions)

def optimize_displacement(array, optimal):
    for i in range(0, len(array)):
        current_total = 0
        for element in array:
            change = abs(element - i)
            usage = sum(range(change + 1))
            current_total += usage
            if current_total > optimal:
                break
        if current_total < optimal:
            optimal = current_total
            place = i
    return optimal, place

min_fuel1, best_position = optimize_displacement(positions, min_fuel1)

print(f'For part 2, the best position is {best_position} with a total fuel consumption of {min_fuel1}')