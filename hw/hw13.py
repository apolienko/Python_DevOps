# Напишите функцию, которая переводит значения показаний
# температуры из Цельсия в Фаренгейт и наоборот.

def main():
    print(convert_temp(11, "C"))
    print(convert_temp(50, "F"))
    print(convert_temp(50, "hahaha"))
    print(convert_temp(50.8, "F"))


def convert_temp(t, mode):
    if mode == "F":
        return str(5/9 * (t - 32)) + " C"
    if mode == "C":
        return str(t * 9/5 + 32) + " F"
    else:
        return "Usage: mode=\"C\" or mode=\"F\""



if __name__ == '__main__':
    main()
