"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copies = {}
        current = head

        while current:
            copies[current] = Node(current.val) # brand new node same value as current
            current = current.next
        
        current = head # reset current to add the .next copies to dictionary
        while current:
            if current.next:
                copies[current].next = copies[current.next]
            else:
                copies[current].next = None
            current = current.next
        
        current = head 
        while current:
            if current.random:
                copies[current].random = copies[current.random]
            else:
                copies[current].random = None
            current = current.next
        
        if head:
            return copies[head] 
        else:
            return None

        



