class Solution {
    int dfs(TreeNode root, int already){
        if(root==null){
            return already;
        }
        root.val += dfs(root.right,already);
        return dfs(root.left,root.val);
    }
    public TreeNode convertBST(TreeNode root) {
        dfs(root,0);
        return root;
    }
}