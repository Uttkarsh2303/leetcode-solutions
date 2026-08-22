# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        left_prev=dummy
        curr=head
        for _ in range(left-1):
            left_prev=left_prev.next
            curr=curr.next
        left_element=curr
        before=left_prev
        for _ in range(right-left+1):
            next_node=curr.next
            curr.next=left_prev
            left_prev=curr
            curr=next_node
        left_element.next=next_node
        before.next=left_prev
        return dummy.next