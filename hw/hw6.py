# https://projecteuler.net/problem=36
#
# The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2. (Please note that the palindromic number,
# in either base, may not include leading zeros.)
#
# Напишите программу, которая решает описанную выше задачу и печатает ответ.


# Ответ : 872187

def main():
    final_sum = 0

    for x in range(1000000):
        x_bin = int(bin(x), 2)
        if is_palindrome(x) & is_palindrome(x_bin):
            final_sum += x

    print(final_sum)


def is_palindrome(digit):
    reversed_digit = str(digit)[::-1]

    if str(digit) == reversed_digit:
        return True
    else:
        return False


if __name__ == '__main__':
    main()

