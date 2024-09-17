import math


def rotateArray(nums, k):
    if len(nums) == 0:
        return []
    if k == 0:
        return nums
    n = len(nums)
    k %= n
    reverse_array(nums, 0, n-k-1)
    reverse_array(nums, n-k, n-1)
    reverse_array(nums, 0, n-1)
    return nums


def reverse_array(nums, start_index, end_index):
    while end_index > start_index:
        temp = nums[start_index]
        nums[start_index] = nums[end_index]
        nums[end_index] = temp
        start_index += 1
        end_index -= 1

# Another approach in Python using slicing technique
def rotateLeft(d, arr):
    n = len(arr)
    d = d % n  # Handle cases where d > n
    return arr[d:] + arr[:d]

print(rotateArray([1,2,3,4,5,6,7], 3))

