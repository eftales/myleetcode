class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

''' 复杂图例 t6 为根节点

'''
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)
t9 = TreeNode(9)
t10 = TreeNode(10)
t6.left = t4
t6.right = t9
t4.left = t2
t4.right = t5
t2.left = t1
t2.right = t3
t9.left = t7
t9.right = t10
t7.left = t8

''' 简单图例 t1 为根节点
t1 = TreeNode(0)
t2 = TreeNode(2)
t3 = TreeNode(-5)

t1.left = t2
t1.right = t3

'''

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if root == None:
            return None

        cur = root
        curMax= None
        err1 = None
        err2 = None
        targetVal = None

        freeze1 = False
        
        def leftChildDone(root:TreeNode,target) -> [bool,TreeNode]:
            if root.right != None:
                if root.right is target:
                    return [True,root]
                else:
                    return leftChildDone(root.right,target)
            return [False,root]


        while cur != None:
            did,rightest = True,None
            if cur.left != None: # 左子树不为 None 先遍历左子树
                did,rightest = leftChildDone(cur.left,cur)


            if did == False: # 左子树没有遍历，先遍历左子树
                rightest.right = cur
                cur = cur.left
            else: # 左子树遍历完了轮到右子树了
                # 删掉原有的链接
                if rightest != None:
                    rightest.right = None

                if freeze1 == True :
                    if cur.val < targetVal:
                        err2 = cur
                        err1.val,err2.val = err2.val,err1.val
                        return None
                else:
                    if curMax == None:
                        curMax = cur.val
                        err1 = cur
                    elif curMax < cur.val :
                        # 更新最大值
                        curMax = cur.val
                        err1 = cur
                    elif curMax > cur.val:
                        # 第一个错误节点就是破坏升序的那个节点
                        targetVal = cur.val # 此时的 root 是 targetVal，err1 是 root 前一个节点
                        freeze1 = True # 此时 err1 保存的就是第一个错误节点 
                        err2 = cur # 初始化 err2，如果整棵树只有两个节点的话此时的 err2 就是真的 err2
                
                cur = cur.right


        # 能运行到这里的，说明树只有两个节点/需要交换的节点紧邻，直接交换一下就行
        err1.val,err2.val = err2.val,err1.val

        

s = Solution()
s.recoverTree(t6)
i = 10 # 多一行看看结果