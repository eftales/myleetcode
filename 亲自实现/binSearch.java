class Solution {
    public boolean replace(int[] data,int toDel,int toAdd){

        int left = 0,right=data.length;
        int i = (left+right) / 2;

        while(left!=right){

            if(data[i] == toDel){
                data[i] = toAdd;
                return true;
            }
            else{
                if(data[i]<toDel){
                    left = Math.max(i,left+1);
                    i = (left+right)/2;
                }
                else{
                    right = i;
                    i = (left+right)/2;
                }
            }
        }
        return false;
    }

}