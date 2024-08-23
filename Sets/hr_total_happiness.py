# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
def total_happiness(n, array, a, b):
    happiness = 0
    for i in range(n):
        if array[i] in a:
            happiness += 1
    for i in range(n):
        if array[i] in b:
            happiness -= 1
    print(happiness)

# Correct input parsing
n, m = map(int, input().split())
array = input().split()
a_set = set(input().split())
b_set = set(input().split())
total_happiness(n, array, a_set, b_set)