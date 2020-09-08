class Solution:
    def combine(self, n: int, k: int):
        if k > n:
            return []
        nums = list(range(1,n+1))
        res = []
        def dfs(n,k,comb):
            for each in nums[n:]:
                comb.append(each)
                if len(comb) < k:
                    dfs(n+1,k,comb)
                else:
                    res.append(comb.copy())
                comb.pop()
                n += 1
        dfs(0,k,[])
        return res


s = Solution()
s.combine(4,2)