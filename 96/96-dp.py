class Solution:
    def numTrees(self, n: int) -> int:
        f = [0] * (n+1)
        f[0] = 1
        f[1] = 1

        for i in range(2,n+1):
            for j in range(1,int(i/2) + 1):
                f[i] += 2 * f[i-j] * f[j-1]
            if i//2 != i/2:
                f[i] += f[int((i-1)/2)] * f[int((i-1)/2)]
        return f[n]
s = Solution()                

print(s.numTrees(5))