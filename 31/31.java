
class Solution {

    // 升序
    public void bubblesort(int[] nums,int begin){
        for(int i=begin;i<nums.length;++i){
            boolean done = true;
            for(int j=begin+1;j<nums.length-(i-begin);++j){
                if(nums[j-1]>nums[j]){
                    int tmp = nums[j-1];
                    nums[j-1] = nums[j];
                    nums[j] = tmp;

                    done = false;
                }
            }
            if(done){
                return;
            }
        }
    }

    public void nextPermutation(int[] nums) {

        int curMax = Integer.MIN_VALUE,index=-1;
        for(int i=nums.length-1;i>=0;--i){
            if(nums[i]<curMax){
                index = i;
                break;
            }
            curMax = Math.max(curMax,nums[i]);
        }

        if(index==-1){
            bubblesort(nums,0);
            return;
        }

        int curMin = Integer.MAX_VALUE,index2=0;
        for(int i=index+1;i<nums.length;++i){
            if(nums[i]>nums[index]){
                if(curMin>nums[i]){
                    curMin = nums[i];
                    index2 = i;
                }
            }
        }

        int tmp = nums[index];
        nums[index] = nums[index2];
        nums[index2] = tmp;

        bubblesort(nums,index+1);


    }


    public void invers(int[] nums,int begin){
        int end=nums.length-1;
        while(begin<end){
            int tmp = nums[begin];
            nums[begin] = nums[end];
            nums[end] = tmp;

            begin += 1;
            end -= 1;
        }

    }
    public void nextPermutationSimplify(int[] nums){
        int ind = -1;
        for(int i=nums.length-1;i>0;--i){
            if(nums[i]>nums[i-1]){
                ind = i-1;
                break;
            }
        }
        if(ind==-1){
            invers(nums,0);
            return ;
        }
        // [ind+1:end] 这段数组是升序的
        for(int i=nums.length-1;i>ind;--i){
            if(nums[i]>nums[ind]){
                int tmp = nums[i];
                nums[i] = nums[ind];
                nums[ind] = tmp;
                break;
            }
        }

        invers(nums,ind+1);
    }
}