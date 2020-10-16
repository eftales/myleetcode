# 116. 填充每个节点的下一个右侧节点指针
这个题目的要求就是搭路，但是之前搭建的道路（root.left.next = root.right）会为之后搭路（root.right.next = root.next.left）提供方便。
