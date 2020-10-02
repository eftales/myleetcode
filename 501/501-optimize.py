class Solution:
    def findMode(self, root):
        if not root:
            return []
        res = [root.val]
        maxNum = root.val
        maxCount = 0
        curNum = root.val
        curCount = 0

        def dfs(root):
            if not root:
                return None
            dfs(root.left)

            nonlocal res,maxCount,maxNum,curNum,curCount
            # 维护 cur 和 max
            if root.val == maxNum:
                maxCount += 1
            elif root.val == curNum:
                curCount += 1
            else:
                curNum = root.val
                curCount = 1
            # 维护答案 res
            if curCount > maxCount:
                maxCount = curCount
                maxNum = curNum
                res = [curNum]
            elif curCount == maxCount:
                res.append(curNum)
            
            dfs(root.right)

        dfs(root)
        return res
            
