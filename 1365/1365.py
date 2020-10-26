class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101
        for each in nums:
            count[each] += 1
        for i in range(1,101):
            count[i] += count[i-1]
        res = []
        for each in nums:
            res.append(count[each]-count[each-1])
        return res
