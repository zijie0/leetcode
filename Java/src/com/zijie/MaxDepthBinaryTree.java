package com.zijie;

/**
 * Created by zijie.zy on 2016/4/26.
 */
public class MaxDepthBinaryTree {
    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
