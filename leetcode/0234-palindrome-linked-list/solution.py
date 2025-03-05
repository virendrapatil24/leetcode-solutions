# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        new_head = self.reverse(slow)

        first, second = head, new_head
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True
    
    def reverse(self, node):
        curr, prev = node, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        
