from decimal import Decimal
import random
import math
import numpy as np

print((999).bit_length())
####
s = 11
d = int(s)
print(d)
sum(Decimal("0.1") for i in range(10)) == Decimal("1.0")


###
def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number //= 10
    return result


def test_convert_to_decimal():
    number, base = 1001, 2
    assert (convert_to_decimal(number, base) == 9)


def convert_from_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % base * multiplier
        multiplier *= 10
        number //= 10
    return result


def test_convert_from_decimal():
    number, base = 9, 2
    assert (convert_from_decimal(number, base) == 1001)


def convert_from_decimal_larger_bases(number, base):
    strings = "0123456789ABCDEFGHIJ"
    result = ""
    while number > 0:
        digits = number % base
        result = strings[digits] + result
        number //= base
    return result


def test_convert_from_decimal_larger_bases():
    number, base = 31, 16
    assert (convert_from_decimal_larger_bases(number, base) == '1F')


def convert_dec_to_any_base_rec(number, base):
    convertstring = '0123456789ABCDEFGHIJ'
    if number < base:
        return convertstring[number]
    else:
        return convert_dec_to_any_base_rec(number // base, base) + convert_dec_to_any_base_rec(number % base, base)


def test_convert_dec_to_any_base_rec():
    number = 9
    base = 2
    assert (convert_dec_to_any_base_rec(number, base) == '1001')


def finding_gcd(a, b):
    while (b != 0):
        result = b
        a, b = b, a % b
    return result


def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert (finding_gcd(number1, number2) == 3)


def testing_random():
    '''Testing the random module'''
    values = [1, 2, 3, 4]
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    print(random.sample(values, 2))
    print(random.sample(values, 3))
    '''shuffle in place'''
    random.shuffle(values)
    print(values)
    ''' create random integers '''
    print(random.randint(0, 10))
    print(random.randint(0, 10))


def fib_rec(n):
    """

    :rtype: Integer
    """
    if n < 3:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


def fib(n):
    """
    :param n: the nth fib number you want tp generate
    :return: fib(n)
    >>> fib(2)
    1
    >>> fib(5)
    5
    >>> fib(7)
    13
    """
    if n < 3:
        return 1
    a, b = 0, 1
    count = 1
    while count < n:
        count += 1
        a, b = b, a + b
    return b


def is_prime(n):
    """
    :param n: positive integer
    :return: True if Prime else false
    """
    for d in range(2, 1 + int(math.sqrt(n))):
        if (n % d) == 0:
            return False
    return True


def find_prime_factors(n):
    """
    :param n: The Number for the prime factors
    :return: A LIST of prime factors for the number
    """
    divisors = [d for d in range(2, n // 2) if n % d == 0]
    prime_factors = [p for p in divisors if is_prime(p)]
    return prime_factors


x = np.array(((11, 12, 13), (13,22, 23), (23, 24, 25)))
print(x)
print(x.ndim)
#### numpy testing:

def testing_numpy():
    ax = np.array([1,2,3])
    ay = np.array([3,4,5])
    print(ax)
    print(ax*2)
    print(ax + 10)
    print(np.sqrt(ax))
    print(np.cos(ax))
    print(ax - ay)
