from functools import reduce 
class Solution:
    def findItinerary(self, tickets):
        def myHash(s):
            base = 31
            slist = list(s)
            sintList = list(map(lambda x:ord(x)-ord('A'),slist))
            hashcode = reduce(lambda x,y:x*base+y,sintList)
            return hashcode
        hashDict = dict()
        fromtoDict = dict()

        for ticket in tickets:
            fromLoc = ticket[0]
            toLoc = ticket[1]

            if fromLoc not in hashDict:
                hashDict[fromLoc] = myHash(fromLoc)
            if toLoc not in hashDict:
                hashDict[toLoc] = myHash(toLoc)

            if fromLoc not in fromtoDict:
                fromtoDict[fromLoc] = [toLoc]
            else:
                for i in range(0,len(fromtoDict[fromLoc])):

                    if hashDict[fromtoDict[fromLoc][i]] > hashDict[toLoc] :
                        fromtoDict[fromLoc].insert(i,toLoc) # 反思一下为什么想不到用 heap 这种数据结构
                        break
                else:
                    fromtoDict[fromLoc].append(toLoc)   

        
        curFrom = "JFK"
        res = [curFrom]
        while True:

            if curFrom not in fromtoDict or  len(fromtoDict[curFrom]) == 0:
                break
            curFrom = fromtoDict[curFrom].pop(0)
            if (curFrom not in fromtoDict) and  (len(fromtoDict[res[-1]]) >= 1): # 一个 fromLoc 不会对应一个以上的不在 fromtoDict 中的 toLoc
                fromtoDict[res[-1]].append(curFrom)
                curFrom = fromtoDict[res[-1]].pop(0)
            res.append(curFrom)

        return res



s = Solution()
s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) # 只考虑的顺序小的在前面，会导致用不完所有的票

s.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]])
