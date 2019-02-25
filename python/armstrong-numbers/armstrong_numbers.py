def is_armstrong(number):
    numberOfDigits = len(str(number))
    sum = 0
    temp = number
    while temp >= 1:
        digit = temp % 10
        sum += int(digit) ** int(numberOfDigits)
        temp /= 10

    if number == sum:
        return True
    else:
        return False
