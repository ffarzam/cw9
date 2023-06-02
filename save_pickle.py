import pickle
import pathlib


class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"{self.name = }, {self.age = }, {self.address = }"





def read_file(x):  ####
    with open(x, 'rb') as f:
        info = pickle.load(f)
        return info

def write_file(x, info):  ####
    with open(x, 'wb') as f:
        pickle.dump(info, f)


def save_object(obj):

    info_file = pathlib.Path("obj.pickle")
    if info_file.exists():
        info = read_file("obj.pickle")

        info.append(obj)

        write_file("obj.pickle", info)
    else:
        with open("obj.pickle", 'wb') as f:
            pickle.dump([obj], f)


if __name__ == "__main__":
    name = input("Enter Your name: ")
    age = input("Enter Your age: ")
    address = input("Enter Your address: ")
    person = Person(name, age, address)

    save_object(person)

    info = read_file("obj.pickle")

    for i in info:
        print(i)


