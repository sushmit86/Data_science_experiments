from decimal import Decimal

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
    assert (convert_from_decimal_larger_bases(number,base) == '1F')
    
def convert_dec_to_any_base_rec(number, base):
    convertstring = '0123456789ABCDEFGHIJ'
    if number < base : return convertstring[number]
    else:
        return convert_dec_to_any_base_rec(number//base) + convert_dec_to_any_base_rec(number % base)
