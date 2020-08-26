class Solution:
    def findSubsequences(self, nums) :
        res = set()
        length = len(nums)
        def dfs(cur,i):
            nonlocal length
            if i < length:
                dfs(cur.copy(),i+1)

                nonlocal nums
                if cur[-1] <= nums[i]:
                    cur.append(nums[i])
                    nonlocal res
                    res.add(".".join(list(map(str,cur))))
                    dfs(cur.copy(),i+1)
        for i,each in enumerate(nums):
            dfs([each],i+1)
        rt = []
        for each in res:
            rt.append(list(map(int,each.split('.'))))


        return rt