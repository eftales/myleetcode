class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return None
        fast = head
        slow = head
        while True:
            if fast.next != None:
                fast = fast.next
                
            if fast.next != None:
                slow = slow.next
                fast = fast.next
            else:
                break
        
        left = None
        mid = slow.next
        slow.next = None
        
        while mid != None:
            right = mid.next
            mid.next = left
            left = mid
            mid = right
        iHead = left


        newHead = head
        head = head.next
        while head != None or iHead != None:
            if iHead != None:
                newHead.next = iHead
                newHead = newHead.next
                iHead = iHead.next
            if head != None:
                newHead.next = head
                head = head.next
                newHead = newHead.next
    
        return newHead