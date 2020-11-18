class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        diff = list(map(lambda x: x[0]-x[1], zip(gas, cost)))
        length = len(diff)
        lastest = None
        for j in range(length-1,-1,-1):
            if diff[j] < 0:
                continue
            remain = diff[j]
            i = (j+1)%length
            while i != j:
                if lastest != None and i == lastest[0]:
                    if lastest[1] < lastest[0] and lastest[1] >= j:
                        return j
                    else:
                        i = lastest[1]
                        i = (i+1)%length
                        remain += lastest[2]
                else:
                    if diff[i] + remain >= 0:
                        remain += diff[i]
                        i = (i+1)%length
                    else:
                        lastest = [j,(i-1+length)%length,remain]
                        break
            if i == j and remain >= 0:
                return j
        return -1


s = Solution()
s.canCompleteCircuit([4,5,2,6,5,3],
[3,2,7,3,2,9])