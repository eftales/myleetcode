class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curCounts = 1
        curNum = s[0]
        lastCounts = 0
        res = 0
        for i in range(1,len(s)):
            if s[i] == curNum:
                curCounts += 1
            else:
                
                if lastCounts != 0:# 非初始状态
                    res += min(lastCounts,curCounts)

                curNum = s[i]
                lastCounts = curCounts
                curCounts = 1

        res += min(lastCounts,curCounts)
            
        return res
