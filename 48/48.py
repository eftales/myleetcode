class Solution:
    def rotate(self, matrix):
        length = len(matrix)
        mid = (length - 1) / 2

        for i in range(0,(length + 1)//2):
            curx = i
            j = i
            while j <= length - 2 - i:
                cury = j
                val = matrix[curx][cury]
                for k in range(0,4):
                    tarx = cury
                    tary = -curx + length - 1
                    temp = matrix[tarx][tary]
                    matrix[tarx][tary] = val
                    curx = tarx
                    cury = tary
                    val = temp
                j += 1
