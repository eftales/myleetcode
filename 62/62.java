class Solution {
    public int uniquePaths(int m, int n) {
        int[][] res = new int[m][n];
        for(int i=0;i<m;++i){
            res[i][0] = 1;
        }
        for(int i=0;i<n;++i){
            res[0][i] = 1;
        }
        for(int i=1;i<m;++i){
            for(int j=1;j<n;++j){
                res[i][j] = res[i-1][j]+res[i][j-1];
            }
        }
        return res[m-1][n-1];

    }
    public int uniquePathsSimplify(int m, int n) {
        long res = 1; // 在本题中用 int 会超时
        for(int x=n,y=1;y<m;++x,++y){
            res = res*x/y;
        }
        return (int)res;
    }
}