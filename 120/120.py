class Solution:
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        f = [0] * n # 这样才能创建一个 n 个元素的数组

        f[0] = triangle[0][0]
        for i in range(1,n):
            f[i] = f[i-1] +  triangle[i][i]
            for j in range(i-1,0,-1): # 注意：需要从后往前遍历，从前往后遍历会提前更新数据
                f[j] = min(f[j-1],f[j]) + triangle[i][j]

            f[0] = f[0] +  triangle[i][0]
            
        
        return min(f)

s = Solution()      
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(s.minimumTotal([[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],[-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],[-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]))