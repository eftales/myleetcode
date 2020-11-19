class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        countZero = 0
        for i in range(0,len(nums)):
            if nums[i] == 0:
                countZero += 1
            else:
                nums[i-countZero] = nums[i]
        for i in range(len(nums)-1,len(nums)-1-countZero,-1):
            nums[i] = 0

