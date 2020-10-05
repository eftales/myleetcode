def qsTopK(nums,begin,end,target):
    res = []
    def run(nums,begin,end,target):
        if begin >= end:
            return 0
        left = begin
        right = end
        mid = nums[begin]

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
        nonlocal res
        if left-begin <= target:
            res += nums[begin:left]
            target -= (left - begin)

            if target >= 1:
                res.append(nums[left])
                target -= 1
            if target != 0:
                target = run(nums,left+1,end,target) 
                # 这里其实没必要返回 target 的值，但是如果不在这里修改 target 的值，调试的时候会很懵逼，即会出现：为什么明明已经找到足够的元素了，target 的值还不为 0
        else:
            target = run(nums,begin,left-1,target)
        return target
    run(nums,begin,end,target)
    return res


l = []
import random
for i in range(0,100):
    l.append(random.randint(1,9999))
print(l)
print(qsTopK(l,0,len(l)-1,5))
print(l)
