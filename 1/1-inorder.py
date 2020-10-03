class Solution:
    def twoSum(self, nums,target):
        i = 0
        j = len(nums)-1

        def qs(nums,begin,end):
            if begin >= end:
                return None
            mid = nums[begin]
            left = begin
            right = end
            while left != right:
                while left != right:
                    if nums[right] < mid:
                        nums[left] = nums[right]
                        break
                    right -= 1
                while left != right:
                    if nums[left] > mid:
                        nums[right] = nums[left]
                        break
                    left += 1
            nums[left] = mid
            qs(nums,begin,left-1)
            qs(nums,left+1,end)
        
        qs(nums,i,j)
        print(nums)
        while i!=j:
            if (nums[i]+nums[j]) < target:
                i += 1
            elif (nums[i]+nums[j]) > target:
                j -= 1
            else:
                break
        return [i,j]

s = Solution()
s.twoSum([3,2,4],6)