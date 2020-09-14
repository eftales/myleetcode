class Solution:
    def exist(self, board, word: str) -> bool:
        if not board:
            return False
        succeed = False
        charLocs = dict()
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] not in charLocs:
                    charLocs[ board[i][j] ] = [(i,j)]
                else:
                    charLocs[ board[i][j] ].append((i,j))
        

        def getNexts(char,beforeLoc):
            if char not in charLocs:
                return []
            if beforeLoc == None:
                return charLocs[char]
            x = beforeLoc[0]
            y = beforeLoc[1]
            res = []
            for x_,y_ in charLocs[char]:
                if (abs(x-x_) == 1 and abs(y-y_) ==0) or (abs(x-x_) == 0 and abs(y-y_) ==1):
                    res.append((x_,y_))
            return res
        
        def dfs(word,path,beforeLoc):
            if len(word) == 0:
                nonlocal succeed # 这种非引用型变量需要使用 nonlocal 声明为全局
                succeed = True
                return None
            char = word.pop(0)
            nexts = getNexts(char,beforeLoc)
            for nextLoc in nexts:
                if nextLoc not in path:
                    path.add(nextLoc)
                    dfs(word,path,nextLoc)
                    if succeed == True:
                        return None
                    path.remove(nextLoc)
            word.insert(0,char)

        word = list(word)
        path = set()
        dfs(word,path,None)
        return succeed
            
            
s = Solution()
s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS")