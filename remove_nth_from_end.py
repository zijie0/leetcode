# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

next_node = None
node = None
for i in range(5, 0, -1):
    node = ListNode(i)
    if next_node:
        node.next = next_node
    next_node = node

def print_node_list(head):
    node_str = ''
    while head:
        node_str += str(head.val)
        if head.next:
            node_str += ' -> '
        head = head.next
    return node_str

print print_node_list(node)

print print_node_list(Solution().removeNthFromEnd(node, 5))