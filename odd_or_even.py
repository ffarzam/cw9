def is_all_even(lst):

    if all([item % 2 == 0 for item in lst]):
        return "All the item in your list are even"
    else:
        return "Not every item in your list are even"


my_lst = list(map(int, input().split(" ")))

print(is_all_even(my_lst))


