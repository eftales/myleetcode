class Solution:
    def commonChars(self, A) :
        if len(A) == 0:
            return []

        def statics(word):
            charStatic = dict()
            for eachChar in word:
                if eachChar not in charStatic:
                    charStatic[eachChar] = 1
                else:
                    charStatic[eachChar] += 1
            return charStatic
        originDict = statics(A[0])

        for i in range(1,len(A)):
            newDict = statics(A[i])
            for eachChar in originDict:
                if eachChar not in newDict:
                    originDict[eachChar] = 0
                else:
                    originDict[eachChar] = originDict[eachChar] if originDict[eachChar] < newDict[eachChar] else newDict[eachChar]
        
        res = []
        for eachChar in originDict:
            res.extend([eachChar]*originDict[eachChar])
        return res




s = Solution()
s.commonChars(["bella","label","roller"])
