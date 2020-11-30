# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        def mergeSort(head):
            slow = head
            fast = head.next

            if fast == None:
                return head
            if fast.next == None:
                if slow.val > fast.val:
                    slow.next = None
                    fast.next = slow
                    return fast
                else:
                    return slow
            while fast.next != None:
                fast = fast.next
                if fast.next != None:
                    slow = slow.next
            
            listNodes1 = head
            listNodes2 = slow.next
            slow.next = None

            listNodes1 = mergeSort(listNodes1)
            listNodes2 = mergeSort(listNodes2)

            dummyHead = ListNode(0)
            res = dummyHead

            while listNodes2 != None and listNodes1 != None:
                if listNodes2.val > listNodes1.val:
                    dummyHead.next = listNodes1
                    listNodes1 = listNodes1.next
                else:
                    dummyHead.next = listNodes2
                    listNodes2 = listNodes2.next
                dummyHead = dummyHead.next
            dummyHead.next = listNodes1 if listNodes2 == None else listNodes2
            return res.next
        return mergeSort(head)

