import secrets
from collections import deque
import string

class Cipher(object):
    def __init__(self, key=None):
        if key == None:
            self.key = ''.join([secrets.choice(string.ascii_lowercase) for i in range(100)])
        else:
            self.key = key

    def encode(self, text):
        result = []
        tmpkey = deque(self.key)
        for c  in text:
            if c.isalpha():
                num = ord(c)
                keyshift=tmpkey.popleft()
                tmpkey.append(keyshift)
                num +=ord(keyshift)-ord('a')
                if c.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
                elif c.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                c = chr(num)
            result.append(c)
        return "".join(result)

    def decode(self, text):
        result = []
        tmpkey = deque(self.key)
        for c  in text:
            if c.isalpha():
                num = ord(c)
                keyshift=tmpkey.popleft()
                tmpkey.append(keyshift)
                num -=ord(keyshift)-ord('a')
                if c.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
                elif c.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                c = chr(num)
            result.append(c)
        return "".join(result)
