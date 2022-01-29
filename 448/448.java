class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int ind = 0;
        while(ind<nums.length){
            if(nums[ind]!=(ind+1)&&nums[ind]>0){
                int tmp = nums[ind],wantedInd = tmp-1;
                if(nums[ind] == nums[wantedInd]){
                    nums[ind] = -1;
                    ind += 1;
                }
                else{
                    nums[ind] = nums[wantedInd];
                    nums[wantedInd] = tmp;
                }

            }
            else{
                ind += 1;
            }
        }
        List<Integer> res = new ArrayList<Integer>();
        for(int i=0;i<nums.length;++i){
            if(nums[i]==-1){
                res.add(i+1);
            }

        }
        return res;
    }

    public List<Integer> findDisappearedNumbersMod(int[] nums){
        for(int i=0;i<nums.length;++i){
            // 原地哈希表
            int ind = (nums[i]-1)%nums.length;
            nums[ind] += nums.length;

        }

        List<Integer> res = new ArrayList<Integer>();
        for(int i=0;i<nums.length;++i){
            if(nums[i]<=nums.length){
                res.add(i+1);
            }

        }
        return res;
    }
}