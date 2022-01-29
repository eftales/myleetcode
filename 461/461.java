class Solution {
    public int hammingDistance(int x, int y) {
        int distance = x^y,cnt=0;
        while(distance!=0){
            distance &= (distance-1); // n&(n-1) 可以消除最右边的 0
            cnt += 1;

        }
        return cnt;
    }
}