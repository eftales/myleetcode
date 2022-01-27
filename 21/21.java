
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}


class Solution {

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1==null || list2==null){
            if (list1!=null){
                return list1;
            }
            else{
                return list2;
            }
        }

        ListNode smaller;
        if(list1.val>=list2.val){
            smaller = list2;
            list2 = list2.next;
        }
        else{
            smaller = list1;
            list1 = list1.next;
        }

        ListNode orderedList=smaller,head=orderedList;

        while(list1!=null && list2!=null){
            if(list1.val>=list2.val){
                orderedList.next = list2;
                list2 = list2.next;
            }
            else{
                orderedList.next = list1;
                list1 = list1.next;
            }
            orderedList = orderedList.next;
        }

        if(list1==null && list2!=null){
            orderedList.next = list2;
        }
        else if(list1!=null && list2==null){
            orderedList.next = list1;
        }


        return head;

    }

    public ListNode mergeTwoListsSimplify(ListNode list1, ListNode list2) {
        ListNode preHead = new ListNode(-1);
        ListNode currNode = preHead;

        while(list1!=null && list2!=null){
            if(list1.val>=list2.val){
                currNode.next = list2;
                list2 = list2.next;
            }
            else{
                currNode.next = list1;
                list1 = list1.next;
            }
            currNode = currNode.next;
        }

        currNode.next = null == list1?list2:list1;


        return preHead.next;

    }

    void rec(ListNode head,ListNode list1, ListNode list2){

        if(list1==null){
            head.next = list2;
            return;
        }
        else if(list2==null){
            head.next = list1;
            return;
        }

        if(list1.val>=list2.val){
            head.next = list2;
            list2 = list2.next;
        }
        else{
            head.next = list1;
            list1 = list1.next;
        }
        rec(head.next,list1, list2);

    }
    public ListNode mergeTwoListsRec(ListNode list1, ListNode list2){
        ListNode preHead = new ListNode(-1);
        rec(preHead,list1,list2);
        return preHead.next;
    }


    public ListNode mergeTwoListsRecSimplify(ListNode list1, ListNode list2){
        if(list1==null){
            return list2;
        }
        else if(list2==null){
            return list1;
        }
        else if(list1.val>=list2.val){
            list2.next = mergeTwoListsRecSimplify(list1,list2.next);
            return list2;
        }
        else {
            list1.next = mergeTwoListsRecSimplify(list1.next,list2);
            return list1;
        }
    }
}
