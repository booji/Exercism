from collections import deque


def largest_palindrome(max_factor, min_factor=0):
    factor_range_check(max_factor, min_factor)
    for i in range(max_factor * max_factor, min_factor * min_factor - 1, -1):
        result = pallindrome(i, max_factor, min_factor)
        if result[0] is not None:
            break
    return result


def smallest_palindrome(max_factor, min_factor=0):
    factor_range_check(max_factor, min_factor)
    for i in range(min_factor * min_factor, max_factor * max_factor + 1, 1):
        result = pallindrome(i, max_factor, min_factor)
        if result[0] is not None:
            break
    return result


def pallindrome(num, max_factor, min_factor):
    fac = []
    value = None
    if str(num) == str(num)[::-1]:
        fac = factors(num, max_factor, min_factor)
        if fac != []:
            value = num
    return [value, fac]


def factor_range_check(max_factor, min_factor):
    if max_factor < min_factor:
        raise ValueError(
            "max_factor has to be larger then min_factor (default 0)")


def factors(n, max_factor, min_factor=0):
    alist = deque(range(min_factor, max_factor + 1))
    factors = []
    while alist:
        i = alist.pop()
        if n % i == 0:
            if min_factor <= int(n / i) <= max_factor and min_factor <= i <= max_factor:
                factors.append((int(n / i), i))
                # Try and reduce list quicker
                try:
                    alist.remove(int(n / i))
                except:
                    pass

    return factors
