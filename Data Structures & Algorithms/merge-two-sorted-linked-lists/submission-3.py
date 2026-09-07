# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # dummy is used build our merged list, it starts at zero
        tail = dummy

        while list1 and list2: # both lists need nodes to compare them 
            if list1.val <= list2.val:
                tail.next = list1 
                tail = tail.next # move tail 
                list1 = list1.next
            
            elif list1.val > list2.val:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
        

        # if one of the two sitll has a node in 
        if list1: 
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next


           

