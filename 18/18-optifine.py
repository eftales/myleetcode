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
        
        base1 = 0
        while base1 <= (length-4): # 这道题对下标很敏感，在循环中对下标进行了多次操作，所以用 while 比 for in range 更好
            if (nums[base1] + nums[base1+1] + nums[base1+2] + nums[base1+3] <= target <= nums[base1] + nums[length-3] + nums[length-2] + nums[length-1]): # 精华 1：剪枝
                if base1 == 0 or nums[base1] != nums[base1-1]: # 跳过相同的元素
                    base2 = base1 + 1
                    while base2 <= (length-3):
                        if base2 == (base1+1) or nums[base2] != nums[base2-1]:
                            targetRemain = target - nums[base1] - nums[base2]
                            left = base2 + 1
                            right = length - 1

                            if (nums[left] + nums[left+1] <= targetRemain <= nums[right] + nums[right-1]): # 精华 1：判断基于这两个 base 有没有可能得到最优解
                                while left != right:
                                    if left > (base2+1) and nums[left] == nums[left-1]:
                                        left += 1
                                        continue
                                    if right < (length-1) and nums[right] == nums[right+1]:
                                        right -= 1
                                        continue
                                    curVal = nums[left]+nums[right]
                                    if curVal > targetRemain:
                                        right -= 1
                                    elif curVal < targetRemain:
                                        left += 1
                                    else:
                                        res.append([nums[base1],nums[base2],nums[left],nums[right]])
                                        left += 1 # 精华 2：打破平衡，寻找下一个可行解
                        base2 += 1
            base1 += 1
        return res
