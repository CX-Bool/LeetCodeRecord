class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.mem = {}
        self.use = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.mem:
            self.use.remove(key)
            self.use.append(key)
            return self.mem[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.mem.keys():
            if len(self.mem) == self.capacity:
                k = self.use.pop(0)
                self.mem.pop(k)
        else:
            self.use.remove(key)
        self.mem[key] = value
        self.use.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)