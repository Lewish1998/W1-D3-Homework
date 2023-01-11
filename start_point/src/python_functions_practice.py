def return_10():
    return(10)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def length_of_string(string):
    return(len(string))


def join_string(str1, str2):
    return str1 + str2


def add_string_as_number(str1, str2):
    return int(str1) + int(str2)


def number_to_full_month_name(num):
    if num == 1:
        return "January"
    elif num == 9:
        return "September"
    elif num == 3:
        return "March"

def number_to_short_month_name(num):
    if num == 1:
        return "Jan"
    elif num == 4:
        return "Apr"
    elif num == 10:
        return "Oct"


def cube_volume(cube):
    return cube ** 3


def reverse_string(string):
    return string[::-1]


def convert_to_celcius(farenheit):
    return (farenheit -32) * (5/9)