# insert 的 index 过大
一个 list 原本只有 3 个元素，然后调用 insert 函数向位置等于 100 的地方插入一个元素，会报错嘛？

不会。会把元素插入到 list 的末尾。

```py
l = [1,2,3]
l.insert(100,4)
print(l) # [1,2,3,4]
```
