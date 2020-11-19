class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        nonZero = 0
        while nonZero < len(nums):
            if nums[nonZero] != 0:
                nums[zero],nums[nonZero] = nums[nonZero],nums[zero]
                zero += 1
            nonZero += 1

