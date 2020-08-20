class Solution:
    def updateBoard(self, board, click):
        def getNeighbors(x,y,m,n): # fix2: 引入了表示四周方位的常数
            around = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            neighbors = []
            for dertaX,dertaY in around:
                if 0 <= dertaX+x <m and 0<= dertaY+y<n:
                    neighbors.append((dertaX+x,dertaY+y))
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
            def clearEmptySquare(board,x,y,m,n):
                mine = getNearMine(board,x,y,m,n)
                if mine != 0:
                    board[x][y] = str(mine)
                else:
                    board[x][y] = 'B'
                    neighbors = getNeighbors(x,y,m,n)
                    for eachX,eachY in neighbors:
                        if board[eachX][eachY] == 'E': # fix1: 不需要维护 visited 集合
                            clearEmptySquare(board,eachX,eachY,m,n)

            clearEmptySquare(board,x,y,m,n)
        
        return board
            


s = Solution()
s.updateBoard([['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']],[3,0])