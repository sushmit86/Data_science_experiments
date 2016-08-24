from decimal import Decimal
print((999).bit_length())
####
s = 11
d = int(s)
print(d)
sum (Decimal ("0.1") for i in range(10)) == Decimal("1.0")
###
def convert_to_decimal(number,base):
    multiplier, result = 1 , 0
    while number > 0:
        result += number%10*multiplier
        multiplier *= base
        number = number//10
    return result
def test_convert_to_decimal():
    number , base = 1001,2
    assert(convert_to_decimal(number, base)==9)
