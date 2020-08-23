class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m
        def minPower2(n): # 10->16 16->32，返回大于该数的2次幂
            n |= n>>1
            n |= n>>2
            n |= n>>4
            n |= n>>8
            n |= n>>16
            return n+1

        def minPower(n): # 10->16 16->16，返回大于等于该数的2次幂
            n -= 1
            n |= n>>1
            n |= n>>2
            n |= n>>4
            n |= n>>8
            n |= n>>16
            return n+1

        powerL = minPower2(m)
        powerR = minPower2(n)

        if powerL != powerR:
            return 0
        
        length = n - m + 1
        powerLen = minPower(length)
        return m&n&(0x7fffffff - powerLen + 1 )  

s = Solution()
s.rangeBitwiseAnd(11,15)