class Solution {
    public void sortColors(int[] nums) {
        int p0=0,p2=nums.length-1;
        int i=0;
        // i 一定满足 >= p0
        while(i<=p2){
            if(nums[i]==0){
                // 因此 p0 位置上存储的值一定不是 2，如果是 2  早就被换走了
                int tmp = nums[i];
                nums[i] = nums[p0];
                nums[p0] = tmp;
                p0 += 1;
                ++i;
            }
            else if(nums[i]==2){
                // p2 位置上存储的值可能是 0，所以不能 ++i，还需要观察一下交换后 i 上的值
                int tmp = nums[i];
                nums[i] = nums[p2];
                nums[p2] = tmp;
                p2 -= 1;
            }
            else{
                ++i;
            }


        }

    }
}