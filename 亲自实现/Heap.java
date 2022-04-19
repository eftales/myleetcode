// 网易2021校招笔试-Java开发工程师（正式第二批）
import java.util.*;

class Heap{
    ArrayList<Integer> data;

    public Heap(int n){
        data = new ArrayList<>(n);
    }

    private int heapify(int loc){
        int leftChild = 2*loc + 1;
        int rightChild = 2*loc + 2;

        int minInd = loc;
        if(leftChild<data.size()&&data.get(minInd)>data.get((leftChild))){
            minInd = leftChild;
        }

        if(rightChild<data.size()&&data.get(minInd)>data.get((rightChild))){
            minInd = rightChild;
        }

        int tmp = data.get(loc);
        data.set(loc,data.get(minInd));
        data.set(minInd,tmp);

        return minInd;
    }

    private void fixT2B(int loc){
        while(loc<data.size()){
            int nextLoc = heapify(loc);
            if(nextLoc==loc){
               break;
            }
            loc = nextLoc;
        }


    }

    private void fixB2T(int loc){
        while(loc>=0){
            loc = (loc-1)/2;
            int nextLoc = heapify(loc);
            if(nextLoc==loc){
               break;
            }

        }
    }

    public void add(int elm){
        data.add(elm);
        fixB2T(data.size()-1);
    }

    public int pop(){
        if(data.size()<0){
            return -1;
        }
        int ret = data.get(0);

        int elm = data.get(data.size()-1);
        data.remove(data.size()-1);
        if(data.size()>0){
            data.set(0,elm);
            fixT2B(0);
        }

        return ret;
    }

    public int peek(){
        return data.get(0);
    }

}


public class Main {


    public static void main(String[] args) {
        Heap heap = new Heap(10);
        Random random = new Random();
        for(int i=10;i>0;--i){
            heap.add(random.nextInt());
        }

        for(int i=10;i>0;--i){
            System.out.println(heap.pop());
        }
    }
}
