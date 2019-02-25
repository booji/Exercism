def verify(isbn):
    """Verify string is ISBN-10 returns a bool."""
    total = 0
    isbn = list(isbn)

    isbn = [x for x in isbn if x not in '-']

    if len(isbn) != 10:
        return False

    if isbn[-1] == 'X':
        isbn[-1] = 10

    try:
        isbn = [int(x) for x in isbn]
    except:
        return False

    for i, item in enumerate(isbn):
        total += item * (10 - i)

    return total % 11 == 0
