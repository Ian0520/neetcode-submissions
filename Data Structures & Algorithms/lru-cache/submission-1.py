class LRUCache:
    class Node:
        def __init__(self, val: int, key: str):
            self.val = val
            self.key = key
            self.next = None
            self.last = None
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}

        self.head = None  # most recently used
        self.tail = None  # least recently used

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        # move to head if not already head
        if node is not self.head:
            if node is self.tail:
                self.tail = node.last
            if node.last:
                node.last.next = node.next if node.next else None
            if node.next:
                node.next.last = node.last if node.last else None 
            if self.head:
                self.head.last = node
                node.next = self.head
                node.last = None
            self.head = node
        return node.val
    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_node:
            # create new head
            node = self.Node(value, key)
            self.key_to_node[key] = node
            # move to head
            if self.head:
                self.head.last = node
                node.next = self.head
            self.head = node
            if self.tail is None:
                self.tail = node
            if len(self.key_to_node) > self.capacity:
                # remove tail
                temp = self.tail
                if self.tail.last:
                    self.tail.last.next = None
                self.tail = self.tail.last if self.tail.last else None
                del self.key_to_node[temp.key]
                del temp
            
        else:
            node = self.key_to_node[key]
            node.val = value
            # move to head if not already head   
            if node is not self.head: 
                if node is self.tail:
                    self.tail = node.last      
                if node.last:
                    node.last.next = node.next if node.next else None
                if node.next:
                    node.next.last = node.last if node.last else None 
                if self.head:
                    self.head.last = node
                    node.next = self.head
                    node.last = None
                self.head = node
