# Complete the function below.
import collections

# PRE : num is a single integer
# POST : returns the Roman representation
def romanizerHelp(num):
    roman_int_map = collections.OrderedDict()
    roman_int_map[1000] = 'M'
    roman_int_map[900] = 'CM'
    roman_int_map[500] = 'D'
    roman_int_map[400] = 'CD'
    roman_int_map[100] = 'C'
    roman_int_map[90] = 'XC'
    roman_int_map[50] = 'L'
    roman_int_map[40] = 'XL'
    roman_int_map[10] = 'X'
    roman_int_map[9] = 'IX'
    roman_int_map[5] = 'V'
    roman_int_map[4] = 'IV'
    roman_int_map[1] = 'I'
    
    roman_numeral = ''
    
    for digit in roman_int_map.keys():
        num_curr_digits = num // digit
        roman_repr = roman_int_map[digit] * int(num_curr_digits)
        roman_numeral += roman_repr
        num = num % digit
        
    return roman_numeral

# PRE : num is a integer array
def romanizer(num):
    result = []
    for n in num:
        roman_n = romanizerHelp(n)
        result.append(roman_n)
        
    return result

num = 4975
print(romanizerHelp(num))

# Complete the function below.
import math

# PRE : Integer n
# POST : 2's complement of the number
def  getIntegerComplement( n):
    fnbase2 = math.floor(math.log(n)/math.log(2))    # Given number to base 2 (floored)
    exponent = 2 ** (fnbase2 + 1)
    complement = exponent - 1 - n
    
    return int(complement)