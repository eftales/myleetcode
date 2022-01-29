class Solution {
    int depth(int n,TreeNode root){
        if (root==null){
            return n;
        }
        else{
            return Math.max(depth(n+1,root.left),depth(n+1,root.right));
        }

    }

    public int maxDepth(TreeNode root) {
        return depth(0,root);
    }

    public int maxDepthSimply(TreeNode root) {
        if(root==null){
            return 0;
        }
        else{
            return Math.max(maxDepthSimply(root.left),maxDepthSimply(root.right))+1;
        }

    }
}