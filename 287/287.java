class Solution {
    public int findDuplicate(int[] nums) {
        int slow=0,fast=0;

        // 阶段 1：找到环
        do{
            slow = nums[slow];
            fast = nums[fast];
            fast = nums[fast];
        }while(slow!=fast); // 实际等于才是真的等于

        // 阶段 2：找到环的入口
        slow = 0;
        while(slow!=fast){
            slow = nums[slow];
            fast = nums[fast];

        }

        return slow;

    }
}