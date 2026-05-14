# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        while len(lists) > 1:
            lists[0] = self.mergeTwoList(lists[0], lists[len(lists) - 1])
            lists.pop()
        return lists[0] 
        

    def mergeTwoList(self, lOne: ListNode, lTwo: ListNode):
        dummy =  ListNode(0)
        cm = dummy
        cOne = lOne
        cTwo = lTwo
        while cOne and cTwo:
            if cOne.val <= cTwo.val:
                cm.next = cOne
                cOne = cOne.next
            else:
                cm.next = cTwo
                cTwo = cTwo.next
            cm = cm.next

        if cOne:
            cm.next = cOne
        if cTwo:
            cm.next = cTwo

        return dummy.next