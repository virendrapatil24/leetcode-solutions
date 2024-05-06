# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev_head = self.reverseList(head)
        curr = rev_head
        curr_max = curr.val
        while curr.next:
            if curr.next.val < curr_max:
                curr.next = curr.next.next
            else:
                curr_max = curr.next.val
                curr = curr.next
        return self.reverseList(rev_head)
    
    def reverseList(self, node):
        prev = None
        curr = node
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        
