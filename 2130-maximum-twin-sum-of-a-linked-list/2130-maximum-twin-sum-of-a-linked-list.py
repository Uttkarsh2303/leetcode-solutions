# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        prev = None

        while mid:
            next_node = mid.next
            mid.next = prev

            prev = mid
            mid = next_node

        p1 = head
        p2 = prev

        maxsum = 0

        while p2:
            current_sum = p1.val + p2.val
            maxsum = max(current_sum, maxsum)

            p1 = p1.next
            p2 = p2.next

        return maxsum
        