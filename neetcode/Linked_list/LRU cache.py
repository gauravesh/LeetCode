class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}  # Use a dictionary to store key-value pairs
        self.order = []  # Use a list to maintain the order of keys

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            # Move the accessed key to the end of the order list (most recently used)
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            # If the key exists, update the value and move it to the end of the order list
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            # If the cache is at capacity, remove the least recently used key
            if len(self.order) >= self.capacity:
                lru_key = self.order.pop(0)
                del self.cache[lru_key]
            
            # Add the new key-value pair to the cache and the end of the order list
            self.cache[key] = value
            self.order.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
