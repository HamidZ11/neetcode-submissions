class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_dict = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
     
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    
    def insert(self, node):
        previous = self.right.prev
    
        previous.next = node
        node.prev = previous

        node.next = self.right
        self.right.prev = node



    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        
        node = self.cache_dict[key]
        self.remove(node)
        self.insert(node)

        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            old_node = self.cache_dict[key]
            self.remove(old_node)
        new_node = Node(key, value)
        self.cache_dict[key] = new_node
        self.insert(new_node)

        if len(self.cache_dict) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache_dict[LRU.key]
        
