from collections import OrderedDict

class LRUCache:
 def __init__(self, capacity: int):
  self.cache = OrderedDict()
  self.capacity = capacity
  # print(self.cache)

 def get(self, key: int) -> int:
  # print(self.cache)
  if key not in self.cache:
   return -1
  else:
   # Move the accessed item to the end to show that it was recently used
   self.cache.move_to_end(key)
   print(self.cache)
   return self.cache[key]

 def put(self, key: int, value: int) -> None:
   # print(self.cache)
   if key in self.cache:
    # Move the existing item to the end to show that it was recently used
    self.cache.move_to_end(key)
   elif len(self.cache) >= self.capacity:
    # Remove the first item (least recently used)
    self.cache.popitem(last=False)
   # Insert the new or updated item
   self.cache[key] = value
   # print(self.cache)


# Example usage
cache = LRUCache(3)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # returns 1
cache.put(3, 3)
print(cache.get(2))    # returns 2
cache.put(4, 4)        # evicts key 1
print(cache.get(1))    # returns -1 (not found)
print(cache.get(3))    # returns 3
print(cache.get(4))    # returns 4
