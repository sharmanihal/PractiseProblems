/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    int res=-99999;
    public int maxPathSum(TreeNode root) {
        
        solve(root);
        return res;
    }
    private int solve(TreeNode root){
        if (root==null){
            return 0;
        }
        int l= solve(root.left);
        int r= solve(root.right);
        
        int temp= Math.max(Math.max(l,r)+root.val,root.val);
        int ans= Math.max(temp,l+r+root.val);
        res= Math.max(res,ans);
        return temp;
    }
}