import java.util.Arrays;

class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int len = nums.length;
        int currMax = 0;
        for(int i = 0;i<len/2;++i){
            currMax = Math.max(currMax,nums[i]+nums[len-i-1]);
        }
        return currMax;

    }
}
