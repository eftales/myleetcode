class Solution:
    def countBits(self, num) :
        res = [0]
        if num == 0:
            return res

        base = 0
        while num >= pow(2,base):
            for i in range(0,len(res)):
                res.append(res[i]+1)
                if len(res) >= num+1:
                    return res
            base += 1
        
        return res[0:num+1]