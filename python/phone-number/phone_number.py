from collections import deque
import re
class Phone(object):
    def __init__(self, phone_number):
        #Pattern meets all test requirments could probably be more robust
        pattern = re.compile("^(?P<country>\+1|1)?(?:[\s\(\.\-]{0,})(?P<area>[2-9][0-9]{2})(?:[\s\(\-\.\)]{0,})(?P<first>[2-9][0-9]{2})(?:[\s\(\-\.]{0,})(?P<second>[0-9]{4})(?:\s{0,})?$")
        match=pattern.search(phone_number)
        if match:
            self.area_code = match.group('area')
            self.first_seg = match.group('first')
            self.second_seg = match.group('second')
            try:
                self.country = match.group('country')
            except:
                self.country = "1"
            self.number = self.area_code+self.first_seg+self.second_seg
        else:
            raise ValueError("Incorrect phone number")

    def pretty(self):
        return f"({self.area_code}) {self.first_seg}-{self.second_seg}"
