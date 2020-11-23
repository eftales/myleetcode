class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        res = 0
        points.sort()
        begin = points[0][0]
        end = points[0][1]

        for i in range(1,len(points)):
            if points[i][0] > end:
                res += 1
                begin = points[i][0]
                end = points[i][1]
            else:
                end = min(end,points[i][1])
        res += 1
        return res