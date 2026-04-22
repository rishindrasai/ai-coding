class HashTable:
    """A hash table implementation using chaining for collision handling."""
    
    def __init__(self, size=10):
        """
        Initialize the hash table with a given size.
        
        Args:
            size (int): Number of buckets in the hash table (default: 10)
        """
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """
        Generate hash value for a given key.
        
        Args:
            key: The key to hash
            
        Returns:
            int: Hash value (index in the table)
        """
        return hash(key) % self.size
    
    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If key exists, update its value.
        
        Args:
            key: The key to insert
            value: The value associated with the key
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        # Check if key already exists and update it
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Key doesn't exist, append new pair
        bucket.append((key, value))
    
    def search(self, key):
        """
        Search for a value by key in the hash table.
        
        Args:
            key: The key to search for
            
        Returns:
            The value if found, None otherwise
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        # Linear search within the bucket (chain)
        for k, v in bucket:
            if k == key:
                return v
        
        return None
    
    def delete(self, key):
        """
        Delete a key-value pair from the hash table.
        
        Args:
            key: The key to delete
            
        Returns:
            bool: True if deleted, False if key not found
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        # Search and remove the key
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return True
        
        return False
    
    def display(self):
        """Display all key-value pairs in the hash table."""
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}: {bucket}")


# Example usage
if __name__ == "__main__":
    ht = HashTable(5)
    
    # Insert operations
    ht.insert("name", "Alice")
    ht.insert("age", 25)
    ht.insert("city", "NYC")
    ht.insert("job", "Engineer")
    
    # Search operations
    print("Search 'name':", ht.search("name"))
    print("Search 'age':", ht.search("age"))
    print("Search 'notfound':", ht.search("notfound"))
    
    # Delete operations
    print("\nDelete 'age':", ht.delete("age"))
    print("Search 'age' after deletion:", ht.search("age"))
    
    # Display hash table
    print("\nHash Table Contents:")
    ht.display()