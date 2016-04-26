package com.zijie;

/**
 * Created by zijie.zy on 2016/4/26.
 */
public class DeleteNode {
    public void deleteNode(ListNode node) {
        if (node == null || node.next == null) {
            return;
        }
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
