package com.zijie;

import java.util.LinkedList;
import java.util.List;

/**
 * Created by zijie.zy on 2016/4/28.
 */
public class LowestCommonAncestor {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || p == null || q == null) {
            return null;
        }
        while (true) {
            if ((root.val - p.val) * (root.val - q.val) <= 0) {
                return root;
            }
            root = p.val < root.val ? root.left : root.right;
        }
    }
}
