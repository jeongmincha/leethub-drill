class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.hash_map = {}
        self.capacity = capacity
        self.size = 0
    
    def addToHead(self, node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node
    
    def removeNode(self, node):
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)
    
    def removeTail(self):
        tail_prev = self.tail.prev
        tail_prev.prev.next = self.tail
        self.tail.prev = tail_prev.prev
        return tail_prev

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        
        node = self.hash_map[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            self.moveToHead(node)
            return
        
        new_node = ListNode(key, value)
        self.hash_map[key] = new_node
        self.addToHead(new_node)
        self.size += 1
        
        if self.size > self.capacity:
            removed = self.removeTail()
            del self.hash_map[removed.key]
            self.size -= 1
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)