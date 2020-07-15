class Solution:
    def numTrees(self, n: int) -> int:
        C = 1
        for i in range(1,n):
            C = 2 * (2*i +1)*C/(i+2)
        return int(C)
        
s = Solution()                

print(s.numTrees(5))