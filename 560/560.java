class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();
        map.put(0,1);
        int cnt=0, subSum=0;
        for(int i=0;i<nums.length;++i){
            subSum += nums[i];

            if(map.containsKey(subSum-k)){
                cnt += map.get(subSum-k);
            }

            if(map.containsKey(subSum)){

                map.put(subSum,map.get(subSum)+1);
            }
            else{
                map.put(subSum,1);
            }

        }

        return cnt;
    }
}