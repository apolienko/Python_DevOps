# Встроенная функция input позволяет ожидать и возвращать данные из стандартного
# ввода ввиде строки (весь введенный пользователем текст до нажатия им enter).
# Используя данную функцию, напишите программу, которая:
#
# 1. После запуска предлагает пользователю ввести неотрицательные целые числа,
# разделенные через пробел и ожидает ввода от пользователя.
# 2. Находит наименьшее положительное число, не входящее в данный пользователем
# список чисел и печатает его.
#
#
# Например:
#
# -> 2 1 8 4 2 3 5 7 10 18 82 2
# 6

def main():
    digits = list(map(int, input("Enter some non-negative digits\n").split()))

    digits.sort()
    last_element_index = len(digits) - 1

    for x in range(1, len(digits)):
        if digits[x] - digits[x - 1] > 1:
            print(digits[x - 1] + 1)
            break
        if x == last_element_index:
            print(digits[last_element_index] + 1)


if __name__ == "__main__":
    main()
