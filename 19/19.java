class Solution {
    public ListNode removeNthFromEnd(ListNode head, final int n) {
        // 精髓就在 newHead 上，无论怎么修改，newHead.next 一定是最终的头节点
        ListNode beforeDel=new ListNode(-1),newHead=beforeDel,endNode=head;
        beforeDel.next = head;
        for(int i=0;i<(n-1);++i){
            endNode = endNode.next;
        }

        while(endNode.next!=null){
            endNode = endNode.next;
            beforeDel = beforeDel.next;
        }
        beforeDel.next = beforeDel.next.next;


        return newHead.next;
    }
}
