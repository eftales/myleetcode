# 100. 相同的树
这道题看起来很简单，但是实际写的时候还是遇到了困难。

第一个困难如何让算法“一步一步”执行，每次遍历一个点，然后输出遍历的结果。还是老生常谈的问题，二叉树不可以很方便的访问指定位置的元素，一般通过递归一次性把树的节点存储在 list 这种直观的容器里面。递归是没有办法随时停下来的，一旦停止那就意味着整个树遍历完了。这样显然不好，在遇到第一个不一样的节点的时候就可以停下算法了，没必要遍历完整个树。

我没有想出如何一个可以实现同时遍历两棵树的递归算法，100-bfs.py 是我完成的第一个版本，用到的思想和 bfs 类似，每次在 list 中读取一个新的节点，然后把与该节点邻接的所有节点加入 list 等待依次遍历。只要分别为两个树维护 list 即可。

## dfs
看了官方解答之后才发现其实可以同时用递归算法遍历两棵树的。

```python
class Solution:
    def isSameTree(self, p, q) -> bool:
        if p == None and q == None: # 两个都是 None
            return True
        elif p == None or q == None: # 两个里面有一个是 None
            return False
        else:
            # 两个都不是 None
            if p.val != q.val: # 发现节点的 val 不一样
                return False
            else:
                # 还需要进一步判断左右子树，一旦发现一次  False，就会把 False 一层一层 return 回去
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

```

现在想了想，既然可以遍历一棵树，那么就一定可以遍历两棵树呀。。。
