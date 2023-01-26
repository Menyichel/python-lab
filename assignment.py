roman_num = input("Enter the Roman Number: ").upper()

def RomanToDecimalConversion(roman_num):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    decimal = 0
    checkPrevious = 0

    for i in range(len(roman_num)-1,-1,-1):
        char = roman_num[i]
        decimal += roman[char]
        if roman[char] > checkPrevious:
            decimal -= 2 * checkPrevious
        checkPrevious = roman[char]
            
    return decimal


print(RomanToDecimalConversion(roman_num))