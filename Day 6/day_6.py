with open('./data.txt') as file:
    line = file.readline().strip()
    fish_list_temp = list(map(int, line.split(',')))

# Create the working list
fish_list = [0]*9
for i in range(len(fish_list_temp)):
    fish_list[fish_list_temp[i]] +=1

days = 80
days2 = 256

# Calculate the fish
def simulate_fish(fish_array, time):
    for i in range(time):
        temp = fish_array[8]
        for j in range(8):
            fish_array[j-1] = fish_array[j]
        fish_array[7] = temp
        fish_array[6] += fish_array[8]
    
    return sum(fish_array)


# Create copies to not affect the original list
fish_list_1 = fish_list.copy()
fish_list_2 = fish_list.copy()

# Part 1
total_1 = simulate_fish(fish_list_1, days)

# Part 2
total_2 = simulate_fish(fish_list_2, days2)

print(f'After {days} days, there are {total_1} lanternfish')
print(f'After {days2} days, there are {total_2} lanternfish')