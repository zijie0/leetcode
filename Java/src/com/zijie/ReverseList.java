package com.zijie;

/**
 * Created by zijie.zy on 2016/4/27.
 */
public class ReverseList {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode temp;
        while (head != null) {
            temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }
        return prev;
    }

    public static void main(String[] args) {
        ListNode a = new ListNode(1);
        ListNode b = new ListNode(2);
        ListNode c = new ListNode(3);
        a.next = b;
        b.next = c;
        ReverseList reverseList = new ReverseList();
        ListNode result = reverseList.reverseList(a);
        while (result != null) {
            System.out.print(String.valueOf(result.val) + " ");
            result = result.next;
        }
    }
}
