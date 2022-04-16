import java.util.*;
// 网易2021校招笔试-Java开发工程师（正式第二批）
/** 动态规划，从后向前进行计算
    如果 nums[i] 是 0，dp[i] = dp[i+1]
    如果 nums[i] 是 1，dp[i] = dp[i+1] + dp[i+2] +dp[i+3]
*/

public class Main {
    public static void main(String[] args) {
        Scanner scin = new Scanner(System.in);
        String nums = scin.nextLine();

        int[] F = new int[nums.length()+1];
        F[nums.length()] = 1;


        for(int i=nums.length()-1;i>=0;--i){
            F[i] = F[i+1];
            if(nums.charAt(i)=='1'){
                // 是 1 的话还需要进行判断组合
                for(int j=2;j<=3&&(i+j<=nums.length());++j){
                    F[i] += F[i+j];
                }

            }


        }

        System.out.println(F[0]);

    }
}
