def collatz_steps(number):
    if number < 1 or number is None:
        raise ValueError("Number has to be postivie value")
    count = 0
    while True:
        if number == 1:
            break
        number = int(number/2) if number%2==0 else int(number*3+1)
        count += 1
    return count
