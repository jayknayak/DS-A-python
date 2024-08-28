# https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
from itertools import product

K, M = map(int, input().split())
square_values = []

for _ in range(K):
    list_i = map(int, input().split()[1:])
    square_values.append([item * item for item in list_i])

print(max(sum(items) % M for items in product(*square_values)))