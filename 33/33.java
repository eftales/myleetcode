class Solution {
    public int partSearch(int[] nums, int left, int right,int target){
        if(right==left){
            if(nums[right]!=target){
                return -1;
            }
            else{
                return right;
            }
        }
        int mid=(left+right)/2;

        // 中右连续
        if(nums[mid]<nums[right] && (nums[mid]<=target&&target<=nums[right])){
            if(nums[mid]==target){
                return mid;
            }
            return partSearch(nums,mid+1,right,target);

        }
        else if(nums[mid]<nums[right]){
            if(nums[left]==target){
                return left;
            }
            return partSearch(nums,left+1,mid,target);
        }

        // 左中连续
        if(nums[mid]>nums[right] && (nums[mid]>=target&&target>=nums[left])){
            if(nums[left]==target){
                return left;
            }
            return partSearch(nums,left+1,mid,target);
        }
        else if(nums[mid]>nums[right]){
            if(nums[mid]==target){
                return mid;
            }
            return partSearch(nums,mid+1,right,target);
        }
        return -1;

    }
    public int search(int[] nums, int target) {

        return partSearch(nums,0,nums.length-1,target);
    }
}
