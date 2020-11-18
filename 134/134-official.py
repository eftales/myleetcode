class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        diff = list(map(lambda x: x[0]-x[1], zip(gas, cost)))
        length = len(diff)
        if length == 1 :
            if diff[0] >= 0:
                return 0
            else:
                return -1

        i = 0
        minI = i
        while minI <= i:
            target = (i-1+length)%length
            remain = 0
            while i != target:
                remain += diff[i]
                i = (i+1)%length
                if remain < 0:
                    break
            if remain>=0 and remain+diff[i] >= 0:
                return (target+1)%length
            minI = max(i,minI)
        return -1

s = Solution()
s.canCompleteCircuit([1,2,3,4,5]
,[3,4,5,1,2])