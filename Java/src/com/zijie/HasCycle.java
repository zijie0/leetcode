package com.zijie;

/**
 * Created by zijie.zy on 2016/5/4.
 */
public class HasCycle {
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }
        ListNode p1 = head;
        ListNode p2 = head;
        while (p2 != null && p2.next != null) {
            p1 = p1.next;
            p2 = p2.next.next;
            if (p1 == p2) {
                return true;
            }
        }
        return false;
    }
}
