class Solution:
    def sortedSquares(self, A) :
        left = 0
        right = len(A) - 1
        res = []
        while left <= right:
            if abs(A[left]) < A[right]:
                res.insert(0,A[right]*A[right])
                right -= 1
            else:
                res.insert(0,A[left]*A[left])
                left += 1
        return res
                