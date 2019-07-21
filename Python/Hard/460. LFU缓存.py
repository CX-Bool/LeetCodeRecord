class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.mem = {}
        self.freq = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.mem:
            for k, v in self.freq.items():
                if key in v:
                    v.remove(key)
                    if not v:
                        self.freq.pop(k)
                    self.freq.setdefault(k + 1, []).append(key)
                    return self.mem[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.cap <= 0:
            return
        if key not in self.mem:
            if len(self.mem) == self.cap:
                # pop LFU
                min_freq = min(self.freq.keys())
                dkey = self.freq[min_freq].pop(0)
                if not self.freq[min_freq]:
                    self.freq.pop(min_freq)
                self.mem.pop(dkey)
            self.mem[key] = value
            self.freq.setdefault(1, []).append(key)
        else:
            self.mem[key] = value
            self.get(key)
# class LFUCache(object):
#
#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.cap = capacity
#         self.mem = {}
#         self.use = {}
#         self.freq = []
#
#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key in self.mem:
#             self.use[key] += 1
#             self.freq.remove(key)
#             self.freq.append(key)
#             return self.mem[key]
#         else:
#             return -1
#
#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         if not self.cap:
#             return
#         if key not in self.mem:
#             if len(self.mem) == self.cap:
#                 # find LFU and delete
#                 dkey = None
#                 minuse = int(1e10)
#                 for k, v in self.use.items():
#                     if v < minuse:
#                         minuse = v
#                         dkey = k
#                     elif v == minuse:
#                         # print('use:%s'%v)
#                         # print('dkey:%s index:%s'%(dkey, self.freq.index(dkey)))
#                         # print('dkey:%s index:%s'%(k, self.freq.index(k)))
#                         dkey = dkey if self.freq.index(dkey) < self.freq.index(k) else k
#
#                 # print('this turn dkey: %s'%dkey)
#                 self.freq.remove(dkey)
#                 self.mem.pop(dkey)
#                 self.use.pop(dkey)
#             self.use[key] = 1
#         else:
#             self.freq.remove(key)
#             self.use[key] += 1
#         self.mem[key] = value
#
#         self.freq.append(key)
#
# # Your LFUCache object will be instantiated and called as such:
# # obj = LFUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)