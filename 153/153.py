class Solution:
    def findMin(self, nums) -> int:
        left = 0
        right = len(nums) -1
        if nums[left] <= nums[right]: # 加等于号是为了解决只有一个元素的情况
            return nums[left]
        if nums[right] <= nums[right-1]:
            return nums[right]
        mid = (left+right)//2

        while not (nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]):
            if nums[mid] > nums[left]:
                left = mid
                mid = (left+right)//2
            elif nums[mid] < nums[left]:
                right = mid
                mid = (left+right)//2
            else:
                pass # 不可能等于
        return nums[mid]

s = Solution()
print(s.findMin([3,4,5,1,2]))
