# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #To reverse a linked list 0 1 2 3
        # what do i do, what do i need to know, i need to know the current number and swap it with next 
        # what hapepns if i keep doing that
        current = head
        previous = None

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        return previous


