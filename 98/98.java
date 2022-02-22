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

    long[] rec(TreeNode root){
        // 返回值为本子树的最小值和最大值 [最小值,最大值]
        if(root==null){
            return new long[]{Long.MAX_VALUE,Long.MIN_VALUE};
        }
        long[] lRes = rec(root.left);
        long[] rRes = rec(root.right);

        if((lRes[1]<root.val)&&(root.val<rRes[0])){ // root > 左子树最大值&& root < 右子树最小值
            long[] childRes = new long[]{Math.min(rRes[0],lRes[0]),Math.max(rRes[1],lRes[1])};

            return new long[]{Math.min(childRes[0],root.val),Math.max(childRes[1],root.val)}; // 将本树的最大最小值上报
        }
        else{
            return new long[]{Integer.MIN_VALUE,Integer.MAX_VALUE}; // 返回这个数值一定不会被判定为搜索树
        }



    }
    public boolean isValidBST(TreeNode root) {
        if(root==null){
            return true;
        }
        long[] rLeft = rec(root.left);
        long[] rRight = rec(root.right);
        if(rLeft[1]<root.val&&root.val<rRight[0]){
            return true;
        }
        else{
            return false;
        }
    }

    public boolean isValidBST(TreeNode root, long lower, long upper){
        if(root==null){
            return true;
        }
        else if(lower<root.val&&root.val<upper){
            return isValidBST(root.left,lower,root.val)&&isValidBST(root.right,root.val,upper);
        }
        else{
            return false;
        }
    }
    
    public boolean isValidBSTSimplify(TreeNode root) {
        return isValidBST(root,Long.MIN_VALUE,Long.MAX_VALUE);
    }
}
