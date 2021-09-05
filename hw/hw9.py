from functools import reduce

# Решить несколько задач из projecteuler.net
#
# Решения должны быть максимально лаконичными, и использовать list comprehensions.
#
# problem9 - list comprehension : one line
# problem6 - list comprehension : one line
# problem48 - list comprehension : one line
# problem40 - list comprehension

# problem9
print(
    [(a, b, c) for a in range(1000) for b in range(a) for c in range(b) if a * a == b * b + c * c if a + b + c == 1000])

# problem6
print(sum([a for a in range(100)])**2 - sum([a*a for a in range(100)]))

# problem48
print(str(sum([a ** a for a in range(1001)]))[-10:])

# problem40
digits_list = [str(a) for a in range(1, 199999)]
digits_str = "".join(digits_list)
result_list = map(int, [digits_str[9], digits_str[99], digits_str[999],
                        digits_str[9999], digits_str[99999], digits_str[999999]])
print(reduce((lambda x, y: x * y), result_list))
