# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        curr = head
        while curr.next:
            temp = ListNode(self.gcd(curr.val, curr.next.val))
            temp.next = curr.next
            curr.next = temp
            curr = curr.next.next
        return head

    def gcd(self, a, b):
        if (b == 0):
            return abs(a)
        else:
            return gcd(b, a % b)
        