# 491. 递增子序列
我只想到了遍历，结果实际上也只能遍历。但是还是有可以改进的地方，比如 list 的哈希。

## list 的哈希
原生 Python 并不提供 list 的哈希，也就是说 list 不可以作为 dict 的 key，这给本题的去重带来了很大的难度。

我的方法也是很暴力：先把 list 变成字符串，对字符串进行哈希，然后把字符串变成 list，作为结果给返回。

官方题解提到了 [Rabin-Karp 字符串编码](https://leetcode-cn.com/problems/longest-happy-prefix/solution/zui-chang-kuai-le-qian-zhui-by-leetcode-solution/)，是在 1392 中提到的。Rabin-Karp.py 简单的演示了这种算法。

491-optifine.py 使用了 Rabin-Karp 编码来哈希上升子序列，并优化了 cur 栈的压入弹出机制，避免了每次递归都会复制两次 cur 栈。
