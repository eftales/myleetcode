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

findBound([-1,0,3,10])
findBound([3])
findBound([-1,-1,-1,-1])

p  = 1