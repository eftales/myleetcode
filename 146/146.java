class BLinkedList{
    public int key;
    public int val;
    public BLinkedList pre;
    public BLinkedList next;

    public BLinkedList(int key_, int val_,BLinkedList pre_,BLinkedList next_){
        key = key_;
        val = val_;
        pre = pre_;
        next = next_;
    }
}

class LRUCache {
    // 精髓在于 这两个虚拟的头部和尾部
    BLinkedList dummyHead;
    BLinkedList dummyTail;
    int capacity;
    int currentNum = 0;

    Map<Integer,BLinkedList> map = new HashMap<>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
        dummyHead = new BLinkedList(Integer.MAX_VALUE,Integer.MAX_VALUE,null,null);
        dummyTail = new BLinkedList(Integer.MIN_VALUE,Integer.MIN_VALUE,null,null);

        dummyHead.next = dummyTail;
        dummyTail.pre = dummyHead;
    }

    public int get(int key) {
        if(map.containsKey(key)){
            BLinkedList toHead = map.get(key);
            // 更新双向链表
            insert2Head(toHead);
            return toHead.val;
        }
        else{
            return -1;
        }
    }

    public void put(int key, int value) {
        if(map.containsKey(key)){
            // 更新值
            BLinkedList toHead = map.get(key);
            toHead.val = value;

            // 更新双向链表
            insert2Head(toHead);

        }
        else{

            if(currentNum<capacity){
                // 直接插入
                insertNew(key,value);
            }
            else{
                //删除最老没有使用的缓存，插入值，更新双向链表
                removeOldest();
                insertNew(key,value);
            }



        }
    }

    private void removeOldest(){
        remove(dummyTail.pre.key);
    }

    private void insertNew(int key,int value){
        BLinkedList newNode = new BLinkedList(key,value,dummyHead,dummyHead.next);
        dummyHead.next = newNode;
        newNode.next.pre = newNode;
        map.put(key,newNode);
        currentNum+=1;
    }

    private void remove(int key){
        // 将 node 从链表中取下
        BLinkedList toDel = map.get(key);
        BLinkedList toDelNext = toDel.next;
        BLinkedList toDelPre = toDel.pre;
        toDelNext.pre = toDelPre;
        toDelPre.next = toDelNext;

        map.remove(toDel.key);
        currentNum -= 1;
    }

    private void insert2Head(BLinkedList node){
        // 将 node 从链表中取下
        remove(node.key);

        // 放置到开头
        insertNew(node.key,node.val);

    }
}
