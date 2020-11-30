class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ""
        pairs = dict()
        pairs[S[0]] = 1
        curmax = [S[0],1]
        for i in range(1,len(S)):
            each = S[i]
            if each not in pairs:
                pairs[each] = 1
            else:
                pairs[each] += 1
            if pairs[each] > curmax[1]:
                curmax = [each,pairs[each]]
        
        
        num = pairs.pop(curmax[0])
        if num > (len(S) + 1) // 2 :
            return ""
        res = [curmax[0]]*num
        index = 1
        for eachKey in pairs:
            num = pairs[eachKey]
            while num != 0:
                res.insert(index,eachKey)
                num -= 1
                index += 2
                if index > len(res):
                    index = 1
        return "".join(list(map(str,res)))