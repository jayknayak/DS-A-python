def bestTimeToBuyAndSellStock(nums):
    if len(nums) == 0:
        return 0
    max_profit = 0
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            max_profit += nums[i] - nums[i-1]
    return max_profit


print(bestTimeToBuyAndSellStock([7,6,4,3,1]))