# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
from collections import Counter
number_of_shoes = int(input())
print(map(int, input().split()))
shoe_size_list_counter = Counter(map(int, input().split()))
total_income = 0
for _ in range(int(input())):
    size, price = map(int, input().split())
    if shoe_size_list_counter[size] > 0:
        total_income += price
        shoe_size_list_counter[size] -= 1
print(total_income)
