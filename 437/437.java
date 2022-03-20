class Solution {
    Map<Integer,Integer> map = new HashMap<>(); // <前缀和,次数>
    int cnt = 0;
    int targetSum;
    void recu(TreeNode root,int already){
        if(root!=null){
            int pathSum = already+root.val;

            cnt += map.getOrDefault(pathSum-targetSum,0);

            map.put(pathSum,map.getOrDefault(pathSum,0)+1);
            recu(root.left,pathSum);
            recu(root.right,pathSum);

            map.put(pathSum,map.get(pathSum)-1);
        }

    }
    public int pathSum(TreeNode root, int targetSum) {
        this.targetSum = targetSum;
        map.put(0,1); // 设置起点
        recu(root, 0);
        return cnt;
    }
}
