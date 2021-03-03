class Solution:
    def countBits(self, num) :
        res = [0] * (num+1)

        curr2 = 0
        for i in range(1,num+1):
            if i&(i-1) == 0:
                res[i] = 1
                curr2 = i
            else:
                res[i] = res[i - curr2] + 1

        return res

