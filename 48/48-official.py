class Solution:
    def rotate(self, matrix):
        length = len(matrix)
        for i in range(0,length//2):
            for j in range(0,length): 
                matrix[i][j],matrix[length - i -1][j] = matrix[length - i -1][j],matrix[i][j]
        
        for i in range(0,length):
            for j in range(i+1,length):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
