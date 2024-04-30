# Hash Tables
"""
Author: Thelma Ofoegbu
Purpose: Implementing Hash Tables
"""
class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        """Hash function to map keys to indices."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))

    def search(self, key):
        """Search for a key in the hash table."""
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None


# Example usage:
'''
if __name__ == "__main__":
    # Hash Tables
    hash_table = HashTable()
    hash_table.insert("apple", "A sweet red fruit")
    hash_table.insert("banana", "A yellow fruit")
    print("Hash Tables:")
    print("apple:", hash_table.search("apple"))
    print("banana:", hash_table.search("banana"))

    # Red-Black Tree
    # Usage example for Red-Black Tree searching'''