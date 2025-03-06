"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        
        curr = head
        prev_next = None
        while curr:
            if curr.child:
                prev_next = curr.next
                child = curr.child
                curr.next = child
                child.prev = curr
                while child.next:
                    child = child.next
                child.next = prev_next
                if prev_next:
                    prev_next.prev = child  
                curr.child = None
            curr = curr.next
        
        curr = head
        while curr:
            if curr.child:
                print(curr.val)
            curr = curr.next

        return head

