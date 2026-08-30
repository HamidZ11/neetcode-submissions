# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next: # while fast can still move 
            prev = slow
            slow = slow.next 
            fast = fast.next.next # think of the track racers analogy (one twice the speed of other)
        

        
        previous = None
        current = slow.next
        slow.next = None
        while current: # Reversing the list after middle (slow)
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        first = head
        second = previous
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2




        # This problem is 3 algos together:
        # Find the middle.
        # Reverse the second half.
        # Alternate-merge the two halves.