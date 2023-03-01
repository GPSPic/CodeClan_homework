# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# 2. Print the difference between the largest and smallest value:
# numbers.sort()
# highest_index = len(numbers) - 1
# diff_numbers = numbers[highest_index] - numbers[0]
# print(diff_numbers)

largest = max(numbers)
smallest = min(numbers)
print(largest - smallest)


# 3. Print True if the list contains a 2 next to a 2 somewhere.

# FOR each NUMBER in NUMBERS
#  compare if index + 1 = 2
#  if 2 NUMBER = 2 in a row
# THEN print TRUE

# numbers_index = 0

# for number in numbers:
    # if number == 2:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

first_two = numbers.index(2)
numbers.pop(first_two)

second_two = numbers.index(2)

if first_two == second_two:
    print(True)

# result = False
# index = 1
# for number in numbers:
#     if (number == 2 and numbers[index-1] ==2):
#         result = True
#     index += 1
# print(result)
        

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

# numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# numbers_six = numbers.index(6)
# numbers_seven = numbers.index(7)

# sum_outside_sixseven = 0

# for number in numbers:
#     if numbers.index(number) < numbers_six and numbers.index(number) > numbers_seven:
#         sum_outside_sixseven += number

# print(sum_outside_sixseven)

# numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# sum_numbers = 0
# index_six = numbers.index(6)
# print(index_six)
# index_seven = numbers.index(7)
# print(index_seven)

total = 0
found_6 = False
for number in numbers:
    if number == 6:
        found_6 = True
    elif found_6:
        if number == 7:
            found_6 = False
    else:
        total += number

print(total)

# while numbers.count(6) != 0 or numbers.count(7) != 0:
#     del numbers[index_six:index_seven]
# another failed attempt

#  another aborted attempt
# for number in numbers:
#     if index_six < index_seven:
#         del numbers[index_six:index_seven]
#     else:
#         sum_numbers += number

# infinite loop, whoops!
# while index_six < index_seven:
#     del numbers[index_six:index_seven]

# print(numbers)
# print(sum_numbers)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

index = 0
total = 0
for number in numbers:
    if number == 13 or numbers[index-1] == 13:
        pass
    else:
        total += number
        index += 1
print(total)