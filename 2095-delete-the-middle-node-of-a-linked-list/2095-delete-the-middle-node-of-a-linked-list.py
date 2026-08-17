# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        prev=None
        count=0
        current=head
        while current is not None:
            count+=1
            current=current.next
        if count==1:
            return None
        while fast is not None and fast.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head