class Solution {
    public int maxSubArray(int[] nums) {
        int[] integral = new int[nums.length+1];
        integral[0] = 0;
        for(int i=1;i<integral.length;++i){
            integral[i] = nums[i-1] + integral[i-1];
        }
        int maxVal = Integer.MIN_VALUE,minInd = 0;
        for(int i = 1;i<integral.length;++i){
            if(integral[i]-integral[minInd]>maxVal){
                maxVal = integral[i]-integral[minInd];
            }

            if(integral[i]<integral[minInd]){
                minInd = i;
            }
        }
        return maxVal;

    }

    public int maxSubArraySimply(int[] nums) {
        int pre = 0, maxAns = nums[0];
        for (int x : nums) {
            pre = Math.max(pre + x, x); // 评估只选择自己，和自己以及之前的序列的代价
            maxAns = Math.max(maxAns, pre);
        }
        return maxAns;
    }

}