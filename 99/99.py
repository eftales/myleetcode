class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)

t1.left = t3
t3.right = t2

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        curMax= None
        err1 = None
        err2 = None
        targetVal = None

        freeze1 = False

        Done = False
        

        def ldr(root):
            nonlocal curMax,err1,err2,targetVal,freeze1,Done

            if Done == True:
                return None

            if root.left != None:
                ldr(root.left)

            if freeze1 == True :
                if root.val < targetVal:
                    err2 = root
                    err1.val,err2.val = err2.val,err1.val
                    Done = True
                    return None
                        
            elif curMax == None:
                # 初始化
                curMax = root.val
                err1 = root
            elif curMax < root.val :
                # 更新最大值
                curMax = root.val
                err1 = root
            elif curMax > root.val:
                # 第一个错误节点就是破坏升序的那个节点
                targetVal = root.val # 此时的 root 是 targetVal，err1 是 root 前一个节点
                freeze1 = True # 此时 err1 保存的就是第一个错误节点 
                err2 = root # 初始化 err2，如果整棵树只有两个节点的话此时的 err2 就是真的 err2


            if root.right != None:
                ldr(root.right)

        if root != None:
            ldr(root)
            if Done == False: # 只有两个数
                err1.val,err2.val = err2.val,err1.val


s = Solution()
s.recoverTree(t1)
