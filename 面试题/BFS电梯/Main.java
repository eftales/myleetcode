import java.util.*;

/**
 * BFS DFS 区别
 * BFS 一定需要手动维护一个队列，一般而言，不使用递归来完成 BFS
 * DFS 一定需要一个栈，一般而言，使用递归来解决 DFS 问题，因为在递归本身就帮忙完成了栈
 */

public class Main {

    public static boolean dfs(int curr,int[] cnt, int[] K, int N, int B){
        int indR = curr+K[curr];
        int indL = curr-K[curr];

        if(indR<=N){
            if(cnt[indR]==0){
                cnt[indR] = cnt[curr] + 1;
            }
            else{
                cnt[indR] = Math.min(cnt[indR],cnt[curr] + 1);
            }

        }
        if(indL>0){
            if(cnt[indL]==0){
                cnt[indL] = cnt[curr] + 1;
            }
            else{
                cnt[indL] = Math.min(cnt[indL],cnt[curr] + 1);
            }

        }

        if(cnt[B]!=0){
            return true;
        }
        else{
            boolean done = false;
            if(indR<=N){
                done = bfs(indR,cnt,K,N,B);
            }
            if(!done&&indL>0){
                done = bfs(indL,cnt,K,N,B);
            }

            return done;
        }


    }

    public static void main(String[] argv){
        Scanner scin = new Scanner(System.in);
        int N = scin.nextInt();
        int A = scin.nextInt();
        int B = scin.nextInt();

        int[] K = new int[N+1];
        for(int i=1;i<=N;++i){
            K[i] = scin.nextInt();
        }

        if(A==B){
            System.out.println(0);
            return;
        }

        int[] cnt = new int[N+1];
        Arrays.fill(cnt,Integer.MAX_VALUE);

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(A);
        cnt[A] = 0;
        while(queue.size()!=0){
            int curr = queue.poll();
            int indR = curr+K[curr];
            int indL = curr-K[curr];

            if(indR<=N){
                if(cnt[indR]>=cnt[curr] + 1){
                    cnt[indR] = cnt[curr] + 1;
                    queue.offer(indR);
                }

            }
            if(indL>0){
                if(cnt[indL]>=cnt[curr] + 1){
                    cnt[indL] = cnt[curr] + 1;
                    queue.offer(indL);
                }

            }

            if(cnt[B]!=Integer.MAX_VALUE){
                break;
            }
        }
        if(cnt[B]!=Integer.MAX_VALUE){
            System.out.println(cnt[B]);
        }
        else{
            System.out.println(-1);
        }


    }

}


