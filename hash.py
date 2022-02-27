
class ChainingHashTable:
    """This class creates a hash table which chains together lists to handle collisions"""

    # Class initializer for the hash table with a default capacity of 10 unless specified
    def __init__(self, capacity=10):
        # Creates an empty table that appends empty lists as buckets depending on capacity
        self.table = []
        for i in range(capacity):
            self.table.append([])  # appends an empty list to the table * capacity

    # Inserts a new key-value pair into the hash table
    def insert(self, key, value):
        # Calculate which index of the hash table the key-value pair will be inserted into
        index = self.table[hash(key) % len(self.table)]

        for key_value_pair in index:
            if key_value_pair[0] == key:
                key_value_pair[1] = value
                return True

        index.append([key, value])
        return True

    # Removes a key-value pair with matching key from the hash table
    def delete(self, key):
        # Calculate which index of the hash table that the key-value pair will be deleted from
        index = self.table[hash(key) % len(self.table)]

        # removes the item from the index if applicable
        for key_value_pair in index:
            if key_value_pair[0] == key:
                index.remove([key_value_pair[0], key_value_pair[1]])

    # Searches for an item using the item's key in the hash table.
    def search(self, key):
        # Calculate which index of the hash table the key-value pair will be in
        index = self.table[hash(key) % len(self.table)]

        # search for the key in the index it is currently on
        for key_value_pair in index:
            if key_value_pair[0] == key:
                return key_value_pair[1]
        return None
