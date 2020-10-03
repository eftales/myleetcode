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

l = []
import random
for i in range(0,100):
    l.append(random.randint(1,9999))
print(l)
qs(l,0,len(l)-1)
print(l)