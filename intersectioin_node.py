# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        visited_a = set()
        ptr_a, ptr_b = headA, headB
        while ptr_a:
            visited_a.add(ptr_a)
            ptr_a = ptr_a.next
        while ptr_b:
            if ptr_b in visited_a:
                return ptr_b
            ptr_b = ptr_b.next
        return None

class Solution2:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        ptr_a, ptr_b = headA, headB
        tail_a, tail_b = None, None
        while True:
            if not ptr_a:
                ptr_a = headB
            if not ptr_b:
                ptr_b = headA
            if not ptr_a.next:
                tail_a = ptr_a
            if not ptr_b.next:
                tail_b = ptr_b
            if tail_a and tail_b and tail_a != tail_b:
                return None
            if ptr_a == ptr_b:
                return ptr_a
            ptr_a = ptr_a.next
            ptr_b = ptr_b.next

node_a1 = ListNode('a1')
node_a2 = ListNode('a2')
node_b1 = ListNode('b1')
node_b2 = ListNode('b2')
node_b3 = ListNode('b3')
node_c1 = ListNode('c1')
node_c2 = ListNode('c2')
node_c3 = ListNode('c3')

node_a1.next = node_a2
node_a2.next = node_c1

node_b1.next = node_b2
node_b2.next = node_b3
node_b3.next = node_c1

node_c1.next = node_c2
node_c2.next = node_c3

print (Solution().getIntersectionNode(node_a1, node_b1)).val