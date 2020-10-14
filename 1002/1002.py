class Solution:
    def commonChars(self, A) :
        splitChar = []
        minLen = None
        for eachStr in A:
            curLen = len(eachStr)
            if minLen == None:
                minLen = curLen
            else: 
                minLen = minLen if minLen < curLen else curLen
            chars = list(eachStr)
            chars.sort()
            splitChar.append(chars)
        
        res = []
        while True:
            needPop = [0]
            for i in range(1,len(splitChar)):
                if splitChar[i][0] == splitChar[needPop[0]][0]:
                    needPop.append(i)
                elif splitChar[i][0] < splitChar[needPop[0]][0]:
                    needPop = [i]
            
            if len(needPop) == len(splitChar):
                res.append(splitChar[needPop[0]][0])
            for i in needPop:
                splitChar[i].pop(0)
                if len(splitChar[i]) == 0:
                    return res


s = Solution()
s.commonChars(["bella","label","roller"])
