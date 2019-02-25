def is_leap_year(year):
    flag = False
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        flag = True

    return flag
