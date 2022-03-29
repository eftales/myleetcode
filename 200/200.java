class Solution {

    void bfs(char[][] grid,int i,int j,int n,int m){
        grid[i][j] = '2';

        if(i-1>=0){
            if(grid[i-1][j]=='1'){
                bfs(grid,i-1,j,n,m);
            }
        }

        if(i+1<n){
            if(grid[i+1][j]=='1'){
                bfs(grid,i+1,j,n,m);
            }
        }

        if(j-1>=0){
            if(grid[i][j-1]=='1'){
                bfs(grid,i,j-1,n,m);
            }
        }

        if(j+1<m){
            if(grid[i][j+1]=='1'){
                bfs(grid,i,j+1,n,m);
            }
        }

    }

    public int numIslands(char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        int res = 0;
        for(int i=0;i<n;++i){
            for(int j=0;j<m;++j){
                if(grid[i][j]=='1'){
                    res += 1;
                    bfs(grid,i,j,n,m);
                }
            }
        }

        return res;

    }
}

