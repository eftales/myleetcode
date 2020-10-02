class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = [[root,1]]

        while len(stack) != 0:
            if stack[-1][1] == 1:
                leftChild = stack[-1][0].left
                if leftChild != None:
                    stack.append([leftChild,1])
                    stack[-2][1] = 2
                else:
                    stack[-1][1] = 2
            elif stack[-1][1] == 2:
                rightChild = stack[-1][0].right
                if rightChild != None:
                    stack.append([rightChild,1])
                    stack[-2][1] = 3
                else:
                    stack[-1][1] = 3
            elif stack[-1][1] == 3:
                res.append(stack[-1][0].val)
                stack.pop(-1)

        return res