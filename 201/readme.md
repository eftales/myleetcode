# 201. 数字范围按位与
这道题我和官方的做法完全不一样。我的想法其实很复杂。我的想法是 201.py，官方想法是 201-official.py。

## 201.py
我的想法与 2 次幂相关。首先找到大于 m/n 的 2 次幂，如：

```
4 -> 100 -> 1000 -> 8
5 -> 101 -> 1000 -> 8
9 -> 1001 -> 10000 -> 16
```

如果这两个次幂不一样（8，16），则区间内按位与的结果一定是 0。

如果一样还需要进一步判断。再看一个例子。

```
159 -> 10011111 -> 100000000 -> 256
160 -> 10100000 -> 100000000 -> 256
161 -> 10100001 -> 100000000 -> 256
163 -> 10100011 -> 100000000 -> 256
```

[159,160] 区间端点直接与就可得到结果；

[159,161] 区间端点直接与会在末尾出现误差。

而末尾的误差与区间长度有关系，所以设区间长度为 L，大于等于 L 的 2 次幂的末尾有几位 0，就把这几位清除。所以最后的表达式为：m&n&(0x7fffffff - powerLen + 1 )  

## 201-official.py
官方的做法很简洁。这道题的本质是找开头相同的部分，所以逐步删掉较大的那个数（n）右边的 1，当 n < m 的时候，就找到开头相同的部分了。

- n&(n-1) 可以删掉 n 最右边的 1。