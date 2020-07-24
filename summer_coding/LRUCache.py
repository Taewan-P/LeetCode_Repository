class LRUCache:

    def __init__(self, capacity: int):
        self.order = []
        self.memory = dict()
        self.capacity = capacity
        self.current = 0
        

    def get(self, key: int) -> int:
        val = self.memory.get(key)
        if key in self.order:
            self.order.remove(key)
            self.order.insert(0, key)
            return val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if self.current < self.capacity:
            # Memory Available
            self.memory[key] = value
            if not key in self.order:
                self.current += 1
                self.order.insert(0, key)
            else:
                self.order.remove(key)
                self.order.insert(0, key)
                
        else:
            # Memory Full
            if key in self.order:
                # Exists
                self.order.remove(key)
                self.order.insert(0, key)
                self.memory[key] = value
            else:
                # Doesn't exist
                tmp = self.order.pop()
                self.memory.pop(tmp)
                self.order.insert(0, key)
                self.memory[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)