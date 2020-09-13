class Solution:
    def combinationSum2(self, candidates, target: int):
        def quicksort(nums,begin,end):
            if end <= begin:
                return None
            left = begin
            right = end
            pivot = nums[left]
            while left<right:
                while left<right:
                    if nums[right] < pivot:
                        nums[left] = nums[right]
                        break
                    right -= 1
                while left<right:
                    if nums[left] > pivot:
                        nums[right] = nums[left]
                        break
                    left += 1
            nums[left] = pivot
            quicksort(nums,begin,left-1)
            quicksort(nums,right+1,end)
        quicksort(candidates,0,len(candidates)-1)
        res = []
        def dfs(candidates,begin,end,target,path):
            for i in range(begin,end):
                if i>0 and candidates[i] == candidates[i-1] and begin<i:
                    continue
                if (target - candidates[i])>0:
                    dfs(candidates,i+1,end,target-candidates[i],path+[candidates[i]])
                elif (target - candidates[i] ) == 0:
                    res.append(path+[candidates[i]])
                    return None
                else:
                    return None
        dfs(candidates,0,len(candidates),target,[])
        return res


s = Solution()
print(s.combinationSum2([1,1,1,1,1,1,1],2))