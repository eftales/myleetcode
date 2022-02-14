class Solution {
    private Set<Integer> visited= new HashSet<Integer>();
    private List<List<Integer>> res = new LinkedList<List<Integer>>();
    private List<Integer> subRes = new LinkedList<Integer>();

    public List<List<Integer>> permute(int[] nums) {
        for(int i=0;i<nums.length;++i){
            if(visited.contains(nums[i])){
                continue;
            }
            visited.add(nums[i]);
            subRes.add(nums[i]);
            if(visited.size()==nums.length){
                List<Integer> rr = new LinkedList<Integer>(subRes);
                res.add(rr);

            }
            else{
                permute(nums);
            }
            subRes.remove(subRes.size()-1); // 删除末尾元素即可
            visited.remove(nums[i]);
        }
        return res;
    }



    private void traceback(int n, List<List<Integer>> res, List<Integer> subRes, int begin){
        if(begin==n){
            res.add(new LinkedList<Integer>(subRes));
            return;
        }
        for(int i=begin;i<n;++i){
            Collections.swap(subRes,begin,i);
            traceback(n,res,subRes,begin+1);
            Collections.swap(subRes,begin,i);
        }

    }
    // 不使用 set 去重，从根本上拒绝重复遍历
    public List<List<Integer>> permuteSimplify(int[] nums){
        List<List<Integer>> res = new LinkedList<List<Integer>>();
        List<Integer> subRes = new LinkedList<>();
        for(int num:nums){
            subRes.add(num);
        }
        traceback(nums.length,res, subRes,0);
        return res;
    }
}
