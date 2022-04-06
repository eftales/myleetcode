# Java 输入输出
## 输入
Scanner.hasNext() 和 Scanner.hasNextLine() 的区别：

1. hasNextLine 会将只包含一个 '\n' 的空行也认为是一个有效行；hasNext 只认包含了非空包字符的行；

2. hasNextLine 读取到的字符串中允许包含空格等空白字符；hasNext 遇到空白字符就会返回。

由于 Scanner 并不允许读入一个字符，因此就出现了奇奇怪怪的现象：

```text
3 7
U 1 2
```

我们两次调用 Scanner.nextInt() 获取 3 和 7。此时我调用 hasNextLine，会返回一个空字符串；调用 hasNext 会返回 "U"。nextInt 在将 3 和 7 这两个字符串读走之后会在缓冲区中剩下一个 '\n'，结合以上的两点区别，我们不难理解为什么会返回不同的值。

可以在牛客网的 华为2016校园招聘上机笔试题 第一道测试这个问题。


## 输出
有时候输出可能是一个具有一定格式的线性表，比如说 "1 2 3 4"，怎么才能很方便的输出这种格式的字符串呢。

```java
List<String> li = new ArrayList<>();
li.add("1");
li.add("2");
li.add("3");
System.out.println(String.join(" ", li));
```


