import calendar

class MeetupDayException(Exception):
    pass


def meetup_day(year, month, day_of_the_week, which):
    day_dict = dict(zip(list(calendar.day_name),
           range(7)))
    c = calendar.Calendar()
    days = [d for d in c.itermonthdates(year, month) if
            d.weekday() == day_dict[day_of_the_week] and
            d.month == month]

    if which == 'teenth':
        result = [d for d in days if d.day >=13 and d.day <= 19][0]
    elif which == 'last':
        result = days[-1]
    else:
        try:
            result = days[int(which[0])-1]
        except:
            raise MeetupDayException('Date criteria not valid')
    return result
