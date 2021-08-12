import pickle

from hw.hw14.main import Employee


def main():
    with open("temp_for_employees.txt", "rb") as file:
        mary = pickle.load(file)
        print(mary)

if __name__ == '__main__':
    main()