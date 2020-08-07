class Solution:
    def rob(self, root) -> int:
        def lrd(root): # 返回值的格式是 [选择自己的最大值，不选择自己的最大值]
            if root == None:
                return [0,0]

            lChild= [0,0]
            if root.left != None:
                lChild = lrd(root.left)
            rChild = [0,0]
            if root.right != None:
                rChild = lrd(root.right)

            fn2 = max(lChild) + max(rChild) # 不选择本节点的最大值，这里的 max 是精华

            fn1 = root.val + lChild[1] + rChild[1] # 选择本节点的最大值
            print(fn1,fn2)

            return [fn1,fn2]

        return max(lrd(root))
