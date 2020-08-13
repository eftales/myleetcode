class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "" or num2 == "":
            return ""
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        res = [0 for i in range(0,m+n)] 

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mul = int(num1[i]) * int(num2[j]) + res[i+j+1] # 注意！！ 防止 res 中的元素可能大于 10
                res[i+j+1] = mul % 10 # 注意！！ 防止 res 中的元素可能大于 10
                res[i+j] += mul // 10

        if res[0] == 0:
            res.pop(0)
        return "".join(list(map(str,res))) 


s = Solution()
s.multiply("123","456")