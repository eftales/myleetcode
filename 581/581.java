class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int LB=-1, RB=-1;
        for(int i=0;i<nums.length-1;++i){
            if(nums[i]>nums[i+1]){
                LB = i;
                break;
            }
        }

        if(LB==-1){
            return 0;
        }

        for(int i=nums.length-1;i>0;--i){
            if(nums[i]<nums[i-1]){
                RB = i;
                break;
            }
        }

        int SAMax = Integer.MIN_VALUE, SAMin = Integer.MAX_VALUE;
        for(int i=LB;i<=RB;++i){
            SAMax = Math.max(SAMax,nums[i]);
            SAMin = Math.min(SAMin,nums[i]);
        }

        // LeftSubArray.max < SubArray.min
        for(int i=LB-1;i>=0;--i){
            LB = i;
            if(nums[i]<=SAMin){
                LB += 1;
                break;
            }
        }

        // RiftSubArray.min > SubArray.max
        for(int i=RB+1;i<nums.length;++i){
            RB = i;
            if(nums[i]>=SAMax){
                RB -= 1;
                break;
            }
        }

        return RB - LB + 1;
    }

    public int findUnsortedSubarraySimplify(int[] nums) {
        int n = nums.length;
        int maxn = Integer.MIN_VALUE, right = -1;
        int minn = Integer.MAX_VALUE, left = -1;
        for (int i = 0; i < n; i++) {
            if (maxn > nums[i]) {
                right = i;
            } else {
                maxn = nums[i];
            }
            if (minn < nums[n - i - 1]) {
                left = n - i - 1;
            } else {
                minn = nums[n - i - 1];
            }
        }
        return right == -1 ? 0 : right - left + 1;
    }

}
