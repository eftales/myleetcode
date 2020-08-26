from functools import reduce

class Solution:
    def findSubsequences(self, nums) :
        res = dict()
        length = len(nums)

        def dfs(cur,i):
            nonlocal length
            if i < length:
                dfs(cur,i+1)

                nonlocal nums
                if cur[-1] <= nums[i]:
                    cur.append(nums[i])
                    nonlocal res
                    key = reduce(lambda x,y: x*203+y,cur) # Rabin-Karp 算法，选 203 是因为数组中数的范围 [-100,100]
                    if key not in res :
                        res[key] = [cur.copy()]
                    elif key in res :
                        for each in res[key]:
                            if len(cur) == len(each):
                                break
                        else:
                            res[key].append(cur.copy())

                    dfs(cur,i+1)
                    cur.pop(-1)
        for i,each in enumerate(nums):
            dfs([each],i+1)
        rt = []
        for key in res:
            for each in res[key]:
                rt.append(each)


        return rt