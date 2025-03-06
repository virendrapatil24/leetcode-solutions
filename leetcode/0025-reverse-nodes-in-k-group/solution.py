# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr:
            n_node = curr
            for _ in range(k):
                n_node = n_node.next
                if not n_node:
                    return dummy.next
            next_curr = n_node.next if n_node else None
            n_node.next = None
            next = curr.next
            rev = self.reverse(curr.next)
            curr.next = rev
            next.next = next_curr
            curr = next

        return dummy.next
    
    def reverse(self, node):
        curr, prev = node, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

        
