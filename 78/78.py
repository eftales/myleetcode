class Solution:
    def subsets(self, nums) :
        res = []

        def dfs(nums,i,subset):
            if i < len(nums):
                dfs(nums,i+1,subset+[])
                dfs(nums,i+1,subset+[nums[i]])
            else:
                res.append(subset)
        dfs(nums,0,[])
        return res

s = Solution()
s.subsets([1,2,3])