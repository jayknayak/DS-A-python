# https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

print(is_leap(2100))

from itertools import islice

print(list(islice('ABCDEFG', 5)))