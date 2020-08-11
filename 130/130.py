class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == [] or board == [[]]:
            return None
        def neighbor(x,y,m,n):
            if x < 0 or x >= m or y < 0 or y >= n:
                return []
            res = []

            # 注意这里是两个 if 并列，不是 if....elif 
            if m != 1 and x != m-1:
                res.append((x+1,y))
            if m != 1  and x != 0:
                res.append((x-1,y))

            if n != 1 and y != n-1:
                res.append((x,y+1))
            if n != 1 and y != 0:
                res.append((x,y-1))
            
            return res

        def bfs(loc,board):
            m = len(board)
            n = len(board[0])
            
            outside_ = set()
            outside_.add(loc)
            nodes = [loc]
            while len(nodes) != 0:
                curloc = nodes.pop()
                x = curloc[0]
                y = curloc[1]
                for x_,y_ in neighbor(x,y,m,n):
                    if board[x_][y_] == 'O':
                        if (x_,y_) not in outside_:
                            outside_.add((x_,y_)) # outside_ 一方面表示连在一起的 "O" 也表示遍历过的 "O"
                            nodes.append((x_,y_)) # 
            return outside_

        outside = set()
        m = len(board)
        n = len(board[0])
        for i in [0,m-1]:
            for j in range(0,n):
                if board[i][j] == 'O':
                    if (i,j) not in outside:
                        outside_ = bfs((i,j),board)
                        outside = set.union(outside,outside_)
        
        for i in range(0,m):
            for j in [0,n-1]:
                if board[i][j] == 'O':
                    if (i,j) not in outside:
                        outside_ = bfs((i,j),board)
                        outside = set.union(outside,outside_)
        for i in range(0,m):
            for j in range(0,n):
                if (i,j) not in outside:
                    board[i][j] = "X"
        

s = Solution()
d = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
s.solve(d)
print(d)