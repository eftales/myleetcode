class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "" or num2 == "":
            return ""
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        res = [0 for i in range(0,m+n)] 

        for i in range(0,m):
            for j in range(0,n):
                mul = int(num1[m-i-1]) * int(num2[n-j-1]) + res[m+n-1-i-j] # 注意！！ 防止 res 中的元素可能大于 10
                res[m+n-1-i-j] = mul % 10 # 注意！！ 防止 res 中的元素可能大于 10
                res[m+n-2-i-j] += mul // 10

        if res[0] == 0:
            res.pop(0)
        return "".join(list(map(str,res))) 


s = Solution()
s.multiply("123","456")