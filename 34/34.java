class Solution {
    public int[] searchRange(int[] nums, int target) {
        int tr=-1,tl=-1;
        int left=0,right=nums.length-1, mid = (left+right)/2;;
        while(left<right){
            if(right-left==1){
                if(nums[right]==target){
                    mid = right;
                    break;
                }
                else if(nums[left]==target){
                    mid = left;
                    break;
                }
                else{
                    return new int[]{tl,tr};
                }
            }

            if(nums[mid]==target){
                break;
            }
            else{
                if(nums[mid]>target){
                    right = mid;
                }
                else{
                    left = mid;
                }
                mid = (left+right)/2;
            }

        }

        if(nums.length<=0||nums[mid]!=target){
            return new int[]{-1,-1};
        }

        // 找左边界
        left = 0;
        right=mid;
        int midl = (left+right)/2;
        tl = left;
        while(left<=right){
            if(nums[midl]<target){
                left = midl;
                midl = Math.max(left+1,(left+right)/2);
            }
            else if(nums[midl]==target){
                if(midl==0||nums[midl-1]!=target){
                    tl = midl;
                    break;
                }
                else{
                    right = midl;
                    midl = (left+right)/2;
                }
            }
        }

        // 找右边界
        left = mid;
        right=nums.length-1;
        int midr = (left+right)/2;
        tr = right;
        while(left<=right){
            if(nums[midr]>target){
                right = midr;
                midr = (left+right)/2;
            }
            else if(nums[midr]==target){
                if(midr==(nums.length-1)||nums[midr+1]!=target){
                    tr = midr;
                    break;
                }
                else{
                    left = midr;
                    midr = Math.max(left+1,(left+right)/2);
                }
            }
        }

        return new int[]{tl,tr};
    }
}
