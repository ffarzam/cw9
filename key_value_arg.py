
def func(*args):
    d={}
    for key, value in enumerate(args):
        d[key+1] = value
    return d


print(func(1,"2",3,"hi",5))
