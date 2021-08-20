#Составить таблицу соответствия между различными объектами
# основных классов: int, str и объектами класса bool.

print(bool("aaa")) # --> True
print(bool("")) # --> False
print(bool("   ")) # --> True
print(bool(" ")) # --> True
print(bool(1)) # --> True
print(bool(100)) # --> True
print(bool(-50)) # --> True
print(bool(0)) # --> False

"""
str:
True -- только непустая строка, пробелы тоже 
Остальное False

int:
True только при ненулевом значении


Разобраться с различиями между input() и raw_input(). Также в контексте разных версий python: 2 и 3.

Python 2 :
raw_input() -- ввод с клавиатуры, который преобразуется в строку
input() -- воспринимает введенный текст как команду и пробует ее запустить

Python 3 :
input() -- это переименованный raw_input() из python2
raw_input -- убрали, но можно использовать eval(input()) 

Про отлчия синтаксиса print в python2 и python3 тоже почитал :) 
"""
