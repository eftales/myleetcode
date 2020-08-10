class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        end = 0 # 滑动窗口的起点
        begin = 0 # 华东窗口的终点
        trans = 0 # 滑动窗口内由一种值变成另一种值的交界点
        res = 0

        for i in range(1,len(s)):
            if s[i] == s[end]:
                end += 1
                if end-trans < trans - begin:
                    res += 1
            else:
                end += 1
                if trans == begin:
                    trans = end
                else:
                    begin = trans
                    trans = end
                res += 1
            
        return res
