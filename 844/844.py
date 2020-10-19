class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = len(S) - 1
        j = len(T) - 1
        while i>=0 or j>=0:
            backspace = 0
            s = ''
            while backspace >= 0:
                if i < -1:
                    break
                if S[i] == "#":
                    i -= 1
                    backspace += 1
                else:
                    s = S[i]
                    i -= 1
                    backspace -= 1
            s = '' if i<-1 else s # 下标等于 -1 表示刚刚好读到第一个字符，更小的下标表示删除的字符更多

            backspace = 0
            t = ''
            while backspace >= 0:
                if j < -1:
                    break
                if T[j] == "#":
                    j -= 1
                    backspace += 1
                else:
                    t = T[j]
                    j -= 1
                    backspace -= 1
            t = '' if j<-1 else t

            if s != t:
                return False
        return True
