class Solution:
    def sortedSquares(self, A) :
        def findBound(A):
            left = 0
            righ = len(A) - 1
            boundary = righ//2 # A[boundary]*A[boundary+1] < 0 or A[boundary] == 0
            while True:
                if not left<=righ:
                    boundary = None
                    break
                elif A[boundary] == 0:
                    break
                elif A[boundary] > 0:
                    if boundary == 0:
                        boundary = None
                        break
                    righ = boundary-1
                    
                elif A[boundary] < 0:
                    if boundary == len(A)-1:
                        boundary = None
                        break
                    if A[boundary+1] > 0:
                        break
                    else:
                        left = boundary + 1
                
                boundary = (left+righ) // 2
            return boundary
        boundary = findBound(A)
        if boundary == None:
            if A[0] < 0:
                boundary = len(A) - 1
            elif A[0] > 0:
                boundary = 0
        i = boundary 
        j = boundary + 1
        res = []
        while i >= 0 or j <= (len(A)-1):
            if i < 0:
                res.append(A[j]*A[j])
                j += 1
            elif j > (len(A)-1):
                res.append(A[i]*A[i])
                i -= 1

            elif abs(A[i]) <= A[j]:
                res.append(A[i]*A[i])
                i -= 1
            else:
                res.append(A[j]*A[j])
                j += 1
        return res

s = Solution()
s.sortedSquares([1])
