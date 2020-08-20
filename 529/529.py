class Solution:
    def updateBoard(self, board, click):
        def getNeighbors(x,y,m,n):
            neighbors = []
            for dertaX in [-1,1]:
                if 0 <= dertaX + x < m:
                    for dertaY in [-1,0,1]:
                        if 0 <= dertaY + y < n:
                            neighbors.append((dertaX + x ,dertaY + y))
            
            for dertaY in [-1,1]:
                if 0 <= dertaY + y < n:
                    neighbors.append((x ,dertaY + y))
            
            return neighbors

        def getNearMine(board,x,y,m,n):
            neighbors = getNeighbors(x,y,m,n)
            mine = 0
            for eachX,eachY in neighbors:
                if board[eachX][eachY] == 'M':
                    mine += 1
            return mine

        if not board:
            return board
        x = click[0]
        y = click[1]
        m = len(board)
        n = len(board[0])
        mine = getNearMine(board,x,y,m,n)

        if board[x][y] == 'M': # 情况 1
            board[x][y] = 'X'
        elif mine != 0: # 情况 3
            board[x][y] = str(mine)
        elif mine == 0: # 情况 2
            visited = set()
            def clearEmptySquare(board,x,y,m,n):
                nonlocal visited
                visited.add((x,y))
                mine = getNearMine(board,x,y,m,n)
                if mine != 0:
                    board[x][y] = str(mine)
                else:
                    board[x][y] = 'B'
                    neighbors = getNeighbors(x,y,m,n)
                    for eachX,eachY in neighbors:
                        if (eachX,eachY) not in visited:
                            clearEmptySquare(board,eachX,eachY,m,n)

            clearEmptySquare(board,x,y,m,n)
        
        return board
            


s = Solution()
s.updateBoard([['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']],[3,0])