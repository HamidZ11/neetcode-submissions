# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # we are given several lists and need to sort them into one linked list

        def mergeTwoLists(list1, list2): # Same function as merge two sorted lists
            dummy = ListNode(0)
            tail = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            if list1:
                tail.next = list1
            else:
                tail.next = list2
            
            return dummy.next

        if not lists:
            return None

        while len(lists) > 1:
            merged = []
        
            for i in range(0, len(lists), 2):
                # we want to merge lists in pairs so our step is 2
                list1 = lists[i]
                if i + 1 < len(lists): #edge case for odd number of lsits
                    list2 = lists[i + 1]
                else:
                    list2 = None

                merged_pair = mergeTwoLists(list1, list2)
                merged.append(merged_pair)
            
            lists = merged

        return lists[0]



