# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy_head = dummy
        nums_set = set(nums)
        while head:
            if head.val not in nums_set:
                dummy_head.next = head
                dummy_head = dummy_head.next
            head = head.next
        
        dummy_head.next = None
        return dummy.next
        
