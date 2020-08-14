# 20. 有效的括号
这道题时比较简单的字符串问题，但是我还是调试了一次之后才通过。。。

问题出在“初始化”，我一开始的代码是下面这个样子的。

```python
for each in s:
    if len(stack) == 0 and each in left:
            stack.append(each)
            continue
    else:
        return False
```

我错误的认为 `len(stack) == 0` 只有在第一次循环的时候才会出现，实际上循环过程中完全可能出现栈空的情况；且这个 else 也导致了严重的问题，如果第二次循环栈不为空，则一定会跳转到 else 分支，直接返回 Fasle。

## 可以优化的地方
1. 如果字符串长度不是偶数直接返回 False

2. not 和 “空” 数据结构的奇妙配合，可以少用几个 len 函数了

    not [] == True

    not {} == True

    not "" == True
    
3. opposit 函数可以直接用 dict 取代