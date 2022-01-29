// 投票算法求众数
class Solution {
    public int majorityElement(int[] nums) {
        int candidate = nums[0],cnt = 0;
        for(int num:nums){
            if(cnt==0){
                candidate = num;
            }
            if(num==candidate){
                cnt += 1;
            }
            else{
                cnt -= 1;
            }

        }
        return candidate;
    }
}
