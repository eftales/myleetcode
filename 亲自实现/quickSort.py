class quickSort(object):
    def sort(self,nums,begin,end):
        if end <= begin:
            return None
        left = begin
        right = end
        pivot = nums[begin]
        while left<right:
            while left < right:
                if nums[right] < pivot:
                    nums[left] = nums[right]
                    break
                else:
                    right -= 1
            while left < right:
                if nums[left] > pivot:
                    nums[right] = nums[left]
                    break
                else:
                    left += 1
        nums[left] = pivot
        self.sort(nums,begin,left-1)
        self.sort(nums,right+1,end)

s = quickSort()
l = []
import random
for i in range(0,100):
    l.append(random.randint(1,9999))
print(l)
s.sort(l,0,len(l)-1)
print(l)