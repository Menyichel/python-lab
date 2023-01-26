tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def ConvertingFunction(romanNumbers):
    result = 0
    for i in range(len(romanNumbers) - 1):
        left = romanNumbers[i]
        right = romanNumbers[i + 1]
        if tallies[left] < tallies[right]:
            result -= tallies[left]
        else:
            result += tallies[left]
    result += tallies[romanNumbers[-1]]

    if result >3999:
        return print("Number is greater than 3999")
    else:
        return result

while 1:
    count = 0
    try: 
        print("Enter any roman number from 1 to 3999")
        acceptedNumber = input()
        if len(acceptedNumber) <= 3:
            print(acceptedNumber," = ",ConvertingFunction(acceptedNumber))
        elif len(acceptedNumber)>3:
            for i in range(0,len(acceptedNumber),1):
                if i>=3:
                    if acceptedNumber[i] == acceptedNumber[i-1] == acceptedNumber[i-2] == acceptedNumber[i-3]:
                        count=count+1
                        break

        if count == 0:
            print(acceptedNumber," = ",ConvertingFunction(acceptedNumber))
            count=0
        else:
            print("Use appropriate ROMAN numbers")
            count=0
    except:
        print("try again")
    

