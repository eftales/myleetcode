// 网易2021校招笔试-Java开发工程师（正式第二批）
import java.util.*;

class Node{
    int id;
    int doneTime = -1;
    List<SendTo> neis = new ArrayList<>();

    public Node(int id) {
        this.id = id;
    }
}

class SendTo{
    int id;
    int time;

    public SendTo(int id, int time) {
        this.id = id;
        this.time = time;
    }
}


public class Main {

    public static int calSendTime(Node[] nodes,int id){
        Node node = nodes[id];
        if(node.doneTime!=-1){
            return node.doneTime;
        }
        int maxTime = 0;
        for(int i=0;i<node.neis.size();++i){
            SendTo sendTo = node.neis.get(i);
            maxTime = Math.max(maxTime,sendTo.time + calSendTime(nodes,sendTo.id));
        }
        node.doneTime = maxTime;
        return maxTime;

    }

    public static void main(String[] args) {
        Scanner scin = new Scanner(System.in);
        int N = scin.nextInt();
        int K = scin.nextInt();
        int M = scin.nextInt();

        Node[] nodes = new Node[N+1];

        for(int n=0;n<=N;++n){
            nodes[n] = new Node(n);
        }

        for(int m=0;m<M;++m){
            int from = scin.nextInt();
            int to = scin.nextInt();
            int time = scin.nextInt();

            Node node = nodes[from];

            node.neis.add(new SendTo(to,time));
        }

        int[] costTime = new int[N+1];
        Arrays.fill(costTime,Integer.MAX_VALUE);
        costTime[0] = 0;

        List<Integer> curList = new LinkedList<>();
        List<Integer> nextList = new LinkedList<>();

        nextList.add(K);
        costTime[K] = 0;

        while (nextList.size()!=0){


            List<Integer> tmp = curList;
            curList = nextList;
            nextList = tmp;

            while(curList.size()!=0){
                int id = curList.remove(0);
                Node node = nodes[id];
                for(int i=0;i<node.neis.size();++i){
                    SendTo sendTo = node.neis.get(i);
                    costTime[sendTo.id] = Math.min(costTime[id] + sendTo.time,costTime[sendTo.id]) ;
                    nextList.add(sendTo.id);
                }
                node.neis.clear();

            }

        }

        int doneTime = 0;
        for(int i=0;i<costTime.length;++i){
            doneTime = Math.max(doneTime,costTime[i]);
        }

        if(doneTime==Integer.MAX_VALUE){
            System.out.println(-1);
            return;
        }

        System.out.println(doneTime);

    }
}
