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
    public int sum;
    public int rangeSumBST(TreeNode root, int low, int high) {
        sum = 0;
        func(root,low,high);
        return sum;
    }
    public void func(TreeNode root,int low,int high)
    {
        if(root == null)
        {
            return;
        }
        if(root.val >= low && root.val <= high)
        {
            sum += root.val;
            func(root.left,low,high);
            func(root.right,low,high);
        }
        else
        {
            if(root.val < low)
            {
            func(root.right,low ,high);
            }
            
            if(root.val > high)
            {
            func(root.left, low, high);
            }
        }
        
    }
}