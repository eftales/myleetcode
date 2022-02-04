
class Solution {
    public List<List<Integer> > threeSum(int[] nums) {

        Arrays.sort(nums);
        List<List<Integer> > res = new LinkedList<List<Integer> > ();
        if(nums.length<3){
            return res;
        }

        int before = Integer.MIN_VALUE;
        for(int i=0;i<nums.length;++i){
            if(before==nums[i]){
                continue;
            }
            before = nums[i];
            int left = i+1,right=nums.length-1;


            while(left<right){
                if(nums[i]+nums[left]+nums[right]==0){
                    LinkedList<Integer> subRes = new LinkedList<Integer>();
                    subRes.add(nums[i]);
                    subRes.add(nums[left]);
                    subRes.add(nums[right]);
                    res.add(subRes);


                    int lBefore = nums[left];
                    do{
                        left += 1;
                    }
                    while(lBefore==nums[left]&&left<right);
                }
                else if(nums[i]+nums[left]+nums[right]>0){
                    int rBefore = nums[right];
                    do{
                        right -= 1;
                    }
                    while(rBefore==nums[right]&&right>left);
                }
                else if(nums[i]+nums[left]+nums[right]<0){
                    int lBefore = nums[left];
                    do{
                        left += 1;
                    }
                    while(lBefore==nums[left]&&left<right);
                }
            }
        }
        return res;

    }

    public List<List<Integer> > threeSumSimplify(int[] nums) {

        Arrays.sort(nums);
        List<List<Integer> > res = new LinkedList<List<Integer> > ();
        if(nums.length<3){
            return res;
        }


        for(int i=0;i<nums.length;++i){
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }

            int left = i+1,right=nums.length-1;


            while(left<right){
                if(nums[i]+nums[left]+nums[right]==0){
                    LinkedList<Integer> subRes = new LinkedList<Integer>();
                    subRes.add(nums[i]);
                    subRes.add(nums[left]);
                    subRes.add(nums[right]);
                    res.add(subRes);

                    // 在找到一组符合条件的解之后，才需要保证元素不同
                    do{
                        left += 1;
                    }
                    while(nums[left-1]==nums[left]&&left<right);
                }
                else if(nums[i]+nums[left]+nums[right]>0){
                    right -= 1;
                }
                else if(nums[i]+nums[left]+nums[right]<0){
                    left += 1;
                }
            }
        }
        return res;

    }

}