# 632
这道题本质上就是遍历嘛。

## 初始

将 k 个数组中的第一个元素取出，组成一个最小堆。这个堆的最小值（begin）为堆首部，但是同时还需要设置一个变量（end）用于记录堆中的最大值。

区间 [begin,end] 满足 k 个列表中的每个列表至少有一个数包含在其中。

但是这个区间并不一定最小区间。

维护一个“指针数组”，用于记录堆中的元素在数组中的位置。此时数组的值为 [0,0,0,...0]

## 第二步

取出堆中的最小元素，例如是第 i 行的元素，根据“指针数组”在第 i 行取出一个新元素，将指针数组中的第 i 行 +1。

将新元素加入堆，得到了新的 [begin,end]，判断是否优于上个答案。优，则保留，劣，则舍弃。

## 最后一步

当堆中最小元素所在的行已经没有下一个元素的时候，算法结束。

# 我自己的想法
我把前 k-1 行的元素构建为 k-1 个完全二叉搜索树，拿着最后一行的元素，依次和 k-1 个树进行对比，得到区间。

二叉搜索树可以再 O(logn) 的情况下找到和目标值距离最近的数。对第 k 行的所有数进行这个操作，就可以得到最小区间。

这种算法复杂度为 O(knlogn)，官方答案是 O(knlogk)。k > n 的时候我的算法有理论优势，但是官方的算法可以提前结束，所以我觉得官方算法更好。

# 如何把一个排序数组变成完全二叉搜索树
比如说如何把 [1,2,3,4,5,6,7] 变成二叉搜索树呢？

创建一个数组 [ , , , , , , ]。

从第一个元素开始对数组进行先序遍历，遇到数据越界就返回。遍历完左子树之后给自己赋值。

这样就把一个排序数组变成完全二叉搜索树了。

```python
def frontRoot(n,tree,root):
    leftChild = 2*root+1
    if leftChild < len(tree): # 先序遍历的逻辑：如果有 X 子树，就遍历，没有就算了
        n = frontRoot(n,tree,leftChild)
        n += 1

    tree[root] = n  

    rightChild = 2*root+2
    if rightChild < len(tree): # 右子树就不需要特殊的判断了
        n = frontRoot(n+1,tree,rightChild)


    return n

```
