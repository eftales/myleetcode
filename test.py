from functools import reduce 
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

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
                fromtoDict[fromLoc].insert(i,toLoc)
                break
        else:
            fromtoDict[fromLoc].append(toLoc)

print(fromtoDict)