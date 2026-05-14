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
            mergedList = []
            for i in range(0, len(lists), 2):
                lOne = lists[i]
                lTwo = None
                if i + 1 < len(lists):
                    lTwo = lists[i + 1]
                mergedList.append(self.mergeTwoList(lOne, lTwo))
            lists = mergedList
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