class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n<m:
            n = n&(n-1)
        return n

s = Solution()
s.rangeBitwiseAnd(11,15)