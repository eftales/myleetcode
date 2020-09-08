class Solution:
    def combine(self, n: int, k: int):
        nums = list(range(1,n+1))
        res = []
        def dfs(n,k,comb):
            for each in nums[n:]:
                if k-len(comb) > (len(nums) - n ) :
                    return None
                comb.append(each)
                if len(comb) < k:
                    dfs(n+1,k,comb)
                else:
                    res.append(comb.copy())
                comb.pop()
                n += 1
        dfs(0,k,[])
        return res