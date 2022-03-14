class Solution {
    public int numSquares(int n) {
        int[] F = new int[n+1];
        for(int i=1;i<=n;++i){
            if(i*i<=n){
                F[i*i] = 1;
            }
            if(F[i]!=1){
                int minCnt = Integer.MAX_VALUE;
                for(int j=1;j<=i/2;++j){
                    minCnt = Math.min(minCnt,F[j]+F[i-j]);        
                }
                F[i] = minCnt;
            }
        }
        return F[n];
    }
}