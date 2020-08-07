# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if p == None or q == None:
            if p == q:
                return True
            return False
        elmp = [p]
        elmq = [q]

        while len(elmp) != 0 and len(elmq) != 0:
            curp = elmp.pop(0)
            curq = elmq.pop(0)

            if curp.val != curq.val:
                return False

            pl = curp.left
            ql = curq.left

            if pl == None and ql == None: 
                pass
            else:
                if (pl != None and pl.val) != (ql != None and ql.val):
                    return False

                elmp.append(pl)
                elmq.append(ql)

            pr = curp.right
            qr = curq.right
            if pr == None and qr == None: 
                pass
            else:
                if (pr != None and pr.val) != (qr != None and qr.val):
                    return False

                elmp.append(pr)
                elmq.append(qr)

        return True      
            



        
