# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        if k == 0 or n == 0 or k % n == 0:
            return head
        k %= n
        curr = head
        for _ in range(n - k - 1):
            curr = curr.next
        
        next = curr.next
        curr.next = None
        prev_head = head
        head = next
        while next.next:
            next = next.next
        
        next.next = prev_head
        return head

