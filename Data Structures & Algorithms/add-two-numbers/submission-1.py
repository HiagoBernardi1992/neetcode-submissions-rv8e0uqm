# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def getNumber(l, number):
            if not l:
                return int(number[::-1]) if number else 0

            number += str(l.val)
            return getNumber(l.next, number)

        value_one = getNumber(l1, "")
        value_two = getNumber(l2, "")

        new_value = value_one + value_two
        new_value_str = str(new_value)

        dummy = ListNode(0)
        curr = dummy

        for i in range(len(new_value_str) - 1, -1, -1):
            curr.next = ListNode(int(new_value_str[i]))
            curr = curr.next

        return dummy.next

