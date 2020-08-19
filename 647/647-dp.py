class Solution:
    def countSubstrings(self, s: str) -> str:
        length = len(s)
        F = [ [0 for i in range(0,length)] for i in range(0,length)] # 0 表示 [i,j] 之间的字符串不是回文串，1 反之

        res = 0
        for i in range(length-1,-1,-1):
            for j in range(i,length):
                if i == j: # 只有一个字符是回文串
                    F[i][j] = 1
                elif (j - i) == 1: # 只有两个元素可以直接判断
                    if s[i] == s[j]:
                        F[i][j] = 1
                else: # 大于两个元素则需要借助 F 数组判断
                    if s[i] == s[j] and F[i+1][j-1] == 1: # 首位元素相同，且中间的子串是回文串
                        F[i][j] = 1
                if F[i][j] == 1:
                    res += 1


        return res

