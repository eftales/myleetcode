class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n):
            fact = 1
            for i in range(2,n+1):
                fact *= i
            return fact

        def multiGradientQuery(num,gradient):
            num = num-1 if (num-1)>-1 else 0
            return num // gradient


        nums = list(map(str,range(1,n+1)))
        res = ""
        lenNums = len(nums)

        while lenNums != 0:
            gradient = factorial(lenNums-1)
            index = multiGradientQuery(k,gradient)
            k -= index*gradient 
            res += nums.pop(index)
            lenNums -= 1
        return res

        