class Solution:
    def canPartition(self, nums) -> bool:
        sumofNum = sum(nums)
        if sumofNum % 2 == 1:
            return False
        target = sumofNum // 2

        nums.sort()

        F = [False] * (target+1)
        F[0] = True

        for each in nums:
            for i in range(0,target+1):
                j = target - i
                if F[j] == False and j-each >=0 and F[j-each] == True:
                    F[j] = True
        return F[-1]


        



s = Solution()
s.canPartition([2,2,3,5])
