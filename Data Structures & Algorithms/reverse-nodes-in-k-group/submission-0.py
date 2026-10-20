# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        previous_tail = dummy
        
        while True:
            group_start = previous_tail.next

            # Check whether k nodes remain
            current = group_start
            
            # 1. Check if there is a valid group of k nodes
            for i in range(k): 
                if not current: # accessing .next on None would cause an error.
                    return dummy.next
                current = current.next
            
            # Reverse this group
            previous = None
            current = group_start
            for i in range(k):
                temp = current.next       # Save the next node
                current.next = previous   # Reverse the pointer
                previous = current        # Move previous forward
                current = temp            # Move current forward
        
            # AT THIS POINT: ( for example 1 2 3 4 5 6)
                # Head points to node 1 (original current)
                # Current points to node 4

            previous_tail.next = previous
            group_start.next = current
            previous_tail = group_start
        
        return head
        

