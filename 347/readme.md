# 347. 前 K 个高频元素
比之前进步了，一看到 `前 k 个元素` 我就想到了用堆这种数据结构。

但是还是调试了两三次才得到结果。。。

第一个问题是粗心把第五行 `for each in nums:` 写成 `for each in count:` 了。

第二个就是思想出了问题，把元素入了堆，实际上应该把元素的频度和元素一起入堆的，而且需要以元素的频度作为 key 来组织堆。

官方还有基于快速排序的算法，之后再看吧。
