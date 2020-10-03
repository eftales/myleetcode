class Solution:
    def twoSum(self, nums,target):
        num2loc = dict()
        for loc,num in enumerate(nums):
            if num not in num2loc:
                num2loc[num] = [loc]
            else:
                num2loc[num].append(loc)
        for eachKey in num2loc:
            if (target - eachKey) in num2loc:
                if (target - eachKey) != eachKey:
                    return [num2loc[eachKey][0],num2loc[target - eachKey][0]]
                else:
                    if len(num2loc[eachKey])>=2:
                        return [num2loc[eachKey][0],num2loc[eachKey][1]]


s = Solution()
s.twoSum([2,5,5,11],10)