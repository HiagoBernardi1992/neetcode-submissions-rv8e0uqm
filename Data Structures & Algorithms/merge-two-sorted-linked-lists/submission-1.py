# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode(0)
        cm = merged
        c1 = list1
        c2 = list2
        while c1 and c2:
            if c1.val <= c2.val:
                cm.next = c1
                c1 = c1.next
            else:
                cm.next = c2
                c2 = c2.next
            cm = cm.next
        if c1:
            cm.next = c1
        if c2:
            cm.next = c2

        return merged.next