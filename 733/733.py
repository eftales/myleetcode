class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image
        toDraw = set()
        toDraw.add((sr,sc))
        neighbors = [(sr,sc)]
        targetColor = image[sr][sc]
        m = len(image)
        n = len(image[0])

        def getNeighbor(m,n,sr,sc):
            neighbor = []
            if m != 1 and sr != (m-1):
                neighbor.append((sr+1,sc))
            if m != 1 and sr != 0:
                neighbor.append((sr-1,sc))
            
            if n != 1 and sc != (n-1):
                neighbor.append((sr,sc+1))
            if n != 1 and sc != 0:
                neighbor.append((sr,sc-1))

            return neighbor

        while neighbors:
            cur = neighbors.pop()
            x = cur[0]
            y = cur[1]
            image[x][y] = newColor
            for x,y in getNeighbor(m,n,x,y):
                if image[x][y] == targetColor:
                    if (x,y) not in toDraw:
                        toDraw.add((x,y))
                        neighbors.append((x,y))
        return image

            