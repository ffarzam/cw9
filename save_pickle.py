import pickle
import pathlib


class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address = }"


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


def show(info):
    for i in info:
        print(i)


if __name__ == "__main__":
    name = input("Enter Your name: ")
    age = input("Enter Your age: ")
    address = input("Enter Your address: ")
    person = Person(name, age, address)

    save_object(person)

    info = read_file("obj.pickle")

    print("Do you want to show you the content of the pickle file?")
    while True:
        ans = input("Yes ==> 1, No ==? 2: ")
        if ans == "1":
            show(info)
            break
        elif ans == "2":
            break
        else:
            print("Enter a valid option")
