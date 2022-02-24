class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for(int num:nums){
            numSet.add(num);
        }

        int maxLen = 0;

        for(int i=0;i<nums.length;++i){
            if(!numSet.contains(nums[i]-1)){
                int tmpLen = 0;
                for(int numJ=nums[i];;++numJ){
                    if(numSet.contains(numJ)){
                        tmpLen += 1;
                    }
                    else{
                        break;
                    }
                }
                maxLen = Math.max(maxLen,tmpLen);
            }
        }
        return maxLen;
    }
}
