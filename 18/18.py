class Solution:
    def fourSum(self, nums, target: int) :
        def qs(nums,begin,end):
            if begin >= end:
                return None
            left = begin 
            right = end
            mid = nums[left]
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
            qs(nums,right+1,end)
        
        length = len(nums)
        qs(nums,0,length-1)
        res = []
        
        for base1 in range(0,len(nums)-3):
            for base2 in range(base1+1,len(nums)-2):
                targetRemain = target - nums[base1] - nums[base2]
                left = base2 + 1
                right = length - 1

                if not (nums[left] + nums[left+1] <= targetRemain <= nums[right] + nums[right-1]): # 精华 1
                    break
                else:
                    while left != right:
                        curVal = nums[left]+nums[right]
                        if curVal > targetRemain:
                            right -= 1
                        elif curVal < targetRemain:
                            left += 1
                        else:
                            res.append([nums[base1],nums[base2],nums[left],nums[right]])
                            break # 精华 2
        return res

s = Solution()
s.fourSum([0,0,0,0],0)