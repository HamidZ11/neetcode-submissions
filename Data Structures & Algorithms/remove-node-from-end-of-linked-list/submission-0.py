# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0) # just gives us a node before the head.
        dummy.next = head

        slow = dummy
        fast = dummy

        for i in range(n + 1): # get ahead of slow by n + 1 nodes.
            fast = fast.next 
        
        #That gap is what will eventually make slow stop one node before the node we want to remove
        
        while fast: # move slow and fast forward together until fast reaches the end.
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
