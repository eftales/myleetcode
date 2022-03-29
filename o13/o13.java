class Solution {

    int dfs(int[][] F,int i,int j,int k){

        F[i][j] = k+1; // 避免重复计数

        int lcnt = 0,rcnt = 0;
        if((i+1<F.length)&&F[i+1][j]<=k){
            lcnt = dfs(F,i+1,j,k);
        }

        if((j+1<F[0].length)&&F[i][j+1]<=k){
            rcnt = dfs(F,i,j+1,k);
        }

        return lcnt+rcnt+1;
    }


/**
1 1 1 1 1 1 1 1 
1 1 1 1 0 1 1 1
1 1 1 0 0 1 1 0
1 1 0 0 0 1 0 0
1 0 0 0 0 0 0 0 
*/

    public int movingCount(int m, int n, int k) {
        int[][] F = new int[m][n]; // 需要创建一个二维数组，因为可能会出现花式连接，如上所示，第二行中间断开了
        F[0][0] = 0;

        for(int i=0;i<m;++i){
            if(i%10==0){
                if(i!=0){
                    F[i][0] = F[i-1][0] - 8;
                }

            }
            else{
                F[i][0] = F[i-1][0] + 1;;
            }
            if(F[i][0]>k){
                break;
            }

            for(int j=1;j<n;++j){
                int diff = 0;
                if(j%10==0){
                    if(j!=0){
                        diff -= 8;
                    }
                }
                else{
                    diff += 1;
                }
                F[i][j] = F[i][j-1] + diff;

            }
        }

        int cnt = dfs(F,0,0,k);
        return cnt;
    }
}