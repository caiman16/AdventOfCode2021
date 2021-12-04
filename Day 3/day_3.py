# Initialize variables
gamma_rate = int()
epsilon_rate = int()
oxygen_generator_rating = int()
co2_scrubber_rating = int()
number_list = list()


# Read file and add tupled elements to a list
with open('data.txt') as file:
    while (line := file.readline().strip()):
        number_list.append(line)

def count_ones(list):
    first_number = str()
    second_number = str()
    if list.count('1') > len(list)/2:
        first_number = 1
        second_number = 0
    else:
        first_number = 0
        second_number = 1
    
    return first_number, second_number

def bin_to_dec(number):
    decimal, i, = 0, 0
    while(number != 0):
        reminder = number % 10
        decimal += reminder * pow(2, i)
        number = number// 10
        i += 1
    return decimal

def rates(list, first_rate, second_rate):
    digits = [[] for i in range(len(list[0]))]
    for i in range(len(digits)):
        for number in list:
            digits[i].append(number[i])
    
    for i, digit in enumerate(digits):
        first_rate_digit, second_rate_digit = count_ones(digit)
        first_rate += first_rate_digit * 10**(len(digits)-i-1)
        second_rate += second_rate_digit * 10**(len(digits)-i-1)
    first_rate, second_rate = bin_to_dec(first_rate), bin_to_dec(second_rate)
    return first_rate, second_rate

def oxygen_generator_calc(list):
    test_list = list
    for i in range(len(list[0])):
        if len(test_list) > 1:
            digit_list = []
            temp_list = []
            for number in test_list:
                digit_list.append(number[i])
            if digit_list.count('1') >= digit_list.count('0'):
                for number in test_list:
                    if number[i] == '1':
                        temp_list.append(number)
            else:
                for number in test_list:
                    if number[i] == '0':
                        temp_list.append(number)
            test_list = temp_list
        else:
            pass

    return bin_to_dec(int(test_list[0]))

def co2_scrubber_calc(list):
    test_list = list
    for i in range(len(list[0])):
        if len(test_list) > 1:
            digit_list = []
            temp_list = []
            for number in test_list:
                digit_list.append(number[i])
            if digit_list.count('1') < digit_list.count('0'):
                for number in test_list:
                    if number[i] == '1':
                        temp_list.append(number)
            else:
                for number in test_list:
                    if number[i] == '0':
                        temp_list.append(number)
            test_list = temp_list
        else:
            pass

    return bin_to_dec(int(test_list[0]))

gamma_rate, epsilon_rate = rates(number_list, gamma_rate, epsilon_rate)
oxygen_generator_rating = oxygen_generator_calc(number_list)
co2_scrubber_rating = co2_scrubber_calc(number_list)

print(f'The power consumption is {gamma_rate * epsilon_rate}')
print(f'The life support rating is {oxygen_generator_rating * co2_scrubber_rating}')