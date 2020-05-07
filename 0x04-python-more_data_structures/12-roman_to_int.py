#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    elem = 0
    roman = roman_string
    if type(roman) is not str or len(roman) is 0:
        return 0
    for elem in range(elem, len(roman)):
        if elem < len(roman) - 1 and dic[roman[elem]] < dic[roman[elem + 1]]:
            result -= dic[roman[elem]]
        else:
            result += dic[roman[elem]]
    return result
