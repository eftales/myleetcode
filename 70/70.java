class Solution {
    public int climbStairs(int n) {
        if(n<=2){
            return n;
        }
        int[] maxStep = new int[n+1];
        maxStep[0] = 0;
        maxStep[1] = 1;
        maxStep[2] = 2;
        for(int i=3;i<=n;i++){
            maxStep[i] = maxStep[i-1]+maxStep[i-2];
        }
        return maxStep[n];
    }
}