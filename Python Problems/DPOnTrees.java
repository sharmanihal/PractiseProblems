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
 class Solution{
    int functionNaem(TreeNode root){
        if root == null:
            return 0
        
        int l= solve(root-> left, res)
        int r= solve(root-> right ,res)
        int tempAns= calulate using l and r

        int ans= someFun(tempAns, some Calulation )

        res = someFun(res,ans)

        return temp
    }
 }