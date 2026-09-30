# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        numlist1 = [] 
        numlist2 = []
        current = l1
        current2 =l2

        while current: 
            numlist1.append(current.val)
            current = current.next
        while current2: 
            numlist2.append(current2.val)
            current2 = current2.next

        
        strnum1 =""
        for i in reversed(numlist1): 
            strnum1 += str(i)
        strnum1 = int(strnum1)

        strnum2 =""
        for i in reversed(numlist2): 
            strnum2 += str(i)
        strnum2 = int(strnum2)


        total = strnum2 + strnum1

        digits = str(total)

        dummy = ListNode(0)
        tail = dummy

        for digit in reversed(digits):
            tail.next = ListNode(int(digit))
            tail = tail.next
        
        return dummy.next




