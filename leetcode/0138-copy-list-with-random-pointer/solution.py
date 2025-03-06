"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
        
        curr = head
        while curr:
            copy = curr.next
            copy.random = curr.random.next if curr.random else None
            curr = curr.next.next
        
        dummy = Node(0)
        copy = dummy
        curr = head
        while curr:
            copy.next = curr.next
            copy = copy.next
            curr.next = curr.next.next
            curr = curr.next

        return dummy.next


        
