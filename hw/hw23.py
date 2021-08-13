# Надо написать функцию которая возвращает N-мерный массив с ширинами заданными в аргументе списком из N элементов:
# n_arr([2,2])
# >> [[“”,“”],[“”,“”]]
# n_arr([2,2,2])
# >> [[[“”,“”],[“”,“”]], [[“”,“”],[“”,“”]]]


def n_arr(dimensions):
    if len(dimensions) > 0:
        cur, rest = dimensions[0], dimensions[1:]
        arr = []
        for i in range(0, cur):
            arr.append([])
            arr[i] = n_arr(rest)
        return arr
    else:
        return ""


print(n_arr([2, 2]))
print(n_arr([2, 2, 2]))
print(n_arr([2, 2, 2, 3]))
