#
# Встроенная функция input позволяет ожидать и возвращать данные из стандартного
# ввода в виде строки (весь введенный пользователем текст до нажатия им enter).
# Используя данную функцию, напишите программу, которая:
#
# 1. После запуска предлагает пользователю ввести текст.
# 2. Проверяет и, если возможно, преобразовывает полученный текст в число,
# используя рекурсивную функцию.
# Если число четное - делит его на 2 и выводит результат.
# Если число нечетное - умножает на 3 и прибавляет 1.
# После чего ждет следующего ввода.
# 3.При получении в качестве вводных данных 'cancel' завершает свою работу.
#
# Пример:
#
# -> Привет123
# Не удалось преобразовать введенный текст в число.
# -> 2
# 1
# -> 3
# 10
# -> Два
# Не удалось преобразовать введенный текст в число.
# -> cancel
# Bye!

def main():
    try:
        data = int(input())
        if data == "exit":
            exit(0)
        print(convert(data))
        main()
    except ValueError:
        print("Не удалось преобразовать введенный текст в число.")
        exit(0)


def convert(number):
    if number % 2 == 1:
        return number * 3 + 1
    else:
        return number // 2


if __name__ == '__main__':
    main()
