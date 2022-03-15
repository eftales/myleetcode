class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] F = new int[nums.length];
        int maxLen = 0;
        for(int i=nums.length-1;i>=0;--i){
            int curMaxMin = -1;
            for(int j=i+1;j<nums.length;++j){
                if(nums[j]>nums[i]){
                    if(curMaxMin==-1||F[curMaxMin]<F[j]){
                        curMaxMin = j;
                    }
                }
            }
            if(curMaxMin!=-1){
                F[i] = F[curMaxMin] + 1;
            }
            else{
                F[i] = 1;
            }
            maxLen = Math.max(F[i],maxLen);
        }

        return maxLen;
    }

    void subSearch(List<Integer> d,int target,int begin,int end){
        if(end-begin<0){

        }
        else{
            // 数组很长，进行二分
            int mid = (begin+end)/2;


            if(d.get(mid)<target){
                if(mid==d.size()-1){
                    // 末尾
                    d.set(mid,target);
                }
                else if(d.get(mid+1)>target){
                    d.set(mid+1,target);
                }
                else{
                    // 在 [mid+1,end] 范围内
                    subSearch(d,target,mid+1,end);
                }
            }
            else{
                // 在 [begin,mid-1] 范围内
                if(mid==0){
                    d.set(mid,target);
                }
                else {
                    subSearch(d,target,begin,mid-1);
                }
            }



        }

    }

    public int lengthOfLISSimplify(int[] nums) {
        List<Integer> d = new ArrayList<>();
        d.add(nums[0]);
        for(int i=1;i<nums.length;++i){
            if(nums[i]<=d.get(d.size()-1)){
                // 二分查找合适的替换位置
                subSearch(d,nums[i],0,d.size()-1);
            }
            else{
                d.add(nums[i]);
            }
        }

        return d.size();
    }
}