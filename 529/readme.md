# 529. 扫雷游戏
不是很难。解完题之后看了别人的代码，有一点收获，优化后的代码是 529-fix.py。

主要修复了以下几个方面：

1. 删除了 visited 数组

    遍历过的元素会被标记为 'B'，没有遍历过的是 'E'，所以不需要额外记录哪些被访问过。

2. 加入常数，简化了 getNeighbors 函数
