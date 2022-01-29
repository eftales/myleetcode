
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
    public boolean isSymmetric(TreeNode root) {
        if(root==null){
            return true;
        }

        TreeNode lt = root.left,rt = root.right;
        if(lt==null && rt==null){
            return true;
        }
        else if(lt!=null && rt==null){
            return false;
        }
        else if(lt==null && rt!=null){
            return false;
        }


        // 其实没必要遵循先序/后序遍历
        ArrayList<TreeNode> Rtovisit = new ArrayList<TreeNode>(),Ltovisit = new ArrayList<TreeNode>();
        Rtovisit.add(rt);
        Ltovisit.add(lt);
        Set<TreeNode> Rvisited = new HashSet<TreeNode>(),Lvisited = new HashSet<TreeNode>();

        while(Rtovisit.size()!=0&&Ltovisit.size()!=0){
            lt = Ltovisit.get(Ltovisit.size()-1);
            rt = Rtovisit.get(Rtovisit.size()-1);

            if(lt.val!=rt.val){
                return false;
            }

            if(lt.left!=null && !Lvisited.contains(lt.left)){
                Ltovisit.add(lt.left);
            }
            else{
                Ltovisit.remove(Ltovisit.size()-1);
                Lvisited.add(lt);
                if(lt.right!=null){
                    Ltovisit.add(lt.right);
                }

            }

            if(rt.right!=null && !Rvisited.contains(rt.right)){
                Rtovisit.add(rt.right);
            }
            else{
                Rtovisit.remove(Rtovisit.size()-1);
                Rvisited.add(rt);
                if(rt.left!=null){
                    Rtovisit.add(rt.left);
                }

            }

        }

        if(Rtovisit.size()==0 && Ltovisit.size()==0){
            return true;
        }
        else{
            return false;
        }

    }

    public boolean check(TreeNode lt,TreeNode rt){

        if (lt==null&&rt==null){
            return true;
        }
        if(lt==null||rt==null){
            return false;
        }
        return lt.val==rt.val && check(lt.left,rt.right) && check(lt.right,rt.left);
    }
    public boolean isSymmetricRec(TreeNode root){
        if (root==null){
            return true;
        }
        return check(root.left, root.right);
    }

    
}