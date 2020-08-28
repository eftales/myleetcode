import heapq
class Solution:
    def findItinerary(self, tickets):
        res = []
        graph = dict()

        for ticket in tickets:
            fromLoc = ticket[0]
            toLoc = ticket[1]

            if fromLoc not in graph:
                graph[fromLoc] = [toLoc]
            else:
                heapq.heappush(graph[fromLoc],toLoc) 
        
        def dfs(curLoc):
            if curLoc in graph:
                while len(graph[curLoc]) != 0:
                    nextLoc = heapq.heappop(graph[curLoc])
                    dfs(nextLoc)
            res.insert(0,curLoc)
        dfs("JFK")
        return res