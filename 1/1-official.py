class Solution:
    def twoSum(self, nums,target):
        num2loc = dict()
        for loc,num in enumerate(nums):
            if (target - num) in num2loc:
                return [num2loc[(target - num)],loc]
            num2loc[num] = loc
        return []