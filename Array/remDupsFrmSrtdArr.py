def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    k = 1
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            nums[k] = nums[j]
            i = j
            k += 1
    return k


print(removeDuplicates([1,1,2]))
