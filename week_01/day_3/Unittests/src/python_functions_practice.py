def return_10():
    return 10

def add(number_1, number_2):
    sum_of_numbers = number_1 + number_2
    return sum_of_numbers 

def subtract(number_1, number_2):
    difference_of_numbers = number_1 - number_2
    return difference_of_numbers 

def multiply (number_1, number_2):
    product_of_numbers = number_1 * number_2
    return product_of_numbers

def divide (number_1, number_2):
    combination_of_numbers = number_1 / number_2
    return combination_of_numbers

def length_of_string(len_test):
    return len(len_test)
    
def join_string(sentence_1, sentence_2):
    return f'{sentence_1}{sentence_2}'

def add_string_as_number(number_1, number_2):
    sum_of_strings = int(number_1) + int(number_2)
    return sum_of_strings

def number_to_full_month_name(number):
    calander = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    calander_index = number - 1 
    return calander[calander_index]

def number_to_short_month_name(month_number):
    # calander_short = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # calander_short_index = number - 1 
    # return calander_short[calander_short_index]
    short_month = number_to_full_month_name(month_number)[0:3]
    return short_month

def volume_cube(side):
    volume = side ** 3
    # return volume
    return pow(side, 3)

# def reverse_string(text):
    # gnirts_desrever = []
    # index = len(text) #calculate length of string and save in index variable
    # while index > 0:
    #     gnirts_desrever += text[index-1] # save the value of text[index-1] in gnirts_desrever
    #     index = index - 1 #decrement index for encon
    # gnirts_desrever = ''.join(gnirts_desrever)
    # return gnirts_desrever
    # gnirts_desrever = list(reversed(text))
    # return ''.join(gnirts_desrever)
    
    # string_reversed = ''
    # index = len(text)
    # while index > 0:
    #     string_reversed += text[ index - 1 ]
    #     index = index -1
    # return string_reversed

def reverse_string(text):
    new_string = ""
    for letter in text:
        new_string = letter + new_string
    return new_string

def fahrenheit_to_celsius(temp_F):
    temp_C = (temp_F - 32) * 5 / 9
    return round(temp_C, 2)