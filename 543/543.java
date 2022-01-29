class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
class Solution {
    int[] rec(TreeNode root){
        int[] res={0,0}; // 最大深度，最大直径
        if(root==null){
            return res;
        }
        int[] lres = rec(root.left);
        int[] rres = rec(root.right);
        res[0] = Math.max(lres[0],rres[0])+1;
        res[1] = Math.max(lres[0]+rres[0],Math.max(lres[1],rres[1]));
        return res;

    }
    public int diameterOfBinaryTree(TreeNode root) {

        return rec(root)[1];
    }
}