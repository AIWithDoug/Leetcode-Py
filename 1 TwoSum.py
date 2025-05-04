def twoSum(nums, target):
    for i, x in enumerate(nums):
        lf = target - x
        # Python lists use 'in' not '.contains()'
        # Also, append takes only one argument
        if lf in nums:
            lf1 = nums.index(lf)
            if i != lf1:
                return [lf1, i]
    return None

# First, define some example input
numbers_to_check = [3,2,4]

print(twoSum(numbers_to_check, 6))





