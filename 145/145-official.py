class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        pre = None

        root = root.left # 因为一开始就把 root 放进去了，所以第一次循环的 root 是 root.left
        while len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left
            cur = stack[-1]
            if cur.right == None or cur.right == pre:
                res.append(cur.val)
                stack.pop(-1)
                pre = cur # 访问过之后才维护 pre
            else:
                root = cur.right # 只有这里维护了 root


        return res