# 557. 反转字符串中的单词 III
这道题很简单，但是我还是调试了依次之后才通过。

反思了一下，主要是两个问题，第一个问题是思维不严密，第二个问题是对 Python 语言特性不熟悉。

## 以特征字符(逗号空格)分词时忽略最后一个单词
557.py 的第 11 行有一句：

```python
subStrs.append(subStr)
```

这句的作用时对 subStr 做一个兜底。只执行上面的循环，如果输入字符串最后一个字符不是空格的话，会导致最后一个单词无法加入到 subStrs 里面。

## 字符串索引
[字符串索引](../Python语言特性/字符串索引.md)
