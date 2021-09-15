import re
# Напишите функцию, которая переводит значения показаний
# температуры из Цельсия в Фаренгейт и наоборот.

def main():
    # print(convert_temp(11, "C"))
    # print(convert_temp(50, "F"))
    # print(convert_temp(50, "hahaha"))
    # print(convert_temp(50.8, "F"))

    print(convert_temp("11C"))
    print(convert_temp("50F"))
    print(convert_temp("50hahaha"))
    print(convert_temp("50.8F"))

def convert_temp(t):
    try:
        if re.match(r'\d+(.\d)*C', t):
            return str(float(t[:-1]) * 9 / 5 + 32) + " F"
        if re.match(r'\d+(.\d)*F', t):
            return str(5/9 * (float(t[:-1]) - 32)) + " C"
        else:
            raise ValueError()
    except ValueError:
        return "Usage: '[0-9]F' or '[0-9]C'"


if __name__ == '__main__':
    main()
