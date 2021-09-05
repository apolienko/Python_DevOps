import pickle


# Создать сотрудника Mary, пользуясь классом
# Employee и перенести его в другую программу,
# используя модуль Pickle и файловую систему.
# Узнать про + и - модуля Pickle.


def main():
    mary = Employee("Mary", 30)
    with open("temp_for_employees.bin", "wb") as file:
        pickle.dump(mary, file)


class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "My name is %s and I am %d years old" % (self.name, self.age)


if __name__ == '__main__':
    main()
