class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        q = [[1, 1], [1, 0]]
        res = self.matrix_pow(q, n - 1)
        return res[0][0]
    
    def matrix_pow(self, a, n: int) :
        ret = [[1, 0], [0, 1]]
        while n > 0:
            if n & 1:
                ret = self.matrix_multiply(ret, a)
            n >>= 1
            a = self.matrix_multiply(a, a) # 返回的不是 a，所以多算一次也无所谓
        return ret

    def matrix_multiply(self, a, b):
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c

s = Solution()
s.fib(13)