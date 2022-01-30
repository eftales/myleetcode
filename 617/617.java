class Solution {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        // 将 root2 合并到 root1 上
        if(root1!=null&&root2!=null){
            root1.val += root2.val;
        }
        else{
            if(root1==null){
                return root2;
            }
            else{
                return root1;
            }
        }

        root1.left = mergeTrees(root1.left,root2.left);
        root1.right = mergeTrees(root1.right,root2.right);

        return root1;
    }
}
