# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []
        if not head or not head.next:
            return [-1, -1]
        prev_val = head.val
        curr = head.next
        idx = 2
        while curr.next:
            if curr.val > prev_val and curr.val > curr.next.val:
                critical_points.append(idx)
            if curr.val < prev_val and curr.val < curr.next.val:
                critical_points.append(idx)
            prev_val = curr.val
            idx += 1
            curr = curr.next
        
        res = [-1, -1]
        if len(critical_points) < 2:
            return res
        
        min_dist = inf
        for i in range(1, len(critical_points)):
            min_dist = min(min_dist, critical_points[i] - critical_points[i - 1])
        res[0] = min_dist
        res[1] = critical_points[-1] - critical_points[0]
        
        return res
        
