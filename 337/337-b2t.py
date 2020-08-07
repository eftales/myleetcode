class Solution:
    def rob(self, root) -> int:
        def lrd(root):
            if root == None:
                return 0
            if hasattr(root,"maxVal"):
                return root.maxVal # 记录一下结果，避免重复计算

            lChild= 0
            if root.left != None:
                lChild = lrd(root.left)
            rChild = 0
            if root.right != None:
                rChild = lrd(root.right)
            fn1 = lChild + rChild

            
            llChild = 0
            if root.left != None and root.left.left != None:
                llChild = lrd(root.left.left)
            lrChild = 0
            if root.left != None and root.left.right != None:
                lrChild = lrd(root.left.right)
            rlChild = 0
            if root.right != None and root.right.left != None:
                rlChild = lrd(root.right.left)
            rrChild = 0
            if root.right != None and root.right.right != None:
                rrChild = lrd(root.right.right)

            fn2 = root.val + llChild + lrChild + rlChild + rrChild

            root.maxVal = max(fn1,fn2)


            return root.maxVal

        return lrd(root)
