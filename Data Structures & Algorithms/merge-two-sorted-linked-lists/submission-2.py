# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        currOne, currTwo, currDummy = list1, list2, dummy
        while currOne and currTwo:
            if currOne.val <= currTwo.val:
                currDummy.next = currOne
                currOne = currOne.next
            else:
                currDummy.next = currTwo
                currTwo = currTwo.next
            currDummy = currDummy.next
        
        if currOne:
            currDummy.next = currOne
        if currTwo:
            currDummy.next = currTwo

        return dummy.next

        