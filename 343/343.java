class Solution {
    public int integerBreak(int n) {
        int[] F = new int[n+1]; // 存储相乘的最大结果
        for(int i=2;i<=n;++i){
            int curMax = 0;
            // F[i] 表示当前长度最大的分解相乘结果，需要在遍历所有的分段方法后得出
            for(int j=1;j<i;++j){
                curMax = Math.max(curMax,Math.max(j*(i-j),j*F[i-j])); // 在 curMax,只分两段，(i-j)的最大分段长度*j 中取最大值
            }
            F[i] = curMax;
        }

        return F[n];
    }
}