#!/usr/bin/python3
if __name__ == "__main__":
    LRUCache = __import__('3-lru_cache').LRUCache

    my_cache = LRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    
    # Access items B and A
    print(my_cache.get("B"))  # World
    print(my_cache.get("A"))  # Hello
    
    # Add item E, which should evict C (the least recently used)
    my_cache.put("E", "Battery")
    my_cache.print_cache()

    # Access D to make it recently used
    print(my_cache.get("D"))  # School
    
    # Add item F, which should now evict B
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    
    # Repeatedly access A
    print(my_cache.get("A"))  # Hello
    print(my_cache.get("A"))  # Hello
    
    # Add item G, which should evict E
    my_cache.put("G", "Street")
    my_cache.print_cache()

    # Final state checks
    print(my_cache.get("A"))  # Hello
    print(my_cache.get("B"))  # None
    print(my_cache.get("C"))  # None
    print(my_cache.get("D"))  # School
    print(my_cache.get("E"))  # None
    print(my_cache.get("F"))  # Mission
    print(my_cache.get("G"))  # Street

