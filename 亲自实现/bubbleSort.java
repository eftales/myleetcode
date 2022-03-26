class Solution {
    public void bubbleSort(int[] data){
        // 从小到大的顺序
        for(int i=0;i<data.length-1;++i){
            boolean done = true;
            for(int j=0;j<(data.length-1-i);++j){
                if(data[j]>data[j+1]){
                    int tmp = data[j];
                    data[j] = data[j+1];
                    data[j+1] = tmp;
                    done = false;
                }
            }
            if(done){
                return;
            }
        }
    }

}