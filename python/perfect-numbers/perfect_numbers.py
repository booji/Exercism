def classify(number: int) -> str:
    perfect = "perfect"
    abundant = "abundant"
    deficient = "deficient"
    if number < 1:
        raise ValueError('Invalid number')
    elif number == 1:
        return deficient
    divider = 2
    listing = set([1])
    while True:
        if number == divider:
            break
        if number % divider == 0:
            listing.add(divider)
            listing.add(number//divider)
        divider += 1
        if divider >= number//divider:
            break
    if sum(listing) == number:
        return perfect
    elif sum(listing) > number:
        return abundant
    elif sum(listing) < number:
        return deficient
