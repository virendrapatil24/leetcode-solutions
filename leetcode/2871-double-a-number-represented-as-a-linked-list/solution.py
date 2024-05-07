# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = self.reverse(head)

        curr = rev
        total, carry = 0, 0
        while curr or carry:
            db = curr.val * 2
            val = (db + carry) % 10
            carry = db // 10
            curr.val = val
            if carry and not curr.next:
                curr.next = ListNode(carry)
                break
            curr = curr.next

        return self.reverse(rev)
            
    
    def reverse(self, node):

        prev = None
        curr = node
        while curr:
            next = curr.next
            curr.next = prev 
            prev = curr
            curr = next
        return prev 
        
