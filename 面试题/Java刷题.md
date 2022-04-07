# Java 集合

## 优先队列
自定义最小堆和最大堆

```
return a-b; // 最小堆
return b-a; // 最大堆
```

## Map 遍历元素

```java
for(Map.Entry<> entry:map.entrySet()){
    Key key = entry.getKey();
    Val val = entry.getValue();
}
```

## 稳定排序和不稳定排序

```
import java.util.*;

class Node{
    int ind;
    int val;

    public Node(int ind, int val) {
        this.ind = ind;
        this.val = val;
    }
}

public class Main{

    public static void main(String[] argvs){
        Node[] nodes = new Node[10];
        for(int i=0;i<10;++i){
            nodes[i] = new Node(0,i);
        }

        Arrays.sort(nodes, new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2) {
                return o1.ind-o2.ind;
            }
        });// 顺序是 0,1,...,9


        PriorityQueue<Node> queue = new PriorityQueue<>(new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2) {
                return o1.ind-o2.ind;
            }
        });
        for(int i=0;i<10;++i){
            queue.add(new Node(0,i));

        }

        for(int i=0;i<10;++i){
            nodes[i] = queue.poll(); // 顺序不再是 0,1,...,9
        }



    }
}
```