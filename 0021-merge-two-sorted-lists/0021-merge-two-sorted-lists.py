# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1
        head1=list1
        head2=list2
        p1=head1
        p2=head2
        if head1.val<head2.val:
            head=head1
            p1=p1.next
        else:
            head=head2
            p2=p2.next
        temp=head
        while p1 and p2:
            if p1.val<=p2.val:
                temp.next=p1
                temp=p1
                p1=p1.next
            else:
                temp.next=p2
                temp=p2
                p2=p2.next
        temp.next=p1 if p1 else p2
        return head
        