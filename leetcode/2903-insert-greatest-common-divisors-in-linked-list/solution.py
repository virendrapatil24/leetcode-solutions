# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            gcd_node = ListNode(gcd(curr.val, curr.next.val))
            gcd_node.next = curr.next
            curr.next = gcd_node
            curr = curr.next.next
        return head

        
        

        
