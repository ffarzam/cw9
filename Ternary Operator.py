my_func = lambda x: f'{x} is a positive integer' if x > 0 else f'{x} is a negative integer' if 0 > x else 'zero!'


def check_number(number):

    try:
        number = int(number)
        print(my_func(number))
    except ValueError:
        print("Input must be an integer")


var = input("Enter an integer: ")
check_number(var)