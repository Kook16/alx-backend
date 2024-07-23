from collections import OrderedDict

class MRUCache:
 def __init__(self, capacity: int):
  # Initialize the cache with the given capacity and an empty OrderedDict
  self.cache = OrderedDict()
  self.capacity = capacity

 def get(self, key: int) -> int:
  # Check if the key is in the cache
  if key not in self.cache:
   return -1 # Return -1 if the key is not found
  
  # Move the accessed item to the end to mark it as most recently used
  value = self.cache.pop(key)
  self.cache[key] = value
  return value

 def put(self, key: int, value: int) -> None:
   # If the key is already in the cache, remove it
   if key in self.cache:
    self.cache.pop(key)
   # If the cache is full, remove the most recently used item
   elif len(self.cache) >= self.capacity:
    self.cache.popitem(last=True)
   # Add the new item to the cache, marking it as the most recently used
   self.cache[key] = value

 def __repr__(self):
  # Provide a string representation of the cache for easy visualization
  return f"{self.cache}"

# Example usage
cache = MRUCache(3)

# Adding items to the cache
cache.put(1, 'A')  # Cache: [1:A]
cache.put(2, 'B')  # Cache: [1:A, 2:B]
cache.put(3, 'C')  # Cache: [1:A, 2:B, 3:C]
cache.put(4, 'D')
cache.get(2)
print(cache)  # Output: OrderedDict([(1, 'A'), (2, 'B'), (3, 'C')])
