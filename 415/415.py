class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)

        lens = max(len1,len2)
        num1_ = list(num1)
        num2_ = list(num2)

        res = ['0' for i in range(0,lens+1)] # 考虑进位


        for i in range(-1,-lens-1,-1):
            if -i > len1:
                n1 = '0'
            else:
                n1 = num1_[i]
            if -i > len2:
                n2 = '0'
            else:
                n2 = num2_[i]

            temp = ord(n1) + ord(n2) + ord(res[i]) - ord('0')*3
            if temp >= 10:
                res[i-1] = '1'
                res[i] = chr(temp-10+ord('0'))
            else:
                res[i] = chr(temp+ord('0'))

        if res[0] == '0':
            res.pop(0)
        return "".join(res)
        

s = Solution()
s.addStrings('1','9')            
s.addStrings('99','9')  
print(s.addStrings("999","999"))
