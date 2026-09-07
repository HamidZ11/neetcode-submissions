# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None

        while current: # run as long as curernt has a value
            temp = current.next      # Save the rest of the list
            current.next = previous  # Reverse the pointer
            previous = current       # Advance previous
            current = temp           # Continue with the saved node
        
        return previous # return previous becasue thats the new head
        

