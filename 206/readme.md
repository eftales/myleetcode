# 206. 反转链表
最精华的是第十行，如果 right 在循环的最后再维护的话就需要写好长的判断。

```Python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        left = None
        mid = head
        right = mid.next

        while mid != None:
            mid.next = left
            left = mid
            mid = right
            right = None if right == None else right.next

        return left
```

## 递归
递归的想法也很简单，每一层递归都要先执行下一次递归，这样就可以确保 head.next 是逆序的

newHead 这个变量其实是逆序链表的头。
