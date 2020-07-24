class LRUCache:

    def __init__(self, capacity: int):
        self.memory = []
        self.capacity = capacity
        self.current = 0
        

    def get(self, key: int) -> int:
        for i, tup in enumerate(self.memory):
            if tup[0] == key:
                self.memory.insert(0, self.memory.pop(i))
                return tup[1]
            
        return -1
        

    def put(self, key: int, value: int) -> None:
        key_index = self.exists(key)
        
        if self.current < self.capacity:
            # Memory Available
            
            if key_index >= 0:
                # Key already exists. Find key and change value
                self.memory.pop(key_index)
                self.memory.insert(0, (key, value))
            else:
                self.memory.insert(0, (key, value))
                self.current += 1
        else:
            # Memory is full. Evict least recently used one.
            # But if key exists, Find key and change value
            
            if key_index >= 0:
                # Key already exists
                self.memory.pop(key_index)
                self.memory.insert(0, (key, value))
            else:
                self.memory.pop()
                self.memory.insert(0, (key, value))
            
    def exists(self, key: int) -> int:
        for i, data in enumerate(self.memory):
            if data[0] == key:
                return i
        
        return -1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)