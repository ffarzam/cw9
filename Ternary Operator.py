

my_func = lambda x: f'{x} is a positive integer' if x > 0 else f'{x} is a negative integer' if 0 > x else f'{x = }'

var = int(input("Enter an integer: "))

print(my_func(var))
