class Solution:
    def fibCircularArray(self, n: int) -> int:
        if n < 2:
            return n
        F = [0,1]
        for i in range(2,n+1):
            Fi = F[0] + F[1]
            F[0] = F[1]
            F[1] = Fi
        return F[1]

    def fibMatMul(self,n):
        if n < 2:
            return n
        def matMul(a,b):
            c = [[0,0],[0,0]]
            for i in range(0,2):
                for j in range(0,2):
                    c[i][j] = a[i][0]*b[0][j] + a[i][1]*b[1][j]
            return c
        def MpowerN(n):
            ret = [[1,0],[0,1]]
            M = [[1,1],[1,0]]
            while n > 1:
                if n&1 : # 判断 n 二进制的最后一位是不是 1
                    ret = matMul(ret,M) # 如果是 1 就要把这个“现存款”取出来
                n = n // 2
                M = matMul(M,M)
            return matMul(M,ret)

        res = MpowerN(n - 1)
        return res[0][0]


