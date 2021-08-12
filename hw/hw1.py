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

# str:
# True -- только непустая строка, пробелы тоже ;
# Остальное False
#
# int:
# True только при ненулевом значении
#